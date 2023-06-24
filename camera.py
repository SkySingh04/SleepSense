import cv2
from drowsiness_detection import getDrowsy
import pygame
from pygame import mixer

from datetime import datetime 
mixer.init()
sound = mixer.Sound(r"./mp3/Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3")


class VideoCamera(object):
    

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.count=0
        self.time_list=[]
    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = (self.video).read()
        score =getDrowsy(ret ,frame)
        
#Add threading
        if self.count<0:
            self.count=0
        
        
        self.count+=score
        if score<0:
            score=0
        if(self.count>28):
            now = datetime.now()
            current_time = now.strftime("%D:%H:%M:%S")
            with open('times.txt',"a") as f:
                        f.write(current_time  + "\n")
            

        ##person is feeling sleepy so we beep the alarm

            if pygame.mixer.get_busy() == False:
                    sound.play()
                    
             
        
        if self.count<28:
            
            try: 
                pygame.mixer.stop()
                
            except:
                pass
        print(self.count)
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        return (jpeg.tobytes())

    

        
