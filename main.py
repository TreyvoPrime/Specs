import platform
import psutil

def get_system_info():
    try:
        info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "OS Release": platform.release(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "CPU Cores (Physical)": psutil.cpu_count(logical=False),
            "CPU Cores (Logical)": psutil.cpu_count(logical=True),
            "Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
            "Disk Total (GB)": round(psutil.disk_usage('/').total / (1024 ** 3), 2)
        }
        return info
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    specs = get_system_info()
    for key, value in specs.items():
        print(f"{key}: {value}")
