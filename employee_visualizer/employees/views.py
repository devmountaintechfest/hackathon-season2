from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Employee
from datetime import datetime

import os
import xmltodict
import json

# *************** chart stat ***************
def stat_group_job_position():
    labels = []
    data = []

    object_list = Employee.objects.all()
    employees = serializers.serialize('python', object_list)
    for employee in employees:
        position = employee['fields']['position']
        if position not in labels:
            labels.append(position)
    
    for label in labels:
        data.append(sum(map(lambda emp : emp['fields']['position'] == label, employees)))

    return {
        'labels': labels,
        'data': data
    }

def stat_group_hired_by_gender(collecting_history_year):
    years = []
    males = []
    females = []

    object_list = Employee.objects.all()
    employees = serializers.serialize('python', object_list)
    # get last year of employee hired
    print([employee['fields']['hired'] for employee in employees])
    last_emp_hired_year = max(dt for dt in [employee['fields']['hired'] for employee in employees]).year
    last_emp_hired_year = last_emp_hired_year + 1
    for year in range(last_emp_hired_year - collecting_history_year, last_emp_hired_year):
        years.append(year)
        males.append(sum(map(lambda emp : emp['fields']['gender'] == 0 and emp['fields']['hired'].year == year, employees)))
        females.append(sum(map(lambda emp: emp['fields']['gender'] == 1 and emp['fields']['hired'].year == year, employees)))

    return {
        'years': years,
        'males': males,
        'females': females
    }

# *************** index ***************
def index(request):
    context = {
        'stat_group_job_position': stat_group_job_position(),
        'stat_group_hired_by_gender': stat_group_hired_by_gender(10)
    }
    return render(request, 'index.html', context)

def get_employees(request):
    object_list = Employee.objects.all()
    employees = serializers.serialize('python', object_list)
    for employee in employees:
        if employee['fields']['gender'] == 0:
            employee['fields']['gender'] = 'Male'
        else:
            employee['fields']['gender'] = 'Female'
        
        if employee['fields']['status'] == 1:
            employee['fields']['status'] = 'Active'
            
    return JsonResponse(employees, safe=False)


    


# ********** load data from file ***********
def clean_data(data_dict):
    temp_dict = {}
    pristine_records = []

    for index in range(len(data_dict['records']['record'])):
        record = data_dict['records']['record'][index]
        emp_id = record['EMPID']
        passport_no = record['PASSPORT']
        if emp_id in temp_dict and passport_no in temp_dict[emp_id]:
            print('found duplicate on employee id: {} and passport no: {} > ignore'.format(emp_id, passport_no))
        elif 'GENDER' in record and record['GENDER'] not in ['0', '1']:
            print('wrong gender type ({}) > ignore'.format(record['GENDER']))
        elif 'STATUS' in record and record['STATUS'] not in ['1', '2', '3']:
            print('wrong status type ({}) > ignore'.format(record['STATUS']))
        elif 'STATUS' in record and record['STATUS'] != '1':
                print('employee status not active ({}) > ignore'.format(record['STATUS']))
        else:
            if emp_id not in temp_dict:
                temp_dict[emp_id] = {}
            temp_dict[emp_id][passport_no] = 'checked'
            pristine_records.append(record)
    
    data_dict['records']['record'] = pristine_records
    return data_dict

def load_init_employees_trigger(request):
    script_path = os.path.realpath(os.path.dirname(__file__))
    with open('{}/../../data-devclub-1.xml'.format(script_path)) as xml_file:
        data_devclub_dict = xmltodict.parse(xml_file.read())
        pristine_data = clean_data(data_devclub_dict)
        
        # write json file
        json_data = json.dumps(pristine_data)
        with open('{}/../data-devclub.json'.format(script_path), 'w') as json_file:
            json_file.write(json_data)

        Employee.objects.all().delete()
        employees = pristine_data['records']['record']
        for employee in employees:
            record = Employee(
                emp_id = employee['EMPID'],
                passport = employee['PASSPORT'],
                firstname = employee['FIRSTNAME'],
                lastname = employee['LASTNAME'],
                gender = employee['GENDER'],
                birthday = datetime.strptime(employee['BIRTHDAY'], '%d-%m-%Y'),
                nationality = employee['NATIONALITY'],
                hired = datetime.strptime(employee['HIRED'], '%d-%m-%Y'),
                dept = employee['DEPT'],
                position = employee['POSITION'],
                status = employee['STATUS'],
                region = employee['REGION']
            )
            record.save()

    return HttpResponse('Data clean and loaded')
