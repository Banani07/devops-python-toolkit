import psutil
import subprocess
import traceback
import platform
import json
import logging
import os 

with open("config.json", "r") as f:
    config = json.load(f)
    
host = config["host"]
ping_count = config["ping_count"]
log_directory = config["log_directory"]

os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_directory, "system.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


try:
    logging.info("System Health Check Started")

    disk = psutil.disk_usage('/')
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    if platform.system() == "Windows":
        ping_cmd = ["ping", "-n", str(ping_count), host]
    else:
        ping_cmd = ["ping", "-c", str(ping_count), host]

    ping = subprocess.run(
    ping_cmd,
    capture_output=True,
    text=True
    )

    if memory.percent > config["memory_threshold"]:
        logging.warning("Memory usage exceeded threshold")

    if cpu > config["cpu_threshold"]:
        logging.warning("CPU usage exceeded threshold")

    output = f"""
CPU Usage: {cpu}%
Memory Usage: {memory.percent}%
Disk Usage: {disk.percent}%

Ping Output:
{ping.stdout}
"""

    logging.info(output)   # 👈 THIS LINE ADDED

    with open(os.path.join(log_directory, "output.txt"), "w") as f:
        f.write(output)

except Exception as e:
    print("ERROR:", e)
    logging.error(str(e))
    logging.error(traceback.format_exc())   # 👈 IMPORTANT
    with open(os.path.join(log_directory, "error_log.txt"), "w") as f:
        f.write(str(e) + "\n")
        f.write(traceback.format_exc())