import json, os, tkinter as tk, customtkinter as ctk

class generic_features():
    def toggle_dark_mode(self):
        ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark")
        
    def exit_app(self):
        self.destroy()  
        