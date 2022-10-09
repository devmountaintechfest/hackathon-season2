<template>
  <v-layout>
    <v-app-bar color="primary" density="compact">
      <template v-slot:prepend>
        <v-icon large>
          mdi-domain
        </v-icon>
      </template>

      <v-app-bar-title>DevClub</v-app-bar-title>

      <template v-slot:append>
        <!-- <v-btn icon="mdi-dots-vertical"></v-btn> -->
      </template>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <div class="d-flex justify-space-around">
          <v-btn variant="tonal" v-on:click="loadXMLDocWithoutFilter">อ่านไฟล์ XML (ไม่กรอง)</v-btn>
          <v-btn variant="tonal" v-on:click="loadXMLDoc">อ่านไฟล์ XML (กรองข้อมูล)</v-btn>
          <v-btn variant="tonal" v-on:click="loadDB">เรียกข้อมูลจาก DB</v-btn>
          <v-btn variant="tonal" v-on:click="importReadXMLtoDB" color="success" :disabled="read_xml_data.length == 0">
            นำข้อมูลเข้า DB
          </v-btn>
          <v-btn variant="tonal" v-on:click="loadJSON" color="success" :disabled="read_xml_data.length == 0">
            Export JSON
          </v-btn>
          <v-btn variant="tonal" v-on:click="exportCSVAll" color="error" :disabled="read_xml_data.length == 0">
            Export CSV พนักงานทั้งหมด
          </v-btn>
          <v-btn variant="tonal" v-on:click="exportCSVByNATIONALITY" color="error"
            :disabled="read_xml_data.length == 0">
            Export CSV แยกตามสัญชาติ
          </v-btn>
        </div>
      </v-container>
      <v-container>

        <div class="d-flex justify-space-around" style="margin: 10px;">
          <v-btn-toggle v-model="toggle_exclusive">
            <v-btn v-on:click="page_select = 'table'">
              <v-icon>mdi-table</v-icon>
              &nbsp;Table
            </v-btn>

            <v-btn v-on:click="page_select = 'chart'">
              <v-icon>mdi-chart-areaspline</v-icon>
              &nbsp;Chart
            </v-btn>
          </v-btn-toggle>
        </div>

        <v-card tonal style="padding: 10px;margin-top: 10px;" v-if="page_select == 'table' && read_xml_data.length > 0">
          <b>จำนวนข้อมูล</b> {{read_xml_data.length}} รายการ | <b>ข้อมูลจาก</b> {{now_data}}
          <v-table>
            <thead>
              <tr>
                <th class=" text-left">EMPID</th>
                <th class="text-left">PASSPORT</th>
                <th class="text-left">FIRSTNAME</th>
                <th class="text-left">LASTNAME</th>
                <th class="text-left">GENDER</th>
                <th class="text-left">BIRTHDAY</th>
                <th class="text-left">NATIONALITY</th>
                <th class="text-left">HIRED</th>
                <th class="text-left">DEPT</th>
                <th class="text-left">POSITION</th>
                <th class="text-left">STATUS</th>
                <th class="text-left">REGION</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="data in read_xml_data" :key="data.EMPID">
                <td>{{ data.EMPID }}</td>
                <td>{{ data.PASSPORT }}</td>
                <td>{{ data.FIRSTNAME }}</td>
                <td>{{ data.LASTNAME }}</td>
                <td>
                  <label v-if="data.STATUS == 0">Male</label>
                  <label v-if="data.STATUS == 1">Female</label>
                </td>
                <td>{{ data.BIRTHDAY }}</td>
                <td>{{ data.NATIONALITY }}</td>
                <td>{{ data.HIRED }}</td>
                <td>{{ data.DEPT }}</td>
                <td>{{ data.POSITION }}</td>
                <td>
                  <label v-if="data.STATUS == 1">Active</label>
                  <label v-if="data.STATUS == 2">Resigned</label>
                  <label v-if="data.STATUS == 3">Retired</label>
                </td>
                <td>{{ data.REGION }}</td>
              </tr>
            </tbody>
          </v-table>
        </v-card>

        <div tonal style="padding: 10px;margin-top: 10px;" v-if="page_select == 'chart' && read_xml_data.length > 0">
          <v-card style="text-align: center;padding: 10px">
            <v-row no-gutters>
              <v-col cols="12" sm="6">
                <b>Gender</b>
                <Pie :chart-options="chartOptions" :chart-data="GenderchartData" :chart-id="chartId"
                  :dataset-id-key="datasetIdKey" :plugins="plugins" :css-classes="cssClasses" :styles="styles"
                  :width="width" :height="height" />
              </v-col>
              <v-col cols="12" sm="6">
                <b>Country</b>
                <Pie :chart-options="chartOptions" :chart-data="CountrychartData" :width="width" :height="height" />
              </v-col>
            </v-row>
            <hr style="margin: 15px">
            <v-row no-gutters style="margin-top: 15px">
              <v-col cols="12" sm="6">
                <b>Nationality</b>
                <Doughnut :chart-options="chartOptions" :chart-data="NationchartData" :width="width" :height="height" />
              </v-col>
              <v-col cols="12" sm="6">
                <b>Age</b>
                <Doughnut :chart-options="chartOptions" :chart-data="AgechartData" :width="width" height="150" />
              </v-col>
            </v-row>
          </v-card>
        </div>

        <div tonal style="padding: 10px;margin-top: 10px;text-align:center" v-if="read_xml_data.length == 0">
          <b>กรุณากดอ่านไฟล์ XML ก่อน</b>
        </div>
      </v-container>
    </v-main>
  </v-layout>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import { Pie, Doughnut } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)

export default {
  name: "App",
  components: {
    Pie,
    Doughnut,
  },

  data: () => ({
    read_xml_data: new Array(),
    now_data: "",
    page_select: 'table', //table, chart
    chartOptions: {
      responsive: true
    },

    GenderchartData: {
      labels: ['Male', 'Female'],
      datasets: [{
        backgroundColor: ['#00D8FF', '#E46651'],
        data: [0, 0]
      }]
    },
    CountrychartData: {
      labels: [],
      datasets: [{
        backgroundColor: [],
        data: []
      }]
    },
    NationchartData: {
      labels: [],
      datasets: [{
        backgroundColor: [],
        data: []
      }]
    },
    AgechartData: {
      labels: [],
      datasets: [{
        backgroundColor: ['#fcdc83'],
        data: []
      }]
    },
  }),

  methods: {
    ChartInit() {
      this.GenderchartData.datasets[0].data[0] = this.read_xml_data.filter(item => { return item.GENDER == '0' }).length
      this.GenderchartData.datasets[0].data[1] = this.read_xml_data.filter(item => { return item.GENDER == '1' }).length
      // Region Chart
      this.CountrychartData.labels = [...new Set(this.read_xml_data.map(item => { return item.REGION }))]
      this.CountrychartData.datasets[0].data = this.CountrychartData.labels.map(item => {
        return this.read_xml_data.filter(item2 => { return item2.REGION == item }).length
      })
      this.CountrychartData.datasets[0].backgroundColor = this.CountrychartData.labels.map(() => {
        return '#' + Math.floor(Math.random() * 16777215).toString(16)
      })
      // Nationarity Chart
      this.NationchartData.labels = [...new Set(this.read_xml_data.map(item => { return item.NATIONALITY }))]
      this.NationchartData.datasets[0].data = this.NationchartData.labels.map(item => {
        return this.read_xml_data.filter(item2 => { return item2.NATIONALITY == item }).length
      })
      this.NationchartData.datasets[0].backgroundColor = this.NationchartData.labels.map(() => {
        return '#' + Math.floor(Math.random() * 16777215).toString(16)
      })
      // Age Chart
      this.AgechartData.labels = [...new Set(this.read_xml_data.map(item => { return Math.floor(Math.abs(new Date() - new Date(item.BIRTHDAY.split("-")[2], item.BIRTHDAY.split("-")[1], item.BIRTHDAY.split("-")[0])) / (1000 * 60 * 60 * 24 * 365)) }))]
      this.AgechartData.datasets[0].data = this.AgechartData.labels.map(item => {
        return this.read_xml_data.filter(item2 => { return Math.floor(Math.abs(new Date() - new Date(item2.BIRTHDAY.split("-")[2], item2.BIRTHDAY.split("-")[1], item2.BIRTHDAY.split("-")[0])) / (1000 * 60 * 60 * 24 * 365)) == item }).length
      })
      console.log(this.AgechartData.datasets[0].data)
      this.AgechartData.datasets[0].backgroundColor = this.AgechartData.labels.map(() => {
        return '#' + Math.floor(Math.random() * 16777215).toString(16)
      })
    },

    loadXMLDocWithoutFilter() {
      var read_xml = new Array();
      var xml = new XMLHttpRequest();
      xml.open("GET", "./data-devclub-1.xml", true);
      xml.send();
      xml.onreadystatechange = () => {
        if (xml.readyState == 4 && xml.status == 200) {
          this.read_xml_data = readXmlFile(this);
          this.now_data = "XML File";
          this.ChartInit()
        }
      };
      function readXmlFile() {
        var i;
        var xmlDoc = xml.responseXML;
        var x = xmlDoc.getElementsByTagName("record");

        // Start to fetch the data by using TagName
        for (i = 0; i < x.length; i++) {
          read_xml.push({
            EMPID: x[i].getElementsByTagName("EMPID")[0].childNodes[0].nodeValue,
            PASSPORT: x[i].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue,
            FIRSTNAME: x[i].getElementsByTagName("FIRSTNAME")[0].childNodes[0].nodeValue,
            LASTNAME: x[i].getElementsByTagName("LASTNAME")[0].childNodes[0].nodeValue,
            GENDER: x[i].getElementsByTagName("GENDER")[0].childNodes[0].nodeValue,
            BIRTHDAY: x[i].getElementsByTagName("BIRTHDAY")[0].childNodes[0].nodeValue,
            NATIONALITY: x[i].getElementsByTagName("NATIONALITY")[0].childNodes[0]
              .nodeValue,
            HIRED: x[i].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue,
            DEPT: x[i].getElementsByTagName("DEPT")[0].childNodes[0].nodeValue,
            POSITION: x[i].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue,
            STATUS: x[i].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue,
            REGION: x[i].getElementsByTagName("REGION")[0].childNodes[0].nodeValue,
          });
        }
        return read_xml;
      }
    },

    loadXMLDoc() {
      var read_xml = new Array();
      var xml = new XMLHttpRequest();
      xml.open("GET", "./data-devclub-1.xml", true);
      xml.send();
      xml.onreadystatechange = () => {
        if (xml.readyState == 4 && xml.status == 200) {
          this.read_xml_data = readXmlFile(this);
          this.now_data = "XML File";
          this.ChartInit()
        }
      };
      function readXmlFile() {
        var i;
        var xmlDoc = xml.responseXML;
        var x = xmlDoc.getElementsByTagName("record");
        var position_accept = ['Airhostess', 'Pilot', 'Steward']

        // Start to fetch the data by using TagName
        for (i = 0; i < x.length; i++) {
          if (x[i].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue == 1 && position_accept.includes(x[i].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue)) {
            if (read_xml.some((item) => item.PASSPORT == x[i].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue) == false) {
              // Check 3 Year
              var now_date = new Date();
              var hired_day = (x[i].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue).split("-")[0];
              var hired_month = (x[i].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue).split("-")[1]
              var hired_year = (x[i].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue).split("-")[2]
              var hired_date = new Date(hired_year, hired_month, hired_day);
              var diffTime = Math.abs(now_date - hired_date);
              var diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
              if (1095 <= diffDays) {
                read_xml.push({
                  EMPID: x[i].getElementsByTagName("EMPID")[0].childNodes[0].nodeValue,
                  PASSPORT: x[i].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue,
                  FIRSTNAME: x[i].getElementsByTagName("FIRSTNAME")[0].childNodes[0].nodeValue,
                  LASTNAME: x[i].getElementsByTagName("LASTNAME")[0].childNodes[0].nodeValue,
                  GENDER: x[i].getElementsByTagName("GENDER")[0].childNodes[0].nodeValue,
                  BIRTHDAY: x[i].getElementsByTagName("BIRTHDAY")[0].childNodes[0].nodeValue,
                  NATIONALITY: x[i].getElementsByTagName("NATIONALITY")[0].childNodes[0]
                    .nodeValue,
                  HIRED: x[i].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue,
                  DEPT: x[i].getElementsByTagName("DEPT")[0].childNodes[0].nodeValue,
                  POSITION: x[i].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue,
                  STATUS: x[i].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue,
                  REGION: x[i].getElementsByTagName("REGION")[0].childNodes[0].nodeValue,
                });
              }
            }
          }
        }
        return read_xml;
      }
    },

    importReadXMLtoDB() {
      this.axios
        .post("api/update/devclub", {
          data_array: this.read_xml_data,
        })
        .then((res) => {
          this.read_xml_data = res.data.data
          this.now_data = "Sqlite3 Database";
        })
    },

    loadDB() {
      this.axios
        .get("api/get/devclub")
        .then((res) => {
          if (res.data.data.length != 0) {
            this.read_xml_data = res.data.data
            this.now_data = "Sqlite3 Database";
            this.ChartInit()
          }
        })
    },

    loadJSON() {
      const data = JSON.stringify(this.read_xml_data)
      const blob = new Blob([data], { type: 'text/plain' })
      const e = document.createEvent('MouseEvents'),
        a = document.createElement('a');
      a.download = "sqlite.json";
      a.href = window.URL.createObjectURL(blob);
      a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
      e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
      a.dispatchEvent(e);
    },

    async exportCSVByNATIONALITY() {
      var nation_lists = [...new Set(this.read_xml_data.map((item) => { return item.NATIONALITY }))];
      for await (let nation of nation_lists) {
        var data_by_nation = this.read_xml_data.filter((item) => {
          return item.NATIONALITY == nation;
        })

        let csvContent = "data:text/csv;charset=utf-8,";
        csvContent += [
          Object.keys(data_by_nation[0]).join(","),
          ...data_by_nation.map(item => Object.values(item).join(","))
        ]
          .join("\n")
          .replace(/(^\[)|(\]$)/gm, "");

        const data = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", data);
        link.setAttribute("download", nation + ".csv");
        link.click();
      }
    },

    async exportCSVAll() {
      let csvContent = "data:text/csv;charset=utf-8,";
      csvContent += [
        Object.keys(this.read_xml_data[0]).join(","),
        ...this.read_xml_data.map(item => Object.values(item).join(","))
      ]
        .join("\n")
        .replace(/(^\[)|(\]$)/gm, "");

      const data = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", data);
      link.setAttribute("download", "All Employee.csv");
      link.click();
    },
  },
  beforeMount() {
    this.loadDB()
  },
};
</script>
