# ============================================================================================================
# ^ ========================================== INCLUDES
import os, json, customtkinter as ctk
from features.general import *
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== MAIN APPLICATION PAGE
class app_page():
    # > Intialise app page
    def _init_login_page_(self):
        #* Main container for app page
        self.app_page = ctk.CTkFrame(self)
    
    def _show_app_page_(self):
        self.login_page.grid(row=0, column=0, sticky="nsew")
        
    def _hide_app_page_(self):
        self.login_page.grid_forget()
    
    def _show_app_frame_(self,row,col):
        self.login_frame.grid(row=row, column=col, sticky="nsew")
        
    def _hide_app_frame_(self):
        self.login_frame.grid_forget()
# ============================================================================================================