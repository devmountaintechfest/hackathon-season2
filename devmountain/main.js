const express = require("express");
const app = express();
var Sequelize = require("sequelize");

app.use("/", express.static(__dirname + "/web_interface/dist"));

app.get("/api", (req, res) => {
    res.json({ test: "Hello World" });
});

// Sequelize Init
var sequelize = new Sequelize(
    "devclub",
    "",
    "",
    {
        host: "0.0.0.0",
        dialect: "sqlite",
        pool: {
            max: 5,
            min: 0,
            idle: 10000
        },
        storage: "./web_interface/dist/database.sqlite"
    }
);
sequelize
    .authenticate()
    .then(function (err) {
        console.log("Connection established.");
    })
    .catch(function (err) {
        console.log("Unable to connect to database: ", err);
    });

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Server is running on port: " + PORT);
});
