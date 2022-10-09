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
      <v-container class="fluid">
        <div class="d-flex justify-space-around">
          <v-btn variant="tonal" v-on:click="loadXMLDoc">อ่านไฟล์ XML</v-btn>
          <v-btn variant="tonal" v-on:click="importReadXMLtoDB" color="success" :disabled="read_xml_data.length == 0">
            นำข้อมูลที่อ่านแล้วเข้า DB
            ({{read_xml_data.length}} รายการ)
          </v-btn>
          <v-btn variant="tonal" v-on:click="exportByNATIONALITY" color="error">
            สร้างไฟล์ CSV
          </v-btn>
        </div>
        <v-table>
          <thead>
            <tr>
              <th class="text-left">EMPID</th>
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
              <td>{{ data.GENDER }}</td>
              <td>{{ data.BIRTHDAY }}</td>
              <td>{{ data.NATIONALITY }}</td>
              <td>{{ data.HIRED }}</td>
              <td>{{ data.DEPT }}</td>
              <td>{{ data.POSITION }}</td>
              <td>{{ data.STATUS }}</td>
              <td>{{ data.REGION }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-container>
    </v-main>
  </v-layout>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
export default {
  name: "App",

  components: {
    //   HelloWorld,
  },

  data: () => ({
    //
    read_xml_data: new Array(),
  }),
  methods: {
    loadXMLDoc() {
      var read_xml = new Array();
      var xml = new XMLHttpRequest();
      xml.open("GET", "./data-devclub-1.xml", true);
      xml.send();
      xml.onreadystatechange = () => {
        if (xml.readyState == 4 && xml.status == 200) {
          this.read_xml_data = readXmlFile(this);
        }
      };
      function readXmlFile() {
        var i;
        var xmlDoc = xml.responseXML;
        var x = xmlDoc.getElementsByTagName("record");

        // Start to fetch the data by using TagName
        for (i = 0; i < x.length; i++) {
          if (x[i].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue == 1 )

            if (read_xml.some((item) => item.PASSPORT == x[i].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue) == false) {
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
        return read_xml;
      }
    },

    importReadXMLtoDB() {

    },

    async exportByNATIONALITY() {
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
  },
};
</script>
