import customtkinter as ctk
from time import sleep

        
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
        self.logged_in = False
        self.failed_logins = 0
        
        self.login_frame = ctk.CTkFrame(master=master,corner_radius=6,fg_color="azure")
        self.login_frame.grid(row=row, column=col, sticky="nsew")
        self.login_frame.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.login_frame.grid_columnconfigure(0, weight=1)
        
        self.username_label = ctk.CTkLabel(self.login_frame,             text="Username :")
        self.username_input = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.password_label = ctk.CTkLabel(self.login_frame,             text="Password :")
        self.password_input = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.login_button   = ctk.CTkButton(self.login_frame, text="LOGIN", command=self.login_event,fg_color="green")
        
        self.username_label.grid_configure(row=0, column=0, padx=20, sticky= "w")
        self.username_input.grid_configure(row=1, column=0, padx=20, sticky="ew")
        self.password_label.grid_configure(row=2, column=0, padx=20, sticky= "w")
        self.password_input.grid_configure(row=3, column=0, padx=20, sticky="ew")
        self.login_button.grid_configure(  row=4, column=0, padx=20, sticky="ew")
        
        
    def login_event(self):
        username_txt = self.username_input.get() # GET USERNAME
        password_txt = self.password_input.get() # GET PASSWORD
        if(self.check_login_info(username_txt, password_txt)): #CHECK LOGIN INFO
            # self.login_button.configure(True,text="DISCONNECT", command=self.disconnect_event,fg_color="red")
            self.username_input.configure(True, state="disabled")
            self.password_input.configure(True, state="disabled")
            self._hide_login_frame_()
            self.logged_in = True
        else:
            self.failed_logins += 1;
    
    def disconnect_event(self):
        self.username_input.configure(True, state="normal")
        self.password_input.configure(True, state="normal")
        self.password_input.delete(0,"end")
        # self.login_button.configure(True,text="LOGIN", command=self.login_event,fg_color="green")
        self.logged_in = False
    
    # > --------- Quality of life features below    
     
    def check_login_info(self, username, password):
        return_value = None
        if(username == "cboule" and password == "dorma"):
            return_value = True
        else:
            return_value = False
        return return_value
    
    def _show_login_page_(self):
        self.login_page.grid(row=0, column=0, sticky="nsew")
        
    def _hide_login_page_(self):
        self.login_page.grid_forget()
    
    def _show_login_frame_(self,row,col):
        self.login_frame.grid(row=row, column=col, sticky="nsew")
        
    def _hide_login_frame_(self):
        self.login_frame.grid_forget()
        

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
    