import logging
import shutil
import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

logging.basicConfig(
    filename="system_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    message = f"CPU usage: {cpu_percent:.1f}%"
    print(message)
    logging.info(message)

    if cpu_percent >= CPU_THRESHOLD:
        warning = "WARNING: High CPU usage!"
        print(warning)
        logging.warning(warning)


def check_memory_usage():
    memory = psutil.virtual_memory()
    message = f"Memory usage: {memory.percent:.1f}%"
    print(message)
    logging.info(message)

    if memory.percent >= MEMORY_THRESHOLD:
        warning = "WARNING: High memory usage!"
        print(warning)
        logging.warning(warning)


def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100

    message = f"Disk usage: {usage_percent:.1f}%"
    print(message)
    logging.info(message)

    if usage_percent >= DISK_THRESHOLD:
        warning = "WARNING: High disk usage!"
        print(warning)
        logging.warning(warning)


def main():
    print("Python System Monitoring Tool")
    print("=============================")
    logging.info("System monitoring started")

    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()

    logging.info("System monitoring finished")


if __name__ == "__main__":
    main()
