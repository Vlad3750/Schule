from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    Plot.templates.default = "material_light"

    # Any code you write here will run before the form opens.
  # Plot some data
    self.diagramm.data = [
      go.Bar(
        x = [2],
        y = [5],
#        marker = dict(
#          color= 'rgb(212, 179, 60)'),
        name = 'Lehrer'
      ),
      go.Bar(
        x = [1],
        y = [3],
#        marker = dict(
#          color= 'rgb(255, 224, 113)'),
        name = 'Schüler'
      )
      
    ]

    self.diagramm.layout = {
      'title': {'text': 'Diagramm'}
    }
      
    self.diagramm.layout.yaxis.title.text = 'Anzahl'

    
      