import cv2
from drowsiness_detection import getDrowsy
import pygame
from pygame import mixer
import threading
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
            start=time.time()
        #     #person is feeling sleepy so we beep the alarm
            if pygame.mixer.get_busy() == False:
                    sound.play()
             
        
        if self.count==28:
            end=time.time()
            try: 
                pygame.mixer.stop()
            except:
                pass
        print(score)
        
        ret, jpeg = cv2.imencode('.jpg', frame)
        print(end-start)
        return (jpeg.tobytes())

    

        
