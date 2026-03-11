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

    # Any code you write here will run before the form opens.

  @handle("schueler", "click")
  def btn_schueler_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite.Schueler')

  @handle("diagramm", "click")
  def diagramm_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Startseite.Diagramm')


      