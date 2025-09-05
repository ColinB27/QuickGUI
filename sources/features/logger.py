import customtkinter as ctk

LOG_LEVELS = ("DEFAULT", "DEBUG", "WARNING", "ERROR")
LOG_STYLES = {
    "DEFAULT": (("Fixedsys", 12), "black"),
    "DEBUG": (("Fixedsys", 12), "blue"),
    "WARNING": (("Fixedsys", 12), "orange"),
    "ERROR": (("Fixedsys", 12, "bold"), "red"),
}


class Log_display_box(ctk.CTkTextbox):
    
    def configure_logs(self):
        self.logs = []
        for log_level, font in LOG_STYLES.items():
            self._textbox.tag_configure(log_level, font=font[0], foreground=font[1])

    def add_log_line(self, msg, level:str="default"):
        if level in LOG_LEVELS:
            self.logs.append(f"{level}:{msg}")
            self.display_log_line(msg, level)
        else:
            print("Error: tried to log message at improper level")
        
    def display_log_line(self, msg, level):
        self.configure(state="normal")
        self.insert("end", msg + "\n", level)
        self.see("end")  # auto-scroll to the bottom
        self.configure(state="disabled")

    def load_log(self, logger_array):
        # clear old text
        self.delete("1.0", "end")
        # insert new text with style
        for line in logger_array:
            line_parts = line.split(":", 1)
            if len(line_parts) == 2:
                level, msg = line_parts
                self.add_log_line(msg , level)


# =---------------- Test App ----------------= # 
def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.geometry("600x400")
    app.title("Logger Test App")

    # logger and display
    log_box = Log_display_box(app, width=500, height=300)
    log_box.pack(padx=20, pady=20, fill="both", expand=True)
    log_box.configure_logs()

    # test logs
    log_box.add_log_line("System started", "DEFAULT")
    log_box.add_log_line("Connected to database", "DEBUG")
    log_box.add_log_line("Low disk space", "WARNING")
    log_box.add_log_line("Fatal error: out of memory", "ERROR")


    app.mainloop()


if __name__ == "__main__":
    main()
