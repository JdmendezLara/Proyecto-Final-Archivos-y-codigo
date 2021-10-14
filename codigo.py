import cv2
import mediapipe as mp
import numpy as np
f=0
palabra=[]
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture('libro2.mp4')
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:

    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        height, width, _ = frame.shape
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=3, circle_radius=5),
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=4, circle_radius=5))
            #COORDENADAS DE LANDMARKS----------------------------------------------------------------------------
                x1=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x*width)
                y1=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y*height)
                x4=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*width)
                y4=int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*height)
                x6=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x*width)
                y6= int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y*height)
                x8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                y8=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*height)
                y10= int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y*height)
                y12= int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y*height)
                y14= int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y*height)
                y16= int(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y*height)
                y18= int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y*height)
                y0= int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y*height)
                x0= int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x*height)
                x17= int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x*400)
                y17= int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y*550)
                x5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x*400)
                y5=int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y*550)
                x20= int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x*400)
                y20= int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y*550)
            #---------------------------------------------------------------------------------
                z=0
            #Para la L -----------------------------------------------------------------------
                
                a=y1-y8
                b=x1-x4
                if a!=0:
                    d=b/a
                c=(np.arctan(d))*(180/np.pi)
                g=c<-0.1
                h=c>-0.4
                i=y20<y18
                j=y14>=y18
                k=y10>=y18
                if c<42:
                    if c>15:
                        z=1
                        print("L")
                        if f==0 :
                            f=f+1
                            palabra.append("L")


                else:
                    print ("-----------------")
                     
            #----------------------------------------------------------------------------------
            #Para la I -----------------------------------------------------------------------
            if i==True:
                        if j== True:
                            if k== True:
                                z=1
                                print ('I')
                                if f==1 :
                                    f=f+1
                                    palabra.append("I")
                              
            #----------------------------------------------------------------------------------    
            #Para la R-------------------------------------------------------------------------
            l=y8>y12
            m=y0-y16
            n=x0-x4
            if m!=0:
                p=n/m
            o=np.arctan(p)
            
            q=o < -0.8
            r=o > -0.95
            if l==True:
                if q==True:
                    if r==True:
                        print("R")
                        z=1
                        if f==3 :
                            f=f+1
                            palabra.append("R")
            #------------------------------------------------------------------------
            #para la B-----------------------------------------------------------
            a2=y17-y5
            b2=x17-x5
            a3=y17-y20
            b3=x20-x17
            c2=np.sqrt((a2*a2)+(b2*b2))
            c3=np.sqrt((a3*a3)+(b3*b3))
            if c2!=0:
                d2=c3/c2
            r=(np.arctan(d2))*(180/np.pi)
            a4=y5-y8
            b4=x8-x5
            a5=y17-y5
            b5=x17-x5
            c4=np.sqrt((a4^2)+(b4^2))
            c5=np.sqrt((a5^2)+(b5^2))
            if c4!= 0:
                r2=(np.arctan(c5/c4))*(180/np.pi)
            if r<55:
                if r>40:
                    if r2<55:
                        if r2>35:  
                             print("B")
                             z=1
                             if f==2 :
                                f=f+1
                                palabra.append("B")
            #------------------------------------------------------------------
            #LETRA O----------------------------------------------------------
            l1=x8-x6
            l2=y8-y6
            r3=(np.arctan(l1/l2))*(180/np.pi)
            l3=x6-x5
            l4=y5-y6
            if l4!=0:
                r4=(np.arctan(l3/l4))*(180/np.pi)
            
            u=x1-x8
            u1=y1-y8
            if r3>25:
                if r3<85:
                    if r4<85:
                        if r4> 30:
                                    print("O")
                                    z=1
                                    if f==4 :
                                        f=f+1
                                        palabra.append("O")
            #---------------------------------------------------------
            if z==0:
                print("-----------")    
                
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows()
if f==5:
    print("La secuencia es : ",palabra)