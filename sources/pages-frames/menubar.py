import json, os, tkinter as tk, customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu

class MenuBar():
    def _init_menu_bar(self,master, row, col):
        pass
    
    def _init_function_dictionnary_(self):
        self.menu_functions_map = {
            "string from json" : _function_,
        }
        
