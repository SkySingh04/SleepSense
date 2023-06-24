import cv2
import numpy
import pygame

from drowsiness_detection import getDrowsy
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.count=0
    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = (self.video).read()
        score = getDrowsy(ret_1=ret , frame_1=frame)

        if self.count<0:
            self.count=0
        
        
        self.count+=score
        if(count>40):
            #person is feeling sleepy so we beep the alarm
            #cv2.imwrite(os.path.join(path,'image.jpg'),frame)
            # try:
            if pygame.mixer.get_busy() == False:
                    sound.play()
            
                
                playsound(r'C:\Users\wwwyo\Downloads\archive (1)\Drowsiness detection\alarm.wav')
            except :  # isplaying = False
                pass
        
            if(thicc<16):
                thicc= thicc+2
            else:
                thicc=thicc-2
                if(thicc<2):
                    thicc=2
            cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc) 
            
        
        if count==40:
            try: 
                pygame.mixer.stop()
            except:
                pass
                # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        print(self.count)
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()