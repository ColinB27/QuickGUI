# ============================================================================================================
# ^ ========================================== INCLUDES
import os, json, customtkinter as ctk
from features.general import *
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== MAIN APPLICATION PAGE
# ^ Add your application here
class app_page():
    # > Intialise app page
    def _init_app_page_(self, master):
        #* Main container for app page
        self.app_page = ctk.CTkFrame(master=master, corner_radius=0)
        self.app_page.grid_columnconfigure(0, weight=1)
        self.app_page.grid_rowconfigure(1, weight=1)
        
        self._init_menu_bar_(path=json_path, master = self.app_page)
        self.app_frame = ctk.CTkFrame(master=self.app_page, corner_radius=0, bg_color="azure2")
        self.app_frame.grid(row=1, column=0, sticky="nsew")
        
        self.app_frame.grid_rowconfigure(0, weight=1)
        
        self._init_sidebar_(self.app_frame,0,0,"azure1")
        
        self._show_app_page_()

    def _show_app_page_(self):
        self.app_page.grid(row=0, column=0, sticky="nsew")
        
    def _hide_app_page_(self):
        self.app_page.grid_forget()

# ============================================================================================================