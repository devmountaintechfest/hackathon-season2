(function(){"use strict";var t={9075:function(t,e,a){a(9773);var n=a(9242),l=a(8957),o=a(3396),d=a(7139),r=a(8796),i=a(1556),s=a(5101),c=a(3748),u=a(1489),h=a(3369),m=a(6824),g=a(8521),f=a(3289),p=a(4454),_=a(3140),T=a(4413);const N={class:"d-flex justify-space-around"},w={class:"d-flex justify-space-around",style:{margin:"10px"}},y=(0,o._)("b",null,"จำนวนข้อมูล",-1),E=(0,o._)("b",null,"ข้อมูลจาก",-1),b=(0,o._)("thead",null,[(0,o._)("tr",null,[(0,o._)("th",{class:"text-left"},"EMPID"),(0,o._)("th",{class:"text-left"},"PASSPORT"),(0,o._)("th",{class:"text-left"},"FIRSTNAME"),(0,o._)("th",{class:"text-left"},"LASTNAME"),(0,o._)("th",{class:"text-left"},"GENDER"),(0,o._)("th",{class:"text-left"},"BIRTHDAY"),(0,o._)("th",{class:"text-left"},"NATIONALITY"),(0,o._)("th",{class:"text-left"},"HIRED"),(0,o._)("th",{class:"text-left"},"DEPT"),(0,o._)("th",{class:"text-left"},"POSITION"),(0,o._)("th",{class:"text-left"},"STATUS"),(0,o._)("th",{class:"text-left"},"REGION")])],-1),D={key:0},A={key:1},I={key:0},v={key:1},S={key:2},O={key:1,tonal:"",style:{padding:"10px","margin-top":"10px"}},x=(0,o._)("b",null,"Gender",-1),k=(0,o._)("b",null,"Country",-1),R=(0,o._)("b",null,"Nationality",-1),M=(0,o._)("b",null,"Age",-1),B={key:2,tonal:"",style:{padding:"10px","margin-top":"10px","text-align":"center"}},C=(0,o._)("b",null,"กรุณากดอ่านไฟล์ XML ก่อน",-1),P=[C];function L(t,e,a,n,l,C){const L=(0,o.up)("Pie"),V=(0,o.up)("Doughnut");return(0,o.wg)(),(0,o.j4)(p.s,null,{default:(0,o.w5)((()=>[(0,o.Wm)(r.L,{color:"primary",density:"compact"},{prepend:(0,o.w5)((()=>[(0,o.Wm)(f.t,{large:""},{default:(0,o.w5)((()=>[(0,o.Uk)(" mdi-domain ")])),_:1})])),append:(0,o.w5)((()=>[])),default:(0,o.w5)((()=>[(0,o.Wm)(i.o,null,{default:(0,o.w5)((()=>[(0,o.Uk)("DevClub")])),_:1})])),_:1}),(0,o.Wm)(_.O,null,{default:(0,o.w5)((()=>[(0,o.Wm)(h.K,{fluid:""},{default:(0,o.w5)((()=>[(0,o._)("div",N,[(0,o.Wm)(s.T,{variant:"tonal",onClick:C.loadXMLDocWithoutFilter},{default:(0,o.w5)((()=>[(0,o.Uk)("อ่านไฟล์ XML (ไม่กรอง)")])),_:1},8,["onClick"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.loadXMLDoc},{default:(0,o.w5)((()=>[(0,o.Uk)("อ่านไฟล์ XML (กรองข้อมูล)")])),_:1},8,["onClick"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.loadDB},{default:(0,o.w5)((()=>[(0,o.Uk)("เรียกข้อมูลจาก DB")])),_:1},8,["onClick"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.importReadXMLtoDB,color:"success",disabled:0==t.read_xml_data.length},{default:(0,o.w5)((()=>[(0,o.Uk)(" นำข้อมูลเข้า DB ")])),_:1},8,["onClick","disabled"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.loadJSON,color:"success",disabled:0==t.read_xml_data.length},{default:(0,o.w5)((()=>[(0,o.Uk)(" Export JSON ")])),_:1},8,["onClick","disabled"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.exportCSVAll,color:"error",disabled:0==t.read_xml_data.length},{default:(0,o.w5)((()=>[(0,o.Uk)(" Export CSV พนักงานทั้งหมด ")])),_:1},8,["onClick","disabled"]),(0,o.Wm)(s.T,{variant:"tonal",onClick:C.exportCSVByNATIONALITY,color:"error",disabled:0==t.read_xml_data.length},{default:(0,o.w5)((()=>[(0,o.Uk)(" Export CSV แยกตามสัญชาติ ")])),_:1},8,["onClick","disabled"])])])),_:1}),(0,o.Wm)(h.K,null,{default:(0,o.w5)((()=>[(0,o._)("div",w,[(0,o.Wm)(c.f,{modelValue:t.toggle_exclusive,"onUpdate:modelValue":e[2]||(e[2]=e=>t.toggle_exclusive=e)},{default:(0,o.w5)((()=>[(0,o.Wm)(s.T,{onClick:e[0]||(e[0]=e=>t.page_select="table")},{default:(0,o.w5)((()=>[(0,o.Wm)(f.t,null,{default:(0,o.w5)((()=>[(0,o.Uk)("mdi-table")])),_:1}),(0,o.Uk)("  Table ")])),_:1}),(0,o.Wm)(s.T,{onClick:e[1]||(e[1]=e=>t.page_select="chart")},{default:(0,o.w5)((()=>[(0,o.Wm)(f.t,null,{default:(0,o.w5)((()=>[(0,o.Uk)("mdi-chart-areaspline")])),_:1}),(0,o.Uk)("  Chart ")])),_:1})])),_:1},8,["modelValue"])]),"table"==t.page_select&&t.read_xml_data.length>0?((0,o.wg)(),(0,o.j4)(u._,{key:0,tonal:"",style:{padding:"10px","margin-top":"10px"}},{default:(0,o.w5)((()=>[y,(0,o.Uk)(" "+(0,d.zw)(t.read_xml_data.length)+" รายการ | ",1),E,(0,o.Uk)(" "+(0,d.zw)(t.now_data)+" ",1),(0,o.Wm)(T.Y,null,{default:(0,o.w5)((()=>[b,(0,o._)("tbody",null,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(t.read_xml_data,(t=>((0,o.wg)(),(0,o.iD)("tr",{key:t.EMPID},[(0,o._)("td",null,(0,d.zw)(t.EMPID),1),(0,o._)("td",null,(0,d.zw)(t.PASSPORT),1),(0,o._)("td",null,(0,d.zw)(t.FIRSTNAME),1),(0,o._)("td",null,(0,d.zw)(t.LASTNAME),1),(0,o._)("td",null,[0==t.STATUS?((0,o.wg)(),(0,o.iD)("label",D,"Male")):(0,o.kq)("",!0),1==t.STATUS?((0,o.wg)(),(0,o.iD)("label",A,"Female")):(0,o.kq)("",!0)]),(0,o._)("td",null,(0,d.zw)(t.BIRTHDAY),1),(0,o._)("td",null,(0,d.zw)(t.NATIONALITY),1),(0,o._)("td",null,(0,d.zw)(t.HIRED),1),(0,o._)("td",null,(0,d.zw)(t.DEPT),1),(0,o._)("td",null,(0,d.zw)(t.POSITION),1),(0,o._)("td",null,[1==t.STATUS?((0,o.wg)(),(0,o.iD)("label",I,"Active")):(0,o.kq)("",!0),2==t.STATUS?((0,o.wg)(),(0,o.iD)("label",v,"Resigned")):(0,o.kq)("",!0),3==t.STATUS?((0,o.wg)(),(0,o.iD)("label",S,"Retired")):(0,o.kq)("",!0)]),(0,o._)("td",null,(0,d.zw)(t.REGION),1)])))),128))])])),_:1})])),_:1})):(0,o.kq)("",!0),"chart"==t.page_select&&t.read_xml_data.length>0?((0,o.wg)(),(0,o.iD)("div",O,[(0,o.Wm)(u._,{style:{"text-align":"center",padding:"10px"}},{default:(0,o.w5)((()=>[(0,o.Wm)(m.o,{"no-gutters":""},{default:(0,o.w5)((()=>[(0,o.Wm)(g.D,{cols:"12",sm:"6"},{default:(0,o.w5)((()=>[x,(0,o.Wm)(L,{"chart-options":t.chartOptions,"chart-data":t.GenderchartData,"chart-id":t.chartId,"dataset-id-key":t.datasetIdKey,plugins:t.plugins,"css-classes":t.cssClasses,styles:t.styles,width:t.width,height:t.height},null,8,["chart-options","chart-data","chart-id","dataset-id-key","plugins","css-classes","styles","width","height"])])),_:1}),(0,o.Wm)(g.D,{cols:"12",sm:"6"},{default:(0,o.w5)((()=>[k,(0,o.Wm)(L,{"chart-options":t.chartOptions,"chart-data":t.CountrychartData,width:t.width,height:t.height},null,8,["chart-options","chart-data","width","height"])])),_:1}),(0,o.Wm)(g.D,{cols:"12",sm:"6"},{default:(0,o.w5)((()=>[R,(0,o.Wm)(V,{"chart-options":t.chartOptions,"chart-data":t.NationchartData,width:t.width,height:t.height},null,8,["chart-options","chart-data","width","height"])])),_:1}),(0,o.Wm)(g.D,{cols:"12",sm:"6"},{default:(0,o.w5)((()=>[M,(0,o.Wm)(V,{"chart-options":t.chartOptions,"chart-data":t.AgechartData,width:t.width,height:"150"},null,8,["chart-options","chart-data","width"])])),_:1})])),_:1})])),_:1})])):(0,o.kq)("",!0),0==t.read_xml_data.length?((0,o.wg)(),(0,o.iD)("div",B,P)):(0,o.kq)("",!0)])),_:1})])),_:1})])),_:1})}a(7658);var V=a(6294),j=a(741);j.kL.register(j.Dx,j.u,j.De,j.qi,j.uw,j.f$);var U={name:"App",components:{Pie:V.by,Doughnut:V.$I},data:()=>({read_xml_data:new Array,now_data:"",page_select:"table",chartOptions:{responsive:!0},GenderchartData:{labels:["Male","Female"],datasets:[{backgroundColor:["#00D8FF","#E46651"],data:[0,0]}]},CountrychartData:{labels:[],datasets:[{backgroundColor:[],data:[]}]},NationchartData:{labels:[],datasets:[{backgroundColor:[],data:[]}]},AgechartData:{labels:[],datasets:[{backgroundColor:["#fcdc83"],data:[]}]}}),methods:{ChartInit(){this.GenderchartData.datasets[0].data[0]=this.read_xml_data.filter((t=>"0"==t.GENDER)).length,this.GenderchartData.datasets[0].data[1]=this.read_xml_data.filter((t=>"1"==t.GENDER)).length,this.CountrychartData.labels=[...new Set(this.read_xml_data.map((t=>t.REGION)))],this.CountrychartData.datasets[0].data=this.CountrychartData.labels.map((t=>this.read_xml_data.filter((e=>e.REGION==t)).length)),this.CountrychartData.datasets[0].backgroundColor=this.CountrychartData.labels.map((()=>"#"+Math.floor(16777215*Math.random()).toString(16))),this.NationchartData.labels=[...new Set(this.read_xml_data.map((t=>t.NATIONALITY)))],this.NationchartData.datasets[0].data=this.NationchartData.labels.map((t=>this.read_xml_data.filter((e=>e.NATIONALITY==t)).length)),this.NationchartData.datasets[0].backgroundColor=this.NationchartData.labels.map((()=>"#"+Math.floor(16777215*Math.random()).toString(16))),this.AgechartData.labels=[...new Set(this.read_xml_data.map((t=>Math.floor(Math.abs(new Date-new Date(t.BIRTHDAY.split("-")[2],t.BIRTHDAY.split("-")[1],t.BIRTHDAY.split("-")[0]))/31536e6))))],this.AgechartData.datasets[0].data=this.AgechartData.labels.map((t=>this.read_xml_data.filter((e=>Math.floor(Math.abs(new Date-new Date(e.BIRTHDAY.split("-")[2],e.BIRTHDAY.split("-")[1],e.BIRTHDAY.split("-")[0]))/31536e6)==t)).length)),console.log(this.AgechartData.datasets[0].data),this.AgechartData.datasets[0].backgroundColor=this.AgechartData.labels.map((()=>"#"+Math.floor(16777215*Math.random()).toString(16)))},loadXMLDocWithoutFilter(){var t=new Array,e=new XMLHttpRequest;function a(){var a,n=e.responseXML,l=n.getElementsByTagName("record");for(a=0;a<l.length;a++)t.push({EMPID:l[a].getElementsByTagName("EMPID")[0].childNodes[0].nodeValue,PASSPORT:l[a].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue,FIRSTNAME:l[a].getElementsByTagName("FIRSTNAME")[0].childNodes[0].nodeValue,LASTNAME:l[a].getElementsByTagName("LASTNAME")[0].childNodes[0].nodeValue,GENDER:l[a].getElementsByTagName("GENDER")[0].childNodes[0].nodeValue,BIRTHDAY:l[a].getElementsByTagName("BIRTHDAY")[0].childNodes[0].nodeValue,NATIONALITY:l[a].getElementsByTagName("NATIONALITY")[0].childNodes[0].nodeValue,HIRED:l[a].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue,DEPT:l[a].getElementsByTagName("DEPT")[0].childNodes[0].nodeValue,POSITION:l[a].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue,STATUS:l[a].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue,REGION:l[a].getElementsByTagName("REGION")[0].childNodes[0].nodeValue});return t}e.open("GET","./data-devclub-1.xml",!0),e.send(),e.onreadystatechange=()=>{4==e.readyState&&200==e.status&&(this.read_xml_data=a(this),this.now_data="XML File",this.ChartInit())}},loadXMLDoc(){var t=new Array,e=new XMLHttpRequest;function a(){var a,n=e.responseXML,l=n.getElementsByTagName("record"),o=["Airhostess","Pilot","Steward"];for(a=0;a<l.length;a++)if(1==l[a].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue&&o.includes(l[a].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue)&&0==t.some((t=>t.PASSPORT==l[a].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue))){var d=new Date,r=l[a].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue.split("-")[0],i=l[a].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue.split("-")[1],s=l[a].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue.split("-")[2],c=new Date(s,i,r),u=Math.abs(d-c),h=Math.ceil(u/864e5);1095<=h&&t.push({EMPID:l[a].getElementsByTagName("EMPID")[0].childNodes[0].nodeValue,PASSPORT:l[a].getElementsByTagName("PASSPORT")[0].childNodes[0].nodeValue,FIRSTNAME:l[a].getElementsByTagName("FIRSTNAME")[0].childNodes[0].nodeValue,LASTNAME:l[a].getElementsByTagName("LASTNAME")[0].childNodes[0].nodeValue,GENDER:l[a].getElementsByTagName("GENDER")[0].childNodes[0].nodeValue,BIRTHDAY:l[a].getElementsByTagName("BIRTHDAY")[0].childNodes[0].nodeValue,NATIONALITY:l[a].getElementsByTagName("NATIONALITY")[0].childNodes[0].nodeValue,HIRED:l[a].getElementsByTagName("HIRED")[0].childNodes[0].nodeValue,DEPT:l[a].getElementsByTagName("DEPT")[0].childNodes[0].nodeValue,POSITION:l[a].getElementsByTagName("POSITION")[0].childNodes[0].nodeValue,STATUS:l[a].getElementsByTagName("STATUS")[0].childNodes[0].nodeValue,REGION:l[a].getElementsByTagName("REGION")[0].childNodes[0].nodeValue})}return t}e.open("GET","./data-devclub-1.xml",!0),e.send(),e.onreadystatechange=()=>{4==e.readyState&&200==e.status&&(this.read_xml_data=a(this),this.now_data="XML File",this.ChartInit())}},importReadXMLtoDB(){this.axios.post("api/update/devclub",{data_array:this.read_xml_data}).then((t=>{this.read_xml_data=t.data.data,this.now_data="Sqlite3 Database"}))},loadDB(){this.axios.get("api/get/devclub").then((t=>{0!=t.data.data.length&&(this.read_xml_data=t.data.data,this.now_data="Sqlite3 Database",this.ChartInit())}))},loadJSON(){const t=JSON.stringify(this.read_xml_data),e=new Blob([t],{type:"text/plain"}),a=document.createEvent("MouseEvents"),n=document.createElement("a");n.download="sqlite.json",n.href=window.URL.createObjectURL(e),n.dataset.downloadurl=["text/json",n.download,n.href].join(":"),a.initEvent("click",!0,!1,window,0,0,0,0,0,!1,!1,!1,!1,0,null),n.dispatchEvent(a)},async exportCSVByNATIONALITY(){var t=[...new Set(this.read_xml_data.map((t=>t.NATIONALITY)))];for await(let a of t){var e=this.read_xml_data.filter((t=>t.NATIONALITY==a));let t="data:text/csv;charset=utf-8,";t+=[Object.keys(e[0]).join(","),...e.map((t=>Object.values(t).join(",")))].join("\n").replace(/(^\[)|(\]$)/gm,"");const n=encodeURI(t),l=document.createElement("a");l.setAttribute("href",n),l.setAttribute("download",a+".csv"),l.click()}},async exportCSVAll(){let t="data:text/csv;charset=utf-8,";t+=[Object.keys(this.read_xml_data[0]).join(","),...this.read_xml_data.map((t=>Object.values(t).join(",")))].join("\n").replace(/(^\[)|(\]$)/gm,"");const e=encodeURI(t),a=document.createElement("a");a.setAttribute("href",e),a.setAttribute("download","All Employee.csv"),a.click()}},beforeMount(){this.loadDB()}},W=a(89);const Y=(0,W.Z)(U,[["render",L]]);var H=Y;async function G(){const t=await a.e(461).then(a.t.bind(a,3657,23));t.load({google:{families:["Roboto:100,300,400,500,700,900&display=swap"]}})}var F=a(70),q=a(6423),X=a(119),z=a(8600);G();const J=(0,n.ri)(H),K=(0,l.Rd)({components:X,directives:z,ssr:!0});J.use(K),J.use(q.Z,F.Z),J.mount("#app")}},e={};function a(n){var l=e[n];if(void 0!==l)return l.exports;var o=e[n]={id:n,loaded:!1,exports:{}};return t[n](o,o.exports,a),o.loaded=!0,o.exports}a.m=t,function(){a.amdO={}}(),function(){var t=[];a.O=function(e,n,l,o){if(!n){var d=1/0;for(c=0;c<t.length;c++){n=t[c][0],l=t[c][1],o=t[c][2];for(var r=!0,i=0;i<n.length;i++)(!1&o||d>=o)&&Object.keys(a.O).every((function(t){return a.O[t](n[i])}))?n.splice(i--,1):(r=!1,o<d&&(d=o));if(r){t.splice(c--,1);var s=l();void 0!==s&&(e=s)}}return e}o=o||0;for(var c=t.length;c>0&&t[c-1][2]>o;c--)t[c]=t[c-1];t[c]=[n,l,o]}}(),function(){a.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return a.d(e,{a:e}),e}}(),function(){var t,e=Object.getPrototypeOf?function(t){return Object.getPrototypeOf(t)}:function(t){return t.__proto__};a.t=function(n,l){if(1&l&&(n=this(n)),8&l)return n;if("object"===typeof n&&n){if(4&l&&n.__esModule)return n;if(16&l&&"function"===typeof n.then)return n}var o=Object.create(null);a.r(o);var d={};t=t||[null,e({}),e([]),e(e)];for(var r=2&l&&n;"object"==typeof r&&!~t.indexOf(r);r=e(r))Object.getOwnPropertyNames(r).forEach((function(t){d[t]=function(){return n[t]}}));return d["default"]=function(){return n},a.d(o,d),o}}(),function(){a.d=function(t,e){for(var n in e)a.o(e,n)&&!a.o(t,n)&&Object.defineProperty(t,n,{enumerable:!0,get:e[n]})}}(),function(){a.f={},a.e=function(t){return Promise.all(Object.keys(a.f).reduce((function(e,n){return a.f[n](t,e),e}),[]))}}(),function(){a.u=function(t){return"js/webfontloader.2af99afc.js"}}(),function(){a.miniCssF=function(t){}}(),function(){a.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){a.hmd=function(t){return t=Object.create(t),t.children||(t.children=[]),Object.defineProperty(t,"exports",{enumerable:!0,set:function(){throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+t.id)}}),t}}(),function(){a.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){var t={},e="dev-mountain:";a.l=function(n,l,o,d){if(t[n])t[n].push(l);else{var r,i;if(void 0!==o)for(var s=document.getElementsByTagName("script"),c=0;c<s.length;c++){var u=s[c];if(u.getAttribute("src")==n||u.getAttribute("data-webpack")==e+o){r=u;break}}r||(i=!0,r=document.createElement("script"),r.charset="utf-8",r.timeout=120,a.nc&&r.setAttribute("nonce",a.nc),r.setAttribute("data-webpack",e+o),r.src=n),t[n]=[l];var h=function(e,a){r.onerror=r.onload=null,clearTimeout(m);var l=t[n];if(delete t[n],r.parentNode&&r.parentNode.removeChild(r),l&&l.forEach((function(t){return t(a)})),e)return e(a)},m=setTimeout(h.bind(null,void 0,{type:"timeout",target:r}),12e4);r.onerror=h.bind(null,r.onerror),r.onload=h.bind(null,r.onload),i&&document.head.appendChild(r)}}}(),function(){a.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){a.p="/"}(),function(){var t={143:0};a.f.j=function(e,n){var l=a.o(t,e)?t[e]:void 0;if(0!==l)if(l)n.push(l[2]);else{var o=new Promise((function(a,n){l=t[e]=[a,n]}));n.push(l[2]=o);var d=a.p+a.u(e),r=new Error,i=function(n){if(a.o(t,e)&&(l=t[e],0!==l&&(t[e]=void 0),l)){var o=n&&("load"===n.type?"missing":n.type),d=n&&n.target&&n.target.src;r.message="Loading chunk "+e+" failed.\n("+o+": "+d+")",r.name="ChunkLoadError",r.type=o,r.request=d,l[1](r)}};a.l(d,i,"chunk-"+e,e)}},a.O.j=function(e){return 0===t[e]};var e=function(e,n){var l,o,d=n[0],r=n[1],i=n[2],s=0;if(d.some((function(e){return 0!==t[e]}))){for(l in r)a.o(r,l)&&(a.m[l]=r[l]);if(i)var c=i(a)}for(e&&e(n);s<d.length;s++)o=d[s],a.o(t,o)&&t[o]&&t[o][0](),t[o]=0;return a.O(c)},n=self["webpackChunkdev_mountain"]=self["webpackChunkdev_mountain"]||[];n.forEach(e.bind(null,0)),n.push=e.bind(null,n.push.bind(n))}();var n=a.O(void 0,[998],(function(){return a(9075)}));n=a.O(n)})();
//# sourceMappingURL=app.918faad7.js.map