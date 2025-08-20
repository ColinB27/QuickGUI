import json, os, tkinter as tk, customtkinter as ctk
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu

json_path = "GIT/sources/utils/menu_format.json"

class MenuBar():
    def _init_menu_bar_(self,path, master, row=0, col=0):
        self.menubar = CTkMenuBar(master=master)
        self.menubar.grid(row=row, column=col, sticky="ew")  
        
        self._init_function_dictionnary_()
        
        menu_data = self.load_json_menu(path)
        
        for menu_name, options in menu_data.items():
            menu_btn = self.menubar.add_cascade(menu_name)
            dropdown = CustomDropdownMenu(widget=menu_btn)

            for option, func_name in options.items():
                if option == "---":
                    dropdown.add_separator()
                else:
                    func = self.menu_functions_map.get(func_name, None)
                    dropdown.add_option(option, command=func)
        
    
    def _init_function_dictionnary_(self):
        self.menu_functions_map = {
            "toggle_theme":self.toggle_dark_mode,
            "exit_app":self.exit_app
        }
    
    def load_json_menu(self,json_path):
        try:
            with open(json_path, "r") as f:
                menu_data = json.load(f)
            return menu_data
        except Exception as e:
            print(e)
            return None

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    class Gf():
        def toggle_dark_mode(self):
            ctk.set_appearance_mode("light" if ctk.get_appearance_mode() == "Dark" else "dark")
            
        def exit_app(self):
            self.destroy()  
    
    class App(ctk.CTk,MenuBar,Gf):
        def __init__(self):
            super().__init__()
            self._init_window_(1100, 580)
            self._init_menu_bar_(path=json_path, master = self.main_frame)
        
        def _init_window_(self, width, height):
            self.width = width
            self.height = height
            # configure window
            self.title("TEST.py")
            self.geometry(f"{self.width}x{self.height}")

            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            
            self.main_frame = ctk.CTkFrame(self)
            self.main_frame.grid(row=0, column=0, sticky="nsew")
            self.main_frame.grid_rowconfigure(0, weight=0)
            self.main_frame.grid_rowconfigure(1, weight=1)
            self.main_frame.grid_columnconfigure(0, weight=1)

    app = App()
    app.mainloop()
    

            
