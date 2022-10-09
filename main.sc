import $ivy.{
	`org.xerial:sqlite-jdbc:3.39.3.0`
}

import java.net._
import java.io.{ByteArrayOutputStream, BufferedWriter, PrintWriter, BufferedReader, FileReader, FileOutputStream, File}
import java.text.{DecimalFormat, SimpleDateFormat}
import java.time.{LocalDate, LocalTime, LocalDateTime}
import java.time.format.DateTimeFormatter
import java.util.concurrent.TimeUnit
import scala.collection.JavaConverters._
import scala.concurrent.{Await, Promise}
import scala.concurrent.duration.Duration
import scala.io._
import scala.math.BigDecimal
import scala.util.{Try, Using, Success, Failure}
import sys.process._

@main
def dataprep1(args: String*) = {
	try {
		os.remove(os.pwd / "devclub.csv")
		os.remove(os.pwd / "devclub.json")
		os.remove(os.pwd / "result.sqlite")
	} catch {
		case t: Throwable => t.printStackTrace
	}
	println(" Read XML ")
	var records = scala.xml.XML.loadFile("data-devclub-1.xml")
	println(" Write CSV ")
	val headFile = "EMPID,PASSPORT,FIRSTNAME,LASTNAME,GENDER,BIRTHDAY,NATIONALITY,HIRED,DEPT,POSITION,STATUS,REGION"
	val csv1File = new PrintWriter("devclub.csv")
	csv1File.println(headFile)
	for (record <- records \ "record") {
		csv1File.print((record \ "EMPID").text)
		csv1File.print(","); csv1File.print((record \ "PASSPORT").text)
		csv1File.print(","); csv1File.print((record \ "FIRSTNAME").text)
		csv1File.print(","); csv1File.print((record \ "LASTNAME").text)
		csv1File.print(","); csv1File.print((record \ "GENDER").text)
		csv1File.print(","); csv1File.print((record \ "BIRTHDAY").text)
		csv1File.print(","); csv1File.print((record \ "NATIONALITY").text)
		csv1File.print(","); csv1File.print((record \ "HIRED").text)
		csv1File.print(","); csv1File.print((record \ "DEPT").text)
		csv1File.print(","); csv1File.print((record \ "POSITION").text)
		csv1File.print(","); csv1File.print((record \ "STATUS").text)
		csv1File.print(","); csv1File.print((record \ "REGION").text)
		csv1File.println()
	}
	csv1File.close

	(records \ "record").map(r => ((r \ "NATIONALITY").text, r)).groupBy(_._1).map {
		case (k, v) => new PrintWriter(s"devclub-$k.csv") { println(headFile); v.foreach(r => println((r._2 \ "EMPID").text + "," + (r._2 \ "PASSPORT").text + "," + (r._2 \ "FIRSTNAME").text + "," + (r._2 \ "LASTNAME").text + "," + (r._2 \ "GENDER").text + "," + (r._2 \ "BIRTHDAY").text + "," + (r._2 \ "NATIONALITY").text + "," + (r._2 \ "HIRED").text + "," + (r._2 \ "DEPT").text + "," + (r._2 \ "POSITION").text + "," + (r._2 \ "STATUS").text + "," + (r._2 \ "REGION").text)); close }
	}

	println(" Read SQLite ")
	var connection = java.sql.DriverManager.getConnection("jdbc:sqlite:result.sqlite");
	var statement = connection.createStatement();
	var result = statement.execute("""CREATE TABLE DEV_CLUB_OLD (
		EMPID varchar(5),
		PASSPORT varchar(40),
		FIRSTNAME varchar(50),
		LASTNAME varchar(50),
		GENDER varchar(5),
		BIRTHDAY varchar(10),
		NATIONALITY varchar(30),
		HIRED varchar(10),
		DEPT varchar(20),
		POSITION varchar(20),
		STATUS varchar(5),
		REGION varchar(20)
	)""")
	 result = statement.execute("""CREATE TABLE DEV_CLUB (
		EMPID varchar(5),
		PASSPORT varchar(40),
		FIRSTNAME varchar(50),
		LASTNAME varchar(50),
		GENDER varchar(5),
		BIRTHDAY varchar(10),
		NATIONALITY varchar(30),
		HIRED varchar(10),
		DEPT varchar(20),
		POSITION varchar(20),
		STATUS varchar(5),
		REGION varchar(20)
	)""")
	println(" Write SQLite ")
	for (record <- records \ "record") {
		statement.execute("INSERT INTO DEV_CLUB_OLD VALUES("
			+"'"+ (record \ "EMPID").text + "'"
			+",'"+ (record \ "PASSPORT").text + "'"
			+",'"+ (record \ "FIRSTNAME").text + "'"
			+",'"+ (record \ "LASTNAME").text + "'"
			+",'"+ (record \ "GENDER").text + "'"
			+",'"+ (record \ "BIRTHDAY").text + "'"
			+",'"+ (record \ "NATIONALITY").text + "'"
			+",'"+ (record \ "HIRED").text + "'"
			+",'"+ (record \ "DEPT").text + "'"
			+",'"+ (record \ "POSITION").text + "'"
			+",'"+ (record \ "STATUS").text + "'"
			+",'"+ (record \ "REGION").text + "'"
			+ ")")
	}
	val allowPosition = Set("Airhostess", "Pilot", "Steward")
	val allowHired = java.sql.Date.valueOf("2019-10-08")
	for (record <- records \ "record") {
		val validPosition = allowPosition.contains((record \ "POSITION").text)
		val isActive = (record \ "STATUS").text == "1"
		val more3y = java.sql.Date.valueOf((record \ "HIRED").text.replaceAll("([0-9]{2})-([0-9]{2})-([0-9]{4})", "$3-$2-$1")).compareTo(allowHired) < 0
		if (validPosition && isActive && more3y) {
			statement.execute("INSERT INTO DEV_CLUB VALUES("
				+"'"+ (record \ "EMPID").text + "'"
				+",'"+ (record \ "PASSPORT").text + "'"
				+",'"+ (record \ "FIRSTNAME").text + "'"
				+",'"+ (record \ "LASTNAME").text + "'"
				+",'"+ (record \ "GENDER").text + "'"
				+",'"+ (record \ "BIRTHDAY").text + "'"
				+",'"+ (record \ "NATIONALITY").text + "'"
				+",'"+ (record \ "HIRED").text + "'"
				+",'"+ (record \ "DEPT").text + "'"
				+",'"+ (record \ "POSITION").text + "'"
				+",'"+ (record \ "STATUS").text + "'"
				+",'"+ (record \ "REGION").text + "'"
				+ ")")
		}
	}
	var rs1 = statement.executeQuery("SELECT * FROM DEV_CLUB")
	println(" Write JSON ")
	val json1File = new PrintWriter("devclub.json")
	while (rs1.next) {
		json1File.println(s"""{ "EMPID": "${rs1.getString(1)}", "PASSPORT": "${rs1.getString(2)}", "FIrs1TNAME": "${rs1.getString(3)}", "LASTNAME": "${rs1.getString(4)}", "GENDER": "${rs1.getString(5)}", "BIRTHDAY": "${rs1.getString(6)}", "NATIONALITY": "${rs1.getString(7)}", "HIRED": "${rs1.getString(8)}", "DEPT": "${rs1.getString(9)}", "POSITION": "${rs1.getString(10)}", "STATUS": "${rs1.getString(11)}", "REGION": "${rs1.getString(12)}" }""")
	}
	json1File.close
	(records \ "record").map(r => ((r \ "REGION").text, r)).groupBy(_._1).map {
		case (k, v) => statement.execute(s"create view dev_club_${k.replace(" ", "_")} as select * from dev_club where region = '$k';")
	}
	(records \ "record").map(r => ((r \ "DEPT").text, r)).groupBy(_._1).map {
		case (k, v) => statement.execute(s"create view dev_club_${k.replace(" ", "_")} as select * from dev_club where dept = '$k';")
	}
	(records \ "record").map(r => ((r \ "NATIONALITY").text, r)).groupBy(_._1).map {
		case (k, v) => statement.execute(s"create view dev_club_${k.replace(" ", "_")} as select * from dev_club where nationality = '$k';")
	}
	connection.close
}
