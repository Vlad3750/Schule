from ._anvil_designer import SchuelerTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Schueler(SchuelerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    self.button_schueler.background = app.theme_colors['Primary Container']

  @handle("button_diagramm", "click")
  def button_diagramm_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Startseite')

  @handle("data_grid_schueler", "show")
  def data_grid_schueler_show(self, **event_args):
    """This method is called when the data grid is shown on the screen"""
    return_value = anvil.server.call('get_Schueler')
    self.repeating_panel_schueler.items = return_value

  