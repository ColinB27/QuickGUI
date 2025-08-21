import json, os, tkinter as tk, customtkinter as ctk

# ============================================================================================================
# ^ ========================================== CONSTANTS, PATHS AND THINGS
# TODO move this to utils 
#& configuration paths
json_path = "utils/menu_format.json"
font_path = "utils/fonts.json"
# ============================================================================================================

class generic_features():
        
    def exit_app(self):
        self.destroy()  

def toggle_dark_mode():
        ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark")


def get_simple_font(font):
    with open(font_path,"r") as f:
        data = json.load(f);
    index = font.lower()
    return (data[index]["family"], data[index]["size"],  data[index]["weight"])


        