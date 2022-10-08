const express = require("express");
const app = express();

app.use("/", express.static(__dirname + "/web_interface/dist"));

app.get("/api", (req, res) => {
    res.json({ changed: count });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Wutthiphon API Server is running on port: " + PORT);
});
