using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Employees
    {
        private string _empId;
        private string _passPort;
        private string _empFirstName;
        private string _empLastName;
        private string _empGender;
        private string _empBirthday;
        private string _empNationality;
        private string _empHired;
        private string _empDept;
        private string _empPosition;
        private string _empStatus;
        private string _empRegion;
        public string empId
        {
            get {
                return _empId;
            }
            set
            {
                _empId = value;
            }
        }
        public string passPort
        {
            get
            {
                return _passPort;
            }
            set
            {
                _passPort = value;
            }
        }
        public string empFirstName
        {
            get
            {
                return _empFirstName;
            }
            set
            {
                _empFirstName = value;
            }
        }
        public string empLastName
        {
            get
            {
                return _empLastName;
            }
            set
            {
                _empLastName = value;
            }
        }
        public string empGender
        {
            get
            {
                return _empGender;
            }
            set
            {
                _empGender = value;
            }
        }
        public string empBirthday
        {
            get
            {
                return _empBirthday;
            }
            set
            {
                _empBirthday = value;
            }
        }
        public string empNationality
        {
            get
            {
                return _empNationality;
            }
            set
            {
                _empNationality = value;
            }
        }
        public string empHired
        {
            get
            {
                return _empHired;
            }
            set
            {
                _empHired = value;
            }
        }
        public string empDept
        {
            get
            {
                return _empDept;
            }
            set
            {
                _empDept = value;
            }
        }
        public string empPosition
        {
            get
            {
                return _empPosition;
            }
            set
            {
                _empPosition = value;
            }
        }
        public string empStatus
        {
            get
            {
                return _empStatus;
            }
            set
            {
                _empStatus = value;
            }
        }
        public string empRegion
        {
            get
            {
                return _empRegion;
            }
            set
            {
                _empRegion = value;
            }
        }

        public Employees(string id = "", string passport = "", string firstname = "", string lastname = "", 
                        string gender = "", string birthday = "", string nationallity = "", string hired = "", 
                        string dept = "", string position = "", string status = "", string region = "")
        {
            _empId = id;
            _passPort = passport;
            _empFirstName = firstname;
            _empLastName = lastname;
            _empGender = gender;
            _empBirthday = birthday;
            _empNationality = nationallity;
            _empHired = hired;
            _empDept = dept;
            _empPosition = position;
            _empStatus = status;
            _empRegion = region;
        }
        public override string ToString()
        {
            return $"id:\t{_empId}\npassport:\t{_passPort}\nname:\t{_empFirstName} { _empLastName}\ngender:\t{_empGender}\nbirthday:\t{_empBirthday}\nnationallity:\t{_empNationality}\nhired:\t{_empHired}\ndept:\t{_empDept}\nposition:\t{_empPosition}\nstatus:\t{_empStatus}\nregion:\t{_empRegion}";
        }
    }
}
