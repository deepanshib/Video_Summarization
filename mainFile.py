
import cv2   
import math 
import matplotlib.pyplot as plt    
#%matplotlib inline
import pandas as pd
from keras.preprocessing import image  
import numpy as np    
from keras.utils import np_utils
from skimage.transform import resize   
import sample 
import pickle 
import os
import nltk
nltk.download('stopwords')
from textsummary import generate_summary
tt=[]
ff=[]
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
#"E:\Deepanshi\deeplearning\video\SumMe\videos\{}.format(vid)))
from os.path import isfile, join
mypath="E:/Deepanshi/deeplearning/video/SumMe/videos"
onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
for k in range(2):
    videoFile = "E:/Deepanshi/deeplearning/video/SumMe/videos/{}".format(onlyfiles[k])
    cap = cv2.VideoCapture(videoFile)   # capturing the video from the given path
    frameRate = cap.get(5) #frame rate(secs)
    directory="frames/{}".format(videoFile.split("/")[-1].split(".")[0])
    
    count = 0
    x=1
    if not os.path.exists(directory):
        os.makedirs(directory)
        while(cap.isOpened()):
            frameId = cap.get(1) #current frame number
            ret, frame = cap.read()
            if (ret != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                filename ="frame%d.jpg" % count;count+=1
                cv2.imwrite("{}/{}".format(directory,filename), frame)
        cap.release()
        
        print ("Done!")
    DIR="{}/".format(directory)
    print(directory)
    answer=""
    count=50
    for i in range(count):
        ans=sample.main(image="{}/frame{}.jpg".format(DIR,i))
        answer+=ans
        
    text_file = open("Output.txt", "w")
    text_file.write(answer)
    text_file = open("Output.txt", "r")
    text=text_file.read()
    tt.append(answer)
    final_ans=' '.join(unique_list(text.split("<end>")))
    text_file.close()
    ff.append(final_ans.replace("<start>",""))
#text_file ="Output.txt"
#text_file = open("Output.txt", 'r').read()
#print(text_file)
#generate_summary( text_file, 3)
#img = plt.imread('frame0.jpg')   #
#plt.imshow(img)
#
#
#a=' '.join(unique_list(text_file.split()))
#print(a)
i=0
for val in ff:
    i+=1
    print("Video{}:{}".format(i,val))
    print("\n")
    
from difflib import SequenceMatcher
ratio = SequenceMatcher(None, a, b).ratio()
print(ratio)