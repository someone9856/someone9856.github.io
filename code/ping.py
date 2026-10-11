import subprocess
import platform

print("=" * 50)
print(" Customized Ping Utility")
print("=" * 50)
host = input("Enter Website or IP Address: ")
system = platform.system()
if system == "Windows":
    command = ["ping", "-n", "4", host]
else:
    command = ["ping", "-c", "4", host]
try:
    result = subprocess.run(command, capture_output=True, text=True)
    print("\nPing Results\n")
    print(result.stdout)
    if result.returncode == 0:
        print("Server Status : Reachable")
    else:
        print("Server Status : Unreachable")
except Exception as e:
    print("Error:", e)
