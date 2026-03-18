import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import sqlite3

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_SchuelerAnzahl_Diagramm():
  conn = sqlite3.connect(data_files["internatsDB.db"])
  cur = conn.cursor()
  value = cur.execute("""
    SELECT
      COUNT(ID) as Anzahl
    FROM Schueler
  """).fetchall()
  return value

@anvil.server.callable
def get_LehrerAnzahl_Diagramm():
  conn = sqlite3.connect(data_files["internatsDB.db"])
  cur = conn.cursor()
  value = cur.execute("""
    SELECT
      COUNT(ID) as Anzahl
    FROM Lehrer
  """).fetchall()
  return value

@anvil.server.callable
def get_ProjekteAnzahl_Diagramm():
  conn = sqlite3.connect(data_files["internatsDB.db"])
  cur = conn.cursor()
  value = cur.execute("""
    SELECT
      COUNT(ID) as Anzahl
    FROM Projekte
  """).fetchall()
  return value

@anvil.server.callable
def get_UnterrichtAnzahl_Diagramm():
  conn = sqlite3.connect(data_files["internatsDB.db"])
  cur = conn.cursor()
  value = cur.execute("""
    SELECT
      COUNT(ID) as Anzahl
    FROM Unterricht
  """).fetchall()
  return value

@anvil.server.callable
def get_Schueler():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT 
          s.Name,
          s.Geburtsdatum,
          s.Internat_ID,
          GROUP_CONCAT(l.Name, ', ') AS Lehrer
        FROM Schueler s
        LEFT JOIN (SELECT DISTINCT Schueler_ID, Lehrer_ID FROM Unterricht) u ON u.Schueler_ID = s.ID
        LEFT JOIN Lehrer l ON l.ID = u.Lehrer_ID
        GROUP BY s.ID
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Lehrer():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT * FROM Lehrer
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Internat():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT Internat.Name, Gruendungsjahr, COUNT(Schueler.Internat_ID) AS Anzahl
        FROM Internat
        LEFT JOIN Schueler ON Schueler.Internat_ID = Internat.ID
        GROUP BY Internat.Name, Gruendungsjahr
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Projekte():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        
    """).fetchall()
    return [dict(row) for row in result]