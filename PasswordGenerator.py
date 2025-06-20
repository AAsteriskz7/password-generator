from tkinter import *
from tkinter import messagebox # For error popups
import string
import secrets

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

    # This check is a fallback; UI should prevent this state.
    if not character_set:
        return "Error: No character types selected."

    try:
        # Build the password using secrets.choice for cryptographic security
        password = ''.join(secrets.choice(character_set) for _ in range(length))
    except IndexError:
        # Should not happen if character_set is not empty and length is positive.
        return "Error: Could not generate password."
    return password

# --- Global Tkinter Variables ---
# These are global so they can be accessed by command functions.
# They will be initialized within setup_ui.
root = None
length_entry = None
uppercase_var, lowercase_var, digits_var, symbols_var = None, None, None, None
password_display_entry = None
copy_button = None

# --- UI Command Functions ---
def display_generated_password():
    """
    Handles the "Generate Password" button click.
    Validates inputs, calls generate_secure_password, and updates the UI.
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
        messagebox.showerror("Error", "Please select at least one character type (e.g., lowercase, numbers).")
        return

    generated_p = generate_secure_password(length, use_upper, use_lower, use_digits, use_symbols)

    # Update the password display entry
    password_display_entry.config(state="normal") # Enable to set text
    password_display_entry.delete(0, END)
    password_display_entry.insert(0, generated_p)
    password_display_entry.config(state="readonly") # Disable again

    # Enable or disable copy button based on success
    if generated_p and not generated_p.startswith("Error:"):
        copy_button.config(state=NORMAL)
    else:
        copy_button.config(state=DISABLED)

def copy_to_clipboard():
    """
    Copies the generated password from the display entry to the clipboard.
    """
    global password_display_entry, root
    password = password_display_entry.get()
    if password and not password.startswith("Error:"):
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    elif password.startswith("Error:"):
        messagebox.showwarning("Copy Error", "Cannot copy an error message.")
    # Do nothing if password field is empty (though copy button should be disabled)

# --- UI Setup ---
def setup_ui(root_window):
    """
    Creates and arranges all Tkinter widgets in the main window.
    """
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, password_display_entry, copy_button

    root_window.title("Secure Password Generator")

    # --- Main Frames ---
    options_frame = Frame(root_window, padx=10, pady=10)
    options_frame.pack(pady=10, fill="x")

    result_frame = Frame(root_window, padx=10, pady=10)
    result_frame.pack(pady=10, fill="x")

    # --- Password Length ---
    length_label_frame = Frame(options_frame) # To keep label and entry on one line
    length_label_frame.pack(fill="x")

    length_label = Label(length_label_frame, text="Password Length (8-128):")
    length_label.pack(side=LEFT, padx=(0,5), pady=5)

    length_entry = Entry(length_label_frame, width=5)
    length_entry.pack(side=LEFT, pady=5)
    length_entry.insert(0, "16") # Default length

    # --- Character Type Checkboxes ---
    # BooleanVars to hold the state of checkbuttons
    uppercase_var = BooleanVar(value=True)
    lowercase_var = BooleanVar(value=True)
    digits_var = BooleanVar(value=True)
    symbols_var = BooleanVar(value=False) # Symbols off by default for broader compatibility

    Label(options_frame, text="Include Character Types:").pack(anchor=W, padx=0, pady=(10,0))

    # Checkbuttons for each character type
    check_frame = Frame(options_frame) # Frame to hold checkboxes
    check_frame.pack(fill="x")

    uppercase_check = Checkbutton(check_frame, text="Uppercase (A-Z)", var=uppercase_var)
    uppercase_check.pack(anchor=W)

    lowercase_check = Checkbutton(check_frame, text="Lowercase (a-z)", var=lowercase_var)
    lowercase_check.pack(anchor=W)

    digits_check = Checkbutton(check_frame, text="Numbers (0-9)", var=digits_var)
    digits_check.pack(anchor=W)

    symbols_check = Checkbutton(check_frame, text="Symbols (!@#$)", var=symbols_var)
    symbols_check.pack(anchor=W)

    # --- Generate Button ---
    generate_button = Button(options_frame, text="Generate Password", command=display_generated_password)
    generate_button.pack(pady=(10,0))

    # --- Generated Password Display & Copy Button ---
    display_frame = Frame(result_frame) # To keep display and copy button on one line
    display_frame.pack(fill="x", pady=(5,0))

    password_display_label = Label(display_frame, text="Generated Password:")
    password_display_label.pack(side=LEFT, padx=(0,5))

    password_display_entry = Entry(display_frame, width=30, state="readonly") # Read-only so user can select
    password_display_entry.pack(side=LEFT, expand=True, fill="x")

    copy_button = Button(display_frame, text="Copy", command=copy_to_clipboard, state=DISABLED)
    copy_button.pack(side=LEFT, padx=(5,0))


# --- Main Application Execution ---
if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
