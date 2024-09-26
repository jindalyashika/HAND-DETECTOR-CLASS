import cv2
import mediapipe as mp
import time

cap =cv2.VideoCapture(0)

mpHands=mp.solutions.hands
hands=mpHands.Hands()                                        # creating an object
mpDraw= mp.solutions.drawing_utils

#frame rate             
pTime =0                                                        #previous time 
cTime =0                                                       #current time

while True:
    sucess,img=cap.read()                                     #to open the web_cam
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)                            #to process the image
    print (results.multi_hand_landmarks)                      #to see something is detected or not
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:                   #handlms is the single hand
            # to get the information about the hand and its points . there id number are alreay list in an order we just have to check their inex number .
            for id, lm in enumerate(handlms.landmark):
                # print(id,lm)        # we will get the landmak and each land mark will have its own x,y . the values of x and y(i.e the location) will be in decimal i.e we will get the ratio of the image. to get the landmark in pixels we are doing the following steps
                h,w,c=img.shape     # to get the height and width
                cx ,cy =int(lm.x*w) , int(lm.y*h)                      #position of the centre
                print (id,cx,cy)                       # will print for all the 21 i'd
                
                # to print for just i'd no =0
                if id ==0:
                    cv2.circle(img,(cx,cy),25,(266,0,266),cv2.FILLED)
            
            mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)       # help to draw the points and  line in between the dots
            
    cTime= time.time()
    fps= 1/(cTime-pTime)
    pTime=cTime
    
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    
    cv2.imshow("Image",img) 
    cv2.waitKey(1)