import os 
import cv2
from rembg import remove
from config import INPUT_FILE, OUTPUT_FOLDER

def remove_background(dir_in, dir_out):
    input = cv2.imread(dir_in)
    output = remove(input)
    cv2.imwrite(dir_out, output)
    return output

def main():
    dir_in = INPUT_FILE
    dir_out = OUTPUT_FOLDER
    output_filename = os.path.join(dir_out, 'output.png')
    remove_background(dir_in, output_filename)

if __name__ == '__main__':
    main()