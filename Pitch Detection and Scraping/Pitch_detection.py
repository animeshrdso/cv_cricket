"""This file outputs the frame number in the video at which the bowler is about to bowl the delivary"""

#importing necessary library
import numpy as np
import cv2
#the path of the video input
PATH='test3.mp4'
#video input
cap = cv2.VideoCapture(PATH)
#fps of the video
fps = cap.get(cv2.CAP_PROP_FPS)

#initialise necessary variables
fno = -1
nf = 0
pitch_bool=0

#loop throughthe whole video
while(cap.isOpened()):
    fno +=1
    ret, frame = cap.read()
    if not ret:
        break
    (h,w,d) = frame.shape
    x=round(h*76/125)
    y=round(w*20/117)
    w1=round(w*40/117)
    h1=round(h*72/125)
    #rbg to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #range to detect the pitch
    lower_d = np.array([95,10,0], dtype = "uint8" )
    upper_d = np.array([140,50,250], dtype = "uint8")
    out_d = cv2.inRange(hsv, lower_d, upper_d)
    lower_n = np.array([0,0,0], dtype = "uint8" )
    upper_n = np.array([30,55,250], dtype = "uint8")

    #masking
    out_n = cv2.inRange(hsv, lower_n, upper_n)
    out = cv2.bitwise_or(out_d,out_n)
    out_l = out[:, :x]
    out_r = out[:, x+w1:]
    out_p = out[y:y+h1, x:x+w1]
    # cv2.imshow("left", out_l)
    # cv2.imshow("pitch", out_p)
    # cv2.imshow("right", out_r)

    #checking conditions
    if np.mean(np.asarray(out_p)) > 80 and np.mean(np.asarray(out_l)) < 40 and np.mean(np.asarray(out_r)) < 40:
        nf += 1
        pitch_bool = 1
    elif pitch_bool:
        pitch_bool = 0
        if nf > fps:
            print(fno-nf)
        nf = 0

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
