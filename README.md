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

## How to Run
1.  **Get the code:**
    *   Clone the repository (if you are using Git):
        ```bash
        git clone <repository_url>
        ```
        (Replace `<repository_url>` with the actual URL if applicable)
    *   Alternatively, download `PasswordGenerator.py` and `wordlist.txt` into the same directory.
2.  **Ensure Python 3 is installed:**
    *   You can download it from [python.org](https://www.python.org/downloads/) if you don't have it.
3.  **Open a terminal or command prompt.**
4.  **Navigate to the directory** where `PasswordGenerator.py` and `wordlist.txt` are located.
    ```bash
    cd path/to/directory
    ```
5.  **Run the script** using the command:
    ```bash
    python PasswordGenerator.py
    ```

## How to Use
The application window is divided into sections for generating standard passwords and passphrases, with a shared area for displaying the output and its calculated strength.

### For Standard Password Generation:
1.  **Locate the "Standard Password Options" section.**
2.  **Enter Password Length:** Input your desired password length in the "Password Length (8-128):" field.
3.  **Select Character Types:** Check the boxes for the character types (Uppercase, Lowercase, Numbers, Symbols) you want to include. At least one type must be selected.
4.  **Generate Password:** Click the "Generate Password" button.
5.  **View Output:** The generated password will appear in the "Generated Output" field. Below it, a strength indicator (e.g., "Strength: Strong") will show the calculated strength with a corresponding color.
6.  **Copy Password:** Click the "Copy" button to copy the generated password to your clipboard.

### For Passphrase Generation:
1.  **Locate the "Passphrase Generation Options" section.**
2.  **Ensure `wordlist.txt` is ready:** The application requires `wordlist.txt`. If not found or empty, passphrase generation is disabled.
3.  **Enter Number of Words:** Input your desired number of words (between 3 and 10) in the "Number of words" field.
4.  **Generate Passphrase:** Click the "Generate Passphrase" button.
5.  **View Output:** The generated passphrase will appear in the "Generated Output" field. Below it, a strength indicator will show its calculated strength.
6.  **Copy Passphrase:** Click the "Copy" button to copy the generated passphrase.

## Configuration
*   **Settings Persistence:** Your preferred settings for password length, character types, and the number of passphrase words are automatically saved to a file named `config.json` when you close the application. This file is created in the same directory as the script.
*   These settings are reloaded the next time you start the application, restoring your previous configuration.
*   **Reset to Defaults:** If you wish to reset the application to its original default settings, you can simply delete the `config.json` file before starting the application.

## Screenshot
*(A screenshot of the application interface could be added here to give users a visual preview.)*

## License
This project is open source. You are free to use, modify, and distribute it. Consider adding a specific open-source license (e.g., MIT License) if you plan to share it widely.
