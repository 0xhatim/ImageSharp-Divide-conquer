import cv2
import numpy as np

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
    # Dividing the image into four quarters
    quarters = [
        image[0:height//2, 0:width//2],
        image[height//2:height, 0:width//2],
        image[0:height//2, width//2:width],
        image[height//2:height, width//2:width]
    ]

    # Applying sharpening filter to each quarter
    sharpened_quarters = [sharpen_image(q) for q in quarters]

    # Merging the quarters
    top_half = np.concatenate((sharpened_quarters[0], sharpened_quarters[2]), axis=1)
    bottom_half = np.concatenate((sharpened_quarters[1], sharpened_quarters[3]), axis=1)

    return np.concatenate((top_half, bottom_half), axis=0)

# Example usage
image_path = 'Picture_third.png'  # Replace with your image path
save_path = 'enhanced_image_new.png'  # Replace with your save path

# Load an image
img = load_image(image_path)

# Apply the divide-and-conquer sharpening
enhanced_img = divide_and_conquer_sharpening(img)

# Save the enhanced image
save_image(enhanced_img, save_path)
