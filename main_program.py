import time
import os

# -----------------------------
# pipe file path
# -----------------------------

FORMAT_REQUEST = "EntryFormatterMicroservice/pipe/format_request.txt"
FORMAT_RESPONSE = "EntryFormatterMicroservice/pipe/format_response.txt"

ID_REQUEST = "IDGeneratorMicroservice/pipe/id_request.txt"
ID_RESPONSE = "IDGeneratorMicroservice/pipe/id_response.txt"

STORAGE_REQUEST = "DataStorageMicroservice/pipe/storage_request.txt"
STORAGE_RESPONSE = "DataStorageMicroservice/pipe/storage_response.txt"

IMAGE_REQUEST = "Image-Microservice/request_image_path.txt"
IMAGE_RESPONSE = "Image-Microservice/response_image_path.txt"


# -----------------------------
# helper functions
# -----------------------------

def send_request(request_file, message):
    with open(request_file, "w") as file:
        file.write(message)


def wait_for_response(response_file):
    while True:
        if os.path.exists(response_file) and os.path.getsize(response_file) > 0:
            with open(response_file, "r") as file:
                response = file.read().strip()

            open(response_file, "w").close()
            return response

        time.sleep(0.5)


# -----------------------------
# microservice functions
# -----------------------------

def format_entry(entry_text):
    print("\nSending entry to Entry Formatter microservice...")
    send_request(FORMAT_REQUEST, entry_text)
    response = wait_for_response(FORMAT_RESPONSE)
    print("Formatted entry received.")
    return response


def generate_id(title):
    print("\nRequesting ID from ID Generator microservice...")
    send_request(ID_REQUEST, title)
    response = wait_for_response(ID_RESPONSE)
    print("Generated ID:", response)
    return response


def store_entry(entry_json):
    print("\nSending data to Data Storage microservice...")
    send_request(STORAGE_REQUEST, entry_json)
    response = wait_for_response(STORAGE_RESPONSE)
    print("Storage response:", response)


def get_image(image_name):
    print("\nRequesting image from Image microservice...")
    send_request(IMAGE_REQUEST, image_name)
    response = wait_for_response(IMAGE_RESPONSE)
    print("Image response:", response)


# -----------------------------
# main menu
# -----------------------------

def main():

    while True:
        print("\n==============================")
        print(" Journal Microservice Program ")
        print("==============================")
        print("1 - Add Journal Entry")
        print("2 - Get Image Path")
        print("3 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            date = input("Enter date: ")
            title = input("Enter title: ")
            content = input("Enter content: ")

            raw_entry = f"{date}|{title}|{content}"

            formatted = format_entry(raw_entry)

            entry_id = generate_id(title)

            entry_json = f"{entry_id}|{formatted}"

            store_entry(entry_json)

            print("\nEntry successfully saved!")

        elif choice == "2":

            image_name = input("Enter image name (example: buffalo.png): ")
            get_image(image_name)

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid option.")


# -----------------------------
# run program
# -----------------------------

if __name__ == "__main__":
    main()
