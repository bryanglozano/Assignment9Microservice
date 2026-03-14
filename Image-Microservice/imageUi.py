"""
Code written by Kevin Sylvia (3/10/26) for CS361 W2026
This script serves as a user interface for requesting
image paths from the image-microservice.py program.
"""

import time
import os
from random import choice

input_file = "request_image_path.txt"
output_file = "response_image_path.txt"

def request_image_path(image_name):
    with open(input_file, 'w') as file:
        file.write(image_name)
    print(f"Request sent for image: {image_name}")

    while True:
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            time.sleep(1)
            with open(output_file, 'r+') as file:
                response1 = file.read().strip()
                file.seek(0)
                file.truncate()
            return response1
        time.sleep(1)

if __name__ == "__main__":
    while True:
        print("Select an action:")
        print("1. Request an image path")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            requested_image = input("Enter a file name (example: My_image.jpg): ")
            time.sleep(5)
            result1 = request_image_path(requested_image)
            print(f"Response from microservice: {result1}")
        elif choice == '2':
            print("Exiting script.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
