import "vuetify/styles"; // Global CSS has to be imported
import { createApp } from "vue";
import { createVuetify } from "vuetify";
import App from "./App.vue";
import { loadFonts } from "./plugins/webfontloader";
import axios from "axios";
import VueAxios from "vue-axios";

//Import Vuetify Components
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

loadFonts();

const app = createApp(App);
const vuetify = createVuetify({
  components,
  directives,
  ssr: true,
});

app.use(vuetify);
app.use(VueAxios, axios);

app.mount("#app");
