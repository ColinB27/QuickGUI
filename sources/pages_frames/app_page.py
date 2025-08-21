# ============================================================================================================
# ^ ========================================== INCLUDES
import os, json, customtkinter as ctk
from features.general import *
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== MAIN APPLICATION PAGE
#  ^ Add your application here
class app_page():
    # > Intialise app page
    def _init_app_page_(self, master):
        #* Main container for app page
        self.app_page = ctk.CTkFrame(master=master)
        self.app_page.grid_columnconfigure(0, weight=1)
        self._init_menu_bar_(path=json_path, master = self.app_page)
        self._show_app_page_()

    def _show_app_page_(self):
        self.app_page.grid(row=0, column=0, sticky="nsew")
        
    def _hide_app_page_(self):
        self.app_page.grid_forget()

# ============================================================================================================