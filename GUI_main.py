from tkinter import filedialog, Tk, Button, Label, Frame, messagebox
import cv2
import numpy as np

# Image processing functions
def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def sharpen_image(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

def divide_and_conquer_sharpening(image):
    height, width, _ = image.shape
    quarters = [
        image[0:height//2, 0:width//2],
        image[height//2:height, 0:width//2],
        image[0:height//2, width//2:width],
        image[height//2:height, width//2:width]
    ]
    sharpened_quarters = [sharpen_image(q) for q in quarters]
    top_half = np.concatenate((sharpened_quarters[0], sharpened_quarters[2]), axis=1)
    bottom_half = np.concatenate((sharpened_quarters[1], sharpened_quarters[3]), axis=1)
    return np.concatenate((top_half, bottom_half), axis=0)

# GUI functions
def load_image_gui():
    global img
    file_path = filedialog.askopenfilename()
    if file_path:
        img = load_image(file_path)
        status_label.config(text="Image loaded successfully.")

def save_image_gui():
    if img is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            save_image(img, file_path)
            status_label.config(text="Image saved successfully.")
    else:
        messagebox.showerror("Error", "No image loaded to save.")

def sharpen_image_gui():
    global img
    if img is not None:
        img = divide_and_conquer_sharpening(img)
        status_label.config(text="Image sharpened successfully.")
    else:
        messagebox.showerror("Error", "No image loaded to sharpen.")

# Setting up the GUI with a vertical layout
root = Tk()
root.title("ImageSharp: Divide-and-Conquer-Based Image Enhancement")

# Main frame for buttons and labels
main_frame = Frame(root)
main_frame.pack(padx=10, pady=10)

# Load Image Section
load_label = Label(main_frame, text="Load Image:", font=("Arial", 12))
load_label.pack(pady=(0, 5))
load_button = Button(main_frame, text="Select Image", command=load_image_gui)
load_button.pack()

# Sharpen Image Section
sharpen_label = Label(main_frame, text="Sharpen Image:", font=("Arial", 12))
sharpen_label.pack(pady=(10, 5))
sharpen_button = Button(main_frame, text="Apply Sharpen", command=sharpen_image_gui)
sharpen_button.pack()

# Save Image Section
save_label = Label(main_frame, text="Save Image:", font=("Arial", 12))
save_label.pack(pady=(10, 5))
save_button = Button(main_frame, text="Save Enhanced Image", command=save_image_gui)
save_button.pack()

# Status Message Section
status_label = Label(root, text="", font=("Arial", 10))
status_label.pack(pady=(10, 0))

# Run the GUI
root.mainloop()