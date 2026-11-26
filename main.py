import customtkinter as ctk
import psutil
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PlottareSistemAPP(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Monitor Sistem Live")
        self.geometry("950x620")
        
        self.max_sec = 60                                                      
        self.valori_timp = deque(maxlen=self.max_sec)     
        self.data_cpu = deque(maxlen=self.max_sec)        
        self.data_ram = deque(maxlen=self.max_sec)

        self._ui()
        self._plottare()
                              
    def _ui(self):
        rama_sus = ctk.CTkFrame(self)
        rama_sus.pack(fill="x", padx=15, pady=(15,5))
        self.cpu_Label = ctk.CTkLabel(rama_sus, text="CPU = 0%", font=ctk.CTkFont(size=18, weight="bold"))
        self.cpu_Label.pack(side="left", padx=20, pady=10)

        self.ram_Label = ctk.CTkLabel(rama_sus, text="RAM = 0%", font=ctk.CTkFont(size=18, weight="bold"))
        self.ram_Label.pack(side="left", padx=20, pady=10)

        self.rama_plot = ctk.CTkFrame(self)
        self.rama_plot.pack(fill="both", expand=True, padx=15, pady=10)

        rama_jos = ctk.CTkFrame(self)
        rama_jos.pack(fill="x", padx=15, pady=(5,15))

        self.buton_pauza = ctk.CTkButton(rama_jos, text="Pause", width=30)
        self.buton_pauza.pack(side="left", padx=15, pady=10)

        self.buton_export = ctk.CTkButton(rama_jos, text="Export", width=30)
        self.buton_export.pack(side="left", padx=20, pady=10)

    def _plottare(self):
        plt.style.use("dark_background")
        self.fig, (self.ax_cpu, self.ax_ram) = plt.subplots(2, 1, figsize=(8, 5), dpi=100)
        self.fig.patch.set_facecolor("#2b2b2b")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.rama_plot)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
                                         
if __name__ == "__main__":
    app = PlottareSistemAPP()
    app.mainloop()
