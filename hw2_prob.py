#Hw2_prob.py
#Given test ham and spam files, will keep track of the occurance of each unique word, and determine their probability of occurance
import os
#def ProbWords()
#Given spam and ham  test files, will record the number of occurances of each unique word
def probWords():
    hamWordOccurance = dict()
    spamWordOccurance = dict()
    hamWordCount = 0
    spamWordCount = 0

    for file in os.listdir("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Train/train_Lemmatized"):
            fileOpen = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Train/train_Lemmatized/"+file,"r") 
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

#def writeProbabilityFiles
#Given the word 
def writeProbabilityFiles(spamWordOccurance, spamWordCount, hamWordOccurance, hamWordCount):
    fileHam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_ham_words.txt", "w")
    fileSpam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_spam_words.txt", "w")
    print(spamWordCount + hamWordCount)
    for word in spamWordOccurance:
        keyValue = spamWordOccurance.get(word)
        wordProbability = keyValue/spamWordCount
        fileSpam.write(str(word) + " ")
        fileSpam.write(str(wordProbability)+"\n")
    fileSpam.close()

    
    for word in hamWordOccurance:
        keyValue = hamWordOccurance.get(word)
        wordProbability = keyValue/hamWordCount
        fileHam.write(str(word) + " ")
        fileHam.write(str(wordProbability)+"\n")
    fileHam.close()
probWords()