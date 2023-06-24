import cv2
import pygame
from pygame import mixer
mixer.init()
sound = mixer.Sound(r"Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3")

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
        if(self.count>28):
        #     #person is feeling sleepy so we beep the alarm
            if pygame.mixer.get_busy() == False:
                    sound.play()
             
        if self.count==28:
            try: 
                pygame.mixer.stop()
            except:
                pass
        print(score)
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()