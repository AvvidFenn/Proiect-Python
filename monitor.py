import psutil
from datetime import datetime

def citeste_parametrii():
   return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "cpu": psutil.cpu_la_suta(interval=None),
        "ram": psutil.memorie_virtuala().percent,
    }
