# built ins
import platform
import socket

# pip install
import psutil

def get_system_info() -> dict:
    """Returns a dictionary containing system information."""
    system_info = {
        "OS": platform.system(),
        "OS version": platform.version(),
        "OS Release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "python_build": platform.python_build(),
        "python_compiler": platform.python_compiler(),
        # "uname": platform.uname(),
    }

    return system_info

def usage_info() -> dict:
    """Returns a dictionary containing usage information."""

    # Memory Information
    svmem = psutil.virtual_memory()

    # Disk Information
    disk_usage = psutil.disk_usage('/') # Use appropriate path for non-Unix systems

    usage_info = {
        "CPU Cores": psutil.cpu_count(logical=False),
        "Total CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Total (GB)": svmem.total / (1024**3),
        "Memory Available (GB)": svmem.available / (1024**3),
        "Memory Used (GB)": svmem.used / (1024**3),
        "Memory Usage Percentage (%)": svmem.percent,
        "Disk Total Space (GB)": disk_usage.total / (1024**3),
        "Disk Used Space (GB)": disk_usage.used / (1024**3),
        "Disk Free Space (GB)": disk_usage.free / (1024**3)
    }

    return usage_info

if __name__ == "__main__":
    # info = get_system_info()
    info = usage_info()
    for key, value in info.items():
        print(f"{key}: {value:.2f}")