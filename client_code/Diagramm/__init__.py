from ._anvil_designer import DiagrammTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Diagramm(DiagrammTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    Plot.templates.default = "material_light"

    # Any code you write here will run before the form opens.

    SchuelerAnzahl = anvil.server.call('get_SchuelerAnzahl_Diagramm')
    LehrerAnzahl = anvil.server.call('get_SchuelerAnzahl_Diagramm')

    y_wertSchueler = [row[0] for row in SchuelerAnzahl]
    y_wertLehrer = [row[0] for row in LehrerAnzahl]
    
    # Plot some data
    self.diagramm.data = [
      go.Bar(
        x = ['Schüler'],
        y = y_wertSchueler
      ),
      go.Bar(
        x = ['Lehrer'],
        y = y_wertLehrer
      )
    ]

    self.diagramm.layout = {
      'title': {'text': 'Diagramm'}
    }

    self.diagramm.layout.yaxis.title.text = 'Anzahl'