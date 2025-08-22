# ============================================================================================================
# ^ ========================================== INCLUDES
import os, json, customtkinter as ctk
from features.general import *
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== SIDEBAR
class sidebar():
    # > Intialise sidebar
    def _init_sidebar_(self,master, row, col,bg_color="transparent"):
        self.sidebar = ctk.CTkFrame(master=master, bg_color=bg_color)
        self.sidebar_label = ctk.CTkLabel(self.sidebar, text="Username :",font = get_simple_font("Logo"))

        self._show_sidebar_(row,col)
    
    def _show_sidebar_(self,row,col):
        self.sidebar.grid(row=row, column=col, sticky="nsew")
    