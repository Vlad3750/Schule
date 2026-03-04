from ._anvil_designer import StartseiteTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from plotly import graph_objects as go

class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    Plot.templates.default = "material_light"

    # Any code you write here will run before the form opens.
  # Plot some data
    self.diagramm.data = [
      go.Scatter(
        x = [1, 2, 3],
        y = [3, 1, 6],
        marker = dict(
          color= 'rgb(0, 0, 0)'
        )
      ),
      go.Bar(
        x = [1, 2, 3],
        y = [3, 1, 6],
        marker = dict(
          color= 'rgb(255, 224, 113)'),
        name = 'Bar Chart Example'
      )
    ]

    self.diagramm.layout = {
      'title': {'text': 'Simple Example'},
      'xaxis': {
        'title': {'text': 'Time'}
      }
    }
    
    self.diagramm.layout.yaxis.title.text = 'Anzahl'
    self.diagramm.layout.annotations = [{
      'text': 'Simple annotation',
      'x': 1,
      'xref': 'x',
      'y': 3.2,
      'yref': 'y'
    }]
    
      