from ConvertCsv import ConvertCsv
import pprint
import random
import csv
from operator import itemgetter
#jobless
def picRandomCandidates(candidates, noOfCandidates):
    #It will generate random candidates and return their details while storing them in a List
    selected = 0
    selectedCandidates = []
    while selected <= noOfCandidates:
        rn = random.randrange(1,len(candidates))
        if(rn in selected_candidates_id):
            continue
        selected_candidates_id.append(candidates[rn][0])
        selected += 1
        selectedCandidates.append(candidates[rn])
    return selectedCandidates



def addWeight(candidateList, noOfCriateria):
    # Calculates score and appends to the end of the each row.
    # candidateList = The list of candidates given.     noOfCriateria = No of critaria user selects

    #List of weights
    wPercentage                 = 2**6
    wBacklog                    = 2**5
    wLocation                   = 2**4
    wLanguage                   = 2**3
    wExp                        = 2**2
    wCertificate                = 2**1
    wPH                         = 2**0

    passedcandidates = []
    score = 0
    passedCriterias = 0
    for rows in candidateList[1:]:

        #PERCENTAGE
        if rows[1] > 60  :
            score += wPercentage
            passedCriterias += 1

        #BACKLOG
        if rows[2] == 0 :
            score += wBacklog
            passedCriterias += 1

        #LOCATION
        if rows[3] < 4 :
            score += wLocation
            passedCriterias += 1

        #LANGUAGES
        if rows[4] > 0 :
            score += wLanguage
            passedCriterias += 1

        #EXPERIENCE
        if rows[5] > 0 :
            score += wExp
            passedCriterias += 1

        #CERTIFICATION
        if rows[6] > 0 :
            score += wCertificate
            passedCriterias += 1

        #Physically Handicaped
        if rows[7] < 1 :
            score += wPH
            passedCriterias += 1

        #Check if candidate passed given cirteria and add to passedcandidates
        if passedCriterias >= noOfCriateria:
            rows.append(score)
            passedcandidates.append(rows)

        #reset value back to 0
        score = passedCriterias = 0

    # pprint.pprint(passedcandidates)
    return passedcandidates

def sortCandidates(candidates):
    #Sorts the candidates into decreasing order.
    sorted(candidates,key=lambda x:x[8], reverse=True)


def printFinalCandidates(finalcandidates, noOfCandidates):
    #print the final selected candidates back to console.
    print("Final candidates that are Selected are:")
    for row in finalcandidates[:5]:
        print("ID:", row[0], "| Score:",row[-1])

def getColumnNames(candidates):
    #returns column headers
    columnHeader = candidates[0]
    columnHeader.append('Score')
    return columnHeader


if __name__ == '__main__':
    #converts csv data to list
    data = ConvertCsv()
    candidates = data.getList()

    selected_candidates_id = []         #stores IDs of the candidates that are selected to avoid dublication
    selectedCandidates = []             #contains the randomly selected candidates in each iteration

    noOfCandidates = int(input("Enter the number of candidates you want to select:"))
    noOfCriateria = int(input("Enter the number of Criterias:"))
    noOfIterations = int(input("How many times do you want to iterate the list: (default is 3): "))

    #iterates 3 times and picks random candidate each time
    for i in range(0,noOfIterations):
        for row in (picRandomCandidates(candidates, noOfCandidates)):
            selectedCandidates.append(row)

    #adds socre to the selected candidates
    finalcandidates = addWeight(selectedCandidates, noOfCriateria)
    #sorts final seleted candidates into decreasing order of their score.
    finalcandidates = sorted(finalcandidates,key=lambda l:l[8], reverse=True)

    #presents the final selected candidates to the user
    printFinalCandidates(finalcandidates, noOfCandidates)

    #get list of headers
    columnHeader = getColumnNames(candidates)

    #Write the data of selected candidates into an output csv file.
    data.listToCsv("Output.csv", columnHeader, finalcandidates[:noOfCandidates])
    print("Succesfully written to the file: Output.csv")
