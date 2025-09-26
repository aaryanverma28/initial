#!/usr/bin/env python3
import psutil
import os
import time
import platform
from datetime import datetime

def format_memory_size(bytes_value):
    """Format memory size into human readable format"""
    units = ['B', 'KB', 'MB', 'GB']
    size = float(bytes_value)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    
    return f"{size:.2f} {units[unit_index]}"

def get_memory_info():
    """Get memory information"""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'used': memory.used,
        'free': memory.available
    }

def get_cpu_usage():
    """Get CPU usage percentage"""
    return psutil.cpu_percent(interval=1)

def get_load_average():
    """Get system load averages"""
    try:
        return os.getloadavg()
    except AttributeError:  # Windows doesn't support getloadavg
        return (0.0, 0.0, 0.0)

def main():
    # Clear screen
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    
    # Print header
    system_name = platform.system()
    print(f"{system_name} System Monitor")
    print("=" * 20 + "\n")

    try:
        while True:
            # Move cursor to start position (works in Unix-like systems)
            if platform.system() != 'Windows':
                print("\033[4;0H", end='')
            else:
                os.system('cls')
                print(f"{system_name} System Monitor")
                print("=" * 20 + "\n")

            # Get and display CPU usage
            cpu_usage = get_cpu_usage()
            print(f"CPU Usage: {cpu_usage:.2f}%")

            # Get and display load averages
            load1, load5, load15 = get_load_average()
            print(f"Load Averages: {load1:.2f} (1 min), {load5:.2f} (5 min), {load15:.2f} (15 min)")

            # Get and display memory information
            memory = get_memory_info()
            print(f"Total Memory: {format_memory_size(memory['total'])}")
            print(f"Used Memory: {format_memory_size(memory['used'])}")
            print(f"Free Memory: {format_memory_size(memory['free'])}")

            time.sleep(1)  # Update every second

    except KeyboardInterrupt:
        print("\nExiting System Monitor...")

if __name__ == "__main__":
    main()