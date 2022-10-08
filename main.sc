import $ivy.{
	`org.slf4j:jcl-over-slf4j:1.7.36`,
	`org.slf4j:jul-to-slf4j:1.7.36`,
	`org.apache.logging.log4j:log4j-slf4j-impl:2.17.2`,
	`com.typesafe:config:1.4.2`,
	`com.lihaoyi::ammonite-ops:2.4.1`,
	`com.lihaoyi::requests:0.7.1`,
	`com.lihaoyi::ujson:2.0.0`,
	`org.mongodb:mongodb-driver-core:4.6.0`,
	`org.mongodb:mongodb-driver-sync:4.6.0`,
	`org.mongodb:bson:4.6.0`,
	`org.mongodb.scala::mongo-scala-driver:4.6.0`,
	`org.apache.spark::spark-sql:3.2.1`,
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

import com.typesafe.config.ConfigFactory

import org.apache.spark.sql._
import org.apache.spark.sql.functions._

import ujson._

@main
def dataprep1(args: String*) = {
	var prmsItem     = args.map(_.trim.split("=") match { case Array(k: String, v: String) => (k, v.replace("'", "")) }).toMap
	println(prmsItem)
	println(" Read JSON ")
	import scala.io._, scala.util._, ujson._
	//var retProc = Using(Source.fromFile("main.json")) { src =>
	//	for (line <- src.getLines) {
	//		cntData += 1
			val         srcJSON = ujson.Obj("field1" -> "value1", "field2" -> ujson.Null)
			val      srcColumns = ujson.read("""{"srcColumns":[{"name":"_1","noColCount":0,"rules":{"CUSTOM":{"boolExpr":"_1 = '3180c249-9565-41fd-9fc8-549484f42a20' or _1 = 'f31f14a0-b0a8-4050-bd3f-b6298b71023c'","dataExpr":null},"IS_DIGIT":{},"IS_CITIZEN_ID":{}}},{"name":"_80005","noColCount":0,"rules":{"IS_NULL":{"validCount":0,"errorCount":0},"IS_DIGIT":{}}}]}""")("srcColumns").arr
	//	}
	//}
	println(" Read CSV ")
	val spark = SparkSession.builder.master("local[*]").appName("test").getOrCreate()
	val sc = spark.sparkContext
	import spark.implicits._
	//val data2 = spark.read.csv("file:///tmp/pipeline-test/1_1342.csv")
	//data2.show
	println(" Read XML ")
	var xmlObj = scala.xml.XML.loadString("""<play><scala title="devmountaintech">hello</scala><scala title="tisco">hello2</scala></play>""")
	xmlObj \ "scala"
	(xmlObj \ "scala" \ "@title").text
	var seq = (xmlObj \ "scala").map(n => (n \ "@title").text).toSeq
	println(" Read SQLite ")
	var connection = java.sql.DriverManager.getConnection("jdbc:sqlite:" + "file");
	var statement = connection.createStatement();
}
