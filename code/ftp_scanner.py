from ftplib import FTP
from ftplib import all_errors

def anonymous_ftp_scan(host, port=21):
    print("=" * 50)
    print(" ANONYMOUS FTP SCANNER")
    print("=" * 50)
    print(f"Target: {host}")
    print(f"Port  : {port}")
    print()
    ftp = FTP()
    try:
        print("[1] Connecting to FTP server...")
        ftp.connect(host, port, timeout=10)
        print("[+] FTP server is reachable")
        print("[+] Server response:", ftp.getwelcome())
        print("\n[2] Testing anonymous login...")
        ftp.login(user="anonymous", passwd="anonymous@example.com")
        print("[+] Anonymous login SUCCESSFUL")
        print("[!] The FTP server permits anonymous access.")
        print("\n[3] Checking accessible directory...")
        files = ftp.nlst()
        if files:
            print("[+] Directory listing is available:")
            for item in files:
                print("   ", item)
        else:
            print("[-] Directory is empty or listing is unavailable.")
        ftp.quit()
    except all_errors as error:
        print("[-] Anonymous login failed or FTP connection failed.")
        print("[!] Error:", error)
        try:
            ftp.close()
        except:
            pass

# Enter an authorized FTP server here
target = input("Enter FTP server address: ")
anonymous_ftp_scan(target)
