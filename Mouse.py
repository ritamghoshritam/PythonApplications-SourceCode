import cv2
import numpy as np
import math
from sys import platform
import pyautogui
import time
import gtk
#from win32api import GetSystemMetrics
def main():
    print "Hello World, This is a code written for experimenting with the mouse in order to reach goals like movements and cursor interaction"
    cap = cv2.VideoCapture(0)
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))
    time.sleep(3)
    width=gtk.gdk.screen_width()
    lower_green=np.array([65,100,100])
    upper_green=np.array([80,255,255])
    lower_red = np.array([169,100,100])
    upper_red = np.array([189,255,255])
    while(1):
        _, frame = cap.read()
        frame=cv2.resize(frame,(pyautogui.size()))
        frame1=cv2.resize(frame,(200,140))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, lower_green, upper_green)
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        maskOpen1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernelOpen)
        maskClose1=cv2.morphologyEx(maskOpen1,cv2.MORPH_CLOSE,kernelClose)
        maskFinal1=maskClose1
        maskOpen2=cv2.morphologyEx(mask2,cv2.MORPH_OPEN,kernelOpen)
        maskClose2=cv2.morphologyEx(maskOpen2,cv2.MORPH_CLOSE,kernelClose)
        maskFinal2=maskClose2
        conts1,h=cv2.findContours(maskFinal1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        conts2,h=cv2.findContours(maskFinal2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        mask=mask1+mask2
        for i in range(len(conts1)):
            x,y,w,h=cv2.boundingRect(conts1[i])
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            print "(",x,",",y,")"
            print "Horizontal",w-x
            print "(",x,",",y,")"
            print "Vertical",h-y
            print width-(x+w/2)
            x_new=width-(x+w/2)
            y_new=(y+h/2)
            pyautogui.moveTo(x_new,y_new)
            for j in range(len(conts2)):
                a,b,c,d=cv2.boundingRect(conts2[j])
                cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,0),3)
                print (abs((x+w)-(a+c)))
                if (abs((x+w)-(a+c))<80):
                    pyautogui.click()
        res = cv2.bitwise_and(frame,frame, mask= mask)
        frame=cv2.flip(frame,1)
        frame1=cv2.flip(frame1,1)
        mask=cv2.flip(mask,1)
        res=cv2.flip(res,1)
        cv2.imshow("MaskFinal",maskFinal1)
        cv2.imshow('frame',frame)
        cv2.imshow('Me',frame1)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()
