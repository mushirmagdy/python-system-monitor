import shutil
import psutil


def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_percent:.1f}%")


def check_memory_usage():
    memory = psutil.virtual_memory()
    print(f"Memory usage: {memory.percent:.1f}%")


def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100

    print(f"Disk usage: {usage_percent:.1f}%")


def main():
    print("Python System Monitoring Tool")
    print("=============================")

    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()


if __name__ == "__main__":
    main()
