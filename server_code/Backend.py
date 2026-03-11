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
def get_Schueler():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute("""
        SELECT * FROM Schueler
    """).fetchall()
    return [dict(row) for row in result]

@anvil.server.callable
def get_Lehrer():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Lehrer
    """)
    return cur.fetchall()

@anvil.server.callable
def get_Internat():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Internat
    """)
    return cur.fetchall()

@anvil.server.callable
def get_Projekte():
  with sqlite3.connect(data_files['internatsDB.db']) as conn:
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Projekte
    """)
    return cur.fetchall()