import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

import RandomizerCLI

# Function to load the current config
def load_config(filename="config.json"):
    try:
        with open(filename, "r") as file:
            config = json.load(file)
        messagebox.showinfo("Success", f"Configuration loaded from {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load configuration: {e}")
        config = {}
    return config

# Function to save the updated config with an optional filename
def save_config(updated_config, filename=None):
    if not filename:
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            title="Save configuration as"
        )
    if filename:
        try:
            with open(filename, "w") as file:
                json.dump(updated_config, file, indent=4)
            messagebox.showinfo("Success", f"Configuration saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save configuration: {e}")

# Function to update the config based on user input and run the randomizer
def run_randomizer(config, check_vars, entry_vars, integer_vars):
    # Update the config based on the checkbutton and entry variables
    for section, options in check_vars.items():
        if isinstance(options, dict):
            for option, var in options.items():
                config[section][option] = "yes" if var.get() else "no"
        else:
            config[section] = "yes" if options.get() else "no"
            
    for section, options in entry_vars.items():
        if isinstance(options, dict):
            for option, entry in options.items():
                config[section][option] = entry.get()
        else:
            config[section] = options.get()
            
    for section, options in integer_vars.items():
        if isinstance(options, dict):
            for option, entry in options.items():
                config[section][option] = int(entry.get())
        else:
            config[section] = int(options.get())
    
    # Save the updated configuration
    save_config(config, "config.json")
    RandomizerCLI.main()
    messagebox.showinfo("Done", "Randomization complete")

# Function to load a new config file and refresh the UI
def load_new_config():
    filename = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        title="Select a configuration file"
    )
    if filename:
        new_config = load_config(filename)
        if new_config:
            refresh_ui(new_config)

# Function to refresh the UI with a new config
def refresh_ui(new_config):
    global config, check_vars, entry_vars
    config = new_config
    for widget in root.winfo_children():
        widget.destroy()
    create_ui()

# Create the main tkinter window
root = tk.Tk()
root.title("Randomizer Configuration")

# Load the initial config
config = load_config()

# Dictionaries to store the tkinter IntVar and Entry references
check_vars = {}
entry_vars = {}

# Function to create the UI elements
def create_ui():
    global check_vars, entry_vars
    check_vars = {}
    entry_vars = {}
    integer_vars = {}
    tabControl = ttk.Notebook(root) 
    # Create checkbuttons and entry widgets for each option in the config file
    for section, options in config.items():
        frame = ttk.Frame(tabControl)
        tabControl.add(frame, text=section.replace('_', ' ').capitalize())
        tabControl.pack(fill="both", expand="yes", padx=10, pady=5)

        check_vars[section] = {}
        entry_vars[section] = {}
        integer_vars[section] = {}
        
        if isinstance(options, dict):
            for option, value in options.items():
                if isinstance(value, str):
                    if value in ["yes", "no"]:
                        # Create a checkbutton for boolean options
                        var = tk.IntVar(value=1 if value == "yes" else 0)
                        check_vars[section][option] = var
                        check_button = ttk.Checkbutton(
                            frame, 
                            text=option.replace('_', ' ').capitalize(), 
                            variable=var
                        )
                        check_button.pack(anchor="w", padx=5, pady=2)
                    else:
                        # Create an entry field for non-boolean options
                        label = ttk.Label(frame, text=option.replace('_', ' ').capitalize())
                        label.pack(anchor="w", padx=5, pady=2)
                        entry = ttk.Entry(frame)
                        entry.insert(0, str(value))
                        entry.pack(fill="x", padx=5, pady=2)
                        entry_vars[section][option] = entry
                elif isinstance(value, int):
                    # Create an entry field for integer options
                    label = ttk.Label(frame, text=option.replace('_', ' ').capitalize())
                    label.pack(anchor="w", padx=10, pady=10)
                    var = tk.IntVar()
                    entry = ttk.LabeledScale(frame, from_=0, to=100, variable=var)
                    entry.scale.set(1)
                    entry.pack(fill="x", padx=5, pady=2)
                    integer_vars[section][option] = var
                
        elif isinstance(options, str):
            if value in ["yes", "no"]:
                # Create a checkbutton for boolean options
                var = tk.IntVar(value=1 if value == "yes" else 0)
                check_vars[section] = var
                check_button = ttk.Checkbutton(
                    frame, 
                    text=option.replace('_', ' ').capitalize(), 
                    variable=var
                )
                check_button.pack(anchor="w", padx=5, pady=2)
            else:
                # Create an entry field for String options
                label = ttk.Label(frame, text=section.replace('_', ' ').capitalize())
                label.pack(anchor="w", padx=10, pady=10)
                entry = ttk.Entry(frame)
                entry.insert(0, str(value))
                entry.pack(fill="x", padx=5, pady=2)
                entry_vars[section] = entry
        elif isinstance(options, int):
            # Create an entry field for integer options
            label = ttk.Label(frame, text=section.replace('_', ' ').capitalize())
            label.pack(anchor="w", padx=10, pady=10)
            var = tk.IntVar()
            entry = ttk.LabeledScale(frame, from_=0, to=100, variable=var)
            entry.scale.set(1)
            entry.pack(fill="x", padx=5, pady=2)
            integer_vars[section] = entry.scale
            

    # Add a button to trigger the randomization process
    run_button = ttk.Button(root, text="Run Randomizer", command=lambda: run_randomizer(config, check_vars, entry_vars, integer_vars))
    run_button.pack(pady=10)

    # Add a button to save the config with an optional filename
    save_button = ttk.Button(root, text="Save Config As", command=lambda: save_config(config))
    save_button.pack(pady=5)

    # Add a button to load a different config file
    load_button = ttk.Button(root, text="Load Config", command=load_new_config)
    load_button.pack(pady=5)

# Initialize the UI
create_ui()

# Start the tkinter main loop
root.mainloop()
