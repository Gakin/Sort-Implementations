class InsertionSort:

    def __init__(self):
        pass
	
	def insertionSort(self,listToBeSorted):
		innerIndex = 0
		outerIndex = 1
		
		while outerIndex < len(listToBeSorted)-1:
			
			innerIndex = outerIndex
			
			while innerIndex > 0 and listToBeSorted[innerIndex-1] < listToBeSorted[innerIndex-1]:
				value = listToBeSorted[innerIndex-1]
				listToBeSorted[innerIndex-1] = listToBeSorted[innerIndex]
				listToBeSorted[innerIndex] = value
				innerIndex -= 1
			
			outerIndex += 1

if __name__ == "__main__":

    toBeSortedList = [5,3,8,2,1,9,7]
    sorter = InsertionSort()
    myList = sorter.insertionSort(toBeSortedList)
    print myList
		