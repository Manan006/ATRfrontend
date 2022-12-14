from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Invalid_Login import Invalid_Login
from ..Signup import Signup
class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.added_warning=False

    # Any code you write here will run when the form opens.

  def login_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = anvil.server.call("login",username=self.username_input.text,password=self.password_input.text)
    if not data:
      if not self.added_warning:
        self.add_component(Invalid_Login())
        self.added_warning=True
    else:
      self.added_warning=False
      self.parent.parent.change_password.visible=True
      self.content_panel.clear()
      open_form('Base')

  def signup_link_click(self, **event_args):
    self.content_panel.clear()
    self.add_component(Signup())

  def password_input_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


