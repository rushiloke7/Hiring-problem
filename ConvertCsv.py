import csv

class ConvertCsv:

    def getList(self):
        with open('canditates2.csv', 'r') as csvFile:
            row = csv.reader(csvFile)
            dataList = []
            for i in row:
                dataList.append(i)
        csvFile.close()

        # Convert second row to last row into int values.
        intDataList = []
        intDataList = dataList[0:1]

        for row in dataList[1:]:
            intDataList.append(list(map(int, row)))

        return intDataList

    def listToCsv(self, fileName, columnHeader, columnData):
        with open(fileName, "w") as outputFile:
            write = csv.writer(outputFile)
            write.writerow(columnHeader)
            write.writerows(columnData)
        outputFile.close()
