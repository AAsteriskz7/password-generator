# Secure Password & Passphrase Generator

## Overview

A Python Tkinter application for generating strong, customizable passwords and memorable passphrases. It provides a user-friendly graphical interface to create secure credentials tailored to your needs, with visual strength feedback and settings persistence.

## Features
*   **Standard Password Generation:**
    *   Generates cryptographically secure passwords using Python's `secrets` module.
    *   Customizable password length (default 16, range 8-128).
    *   Options to include or exclude specific character types:
        *   Uppercase letters (A-Z)
        *   Lowercase letters (a-z)
        *   Numbers (0-9)
        *   Symbols (e.g., !@#$%^&*)
*   **Passphrase Generation:**
    *   Generates memorable passphrases from a customizable word list (e.g., "word1-word2-word3-word4").
    *   Uses `secrets.choice` for selecting words from the list.
    *   Customizable number of words for passphrases (default 4, range 3-10).
*   **General:**
    *   User-friendly Graphical User Interface (GUI).
    *   Convenient "Copy to Clipboard" functionality for the generated password or passphrase.

 *   **Password/Passphrase Strength Indicator:** Provides immediate visual feedback (e.g., "Strength: Strong" with corresponding colors) on the generated output.
    *   **Settings Persistence:** Automatically saves your last used password generation options (length, character types) and passphrase options (number of words) to a `config.json` file. These settings are loaded when the app starts.
    *   Includes a sample `wordlist.txt` for passphrase generation.

## Requirements/Dependencies & Files
*   **Python 3.x:** The application is written in Python 3.
*   **Tkinter:** Uses the Tkinter library for the GUI, which is part of the Python standard library. No separate installation is typically required.
*   **Application Files:**
    *   `PasswordGenerator.py`: The main Python script.
    *   `wordlist.txt`: A plain text file containing words (one per line) required for the passphrase generation feature. A sample file is included. This file must be in the same directory as the script.
    *   `config.json` (Generated): This file is automatically created by the application in the same directory to store your last used settings. It will be created after you close the application for the first time.

## License
This project is open source. You are free to use, modify, and distribute it. Consider adding a specific open-source license (e.g., MIT License) if you plan to share it widely.
