import json
import tkinter as tk
from tkinter import filedialog

def json_to_readable(file_path):
    with open(file_path, 'r') as f:  # 'r' for read text
        data = json.load(f)
    
    readable_text = json.dumps(data, indent=4, sort_keys=True)
    
    return readable_text

def write_to_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select the input file
    input_file = filedialog.askopenfilename(title="Select JSON file")

    if input_file:
        # Ask the user to select the output file
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

        if output_file:
            readable_text = json_to_readable(input_file)
            write_to_file(output_file, readable_text)
            
            print(f"The formatted JSON has been written to {output_file}")

if __name__ == "__main__":
    main()
