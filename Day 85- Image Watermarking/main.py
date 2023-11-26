import tkinter as tk
from tkinter import filedialog, PhotoImage, Canvas
from PIL import Image, ImageTk, ImageDraw, ImageFont


RAW_IMAGE_LIST = []
root = tk.Tk()
root.title("Image Watermarking Software")
custom_font = ("Helvetica", 20, "bold")

# Create and grid the label
label = tk.Label(root, text="Image Watermarking Software!", font=custom_font)
label.grid(row=0, column=1, padx=10, pady=10)

# Create and grid the canvas
canvas = tk.Canvas(root, width=500, height=500)
canvas.grid(row=1, column=1)


def add_watermark(raw_non_photoimage):
    watermark_text = "Pranish Poudel"
    draw = ImageDraw.Draw(raw_non_photoimage)
    watermark_position = (50, 50)
    font = ImageFont.load_default()
    watermark_color = "black"
    draw.text(watermark_position, watermark_text, fill=watermark_color, font=font)
    original_image_tk = ImageTk.PhotoImage(raw_non_photoimage)
    display_proccesed_image_in_frontend(original_image_tk)


def display_proccesed_image_in_frontend(imagee):
    canvas.create_image(250, 250, image=imagee)  # Centered image position
    canvas.image = imagee  # Keep a reference to the image
    canvas.grid(row=1, column=2)


def display_image_in_frontend(imagee):
    canvas.create_image(250, 250, image=imagee)  # Centered image position
    canvas.image = imagee  # Keep a reference to the image
    canvas.grid(row=0, column=0)  # Make sure to update grid position


def open_image_func():
    filetypes = [("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg"), ("GIF files", "*.gif"), ("BMP files", "*.bmp")]
    file_path = filedialog.askopenfilename(filetypes=filetypes)

    if file_path:
        # Open the image using Pillow
        original_image = Image.open(file_path)

        # Resize the image to fit within the canvas
        original_image.thumbnail((500, 500))

        RAW_IMAGE_LIST.append(original_image)
        img_tk = ImageTk.PhotoImage(original_image)
        display_image_in_frontend(img_tk)


open_image = tk.Label(root, text="Original Image", font=("Helvetica", 15, "bold"))
open_image.grid(row=1, column=0, pady=50, padx=30)

open_image_button = tk.Button(root, text="Open Button", command=open_image_func)
open_image_button.grid(row=0, column=0, rowspan=3)

process_image = tk.Label(root, text="Processed Image", font=("Helvetica", 15, "bold"))
process_image.grid(row=1, column=2, pady=50)  # Adjusted column index

process_image_button = tk.Button(root, text="Process Button", command=lambda: add_watermark(RAW_IMAGE_LIST[0]))
process_image_button.grid(row=1, column=2, rowspan=3)

root.mainloop()
