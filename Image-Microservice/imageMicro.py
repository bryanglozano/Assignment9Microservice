"""
Code written by Kevin Sylvia (3/10/26) for CS361 W2026
This microservice listens for image name from the 'input.txt' file, 
searches for the requested image in the 'Images' folder, 
and responds with the full file path of the image 
or an error message if the image is not found, 
writing the response to 'output.txt'.
"""
import os
import time

image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
input_file = 'request_image_path.txt'
output_file = 'response_image_path.txt'

def find_image_path(image_name):
    """
    generates a complete file path for an image name
    """
    for root, _, file in os.walk(image_folder):
        if image_name in file:
            return os.path.join(root, image_name)
    return None

print('Microservice started. Waiting for requests...')
while True:
    time.sleep(1)
    if os.path.exists(input_file) and os.path.getsize(input_file) > 0:
        with open(input_file, 'r+') as file:
            image_name = file.read().strip()
            file.seek(0)
            file.truncate()

        print(f'Received request for image: {image_name}')
        image_path = find_image_path(image_name)

        with open(output_file, 'w') as file:
            if image_path:
                file.write(image_path)
                print(f'Image found: {image_path}')
            else:
                file.write(f"Error: Image '{image_name}' not found.")
                print(f"Image '{image_name}' not found.")
