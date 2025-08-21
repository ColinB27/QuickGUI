# ============================================================================================================
# ^ ========================================== INCLUDES
import os, json, customtkinter as ctk
from chlorophyll import CodeView
from pygments.lexers import get_lexer_by_name
from features.general import *
# ============================================================================================================


# ============================================================================================================
# ^ ========================================== CODE EDITOR PAGE
class code_editor_page():
    # > Initialise code editor page
    def _init_code_editor_page_(self, master, language="python"):
        #* Main container for code editor page
        self.folder_path = "../.."
        
        self.code_editor_page = ctk.CTkFrame(master=master,corner_radius=0)
        
        self.code_editor_page.grid_columnconfigure(0, weight=1)
        self.code_editor_page.grid_rowconfigure(1, weight=1)
        
        self._init_menu_bar_(path=json_path, master = self.code_editor_page)
        self._init_code_editor_frame(self.code_editor_page,1,0,"python")

       
        # Show the page by default
        self._show_code_editor_page_()
    
    def _init_code_editor_frame(self,master,row,col,language):
        self.language = language
        self.code_editor_frame = ctk.CTkFrame(master=master,corner_radius=0)
        
        self.code_editor_page.grid_columnconfigure(0, weight=0)
        self.code_editor_page.grid_columnconfigure(1, weight=1)
        
        # Create Chlorophyll CodeView widget
        self.editor = CodeView(
            master=self.code_editor_frame,
            lexer=get_lexer_by_name(self.language), 
            color_scheme="monokai",
            font=("Consolas", 14)
        )
        self._init_file_explorer_sidebar_(self.code_editor_frame,0,0)
        self.editor.grid(row=0, column=1, sticky="nsew")
        self.code_editor_frame.grid_configure(row=row, column=col, sticky="nsew")
    
    def _init_file_explorer_sidebar_(self,master,col,row):
        # Scrollable frame
        self.scroll_frame = ctk.CTkScrollableFrame(master=master)
        self.scroll_frame.grid(row=row, column=col, sticky="nsew")
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Clear previous widgets
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # List files in the path
        try:
            files = os.listdir(self.folder_path)
        except FileNotFoundError:
            files = []

        files.sort()

        # Add buttons for each file with alternating background using grid
        for index, file_name in enumerate(files):
            full_path = os.path.join(self.folder_path, file_name)
            if os.path.isfile(full_path):
                btn = ctk.CTkButton(
                    self.scroll_frame,
                    text=file_name,
                    command=lambda f=file_name: self.load_file_in_editor(f"{self.folder_path}/{f}"),
                    anchor="w",
                    corner_radius=0
                )
                btn.grid(row=index, column=0, sticky="nsew", padx=5, pady=0)  # fill horizontally
        
    
    
    def load_file_in_editor(self, path):
        with open(path,"r") as f:
            data = f.read()
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", data)
        
    def _set_language_(self, language):
        """Change syntax highlighting mode dynamically."""
        self.language = language
        self.editor.configure(lexer=get_lexer_by_name(self.language))

    def _set_language_(self, language):
        """Change syntax highlighting mode dynamically."""
        self.language = language
        self.editor.configure(lexer=self.language)

    def _show_code_editor_page_(self):
        self.code_editor_page.grid(row=0, column=0, sticky="nsew")

    def _hide_code_editor_page_(self):
        self.code_editor_page.grid_forget()
# ============================================================================================================
