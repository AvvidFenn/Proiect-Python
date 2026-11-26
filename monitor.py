import psutil
from datetime import datetime

def citeste_parametrii():
   return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "cpu": psutil.cpu_percent(interval=None),
        "ram": psutil.virtual_memory().percent,
    }
