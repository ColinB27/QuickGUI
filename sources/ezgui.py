
# ============================================================================================================
# ^ ========================================== INCLUDES
import json, os, time, tkinter as tk, customtkinter as ctk
from features.general import *
from features.general import generic_features as generic
from pages_frames.login_page import login_page as login
from pages_frames.app_page import app_page as app
from pages_frames.menubar import MenuBar as menu
from pages_frames.code_editor import code_editor_page as code
# ============================================================================================================
 

# ============================================================================================================
# ^ ========================================== APP
class ezGUI(ctk.CTk,menu,login,generic,app,code):
    def __init__(self,app_name):
        super().__init__()
        self.app_name = app_name
        self._init_window_(1100, 580)
        # self._init_app_page_(self) # & uncomment to remove login pages
        self._init_login_page_(self) # &   comment to remove login page
        
    
    def _init_window_(self, width, height):
        self.width = width
        self.height = height
        # configure window
        self.title(self.app_name)
        self.geometry(f"{self.width}x{self.height}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== Implementation
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("utils/themes/red.json")

    interface = ezGUI("TEST")
    interface.mainloop()
# ============================================================================================================