from PIL import Image
import os
from tkinter import Tk, filedialog

def select_file():
    """Open a file dialog to select the input PNG file."""
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a PNG file",
        filetypes=[("PNG files", "*.png")]
    )
    return file_path

def select_save_location():
    """Open a file dialog to select the output ICO file location."""
    root = Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(
        title="Save as",
        defaultextension=".ico",
        filetypes=[("ICO files", "*.ico")]
    )
    return file_path

def convert_png_to_ico(png_file, output_file):
    # Define the custom sizes required
    sizes = [
        (256, 256), (195, 195), (128, 128), (114, 114), (96, 96),
        (72, 72), (64, 64), (57, 57), (32, 32), (24, 24), (16, 16)
    ]

    # Open the input PNG image
    with Image.open(png_file) as img:
        # Convert the image to RGBA if it's not already in that mode
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Save the image as an ICO file with all the specified sizes
        img.save(output_file, format='ICO', sizes=sizes)
    
    print(f"ICO file saved as {output_file}")

if __name__ == "__main__":
    # Let the user select the input PNG file
    png_file = select_file()
    if not png_file:
        print("No file selected, exiting.")
        exit()

    # Let the user select the output ICO file location
    output_file = select_save_location()
    if not output_file:
        print("No save location selected, exiting.")
        exit()

    # Convert PNG to ICO
    convert_png_to_ico(png_file, output_file)
