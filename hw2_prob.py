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
                    for word in line.split(): #for each word, increment its occurance in the appropriate dictionary
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
#Given the word count, will write in probability_ham_words.txt and probability_spam_words.txt the given probabiity of a word occuring 
# by doing #Of times word is seen in all files / number of words in all
def writeProbabilityFiles(spamWordOccurance, spamWordCount, hamWordOccurance, hamWordCount):
    fileHam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_ham_words.txt", "w")
    fileSpam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_spam_words.txt", "w")
    fileHam.write("***The probability of a word will be adjacent to the word, seperated by a single space***\n\n\n")
    fileSpam.write("***The probability of a word will be adjacent to the word, seperated by a single space***\n\n\n")
    for word in spamWordOccurance:
        keyValue = spamWordOccurance.get(word)
        wordProbability = keyValue/spamWordCount
        fileSpam.write(str(word) + " ")             #write the word that is found in the test file
        fileSpam.write(str(wordProbability)+"\n") #write the probability of occurance of said word
    fileSpam.close()

    
    for word in hamWordOccurance:
        keyValue = hamWordOccurance.get(word)
        wordProbability = keyValue/hamWordCount
        fileHam.write(str(word) + " ")           #write the word that is found in the test file
        fileHam.write(str(wordProbability)+"\n") #write the probability of occurance of said word
    fileHam.close()
probWords()