const express = require("express");
const app = express();
const bodyParser = require('body-parser');
var Sequelize = require("sequelize");

app.use(bodyParser.json());
app.use("/", express.static(__dirname + "/web_interface/dist"));

// Sequelize Init
var sequelize = new Sequelize(
    "main",
    process.env.USER,
    process.env.PASSWORD,
    {
        host: "0.0.0.0",
        dialect: "sqlite",
        pool: {
            max: 5,
            min: 0,
            idle: 10000
        },
        storage: "./database.sqlite"
    }
);
sequelize
    .authenticate()
    .then(function (err) {
        console.log("Connection established.");
        db_DevClub = sequelize.define("devclub", {
            EMPID: {
                primaryKey: true,
                type: Sequelize.INTEGER
            },
            PASSPORT: {
                type: Sequelize.STRING
            },
            FIRSTNAME: {
                type: Sequelize.STRING
            },
            LASTNAME: {
                type: Sequelize.STRING
            },
            GENDER: {
                type: Sequelize.STRING
            },
            BIRTHDAY: {
                type: Sequelize.DATE
            },
            NATIONALITY: {
                type: Sequelize.STRING
            },
            HIRED: {
                type: Sequelize.STRING
            },
            DEPT: {
                type: Sequelize.STRING
            },
            POSITION: {
                type: Sequelize.STRING
            },
            STATUS: {
                type: Sequelize.TINYINT
            },
            REGION: {
                type: Sequelize.STRING
            },
        }, {
            sequelize,
            tableName: 'devclub',
            timestamps: false,
        }
        );
    })
    .catch(function (err) {
        console.log("Unable to connect to database: ", err);
    });

// API Request
app.get("/api", (req, res) => {
    db_DevClub.findAll().then((data) => {
        res.send(data);
    })
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Server is running on port: " + PORT);
});
