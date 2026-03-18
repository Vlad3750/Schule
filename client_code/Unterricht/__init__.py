from ._anvil_designer import UnterrichtTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Unterricht(UnterrichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.layout.reset()
    self.layout.unterricht.role = 'selected'
    # Any code you write here will run before the form opens.

  @handle("repeating_panel_unterricht", "show")
  def repeating_panel_unterricht_show(self, **event_args):
    """This method is called when the repeating panel is shown on the screen"""
    return_value = anvil.server.call('get_Unterricht')
    self.repeating_panel_unterricht.items = return_value
