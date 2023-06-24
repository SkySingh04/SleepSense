import cv2
from drowsiness_detection import *
import pygame
from pygame import mixer
import time

mixer.init()
sound = mixer.Sound(r"./mp3/Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3")


class VideoCamera(object):
    
       
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.count=0
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
            
            timetaken(1)
        #    #person is feeling sleepy so we beep the alarm
            if pygame.mixer.get_busy() == False:
                    sound.play()
                
             
        if self.count==28:
            
            try: 
                
                pygame.mixer.stop()
                timetaken(2)
                timetaken(3)
               
            except:
                pass
        
            
        print(self.count)
        
        #file.write(time1)
        
        ret, jpeg = cv2.imencode('.jpg', frame)

        return (jpeg.tobytes())
    
    
        
