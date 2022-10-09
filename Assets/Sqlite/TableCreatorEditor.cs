using Mono.Data;
using Mono.Data.Sqlite;
using System;
using System.Data;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(SqliteManager))]
public class TableCreatorEditor : Editor
{
	public override void OnInspectorGUI(){
		var sqliteManager = target as SqliteManager;
		DrawDefaultInspector();

		if (GUILayout.Button("Create Table"))
        {
			try 
            {
				CreateTable(sqliteManager);
			} 
            catch (System.Exception e)
            {
				Debug.LogError(e.Message);
			}
		}

		if (GUILayout.Button("Delete Table"))
        {
			try 
            {
				DeleteTable(sqliteManager);
			} 
            catch (System.Exception e)
            {
				Debug.LogError(e.Message);
			}
		}

		if (GUILayout.Button("Import CSV"))
        {
			try 
            {
				ImportCSV(sqliteManager);
			} 
            catch (System.Exception e)
            {
				Debug.LogError(e.Message);
			}
		}
	}

	void CreateTable(SqliteManager sqliteManager)
    {
        // Create database
		string connection = "URI=file:" + Application.dataPath + "/Sqlite/" + sqliteManager.fileName;
        List<string> headers = new List<string>{"EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY", 
                                                "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"};
		
		// Open connection
		IDbConnection dbcon = new SqliteConnection(connection);
		dbcon.Open();

		// Create table
		IDbCommand dbcmd;
		dbcmd = dbcon.CreateCommand();
		string q_createTable = "CREATE TABLE IF NOT EXISTS " + sqliteManager.tableName + " (" + String.Join(", ", headers) + ")";
		
		dbcmd.CommandText = q_createTable;
		dbcmd.ExecuteReader();

		// // Read and print all values in table
		// IDbCommand cmnd_read = dbcon.CreateCommand();
		// IDataReader reader;
		// string query ="SELECT * FROM " + sqliteManager.tableName;
		// cmnd_read.CommandText = query;
		// reader = cmnd_read.ExecuteReader();

		// while (reader.Read())
		// {
		// 	Debug.Log("id: " + reader[0].ToString());
		// 	Debug.Log("val: " + reader[1].ToString());
		// }

		// Close connection
		dbcon.Close();
	}
	
	void DeleteTable(SqliteManager sqliteManager)
    {
        // Create database
		string connection = "URI=file:" + Application.dataPath + "/Sqlite/" + sqliteManager.fileName;
        List<string> headers = new List<string>{"EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY", 
                                                "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"};
		
		// Open connection
		IDbConnection dbcon = new SqliteConnection(connection);
		dbcon.Open();

		// Create table
		IDbCommand dbcmd;
		dbcmd = dbcon.CreateCommand();
		string q_createTable = "DROP TABLE IF EXISTS " + sqliteManager.tableName;
		
		dbcmd.CommandText = q_createTable;
		dbcmd.ExecuteReader();

		// // Read and print all values in table
		// IDbCommand cmnd_read = dbcon.CreateCommand();
		// IDataReader reader;
		// string query ="SELECT * FROM " + sqliteManager.tableName;
		// cmnd_read.CommandText = query;
		// reader = cmnd_read.ExecuteReader();

		// while (reader.Read())
		// {
		// 	Debug.Log("id: " + reader[0].ToString());
		// 	Debug.Log("val: " + reader[1].ToString());
		// }

		// Close connection
		dbcon.Close();
	}


    void ImportCSV(SqliteManager sqliteManager)
    {
        
        // Create database
		string connection = "URI=file:" + Application.dataPath + "/Sqlite/" + sqliteManager.fileName;
        List<string> headers = new List<string>{"EMPID", "PASSPORT", "FIRSTNAME", "LASTNAME", "GENDER", "BIRTHDAY", 
                                                "NATIONALITY", "HIRED", "DEPT", "POSITION", "STATUS", "REGION"};

		// Open connection
		IDbConnection dbcon = new SqliteConnection(connection);
		dbcon.Open();

		// Insert values in table
		IDbCommand cmnd = dbcon.CreateCommand();
		cmnd.CommandText = "INSERT INTO " + sqliteManager.tableName + " (" + String.Join(", ", headers) + ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

        using(var reader = new StringReader(sqliteManager.csvFile.text))
        {
            reader.ReadLine();
            string line;
            while (null != (line = reader.ReadLine()))
            {
                var values = line.Split(',');

				cmnd.Parameters.Clear();
                cmnd.Parameters.Add(new SqliteParameter("", values[0]));
                cmnd.Parameters.Add(new SqliteParameter("", values[1]));
                cmnd.Parameters.Add(new SqliteParameter("", values[2]));
                cmnd.Parameters.Add(new SqliteParameter("", values[3]));
                cmnd.Parameters.Add(new SqliteParameter("", values[4]));
                cmnd.Parameters.Add(new SqliteParameter("", values[5]));
                cmnd.Parameters.Add(new SqliteParameter("", values[6]));
                cmnd.Parameters.Add(new SqliteParameter("", values[7]));
                cmnd.Parameters.Add(new SqliteParameter("", values[8]));
                cmnd.Parameters.Add(new SqliteParameter("", values[9]));
                cmnd.Parameters.Add(new SqliteParameter("", values[10]));
                cmnd.Parameters.Add(new SqliteParameter("", values[11]));
                cmnd.Prepare();
                cmnd.ExecuteNonQuery();
            }
        }

		// Close connection
		dbcon.Close();
    }
}