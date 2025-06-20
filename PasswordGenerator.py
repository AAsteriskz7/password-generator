from tkinter import *
from tkinter import messagebox # For error popups
import string
import secrets
import os # For path joining, though not strictly necessary for a single filename

# --- Word List Loading ---
def load_word_list(filepath="wordlist.txt") -> list:
    """
    Loads a list of words from the specified filepath.
    Each word is expected on a new line.
    Strips whitespace and filters out empty lines.
    Returns an empty list if the file is not found or an error occurs.
    """
    words = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                word = line.strip()
                if word:
                    words.append(word)
        if not words and filepath == "wordlist.txt": # Only print critical warning for default list
            print(f"Warning: Default wordlist file '{filepath}' was empty or contained no valid words.")
    except FileNotFoundError:
        if filepath == "wordlist.txt": # Only print critical error for default list
            print(f"Error: Default wordlist file '{filepath}' not found. Passphrase generation will be disabled.")
    except IOError as e:
        if filepath == "wordlist.txt":
            print(f"Error reading default wordlist file '{filepath}': {e}. Passphrase generation will be disabled.")
    return words

WORDS = load_word_list()

# --- Passphrase Generation ---
def generate_passphrase(num_words: int, word_list: list) -> str:
    """
    Generates a passphrase by randomly selecting words from the given word_list.

    Args:
        num_words (int): The number of words to include in the passphrase.
        word_list (list): A list of strings from which to select words.

    Returns:
        str: A hyphen-separated passphrase string, or an error message string
             if the word_list is empty or num_words is invalid.
    """
    if not word_list or num_words < 1: # num_words < 1 check is now more for API robustness
        return "Error: Word list is empty or invalid number of words requested."
    try:
        chosen_words = [secrets.choice(word_list) for _ in range(num_words)]
    except IndexError: # Should be rare if word_list is not empty
        return "Error: Could not select words from the list."
    return "-".join(chosen_words)

# --- Core Password Generation Logic ---
def generate_secure_password(length: int, use_uppercase: bool, use_lowercase: bool, use_digits: bool, use_symbols: bool) -> str:
    """
    Generates a secure password based on specified criteria.
    """
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    if not character_set:
        return "Error: No character types selected."
    try:
        password = ''.join(secrets.choice(character_set) for _ in range(length))
    except IndexError:
        return "Error: Could not generate password."
    return password

# --- Global Tkinter Variables ---
root = None
length_entry = None
uppercase_var, lowercase_var, digits_var, symbols_var = None, None, None, None
password_display_entry = None
copy_button = None
num_words_entry = None # For passphrase UI

# --- UI Command Functions ---
def display_generated_password():
    """
    Handles the "Generate Password" button click for standard passwords.
    """
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, password_display_entry, copy_button
    try:
        length = int(length_entry.get())
        if not (8 <= length <= 128):
            messagebox.showerror("Error", "Password length must be between 8 and 128 characters.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid password length. Please enter a number.")
        return

    use_upper = uppercase_var.get()
    use_lower = lowercase_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    if not (use_upper or use_lower or use_digits or use_symbols):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    generated_p = generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols)

    password_display_entry.config(state="normal")
    password_display_entry.delete(0, END)
    password_display_entry.insert(0, generated_p)
    password_display_entry.config(state="readonly")

    if generated_p and not generated_p.startswith("Error:"):
        copy_button.config(state=NORMAL)
    else:
        copy_button.config(state=DISABLED)

def display_generated_passphrase():
    """
    Handles the "Generate Passphrase" button click.
    Validates inputs, calls generate_passphrase, and updates the UI.
    """
    global num_words_entry, WORDS, password_display_entry, copy_button

    if not WORDS: # Check if wordlist is loaded (button might be enabled if loaded then file deleted)
        messagebox.showerror("Error", "Word list is not loaded or is empty. Cannot generate passphrase.")
        # Optionally, disable the button again if this happens, though initial check in setup_ui is primary
        # passphrase_generate_button = passphrase_options_frame.winfo_children()[-1] # This needs to be robust
        # if passphrase_generate_button: passphrase_generate_button.config(state=DISABLED)
        return

    try:
        num_words_val = int(num_words_entry.get())
        if not (3 <= num_words_val <= 10): # Example range, adjust as needed
            messagebox.showerror("Error", f"Number of words should be between 3 and 10. You entered: {num_words_val}.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input: Number of words must be an integer.")
        return

    # Call the core passphrase generation function
    passphrase = generate_passphrase(num_words_val, WORDS)

    # Update the shared display entry
    password_display_entry.config(state="normal")
    password_display_entry.delete(0, END)
    password_display_entry.insert(0, passphrase)
    password_display_entry.config(state="readonly")

    # Enable or disable copy button based on success
    if passphrase and not passphrase.startswith("Error:"):
        copy_button.config(state=NORMAL)
    else:
        copy_button.config(state=DISABLED) # Disable if an error message was returned

def copy_to_clipboard():
    """
    Copies the content from the display entry to the clipboard.
    """
    global password_display_entry, root
    content = password_display_entry.get()
    if content and not content.startswith("Error:"):
        root.clipboard_clear()
        root.clipboard_append(content)
        messagebox.showinfo("Copied", "Content copied to clipboard!")
    elif content.startswith("Error:"):
        messagebox.showwarning("Copy Error", "Cannot copy an error message.")

# --- UI Setup ---
def setup_ui(root_window):
    """
    Creates and arranges all Tkinter widgets in the main window.
    """
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var
    global password_display_entry, copy_button, num_words_entry

    root_window.title("Secure Password & Passphrase Generator")
    root_window.geometry("500x550")

    # --- Password Options Frame ---
    password_options_main_frame = LabelFrame(root_window, text="Standard Password Options", padx=10, pady=10)
    password_options_main_frame.pack(pady=10, padx=10, fill="x")

    length_label_frame = Frame(password_options_main_frame)
    length_label_frame.pack(fill="x", pady=5)
    Label(length_label_frame, text="Password Length (8-128):").pack(side=LEFT, padx=(0,5))
    length_entry = Entry(length_label_frame, width=5)
    length_entry.pack(side=LEFT)
    length_entry.insert(0, "16")

    Label(password_options_main_frame, text="Include Character Types:").pack(anchor=W, pady=(5,0))
    check_frame = Frame(password_options_main_frame)
    check_frame.pack(fill="x")
    uppercase_var = BooleanVar(value=True)
    Checkbutton(check_frame, text="Uppercase (A-Z)", var=uppercase_var).pack(anchor=W)
    lowercase_var = BooleanVar(value=True)
    Checkbutton(check_frame, text="Lowercase (a-z)", var=lowercase_var).pack(anchor=W)
    digits_var = BooleanVar(value=True)
    Checkbutton(check_frame, text="Numbers (0-9)", var=digits_var).pack(anchor=W)
    symbols_var = BooleanVar(value=False)
    Checkbutton(check_frame, text="Symbols (!@#$)", var=symbols_var).pack(anchor=W)

    Button(password_options_main_frame, text="Generate Password", command=display_generated_password).pack(pady=(10,0))

    # --- Passphrase Options Frame ---
    passphrase_options_frame = LabelFrame(root_window, text="Passphrase Generation Options", padx=10, pady=10)
    passphrase_options_frame.pack(pady=10, padx=10, fill="x")

    num_words_frame = Frame(passphrase_options_frame)
    num_words_frame.pack(fill="x", pady=5)
    Label(num_words_frame, text="Number of words (e.g., 3-10):").pack(side=LEFT, padx=(0,5)) # Updated range in label
    num_words_entry = Entry(num_words_frame, width=5)
    num_words_entry.pack(side=LEFT)
    num_words_entry.insert(0, "4")

    passphrase_generate_button = Button(passphrase_options_frame, text="Generate Passphrase", command=display_generated_passphrase) # Updated command
    passphrase_generate_button.pack(pady=(10,0))

    if not WORDS:
        passphrase_generate_button.config(state=DISABLED)
        Label(passphrase_options_frame, text="Wordlist not loaded. Passphrase generation disabled.", fg="red").pack(pady=5)

    # --- Result Display Frame (Shared) ---
    result_frame = LabelFrame(root_window, text="Generated Output", padx=10, pady=10)
    result_frame.pack(pady=10, padx=10, fill="x")

    display_frame = Frame(result_frame)
    display_frame.pack(fill="x", pady=5)
    password_display_entry = Entry(display_frame, width=35, state="readonly")
    password_display_entry.pack(side=LEFT, expand=True, fill="x", padx=(0,5))
    copy_button = Button(display_frame, text="Copy", command=copy_to_clipboard, state=DISABLED)
    copy_button.pack(side=LEFT)

# --- Main Application Execution ---
if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    if WORDS:
        print(f"Successfully loaded {len(WORDS)} words from wordlist.txt")
    else:
        print("Wordlist is empty or could not be loaded. Check for previous error messages from load_word_list.")
    root.mainloop()
