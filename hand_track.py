import cv2
import  mediapipe as mp
import time 
import hand_tracking_module as htm
pTime =0                                                        #previous time 
cTime =0                                                        #current time
cap =cv2.VideoCapture(0)
    # object
detector=htm.handDetector() #default parametor are already given 

while True:
        sucess,img=cap.read()  
        img=detector.findHands(img)          # method inside the class 
        lmList= detector.findPosition(img)
        if len(lmList) !=0:
          print(lmList)
        
        cTime= time.time()
        fps= 1/(cTime-pTime)
        pTime=cTime
    
        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
        cv2.imshow("Image",img) 
        cv2.waitKey(1)