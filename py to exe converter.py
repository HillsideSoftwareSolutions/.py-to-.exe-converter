import os
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt):
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        exit()

def print_banner():
    print(r"""
                 _                                                         _            
   _ __  _   _  | |_ ___      _____  _____    ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
  | '_ \| | | | | __/ _ \    / _ \ \/ / _ \  / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 _| |_) | |_| | | || (_) |  |  __/>  <  __/ | (_| (_) | | | \ V /  __/ |  | ||  __/ |   
(_) .__/ \__, |  \__\___/  (_)___/_/\_\___|  \___\___/|_| |_|\_/ \___|_|   \__\___|_|   
  |_|    |___/                                                                          
    """)

def convert_py_to_exe(path, filename):
    src_file = os.path.join(path, filename)
    if not os.path.isfile(src_file):
        print("[!] File does not exist.")
        return

    clear_screen()
    print_banner()
    print(f"[*] Converting '{filename}' to .exe...\n")

    try:
        os.chdir(path)  # Change to directory of the script

        # Use Python to run pyinstaller as a module
        result = subprocess.run([
            "python", "-m", "PyInstaller",
            "--onefile",
            "--noconsole",  # Remove this if you want to keep the console visible
            filename
        ], text=True, capture_output=True)

        if result.returncode == 0:
            print(f"\n[+] The file is now a .exe, you may open the dist folder to view it.")
        else:
            print("[!] PyInstaller failed with the following error:\n")
            print(result.stderr)
    except Exception as e:
        print(f"\n[!] Unexpected Error: {e}")
    finally:
        input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print_banner()

        path = get_input("Enter File Path: ")
        if not os.path.isdir(path):
            print("[!] Invalid path.")
            input("\nPress Enter to retry...")
            continue

        filename = get_input("Enter File Name (e.g. script.py): ")
        full_file = os.path.join(path, filename)
        if not os.path.isfile(full_file):
            print("[!] File not found.")
            input("\nPress Enter to retry...")
            continue

        confirm = get_input(f"Confirm Convert '{filename}' to .exe? [Y/N]: ").lower()
        if confirm == 'y':
            convert_py_to_exe(path, filename)
        else:
            print("[*] Cancelled. Restarting...\n")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
