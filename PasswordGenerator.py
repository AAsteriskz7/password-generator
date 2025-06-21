from tkinter import *
from tkinter import messagebox # For error popups
import string
import secrets
import os # For path joining, though not strictly necessary for a single filename
import json # For saving and loading settings

# --- Word List Loading ---
def load_word_list(filepath="wordlist.txt") -> list:
    words = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                word = line.strip()
                if word: words.append(word)
        if not words and filepath == "wordlist.txt": 
            print(f"Warning: Default wordlist file '{filepath}' was empty or contained no valid words.")
    except FileNotFoundError:
        if filepath == "wordlist.txt": 
            print(f"Error: Default wordlist file '{filepath}' not found. Passphrase generation will be disabled.")
    except IOError as e:
        if filepath == "wordlist.txt":
            print(f"Error reading default wordlist file '{filepath}': {e}. Passphrase generation will be disabled.")
    return words

WORDS = load_word_list()

# --- Generation Logic (Passphrase, Password, Strengths) ---
def generate_passphrase(num_words: int, word_list: list) -> str:
    if not word_list or num_words < 1: return "Error: Word list is empty or invalid."
    try: return "-".join(secrets.choice(word_list) for _ in range(num_words))
    except IndexError: return "Error: Could not select words."

def generate_secure_password(length: int, use_uppercase: bool, use_lowercase: bool, use_digits: bool, use_symbols: bool) -> str:
    char_set = ""
    if use_uppercase: char_set += string.ascii_uppercase
    if use_lowercase: char_set += string.ascii_lowercase
    if use_digits: char_set += string.digits
    if use_symbols: char_set += string.punctuation
    if not char_set: return "Error: No character types selected."
    try: return ''.join(secrets.choice(char_set) for _ in range(length))
    except IndexError: return "Error: Could not generate password."

def calculate_password_strength(password: str) -> tuple[str, str]:
    if not password: return ("Unknown", "grey")
    score, length = 0, len(password)
    if length < 8: score += 0
    elif length < 12: score += 1
    elif length < 16: score += 2
    else: score += 3
    char_types = sum([any(c in s for c in password) for s in [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]])
    if char_types == 1 and length >= 8: score += 1
    elif char_types == 2: score += 2
    elif char_types == 3: score += 3
    elif char_types == 4: score += 4
    if score <= 1: return ("Very Weak", "red")
    elif score == 2: return ("Weak", "orangered")
    elif score == 3: return ("Medium", "orange")
    elif score == 4: return ("Strong", "yellowgreen")
    return ("Very Strong", "green") if score >= 5 else ("Unknown", "grey")

def calculate_passphrase_strength(num_words: int) -> tuple[str, str]:
    if num_words <= 0: return ("Unknown", "grey")
    elif num_words < 3: return ("Weak", "orangered")
    elif num_words == 3: return ("Medium", "orange")
    elif num_words == 4: return ("Strong", "yellowgreen")
    return ("Very Strong", "green") if num_words >= 5 else ("Unknown", "grey")

# --- Settings Persistence & Application Lifecycle ---
def save_settings():
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, num_words_entry
    if not all([length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, num_words_entry]):
        print("Error: UI elements not initialized. Cannot save settings.")
        return
    settings = {
        'password_length': length_entry.get(), 'use_uppercase': uppercase_var.get(),
        'use_lowercase': lowercase_var.get(), 'use_digits': digits_var.get(),
        'use_symbols': symbols_var.get(), 'num_passphrase_words': num_words_entry.get()
    }
    try:
        with open("config.json", 'w') as f: json.dump(settings, f, indent=4)
        print("Settings saved to config.json")
    except IOError: print("Error: Could not save settings to config.json.")
    except Exception as e: print(f"An unexpected error occurred while saving settings: {e}")

def load_settings():
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, num_words_entry
    if not all([length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, num_words_entry]):
        print("Error: UI elements not initialized. Cannot load settings.")
        return
    try:
        with open("config.json", 'r') as f: loaded_settings = json.load(f)
        length_entry.delete(0, END); length_entry.insert(0, loaded_settings.get('password_length', '16'))
        uppercase_var.set(loaded_settings.get('use_uppercase', True))
        lowercase_var.set(loaded_settings.get('use_lowercase', True))
        digits_var.set(loaded_settings.get('use_digits', True))
        symbols_var.set(loaded_settings.get('use_symbols', False))
        num_words_entry.delete(0, END); num_words_entry.insert(0, loaded_settings.get('num_passphrase_words', '4'))
        print("Settings loaded from config.json")
    except FileNotFoundError: print("config.json not found. Using default settings.")
    except json.JSONDecodeError: print("Error decoding config.json. Using default settings.")
    except IOError: print("Error reading config.json. Using default settings.")
    except Exception as e: print(f"An unexpected error occurred while loading settings: {e}. Using default settings.")

def on_closing():
    """
    Handles the application shutdown sequence: saves settings and closes the window.
    """
    global root # Access the global root window instance
    print("Application closing. Saving settings...")
    save_settings()
    if root:
        root.destroy()

# --- Global Tkinter Variables ---
root = None
length_entry, num_words_entry = None, None
uppercase_var, lowercase_var, digits_var, symbols_var = None, None, None, None
password_display_entry, copy_button, strength_display_label = None, None, None

# --- UI Command Functions ---
def display_generated_password():
    global strength_display_label 
    strength_display_label.config(text="", fg="black")
    try:
        length = int(length_entry.get())
        if not (8 <= length <= 128): messagebox.showerror("Error", "Length must be 8-128."); return
    except ValueError: messagebox.showerror("Error", "Invalid length."); return
    use_upper, use_lower, use_digits, use_symbols = uppercase_var.get(), lowercase_var.get(), digits_var.get(), symbols_var.get()
    if not any([use_upper, use_lower, use_digits, use_symbols]): messagebox.showerror("Error", "Select char types."); return
    pwd_str = generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols)
    password_display_entry.config(state="normal"); password_display_entry.delete(0, END)
    password_display_entry.insert(0, pwd_str); password_display_entry.config(state="readonly")
    if not pwd_str.startswith("Error:"):
        copy_button.config(state=NORMAL)
        txt, color = calculate_password_strength(pwd_str)
        strength_display_label.config(text=f"Strength: {txt}", fg=color)
    else:
        copy_button.config(state=DISABLED); strength_display_label.config(text="", fg="black")

def display_generated_passphrase():
    global strength_display_label
    strength_display_label.config(text="", fg="black")
    if not WORDS: messagebox.showerror("Error", "Wordlist not loaded."); return
    try:
        num_val = int(num_words_entry.get())
        if not (3 <= num_val <= 10): messagebox.showerror("Error", "Words must be 3-10."); return
    except ValueError: messagebox.showerror("Error", "Invalid number of words."); return
    phrase_str = generate_passphrase(num_val, WORDS)
    password_display_entry.config(state="normal"); password_display_entry.delete(0, END)
    password_display_entry.insert(0, phrase_str); password_display_entry.config(state="readonly")
    if not phrase_str.startswith("Error:"):
        copy_button.config(state=NORMAL)
        txt, color = calculate_passphrase_strength(num_val)
        strength_display_label.config(text=f"Strength: {txt}", fg=color)
    else:
        copy_button.config(state=DISABLED); strength_display_label.config(text="", fg="black")

def copy_to_clipboard():
    content = password_display_entry.get()
    if content and not content.startswith("Error:"):
        root.clipboard_clear(); root.clipboard_append(content)
        messagebox.showinfo("Copied", "Content copied!")
    elif content.startswith("Error:"): messagebox.showwarning("Copy Error", "Cannot copy error.")

# --- UI Setup ---
def setup_ui(root_window):
    global root, length_entry, uppercase_var, lowercase_var, digits_var, symbols_var 
    global password_display_entry, copy_button, num_words_entry, strength_display_label
    root = root_window 
    root_window.title("Secure Password & Passphrase Generator"); root_window.geometry("500x580") 

    # Password Options
    pwd_frame = LabelFrame(root_window, text="Standard Password Options", padx=10, pady=10)
    pwd_frame.pack(pady=10, padx=10, fill="x")
    
    length_label_frame = Frame(pwd_frame) # Standard creation for length entry
    Label(length_label_frame, text="Password Length (8-128):").pack(side=LEFT, padx=(0,5))
    length_entry = Entry(length_label_frame, width=5)
    length_entry.pack(side=LEFT)
    length_entry.insert(0, "16")
    length_label_frame.pack(fill="x", pady=5)

    Label(pwd_frame, text="Include Character Types:").pack(anchor=W, pady=(5,0))
    chk_frame = Frame(pwd_frame); chk_frame.pack(fill="x")
    uppercase_var = BooleanVar(value=True); Checkbutton(chk_frame, text="Uppercase", var=uppercase_var).pack(anchor=W)
    lowercase_var = BooleanVar(value=True); Checkbutton(chk_frame, text="Lowercase", var=lowercase_var).pack(anchor=W)
    digits_var = BooleanVar(value=True); Checkbutton(chk_frame, text="Numbers", var=digits_var).pack(anchor=W)
    symbols_var = BooleanVar(value=False); Checkbutton(chk_frame, text="Symbols", var=symbols_var).pack(anchor=W)
    Button(pwd_frame, text="Generate Password", command=display_generated_password).pack(pady=(10,0))

    # Passphrase Options
    phrase_frame = LabelFrame(root_window, text="Passphrase Generation", padx=10, pady=10)
    phrase_frame.pack(pady=10, padx=10, fill="x")
    num_words_fr = Frame(phrase_frame); num_words_fr.pack(fill="x", pady=5)
    Label(num_words_fr, text="Number of words (3-10):").pack(side=LEFT, padx=(0,5))
    num_words_entry = Entry(num_words_fr, width=5); num_words_entry.pack(side=LEFT); num_words_entry.insert(0, "4")
    btn_phrase = Button(phrase_frame, text="Generate Passphrase", command=display_generated_passphrase)
    btn_phrase.pack(pady=(10,0))
    if not WORDS: btn_phrase.config(state=DISABLED); Label(phrase_frame, text="Wordlist not loaded.", fg="red").pack(pady=5)

    # Result Display
    res_frame = LabelFrame(root_window, text="Generated Output", padx=10, pady=10)
    res_frame.pack(pady=10, padx=10, fill="x")
    disp_fr = Frame(res_frame); disp_fr.pack(fill="x", pady=5)
    password_display_entry = Entry(disp_fr, width=35, state="readonly")
    password_display_entry.pack(side=LEFT, expand=True, fill="x", padx=(0,5))
    copy_button = Button(disp_fr, text="Copy", command=copy_to_clipboard, state=DISABLED); copy_button.pack(side=LEFT)
    strength_display_label = Label(res_frame, text="", font=("Arial", 10)); strength_display_label.pack(pady=(5,0))
    
    load_settings() 

# --- Main Application Execution ---
if __name__ == "__main__":
    root_tk = Tk() 
    setup_ui(root_tk) # This now also assigns to the global 'root'
    
    # Set the close protocol
    root_tk.protocol("WM_DELETE_WINDOW", on_closing)
    
    if WORDS: print(f"Loaded {len(WORDS)} words.")
    else: print("Wordlist empty/not loaded.")
    
    root_tk.mainloop()
