import subprocess
import os
import re
from datetime import datetime

def get_wifi_profiles():
    """
    Retrieve all WiFi profiles from the system.

    Returns:
        list: List of WiFi profile names
    """
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore")
        profile_names = re.findall(r'All User Profile\s*: (.*)', output)
        return [profile.strip() for profile in profile_names]
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving WiFi profiles: {e}")
        return []

def get_wifi_password(profile_name):
    """
    Get the password for a specific WiFi profile.

    Args:
        profile_name (str): Name of the WiFi profile

    Returns:
        str or None: Password if found, None otherwise
    """
    try:
        output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']
        ).decode('utf-8', errors="ignore")
        password = re.search(r'Key Content\s*: (.*)', output)
        return password.group(1).strip() if password else None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving password for {profile_name}: {e}")
        return None

def print_banner():
    """
    Print merged ASCII art banner with copyright.
    """
    banner = r"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║                         WiFi PassHunter - Password Extractor                    ║
║                     Copyright (c) 2025 Vijay Vairagade                          ║
║                            All Rights Reserved                                  ║
╚══════════════════════════════════════════════════════════════════════════════════╝

🔐 WiFi PassHunter - Extract & Save Your WiFi Passwords Securely
📧 Author: Vijay Vairagade
🚀 Version: 1.0
========================================================================================
"""
    print(banner)

def save_wifi_passwords():
    """
    Main function to extract and save WiFi passwords to current working directory.
    """
    print_banner()

    wifi_profiles = get_wifi_profiles()
    if not wifi_profiles:
        print("No WiFi profiles found.")
        return

    print(f"Found {len(wifi_profiles)} WiFi profiles. Extracting passwords...")

    wifi_passwords = {}
    profiles_without_passwords = []

    for profile in wifi_profiles:
        print(f"Processing: {profile}")
        password = get_wifi_password(profile)
        if password:
            wifi_passwords[profile] = password
        else:
            profiles_without_passwords.append(profile)

    try:
        current_dir = os.getcwd()
        filename = "wifi_passwords.txt"
        filepath = os.path.join(current_dir, filename)

        with open(filepath, "w", encoding='utf-8') as file:
            file.write("WiFi PassHunter - WiFi Password Extraction Tool\n")
            file.write("Copyright (c) 2025 Vijay Vairagade\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")

            if wifi_passwords:
                file.write("SAVED WIFI PASSWORDS:\n")
                file.write("-" * 25 + "\n\n")
                for profile, password in wifi_passwords.items():
                    file.write(f"Profile: {profile}\n")
                    file.write(f"Password: {password}\n")
                    file.write("-" * 30 + "\n\n")

            if profiles_without_passwords:
                file.write("PROFILES WITHOUT PASSWORDS:\n")
                file.write("-" * 30 + "\n\n")
                for profile in profiles_without_passwords:
                    file.write(f"- {profile}\n")
                file.write("\n")

            file.write(f"Total profiles found: {len(wifi_profiles)}\n")
            file.write(f"Profiles with passwords: {len(wifi_passwords)}\n")
            file.write(f"Profiles without passwords: {len(profiles_without_passwords)}\n")

        print(f"\n✅ SUCCESS! WiFi passwords saved to: {filepath}")
        print(f"🔑 Profiles with passwords: {len(wifi_passwords)}")
        if profiles_without_passwords:
            print(f"⚠️  Profiles without passwords: {len(profiles_without_passwords)}")

    except Exception as e:
        print(f"❌ Error saving WiFi passwords: {e}")

if __name__ == "__main__":
    if os.name != 'nt':
        print("❌ This script is designed for Windows systems only.")
        exit(1)

    try:
        save_wifi_passwords()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    input("\nPress Enter to exit...")
