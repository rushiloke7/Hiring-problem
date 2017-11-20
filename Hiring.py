from ConvertCsv import ConvertCsv
import pprint
import random
from operator import itemgetter

# data = ConvertCsv()
# candidates = data.getList()
# print(candidates)

#list of global variables:


def addZero(candidates):
    count = -1
    for row in candidates:
        count += 1
        candidates[count].append(0)
    print(candidates)
    return candidates


def dataToBinary(rawCsvData=None):

    wPercentage                 = 64
    wBacklog                    = 32
    wLocation                   = 16
    wLanguage                   = 8
    wExp                        = 4
    wCertificate                = 2
    wPH                         = 1

    columnHeader = rawCsvData[0]
    print(columnHeader)
    rows = rawCsvData[1:]
    pprint.pprint(rows)
    #incomplete function


def processRawData(rawCsvData=None):
    # experinceScore = 0.3*4
    # candidateScore = experinceScore + percentageScore - backlogScore
    columnHeader = rawCsvData[0]
    rows         = rawCsvData[1:]
    availableCandidateList = []
    data = {}
    candidatesList = []
    #ListData Store the FinalData to be returned from this function
    ListData = []
    ListData.append(columnHeader)

    for candidateDetails in rows:
        for i in range(0,len(candidateDetails)):
            data[columnHeader[i]] = candidateDetails[i]
        candidatesList.append(data)
        data = {}
    ListData.append(candidatesList)

    return ListData

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

    pprint.pprint(passedcandidates)

def sortCandidates(candidates):
    sorted(candidates,key=lambda x:x[8], reverse=True)




if __name__ == '__main__':

    data = ConvertCsv()
    candidates = data.getList()
    # pprint.pprint(candidates)
    selected_candidates_id = []
    selectedCandidates = []
    for i in range(0,3):
        for row in (picRandomCandidates(candidates, 5)):
            selectedCandidates.append(row)
    pprint.pprint(selectedCandidates)

    finalcandidates = addWeight(selectedCandidates, 3)
    pprint.pprint(finalcandidates)
    finalcandidates = sorted(finalcandidates,key=lambda l:l[8], reverse=True)
    pprint.pprint(finalcandidates)


    #addWeight(candidates, 4)

    #ListData = processRawData(candidates)
    # pprint.pprint(ListData)
