def getDrowsy(ret_1 , frame_1):
    import cv2
    import os
    from keras.models import load_model
    import numpy as np
    score=0
    leye = cv2.CascadeClassifier(".\haar cascade files\haarcascade_lefteye_2splits.xml")
    reye = cv2.CascadeClassifier(".\haar cascade files\haarcascade_righteye_2splits.xml")
    lbl=['Close','Open']
    model = load_model('./models/cnnCat2.h5')
    path = os.getcwd()
    count=0
    score=0
    rpred=[99]
    lpred=[99]
    ret, frame = ret_1 , frame_1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    left_eye = leye.detectMultiScale(gray)
    right_eye =  reye.detectMultiScale(gray)

    for (x,y,w,h) in right_eye:
        r_eye=frame[y:y+h,x:x+w]
        count=count+1
        r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
        r_eye = cv2.resize(r_eye,(24,24))
        r_eye= r_eye/255
        r_eye=  r_eye.reshape(24,24,-1)
        r_eye = np.expand_dims(r_eye,axis=0)
        rpred = model.predict(r_eye)
        rpred=np.where(rpred[0][0] < 0.5, 0, 1)
        
        if(rpred==1):
            lbl='Open' 
        if(rpred==0):
            lbl='Closed'
            break

    for (x,y,w,h) in left_eye:
        l_eye=frame[y:y+h,x:x+w]
        count=count+1
        l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
        l_eye = cv2.resize(l_eye,(24,24))
        l_eye= l_eye/255
        l_eye=l_eye.reshape(24,24,-1)
        l_eye = np.expand_dims(l_eye,axis=0)
        lpred = model.predict(l_eye)
        lpred=np.where(lpred[0][0] < 0.5, 0, 1)
        
        if(lpred==1):
            lbl='Open'
            break   
        if(lpred==0):
            lbl='Closed'
            break

    if(rpred==1 and lpred==1):
        score=2
        print('Close')
    else:
        score=-3
        print('Open')
  
    
    return score
