using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu(menuName = "My Script/Create Sqlite Manager")]
public class SqliteManager : ScriptableObject
{
    public string fileName;
    public string tableName;
    public TextAsset csvFile;
}