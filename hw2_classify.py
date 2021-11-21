import math
import sys

#def classifyEmails()
#opens the probability_ham/spam files
#then proceeds to search through the test files and look for each unique word, and add its log10 probability of existing in the test file
#after adding all the spam and ham values together, will write in the output(#).txt file wether it is spam or ham
def classifyEmails(filesToUse):
    fileHam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_ham_words.txt", "r").read().split()
    fileSpam = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/probability_spam_words.txt", "r").read().split()
    fileHam = fileHam[16:] # get rid of the initial line describing layout of file
    fileSpam = fileSpam[16:]
    hamProbability = 0
    spamProbability = 0

    fileOpen = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Test/test_Lemmatized/"+filesToUse[1]) #will open test file
    fileWrite = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/"+filesToUse[2],"w") #open correct output file, will create if does not exist in directory
    fileWrite.write("(1) P(Spam, all words)\n")

    for line in fileOpen:
        for word in line.split(): #for each word in test file
            inSpamFile = False 
            if word in fileSpam: #if word is found in probability_spam_words.txt
                wordIndex = fileSpam.index(word)
                fileWrite.write("P('"+word+"'|Spam) = "+ str((fileSpam[wordIndex + 1] + "\n"))) #write probability value in
                spamProbability += math.log10(float(fileSpam[wordIndex + 1])) #add log10 probability value to total
                inSpamFile = True
            if inSpamFile == False: #if word not found in probability_spam_words.txt
                fileWrite.write("P('"+word+"'|Spam) = "+str(1/84722) +"\n")
                spamProbability += math.log10(1/84722)
    fileWrite.write("log P(Spam, all words) = " + str(round(spamProbability,8)) + "\n\n\n")
    fileOpen.close()

    fileOpen = open("D:/Programming/Repositories/SpamFiltering/spamFiltering/Data/Test/test_Lemmatized/"+filesToUse[1]) #open again so can iterate lines again
    fileWrite.write("(2) P(Ham, all words)\n")
    for line in fileOpen:
        for word in line.split():
            inHamFile = False
            if word in fileHam: #if found in probability_ham_words.txt
                wordIndex = fileHam.index(word)
                fileWrite.write("P('"+word+"'|Ham) = "+ str((fileHam[wordIndex + 1] +"\n"))) #same thing, but with ham
                hamProbability += math.log10(float(fileHam[wordIndex + 1])) 
                inHamFile = True 
            if inHamFile == False: #if word not found in probability_ham_words.txt
                fileWrite.write("P('"+word+"'|Ham) = "+str(1/84722) + "\n")
                hamProbability += math.log10(1/84722)          

    fileWrite.write("log P(Ham, all words) = " + str(round(hamProbability,8)) + "\n\n\n")
    fileWrite.write("\n")
    fileWrite.write("Conclusion: This message is classified as")

    if(hamProbability > spamProbability):
        print("HAM " + filesToUse[1])
        fileWrite.write(" Ham\n")
    else:
        print("SPAM " + filesToUse[1])
        fileWrite.write(" Spam\n")
    fileOpen.close()

classifyEmails(sys.argv)