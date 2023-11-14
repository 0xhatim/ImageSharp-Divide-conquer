import cv2
import numpy as np
from memory_profiler import memory_usage
from Console_main import *
# [Include your image processing functions here]

def measure_performance(image_path):
    img = load_image(image_path)
    mem_usage = memory_usage((divide_and_conquer_sharpening, (img,)))

    return max(mem_usage)

def main():
    image_path = 'Picture_first.png'  # Replace with your image path
    memory_usage = measure_performance(image_path)
    print(f"Memory Usage: {memory_usage} MB")

if __name__ == '__main__':
    main()
