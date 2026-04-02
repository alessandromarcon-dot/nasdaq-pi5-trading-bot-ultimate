import customtkinter as ctk

class MainDashboard(ctk.CTk):
      def __init__(self, config_manager):
                super().__init__()
                self.config = config_manager
                self.title("Topstep Elite Bot - Dashboard")
                self.geometry("800x600")
                self._setup_ui()

      def _setup_ui(self):
                self.label = ctk.CTkLabel(self, text="Bot Status: Ready", font=("Inter", 20))
                self.label.pack(pady=20)
                self.start_btn = ctk.CTkButton(self, text="Start Bot", command=self.on_start)
                self.start_btn.pack(pady=10)

      def on_start(self):
                self.label.configure(text="Bot Status: Running", text_color="green")
        
