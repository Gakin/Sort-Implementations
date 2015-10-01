class MergeSort:
	
	def __init__(self):
		pass
		
	def mergeSort(self,argList):
	
		sortedList = []
	
		if len(argList) == 1:
			return argList
		
		leftList = argList[0:len(argList)/2]
		rightList = argList[(len(argList)/2)+1:len(argList)-1]
		
		sortedLeftList = mergeSort(leftList)
		sortedRightList = mergeSort(rightList)
		
		leftIndex = 0
		rightIndex = 0
		listIndex = 0
		
		#there is some mistake in the merge step currently will be checked !
		#Sorts in increasing order
		while leftIndex < len(sortedLeftList) and rightIndex < len(sortedRightList):
			if sortedLeftList[leftIndex] >= sortedRightList[rightIndex]:
				sortedList[listIndex] = sortedRightList[rightIndex]
				rightIndex += 1
				listIndex += 1
			else:
				sortedList[listIndex] = sortedLefttList[leftIndex]
				leftIndex += 1
				listIndex += 1
				
		if leftIndex == len(sortedLeftList):
			while rightIndex < len(sortedRightList):
				sortedList[listIndex] = sortedRightList[rightIndex]
				rightIndex += 1
				listIndex += 1
				
		else:
			while leftIndex < len(sortedLeftList):
				sortedList[listIndex] = sortedLefttList[leftIndex]
				leftIndex += 1
				listIndex += 1
		
		return sortedList
		
		
if __name__ == "__main__":
    sorter = MergeSort()
    toBeSortedList = [5,3,8,2,1,9,7]
    myList = sorter.mergeSort(toBeSortedList)
    print myList[0]