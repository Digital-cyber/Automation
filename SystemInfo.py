import platform
import psutil

def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Total Memory": round(psutil.virtual_memory().total / (1024 ** 3), 2)
    }

    for key, value in system_info.items():
        print(f"{key}: {value}")


get_system_info()
