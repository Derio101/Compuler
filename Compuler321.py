import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading
import webbrowser

# Global output directory for the EXE file
output_dir = os.path.expanduser("~/output")
additional_files = []  # List to store additional files for multi-file packaging

# Function to validate the inputs (script, icon)
def validate_inputs(script_path, icon_path):
    if not script_path.endswith('.py'):
        messagebox.showerror("Error", "Please select a valid Python (.py) file.")
        return False
    if icon_path and not icon_path.endswith('.ico'):
        messagebox.showerror("Error", "Please select a valid Icon (.ico) file.")
        return False
    return True

# Function to run PyInstaller to create the .exe
def convert_to_exe(script_path, icon_path, app_name, log_text):
    if not validate_inputs(script_path, icon_path):
        return

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define PyInstaller command
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--optimize=1",
        "--strip",
        f"--name={app_name if app_name else 'App'}",
        f"--distpath={output_dir}",
        script_path
    ]

    # Include icon if provided
    if icon_path:
        command.append(f"--icon={icon_path}")

    # Include additional files for multi-file packaging
    for file in additional_files:
        command.append(f"--add-data={file}")

    # Enable logging for debugging if needed
    command.extend(["--log-level=DEBUG"])

    # Run the PyInstaller command in a separate thread
    def run_pyinstaller():
        try:
            log_text.insert(tk.END, "Starting conversion...\n")
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            log_text.insert(tk.END, result.stdout.decode())
            log_text.insert(tk.END, "\nConversion completed successfully!\n")
            open_location_button.config(state=tk.NORMAL)
        except subprocess.CalledProcessError as e:
            log_text.insert(tk.END, f"Error: {e.stderr.decode()}\n")
        finally:
            progress.stop()  # Stop the progress bar

    # Start the thread and progress bar
    progress.start()
    threading.Thread(target=run_pyinstaller).start()

# Function to open the folder containing the generated executable
def open_file_location():
    if os.path.exists(output_dir):
        webbrowser.open(output_dir)
    else:
        messagebox.showerror("Error", "Output folder does not exist.")

# Function to select a Python script
def select_script():
    script_path = filedialog.askopenfilename(title="Select Python Script", filetypes=[("Python Files", "*.py")])
    if script_path:
        script_entry.delete(0, tk.END)
        script_entry.insert(0, script_path)

# Function to select an icon file
def select_icon():
    icon_path = filedialog.askopenfilename(title="Select Icon File", filetypes=[("Icon Files", "*.ico")])
    if icon_path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, icon_path)

# Function to add additional files for multi-file packaging
def add_data_file():
    data_file = filedialog.askopenfilename(title="Select File to Bundle with EXE")
    if data_file:
        additional_files.append(data_file)
        data_files_listbox.insert(tk.END, data_file)

# Function to trigger the conversion when "Convert" button is clicked
def on_convert():
    script_path = script_entry.get().strip()
    icon_path = icon_entry.get().strip() if icon_entry.get().strip() else None  # Use None for default icon
    app_name = app_name_entry.get().strip()

    convert_to_exe(script_path, icon_path, app_name, log_text)

# Creating the main Tkinter window
root = tk.Tk()
root.title("Modern Python to EXE Converter")
root.geometry("600x600")
root.configure(bg="#2b2b2b")  # Dark background

# Style configurations
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=6)
style.configure("TLabel", font=("Helvetica", 12), foreground="white", background="#2b2b2b")
style.configure("TEntry", fieldbackground="#2b2b2b", foreground="white")
style.configure("TProgressbar", thickness=20)

# Create the progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate", style="TProgressbar")
progress.pack(pady=10)

# Script selection
ttk.Label(root, text="Select Python Script:").pack(pady=10)
script_frame = tk.Frame(root, bg="#2b2b2b")
script_frame.pack(pady=5)
script_entry = ttk.Entry(script_frame, width=40)
script_entry.pack(side=tk.LEFT, padx=5)
script_button = ttk.Button(script_frame, text="Browse", command=select_script)
script_button.pack(side=tk.LEFT)

# Icon selection
ttk.Label(root, text="Select Icon (.ico) File (Optional):").pack(pady=10)
icon_frame = tk.Frame(root, bg="#2b2b2b")
icon_frame.pack(pady=5)
icon_entry = ttk.Entry(icon_frame, width=40)
icon_entry.pack(side=tk.LEFT, padx=5)
icon_button = ttk.Button(icon_frame, text="Browse", command=select_icon)
icon_button.pack(side=tk.LEFT)

# App name input
ttk.Label(root, text="Enter App Name (Optional):").pack(pady=10)
app_name_entry = ttk.Entry(root, width=45)
app_name_entry.pack(pady=5)

# Additional files selection
ttk.Button(root, text="Add Additional Files", command=add_data_file).pack(pady=10)
data_files_listbox = tk.Listbox(root, width=50, height=5)
data_files_listbox.pack(pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert to EXE", command=on_convert)
convert_button.pack(pady=20)

# Open File Location button (disabled by default)
open_location_button = ttk.Button(root, text="Open File Location", command=open_file_location)
open_location_button.pack(pady=10)
open_location_button.config(state=tk.DISABLED)

# Log section
ttk.Label(root, text="Conversion Log:").pack(pady=10)
log_text = tk.Text(root, height=10, wrap="word", bg="#1e1e1e", fg="white", insertbackground="white")
log_text.pack(expand=True, fill="both", padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()
