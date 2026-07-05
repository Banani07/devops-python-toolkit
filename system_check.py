import psutil
import subprocess
import traceback
import platform

try:
    print("NEW VERSION RUNNING")

    disk = psutil.disk_usage('/')
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    if platform.system() == "Windows":
        ping_cmd = ["ping", "-n", "4", "google.com"]
    else:
        ping_cmd = ["ping", "-c", "4", "google.com"]

    ping = subprocess.run(
    ping_cmd,
    capture_output=True,
    text=True
    )

    output = f"""
CPU Usage: {cpu}%
Memory Usage: {memory.percent}%
Disk Usage: {disk.percent}%

Ping Output:
{ping.stdout}
"""

    print(output)   # 👈 THIS LINE ADDED

    with open("output.txt", "w") as f:
        f.write(output)

except Exception as e:
    print("ERROR:", e)   # 👈 IMPORTANT
    with open("error_log.txt", "w") as f:
        f.write(str(e) + "\n")
        f.write(traceback.format_exc())