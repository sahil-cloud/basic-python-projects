import cv2

# for initialising the webcam
imagecapture = cv2.VideoCapture(0)
result = True

while(result):
    # capturing the image
    ret , frame = imagecapture.read()
    # saving into the file 
    cv2.imwrite('test.jpg',frame)
    result = False
    print("captured successfully")

imagecapture.release()