import cv2
import mediapipe as mp
import time

# visualisation
class handDetector():
    def __init__(self ,mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode=mode             # we are craeting an obj and obj will have its own variable 
        self.maxHands= maxHands
        self.detectionCon =detectionCon
        self.trackCon= trackCon
        

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxHands,int(self.detectionCon),int(self.trackCon))                                        # creating an object
        self.mpDraw= mp.solutions.drawing_utils

# detection
    def findHands(self,img, draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results= self.hands.process(imgRGB)                            #to process the image
    # print (results.multi_hand_landmarks)                      #to see something is detected or not
    
        if self.results.multi_hand_landmarks:
         for handlms in self.results.multi_hand_landmarks:                   #handlms is the single hand
           if draw:
               
    # to get the information about the hand and its points . there id number are alreay list in an order we just have to check their index number .
            self.mpDraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)       # help to draw the points and  line in between the dots
        return img

    def findPosition(self,img,handNo=0,draw= True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h,w,c=img.shape     # to get the height and width
                cx ,cy =int(lm.x*w) , int(lm.y*h)                      #position of the centre
                lmList.append([id,cx,cy])
            if draw:     
                cv2.circle(img,(cx,cy),15,(266,0,0),cv2.FILLED)
            
        return lmList

    
def main():
    pTime =0                                                        #previous time 
    cTime =0                                                        #current time
    cap =cv2.VideoCapture(0)
    # object
    detector=handDetector() #default parametor are already given 

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
    
if __name__ =="__main__":
    main()