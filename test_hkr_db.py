import sqlite3
import json

def insertCombination(dictCombination):
    # print(dictCombination)
    conn = sqlite3.connect("test_hkr.db")
    cursor = conn.cursor()
    # name, combo_list = dictCombination.items()
    name, combo_list = list(dictCombination.items())[0]
    combo_json = json.dumps(combo_list)
    cursor.execute("INSERT OR REPLACE INTO combinations (name, combination) VALUES (?, ?)", (name, combo_json))
    conn.commit()
    conn.close()

def getAllCombinations():
    conn = sqlite3.connect("test_hkr.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, combination FROM combinations")
    rows = cursor.fetchall()
    dictCombinations = {name: json.loads(combo_json) for name, combo_json in rows}
    # print(dictCombinations)
    conn.close()
    return dictCombinations