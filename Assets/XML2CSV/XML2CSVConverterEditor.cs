using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Xml.Linq;
using UnityEngine;
using UnityEditor;

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

        List<string> acceptedPositions = new List<string>{"Airhostess", "Pilot", "Steward"};
        DateTime acceptedHiredDate = DateTime.Now.AddYears(-3);

        List<string> countries = new List<string>();

		foreach (var record in dataElements)
        {
			Dictionary<string, string> recordDictionary = new Dictionary<string, string>();
			foreach (string header in columnArray) recordDictionary.Add(header, "");
			foreach (var recordElement in record.Elements()) recordDictionary[recordElement.Name.LocalName] = recordElement.Value;

            DateTime hiredDate = DateTime.ParseExact(recordDictionary["HIRED"], "dd-MM-yyyy", null);

            if (
                recordDictionary["EMPID"] == recordDictionary["PASSPORT"] ||
                recordDictionary["STATUS"] != "1" ||
                !acceptedPositions.Contains(recordDictionary["POSITION"]) ||
                hiredDate > acceptedHiredDate
            )
                continue;

			List<string> recordLine = new List<string>();
			foreach (string header in columnArray) recordLine.Add(recordDictionary[header]);
			string[] dataArray = recordLine.ToArray();
			sw.WriteLine(string.Join(",", dataArray));

			if (!countries.Contains(recordDictionary["NATIONALITY"]))
				countries.Add("\"" + recordDictionary["NATIONALITY"] + "\"");
		}
		sw.Flush();
		sw.Close();

		AssetDatabase.Refresh();

		// Go go! https://www.mapchart.net/world.html
		string mapTemplate = "{\"groups\":{\"#66c2a4\":{\"label\":\"\",\"paths\":[" + string.Join(",", countries) + "]}},\"title\":\"Employee by Nationality\",\"hidden\":[\"Prince_Edward_Island_CA\",\"New_Brunswick_CA\",\"Ontario_CA\",\"British_Columbia_CA\",\"Alberta_CA\",\"Saskatchewan_CA\",\"Manitoba_CA\",\"Quebec_CA\",\"Yukon_CA\",\"Nunavut_CA\",\"Newfoundland_and_Labrador_CA\",\"Northwest_Territories_CA\",\"Nova_Scotia_CA\",\"Scotland\",\"Wales\",\"England\",\"Northern_Ireland\",\"USA_Wisconsin\",\"USA_Montana\",\"USA_Minnesota\",\"USA_Washington\",\"USA_Idaho\",\"USA_North_Dakota\",\"USA_Michigan\",\"USA_Maine\",\"USA_Ohio\",\"USA_New_Hampshire\",\"USA_New_York\",\"USA_Vermont\",\"USA_Pennsylvania\",\"USA_Arizona\",\"USA_California\",\"USA_New_Mexico\",\"USA_Texas\",\"USA_Alaska\",\"USA_Louisiana\",\"USA_Mississippi\",\"USA_Alabama\",\"USA_Florida\",\"USA_Georgia\",\"USA_South_Carolina\",\"USA_North_Carolina\",\"USA_Virginia\",\"USA_Washington_DC\",\"USA_Maryland\",\"USA_Delaware\",\"USA_New_Jersey\",\"USA_Connecticut\",\"USA_Rhode_Island\",\"USA_Massachusetts\",\"USA_Oregon\",\"USA_Hawaii\",\"USA_Utah\",\"USA_Wyoming\",\"USA_Nevada\",\"USA_Colorado\",\"USA_South_Dakota\",\"USA_Nebraska\",\"USA_Kansas\",\"USA_Oklahoma\",\"USA_Iowa\",\"USA_Missouri\",\"USA_Illinois\",\"USA_Kentucky\",\"USA_Arkansas\",\"USA_Tennessee\",\"USA_West_Virginia\",\"USA_Indiana\"],\"background\":\"#252525\",\"borders\":\"#252525\",\"legendFont\":\"Century Gothic\",\"legendFontColor\":\"#d9d9d9\",\"legendBgColor\":\"#00000000\",\"areBordersShown\":true,\"defaultColor\":\"#737373\",\"labelsColor\":\"#d9d9d9\",\"strokeWidth\":\"medium\",\"areLabelsShown\":true,\"usaStatesShown\":false,\"canadaStatesShown\":false,\"splitUK\":false,\"legendPosition\":\"bottom_left\",\"legendSize\":\"medium\",\"legendStatus\":\"show\",\"scalingPatterns\":true,\"legendRowsSameColor\":true,\"legendColumnCount\":1}";
		
		outputPath = AssetDatabase.GetAssetPath(xml2csvConverter);
		outputPath = outputPath.Substring(0, outputPath.LastIndexOf(xml2csvConverter.name)) + "mapTemplate.json";
		StreamWriter writer = new StreamWriter(outputPath, true);
		writer.WriteLine(mapTemplate);
		writer.Close();
	}
}