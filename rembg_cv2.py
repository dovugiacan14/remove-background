import cv2 
import numpy as np 
from config import INPUT_FILE

def remove_bg(img_path):
    # read image 
    image = cv2.imread(img_path) 
    # convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # convert to blalck and white image 
    _, thresold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    # find contours
    contours, _  = cv2.findContours(thresold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # find largest contour
    largest_contour = max(contours, key= cv2.contourArea)
    result  = np.ones_like(image) * 255 
    # draw largest contour
    cv2.drawContours(result, [largest_contour], -1, (0,0,0), -1)
    # remove background 
    final_result = cv2.bitwise_and(image, result) 
    return final_result

def main():
    img_path = INPUT_FILE
    img_rembg = remove_bg(img_path)
    cv2.imwrite('result.png', img_rembg)

if __name__ == '__main__':
    main()