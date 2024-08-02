## What is a Bad USB?
A bad USB, "Rubber Ducky", or o.MG is a device disguised as a USB drive or cable.  It emulates keyboard and mouse input, in order to deploy malicious payloads.  The device is used by an unsuspecting victim, or an attacker can insert the device into the target machine directly.  The device can be used to deploy payloads that can steal data, install malware, or even take control of the machine.

Enterprise defenses against this attack include disabling USB ports, or requiring administrative privileges to install new devices. 

# Bad USB Blocker
This project is a simple proof of concept that attempts to detect faster-than-human keyboard input.  When this is detected, the script will insert random keypresses into the input stream.  Since most of these devices work by delivering pre-scripted keystrokes and mouse movements, this may be enough to disrupt the attack in many cases.  This method could be easily defeated by the attacker adding additional delay between keystrokes (eg DuckyScript DEFAULT_CHAR_DELAY) although this opens them to a greater chance of detection.
