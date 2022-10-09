using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(menuName = "My Script/Create XML2CSV Converter")]
public class XML2CSVConverter : ScriptableObject
{
    public TextAsset xmlFile;
    public string csvFileName;
}