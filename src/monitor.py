import shutil


def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)

    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    usage_percent = (used / total) * 100

    print(f"Disk total: {total_gb:.2f} GB")
    print(f"Disk used: {used_gb:.2f} GB")
    print(f"Disk free: {free_gb:.2f} GB")
    print(f"Disk usage: {usage_percent:.1f}%")


def main():
    print("Python System Monitoring Tool")
    print("=============================")
    check_disk_usage()


if __name__ == "__main__":
    main()
