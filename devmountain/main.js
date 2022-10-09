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
    })
    .catch(function (err) {
        console.log("Unable to connect to database: ", err);
    });

// API Request
app.post("/api/update/devclub", async (req, res) => {
    req.body.data_array.map(element => {
        if (element.STATUS == "1") {
            sequelize.query("SELECT * FROM devclub WHERE EMPID = :EMPID OR PASSPORT = :PASSPORT LIMIT 1", { replacements: { EMPID: element.EMPID, PASSPORT: element.PASSPORT }, type: QueryTypes.SELECT }).then((chk) => {
                if (chk.length == 0) {
                    sequelize.query("INSERT INTO devclub (EMPID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION) VALUES(:EMPID,:PASSPORT,:FIRSTNAME,:LASTNAME,:GENDER,:BIRTHDAY,:NATIONALITY,:HIRED,:DEPT,:POSITION,:STATUS,:REGION)",
                        {
                            replacements: {
                                EMPID: element.EMPID,
                                PASSPORT: element.PASSPORT,
                                FIRSTNAME: element.FIRSTNAME,
                                LASTNAME: element.LASTNAME,
                                GENDER: element.GENDER,
                                BIRTHDAY: element.BIRTHDAY,
                                NATIONALITY: element.NATIONALITY,
                                HIRED: element.HIRED,
                                DEPT: element.DEPT,
                                POSITION: element.POSITION,
                                STATUS: element.STATUS,
                                REGION: element.REGION,
                            }
                        }
                    )
                }
            })
        }
    });
    var loaddata = await sequelize.query("SELECT * FROM devclub", { type: QueryTypes.SELECT })
    res.send({
        status: "Success",
        data: loaddata
    });
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
