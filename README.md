# Secure Password Generator

## Overview
A Python Tkinter application for generating strong, customizable passwords. It provides a user-friendly graphical interface to create passwords tailored to your security needs.

## Features
*   Generates cryptographically secure passwords using Python's `secrets` module.
*   Customizable password length.
*   Options to include or exclude specific character types:
    *   Uppercase letters (A-Z)
    *   Lowercase letters (a-z)
    *   Numbers (0-9)
    *   Symbols (e.g., !@#$%^&*)
*   User-friendly Graphical User Interface (GUI).
*   Convenient "Copy to Clipboard" functionality for the generated password.

## Requirements/Dependencies
*   **Python 3.x:** The application is written in Python 3.
*   **Tkinter:** Uses the Tkinter library for the GUI, which is part of the Python standard library. No separate installation is typically required.

## How to Run
1.  **Get the code:**
    *   Clone the repository (if you are using Git):
        ```bash
        git clone <repository_url>
        ```
    *   Alternatively, download the `PasswordGenerator.py` file directly.
2.  **Ensure Python 3 is installed:**
    *   You can download it from [python.org](https://www.python.org/downloads/) if you don't have it.
3.  **Open a terminal or command prompt.**
4.  **Navigate to the directory** where `PasswordGenerator.py` is located.
    ```bash
    cd path/to/directory
    ```
5.  **Run the script** using the command:
    ```bash
    python PasswordGenerator.py
    ```

## How to Use
1.  **Enter Password Length:** Input your desired password length in the "Password Length (8-128):" field. The length must be between 8 and 128 characters.
2.  **Select Character Types:** Check the boxes for the character types you want to include in your password:
    *   Uppercase (A-Z)
    *   Lowercase (a-z)
    *   Numbers (0-9)
    *   Symbols (!@#$)
    You must select at least one character type.
3.  **Generate Password:** Click the "Generate Password" button.
4.  **View Password:** The newly generated password will appear in the text field next to "Generated Password:".
5.  **Copy Password:** Click the "Copy" button to copy the generated password to your system clipboard. A confirmation message will appear.

## Screenshot
*(A screenshot of the application interface could be added here to give users a visual preview.)*

## License
This project is open source. You are free to use, modify, and distribute it. Consider adding a specific open-source license (e.g., MIT License) if you plan to share it widely.
