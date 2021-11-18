#P(cause, Ef1, Ef2....) = P(Cause) * P(Ef1|Cause) * P(Ef2|Cause) .... No need to put other causes on the right side as the effects are independent
#use log base 10
import os
def probWords():
    hamWordOccurance = dict()
    spamWordOccurance = dict()
    hamWordCount = 0
    spamWordCount = 0

    for file in os.listdir("D:/Programming/Repo/spamFiltering/spamFiltering/Data/Train/train_Lemmatized"):
            fileOpen = open("D:/Programming/Repo/spamFiltering/spamFiltering/Data/Train/train_Lemmatized/"+file,"r") 
            if(file[0] == '3' or file[0] == '5'): #ham dictionary
                for line in fileOpen:
                    for word in line.split():
                        if(word not in hamWordOccurance):
                            hamWordOccurance[word] = 1
                            hamWordCount += 1
                        else:
                            hamWordOccurance[word] += 1
                            hamWordCount += 1
            elif(file[0] == 's'): #spam dictionary
                for line in fileOpen:
                    for word in line.split():
                        if(word not in spamWordOccurance):
                            spamWordOccurance[word] = 1
                            spamWordCount += 1
                        else:
                            spamWordOccurance[word] += 1
                            spamWordCount += 1
            fileOpen.close()
    writeProbabilityFiles(spamWordOccurance, spamWordCount, hamWordOccurance, hamWordCount)


def writeProbabilityFiles(spamWordOccurance, spamWordCount, hamWordOccurance, hamWordCount):
    fileHam = open("D:/Programming/Repo/spamFiltering/spamFiltering/probability_ham_words.txt", "w")
    fileSpam = open("D:/Programming/Repo/spamFiltering/spamFiltering/probability_spam_words.txt", "w")

    for word in spamWordOccurance:
        keyValue = spamWordOccurance.get(word)
        wordProbability = keyValue/spamWordCount
