import argparse
from distutils.cmd import Command
import sys
from fileinput import filename
import cv2
import numpy as np
import threading
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

def play_video(cap, double_buffer, canvas_w, canvas_h):
    while cap.isOpened():
        im_pils = []
        start = time.time()
        for i in range(2):
            ret, im = cap.read()
            if(ret == False):
                break
            im = cv2.resize(im, (canvas_w, canvas_h))
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(im)
            im_pils.append(im_pil)

        if(ret == False):
            break

        double_buffer.SetImage(im_pils[0])
        double_buffer.SetImage(im_pils[1], canvas_w)
        double_buffer = matrix.SwapOnVSync(double_buffer)

        elapsed = time.time() - start
        # print('elapsed:%f'%(elapsed))
        time.sleep(max([0, 0.05 - elapsed]))

# Configuration for the matrix
options = RGBMatrixOptions()
options.cols = 64
options.rows = 32
options.chain_length = 2 
options.parallel = 3
options.brightness = 75
options.pwm_bits = 11
options.gpio_slowdown = 4.0
options.show_refresh_rate = 0
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.pwm_dither_bits = 0

matrix = RGBMatrix(options = options)

canvas_w = 2 * options.cols
canvas_h = 3 * options.rows

def event_job():
    global fileName 
    fileName = ''
    global stopVideo 
    stopVideo = True
    while True:
        cmd = input()
        if cmd == '3301':
            fileName = 'exit'
            stopVideo = True
            sys.exit(0)
        if cmd == "0":
            stopVideo = True
        if cmd == "1" :
            fileName = 'vid1.mp4'
            stopVideo = False
        if cmd == "2":
            fileName = 'vid2.mp4'
            stopVideo = False
        if cmd == "3":
            fileName = 'vid3.mp4'
            stopVideo = False
        if cmd == "4":
            fileName = 'vid4.gif'
            stopVideo = False
        if cmd == "5":
            fileName = 'vid5.gif'
            stopVideo = False
        if cmd == "6":
            fileName = 'vid6.mp4'
            stopVideo = False
        if cmd == "7":
            fileName = 'vid7.gif'
            stopVideo = False
        if cmd == "8":
            fileName = 'vid8.mp4'
            stopVideo = False
        if cmd == "9":
            fileName = 'vid9.mp4'
            stopVideo = False
        if cmd == "10":
            fileName = 'vid10.gif'
            stopVideo = False
        if cmd == "11":
            fileName = 'vid11.gif'
            stopVideo = False
        if cmd == "12":
            fileName = 'vid12.gif'
            stopVideo = False
        if cmd == "13":
            fileName = 'vid13.mp4'
            stopVideo = False
        if cmd == "14":
            fileName = 'vid14.gif'
            stopVideo = False
        if cmd == "15":
            fileName = 'vid15.gif'
            stopVideo = False    
        if cmd == "16":
            fileName = 'vid16.gif'
            stopVideo = False    
        if cmd == "17":
            fileName = 'vid17.gif'
            stopVideo = False 
        if cmd == "18":
            fileName = 'vid18.gif'
            stopVideo = False
        if cmd == "19":
            fileName = 'vid19.gif'
            stopVideo = False
        if cmd == "20":
            fileName = 'vid20.gif'
            stopVideo = False 


threading1 = threading.Thread(target=event_job)
threading1.daemon = True
threading1.start()
while True:
    while stopVideo == False:
        print('image is playing')
        cap = cv2.VideoCapture(fileName)
        double_buffer = matrix.CreateFrameCanvas()
        play_video(cap, double_buffer, canvas_w, canvas_h)
    if fileName == 'exit':
        sys.exit(0)
    
    
