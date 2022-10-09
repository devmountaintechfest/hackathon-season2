using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.IO;
using System.Xml.Linq;

[CustomEditor(typeof(XML2CSVConverter))]
public class XML2CSVConverterEditor : Editor
{
	public override void OnInspectorGUI(){
		var xml2csvConverter = target as XML2CSVConverter;
		DrawDefaultInspector();

		if (GUILayout.Button("Convert to CSV"))
        {
			try 
            {
				ConvertXML2CSV(xml2csvConverter);
			} 
            catch (System.Exception e)
            {
				Debug.LogError(e.Message);
				Debug.LogError("Failed to parse the XML file. Make sure the correct XML file is referenced.");
			}
		}
	}

	void ConvertXML2CSV(XML2CSVConverter xml2csvConverter)
    {
		if (xml2csvConverter.xmlFile == null)
        {
			Debug.LogWarning("XML file to read is not set.");
			return;
		}
		if (string.IsNullOrEmpty(xml2csvConverter.csvFileName))
        {
			Debug.LogWarning("The output CSV file name has not been entered.");
			return;
		}

		string xmlText = xml2csvConverter.xmlFile.text;
		XDocument xDocument = XDocument.Parse(xmlText);
		XElement rootXElement = xDocument.Root;
		var dataElements = rootXElement.Elements();

		List<string> columns = new List<string>();
		foreach (var record in dataElements)
        {
			foreach (var recordElement in record.Elements())
				if (!columns.Contains(recordElement.Name.LocalName)) columns.Add(recordElement.Name.LocalName);
			break;
		}

		string outputPath = AssetDatabase.GetAssetPath(xml2csvConverter);
		outputPath = outputPath.Substring(0, outputPath.LastIndexOf(xml2csvConverter.name)) + xml2csvConverter.csvFileName + ".csv";
		FileInfo fileInfo = new FileInfo(outputPath);
		StreamWriter sw = fileInfo.CreateText();

		string[] columnArray = columns.ToArray();
		sw.WriteLine(string.Join(",", columnArray));

		foreach (var record in dataElements)
        {
			Dictionary<string, string> recordDictionary = new Dictionary<string, string>();
			foreach (string tag in columnArray) recordDictionary.Add(tag, "");
			foreach (var recordElement in record.Elements()) recordDictionary[recordElement.Name.LocalName] = recordElement.Value;

			List<string> recordLine = new List<string>();
			foreach (string tag in columnArray) recordLine.Add(recordDictionary[tag]);
			string[] dataArray = recordLine.ToArray();
			sw.WriteLine(string.Join(",", dataArray));
		}
		sw.Flush();
		sw.Close();

		AssetDatabase.Refresh();
	}
}