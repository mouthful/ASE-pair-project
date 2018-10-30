import time
import re
from collections import Counter
import operator as op
import os
###################################################################################
#Name:count_letters
#Inputs:file_name
#       n : output the top N items in letters
#       stopName: the file of stopwords skipped
#       verbName: the file of verb dict
#outputs:None
#Author: ThomasY, changed by mouthful
#Date:2018.10.28
###################################################################################
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def CountLetters(file_name,n,stopName,verbName):
    print("File name:" + file_name)
    if (stopName != None):
        stopflag = True
    else:
        stopflag = False
    if(verbName != None):
        print("Verb tenses normalizing is not supported in this function!")
    else:
        pass
    totalNum = 0
    dicNum = {}
    t0 = time.clock()
    if (stopflag == True):
        with open(stopName) as f:
            stoplist = f.readlines()
            stopNum = len(stoplist)
    with open(file_name) as f:
        txt = f.read().lower()
    for letter in letters:
        dicNum[letter] = txt.count(letter) #here count is faster than re
        totalNum += dicNum[letter]
    for letter in letters:
        dicNum[letter] = dicNum[letter]
    if (stopflag == True):
        for word in stoplist:
            word = word.replace('\n','')
            try:
                del dicNum[word]
            except:
                pass
    dicNum = sorted(dicNum.items(), key=lambda k: k[0])
    dicNum = sorted(dicNum, key=lambda k: k[1], reverse=True)
    t1 = time.clock()
    display(dicNum[:n],'character',totalNum,9)
    print("Time Consuming:%4f" % (t1 - t0))
###################################################################################
#Name:display
#Inputs:dicNum: a dict of data displayed in the screen
#       type :
#       totalNum:
#       k:
#outputs:None
#Author: ThomasY, changed by mouthful
#Date:2018.10.28
###################################################################################
def display(dicNum,type,totalNum,k):
    maxLen = 0
    if(not dicNum):
        print("Error:Nothing matched!!")
        return
    for word, fre in dicNum:
        if(len(word)>maxLen):
            maxLen = len(word)
    print("-"*int(2.18*k*maxLen))
    formatstr = "|{:^" + str(2*k * maxLen+1) + "}|"
    print(formatstr.format('The Rank List'))
    formatstr = "|{:" + str(k*maxLen) + "}|{:<" + str(k*maxLen) + "}|"
    print(formatstr.format(type, "Frequency"))
    if totalNum >0:
        formatstr = "|{:" + str(k*maxLen) + "}|{:<" + str(k*maxLen) + ".2%}|"
        for word, fre in dicNum:
            print(formatstr.format(word, fre/totalNum))
        print("-" * int(2.18*k * maxLen))

###################################################################################
#Name:OperateInDir
#Inputs:dicNum: a dict of data displayed in the screen
#       n : output the top N items in dict
#       stopName: the file of stopwords skipped
#       verbName: the file of verb dict
#       reflag:  whether to go through subdir
#outputs:None
#Author: ThomasY, changed by mouthful
#Date:2018.10.28
###################################################################################
def OperateInDir(Fuc,Dir_name,n,stopName,verbName,reflag,*arges):
    if(reflag):
        for path, _, filelist in os.walk(Dir_name):
            for file in filelist:
                if(arges):
                    Fuc(os.path.join(path, file), n, stopName, verbName,arges[0])
                else:
                    Fuc(os.path.join(path, file),n,stopName,verbName)
    else:
        for file in os.listdir(Dir_name):
            if(os.path.isdir(os.path.join(Dir_name, file))):
                pass
            else:
                if (arges):
                    Fuc(os.path.join(Dir_name, file), n, stopName, verbName, arges[0])
                else:
                    Fuc(os.path.join(Dir_name, file), n, stopName, verbName)