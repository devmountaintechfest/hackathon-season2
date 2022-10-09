const express = require("express");
const app = express();
const bodyParser = require('body-parser');
var Sequelize = require("sequelize");
const { QueryTypes } = require('sequelize');

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
            tableName: 'devclub',
            timestamps: false,
            freezeTableName: true
        }
        );
    })
    .catch(function (err) {
        console.log("Unable to connect to database: ", err);
    });

// API Request
app.post("/api/update/devclub", (req, res) => {
    console.log(req.body.data_array)

});

app.get("/api/create/view/dept", (req, res) => {
    sequelize.query("SELECT DISTINCT DEPT FROM devclub", { type: QueryTypes.SELECT }).then((depts) => {
        depts.forEach(dept => {
            sequelize.query("DROP VIEW IF EXISTS :view_name", { type: QueryTypes.SELECT, replacements: { view_name: "devclub_dept_" + dept.DEPT } })
            sequelize.query("CREATE VIEW :view_name AS SELECT * FROM devclub WHERE DEPT = :dept_data", { replacements: { view_name: "devclub_dept_" + dept.DEPT, dept_data: dept.DEPT } })
        });
        res.send(depts);
    })
})

app.get("/api/create/view/region", (req, res) => {
    sequelize.query("SELECT DISTINCT REGION FROM devclub", { type: QueryTypes.SELECT }).then((regions) => {
        regions.forEach(region => {
            sequelize.query("DROP VIEW IF EXISTS :view_name", { type: QueryTypes.SELECT, replacements: { view_name: "devclub_region_" + region.REGION } })
            sequelize.query("CREATE VIEW :view_name AS SELECT * FROM devclub WHERE REGION = :region_data", { replacements: { view_name: "devclub_region_" + region.REGION, region_data: region.REGION } })
        });
        res.send(regions);
    })
})

app.get("/api/create/view/nationality", (req, res) => {
    sequelize.query("SELECT DISTINCT NATIONALITY FROM devclub", { type: QueryTypes.SELECT }).then((nationalitys) => {
        nationalitys.forEach(nationality => {
            sequelize.query("DROP VIEW IF EXISTS :view_name", { type: QueryTypes.SELECT, replacements: { view_name: "devclub_nationality_" + nationality.NATIONALITY } })
            sequelize.query("CREATE VIEW :view_name AS SELECT * FROM devclub WHERE NATIONALITY = :nationality_data", { replacements: { view_name: "devclub_nationality_" + nationality.NATIONALITY, nationality_data: nationality.NATIONALITY } })
        });
        res.send(nationalitys);
    })
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Server is running on port: " + PORT);
});
