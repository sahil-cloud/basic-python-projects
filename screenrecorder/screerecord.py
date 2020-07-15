import cv2
import numpy as np
from PIL import ImageGrab

def screenrecord():
    # initialising the 4 character code for the player
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # initialising the output variable
    out = cv2.VideoWriter('test.avi',fourcc,5.0,(1366,768))

    while True:
        # taking the image
        img = ImageGrab.grab()
        # converting into 2d array 
        img_np = np.array(img)
        # creating frame and converting the color code to RBG
        frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        # shpowing the frame 
        # cv2.imshow("Screen Recorder",frame) 
        out.write(frame)


        # breaking the loop
        # for k key in the keybord
        if cv2.waitKey(1) == 27:
            break
    
    out.release()
    cv2.destroyAllWindows()

screenrecord()
