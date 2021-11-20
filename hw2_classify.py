import math
import os

def classifyEmails():
    fileHam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_ham_words.txt", "r").read().split()
    fileSpam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_spam_words.txt", "r").read().split()

    hamProbability = 0
    spamProbability = 0 
    inHamFile = False
    inSpamFile = False
    fileNo = 0
    for file in os.listdir("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Test/test_Lemmatized"):
        if(file[1] == '.'):
            fileNo = file[0]
        else:
            fileNo = file[0:2]
        hamProbability = 0
        spamProbability = 0
        fileOpen = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Test/test_Lemmatized/"+file)
        fileWrite = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/output"+str(fileNo)+".txt","w")
        fileWrite.write("(1) P(Spam, all words)\n")
        for line in fileOpen:
            for word in line.split():
                inSpamFile = False
                if word in fileSpam:
                  wordIndex = fileSpam.index(word)
                  fileWrite.write("P('"+word+"'|Spam) = "+ str((fileSpam[wordIndex + 1] + "\n")))
                  spamProbability += math.log10(float(fileSpam[wordIndex + 1]))
                  inSpamFile = True
                if inSpamFile == False:
                    fileWrite.write("P('"+word+"'|Spam) = "+str(1/84722) +"\n")
                    spamProbability += math.log10(1/84722)
        fileWrite.write("log P(Spam, all words) = " + str(spamProbability) + "\n\n\n")
        fileOpen.close()

        fileOpen = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Test/test_Lemmatized/"+file) #open again so can iterate lines again
        fileWrite.write("(2) P(Ham, all words)\n")
        for line in fileOpen:
            for word in line.split():
                inHamFile = False
                if word in fileHam:
                    wordIndex = fileHam.index(word)
                    fileWrite.write("P('"+word+"'|Ham) = "+ str((fileHam[wordIndex + 1] +"\n")))
                    hamProbability += math.log10(float(fileHam[wordIndex + 1]))
                    inHamFile = True 
                if inHamFile == False:
                    fileWrite.write("P('"+word+"'|Ham) = "+str(1/84722) + "\n")
                    hamProbability += math.log10(1/84722)          
        fileWrite.write("log P(Ham, all words) = " + str(hamProbability) + "\n\n\n")
        fileWrite.write("\n")
        fileWrite.write("Conclusion: This message is classified as")

        if(hamProbability > spamProbability):
            print("HAM " + file)
            fileWrite.write(" Ham\n")
        else:
            print("SPAM " + file)
            fileWrite.write(" Spam\n")
    fileOpen.close()

classifyEmails()