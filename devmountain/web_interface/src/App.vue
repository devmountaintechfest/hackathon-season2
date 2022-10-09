<template>
  <v-layout>
    <v-app-bar color="primary" density="compact">
      <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template>

      <v-app-bar-title>Dev Club</v-app-bar-title>

      <template v-slot:append>
        <!-- <v-btn icon="mdi-dots-vertical"></v-btn> -->
      </template>
    </v-app-bar>

    <v-main>
      <v-container class="fluid">
        <div class="d-flex justify-space-between">
          <v-btn variant="tonal" v-on:click="loadXMLDoc">อ่านไฟล์ XML</v-btn>
        </div>
        {{ read_xml_data }}

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
          // if (x[i].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue == 1 ){
          //   if (read_xml.some((item) => item.PASSPORT == x[i].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue) == false) {
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
              // }
            // }
        }
        return read_xml;
      }
    },
  },
};
</script>
