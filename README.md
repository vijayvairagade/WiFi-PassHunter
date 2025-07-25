# WiFi PassHunter

🔐 A powerful Python tool to extract and saved WiFi passwords from Windows systems.

## Copyright

Copyright (c) 2025 Vijay Vairagade  
All rights reserved.

## Description

WiFi PassHunter is a feature-rich Python script that extracts saved WiFi passwords from Windows systems using the built-in `netsh` command. It presents results with beautiful ASCII art and saves them to a formatted text file in the current working directory. Perfect for backing up your WiFi passwords or transferring them to a new device!

## Features

- 🎨 Beautiful ASCII art banner with copyright information
- ✅ Extracts all saved WiFi profiles from Windows
- ✅ Retrieves passwords for profiles that have them stored
- ✅ Saves results to a formatted text file in the current directory
- ✅ Provides detailed summary of extraction results
- ✅ Handles profiles without stored passwords gracefully
- ✅ Cross-platform detection (Windows only)
- 🚀 Professional console output with progress indicators

## Requirements

- **Operating System**: Windows (Windows 7, 8, 10, 11)
- **Python**: Python 3.6 or higher
- **Permissions**: Administrator privileges (required for accessing WiFi passwords)

No additional dependencies required - uses only Python standard library!

## Usage

### Method 1: Run as Administrator (Recommended)
1. Right-click on Command Prompt or PowerShell
2. Select "Run as administrator"
3. Navigate to the script directory
4. Run the script:
```bash
python wifi_passhunter.py
```

### Method 2: Double-click execution
1. Right-click on the Python script
2. Select "Run as administrator"

## Output

The script creates a file named `wifi_passwords.txt` in the current working directory with the following information:

- Header with copyright and generation timestamp
- List of all WiFi profiles with their passwords
- List of profiles without stored passwords
- Summary statistics

### Example Output File:
```
WiFi PassHunter - WiFi Password Extraction Tool
Copyright (c) 2025 Vijay Vairagade
Generated on: 2025-01-20 14:30:25
==================================================

SAVED WIFI PASSWORDS:
-------------------------

Profile: HomeNetwork_5G
Password: mySecurePassword123
------------------------------

Profile: OfficeWiFi
Password: company_wifi_2024
------------------------------

PROFILES WITHOUT PASSWORDS:
------------------------------
- GuestNetwork
- PublicHotspot

Total profiles found: 4
Profiles with passwords: 2
Profiles without passwords: 2
```

## Important Notes

### ⚠️ Security Considerations
- **Administrator Rights Required**: This script needs administrator privileges to access stored WiFi passwords
- **Sensitive Data**: The output file contains plain-text passwords - handle with care
- **Local Use Only**: Designed for personal use on your own devices

### 🔒 Legal and Ethical Use
- Only use this script on computers you own or have explicit permission to access
- Do not use this tool to access unauthorized networks
- Respect privacy and security policies in your organization

### 🛠️ Troubleshooting

**"Access Denied" Error:**
- Run Command Prompt or PowerShell as Administrator
- Ensure you have the necessary permissions on the system

**"No WiFi profiles found":**
- Check if WiFi is enabled on your system
- Verify that you have previously connected to WiFi networks

**Script fails on non-Windows systems:**
- This script is Windows-specific and uses `netsh` command
- Linux/Mac users should use alternative tools like `nmcli` or Keychain Access

## Technical Details

- Uses Windows `netsh wlan` commands to access WiFi profile information
- Employs regular expressions to parse command output
- Handles encoding issues with special characters
- Provides comprehensive error handling and user feedback

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is proprietary software. All rights reserved by Vijay Vairagade.

## Changelog

### Version 1.0 (2025-01-20)
- Initial release
- Basic WiFi password extraction functionality
- Save to current working directory
- Comprehensive error handling and user feedback

---

**Disclaimer**: This tool is for legitimate use only. Users are responsible for complying with all applicable laws and regulations.
