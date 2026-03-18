from ._anvil_designer import ProjekteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Projekte(ProjekteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("link_1", "show")
  def link_1_show(self, **event_args):
    """This method is called when the Link is shown on the screen"""
    return_value = anvil.server.call('get_Projekte')
    self.repeating_panel_projekte.items = return_value
