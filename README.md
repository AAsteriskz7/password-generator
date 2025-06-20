# Secure Password & Passphrase Generator

## Overview
A Python Tkinter application for generating strong, customizable passwords and memorable passphrases. It provides a user-friendly graphical interface to create secure credentials tailored to your needs.

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
    *   Includes a sample `wordlist.txt` for passphrase generation.

## Requirements/Dependencies
*   **Python 3.x:** The application is written in Python 3.
*   **Tkinter:** Uses the Tkinter library for the GUI, which is part of the Python standard library. No separate installation is typically required.
*   **`wordlist.txt`:** For the passphrase generation feature, a file named `wordlist.txt` containing words (one per line) must be present in the same directory as `PasswordGenerator.py`. A sample file with English words is included. You can customize this file with your own words. If this file is not found or is empty, passphrase generation will be disabled.

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
The application window is divided into sections for generating standard passwords and passphrases, with a shared area for displaying the output.

### For Standard Password Generation:
1.  **Locate the "Standard Password Options" section.**
2.  **Enter Password Length:** Input your desired password length in the "Password Length (8-128):" field.
3.  **Select Character Types:** Check the boxes for the character types (Uppercase, Lowercase, Numbers, Symbols) you want to include. At least one type must be selected.
4.  **Generate Password:** Click the "Generate Password" button.
5.  **View and Copy:** The generated password will appear in the "Generated Output" field. Click the "Copy" button to copy it to your clipboard.

### For Passphrase Generation:
1.  **Locate the "Passphrase Generation Options" section.**
2.  **Ensure `wordlist.txt` is ready:** The application requires `wordlist.txt` to be in the same directory. If the wordlist is not found or is empty, the "Generate Passphrase" button will be disabled, and a warning message will be shown in this section.
3.  **Enter Number of Words:** Input your desired number of words (between 3 and 10) in the "Number of words" field.
4.  **Generate Passphrase:** Click the "Generate Passphrase" button.
5.  **View and Copy:** The generated passphrase (e.g., "random-chosen-words-here") will appear in the "Generated Output" field. Click the "Copy" button to copy it to your clipboard.

## Screenshot
*(A screenshot of the application interface could be added here to give users a visual preview.)*

## License
This project is open source. You are free to use, modify, and distribute it. Consider adding a specific open-source license (e.g., MIT License) if you plan to share it widely.
