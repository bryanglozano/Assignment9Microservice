# Image Microservice Communication

A microservice using text files as the communication pipeline to provide an absolute image path for other projects/programs. 

All communication happens through two files in the same directory as `imageMicro.py`:

- `request_image_path.txt`
- `response_image_path.txt`
* Both files must be made. File names can be changed, just make sure to adjust `imageMicro.py` to reflect this change on lines 13 and 14
* If using the `imageUi.py` to test the file names can be changed on line 11 and 12, if you change them
- Images must be added to the `Images` folder in the same directory as the `imageMicro.py`program

---   

Current features:
Generates the absolute image path if the image is in the indicated folder

---

## How to run

1. Make sure `imageMicro.py`, `request_image_path.txt`, `response_image_path.txt` and `Images` folder are in the same directory.
2. Start the microservice in a terminal:
   python imageMicro.py
3. In a separate terminal, run the program that will write the image name into `request_image_path.txt` and recive the image path from `response_image_path.txt`

---

Example Ui file included to demonstrate calling the microservice
- `imageUi.py`
