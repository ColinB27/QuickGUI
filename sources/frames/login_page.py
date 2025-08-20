import customtkinter as ctk

        
class login_page():
    # > Intialise Login page and places login frame at the center
    def _init_login_page_(self, rows=3, columns=7, center_weight=3, other_weight=2):
        #* Main container for login page
        self.login_page = ctk.CTkFrame(self)

        #* Compute the center cell
        center_row = rows // 2
        center_col = columns // 2

        #* Configure inner grid
        for r in range(rows):
            weight = center_weight if r == center_row else other_weight
            self.login_page.grid_rowconfigure(r, weight=weight)
        for c in range(columns):
            weight = center_weight if c == center_col else other_weight
            self.login_page.grid_columnconfigure(c, weight=weight)

        #* Create the login frame in the center
        self._init_login_frame_(self.login_page, center_row, center_col)
        self._show_login_page_()
        
    # > Initialise the frame with login features
    def _init_login_frame_(self,master,row,col):
        self.login_frame = ctk.CTkFrame(master=master,corner_radius=6,fg_color="azure")
        self.login_frame.grid(row=row, column=col, sticky="nsew")
    
    
    # > --------- Quality of life features below     
    def _show_login_page_(self):
        self.login_page.grid(row=0, column=0, sticky="nsew")
        
    def _hide_login_page_(self):
        self.login_page.grid_forget()
        

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    class App(ctk.CTk,login_page):
        def __init__(self):
            super().__init__()
            self._init_window_(1100, 580)
            self._init_login_page_()
        
        def _init_window_(self, width, height):
            self.width = width
            self.height = height
            # configure window
            self.title("TEST.py")
            self.geometry(f"{self.width}x{self.height}")

            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)

    app = App()
    app.mainloop()
    