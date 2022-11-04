from ._anvil_designer import thoughtsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

class thoughts(thoughtsTemplate):
  def __init__(self,thought,time_,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.thought_.text=thought
    self.time__.content = time_
    # Any code you write here will run when the form opens.
