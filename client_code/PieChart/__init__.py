from ._anvil_designer import PieChartTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class PieChart(PieChartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.button_1.background = app.theme_colors['Primary Container']

    # Any code you write here will run before the form opens.

    SchuelerAnzahl = anvil.server.call('get_SchuelerAnzahl_Diagramm')
    LehrerAnzahl = anvil.server.call('get_LehrerAnzahl_Diagramm')
    
    AnzahlSchueler = [row[0] for row in SchuelerAnzahl]
    AnzahlLehrer = [row[0] for row in LehrerAnzahl]
    
    self.pieChart.data = [
      go.Pie(
        labels=['Schüler', 'Lehrer'],
        values=[AnzahlSchueler[0], AnzahlLehrer[0]]
      )
    ]
    
    self.pieChart.layout = {
      'title': {'text': 'Kreisdiagramm'},
      'showlegend': False,
      'hovermode': 'closest',
    }
    self.pieChart.config = {'displayModeBar': False}

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Diagramm')

  @handle("pieChart", "click")
  def pieChart_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass
