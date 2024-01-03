# Remove Background
![](RemoveBR/images/tiger.png)  ![](RemoveBR/images/out.png)

## Overview 
This repository implements the functionality of removing the background of an image using the `OpenCV` and `rembg` libraries.

I hope this helps! Let me know if you have any other questions.

## Installation
**Getting Started:** 
1. **Install require packages:**
>       pip install -r requirements.txt
This one-line command effortlessly equips your environment with the necessary tools for background removal magic! ✨

2. **Set up configuration:**

* Open the `config.py` file and make the following changes:

    * `INPUT_FILE`: Provide the relative path to the image you wish to transform.
    
    * `OUTPUT_FOLDER`: Specify the destination where the background-free image will be saved.

3. **Demo**
* Remove background with `OpenCV` libraries: 
>       python rembg_cv2.py

* Remove background with `rembg` libraries: 
>       python rembg.py
