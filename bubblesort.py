class BubbleSort:

    def __init__(self):
        pass
	
	def bubbleSort(self,listToBeSorted):
		
		flag = true
		
		while flag:
			index = 1
			while index < len(listToBeSorted)-1:
				if listToBeSorted[index-1] > listToBeSorted[index]:
					value = listToBeSorted[index]
					listToBeSorted[index] = listToBeSorted[index-1]
					listToBeSorted[index-1] = value
				
if __name__ == "__main__":

    toBeSortedList = [5,3,8,2,1,9,7]
    sorter = BubbleSort()
    myList = sorter.bubbleSort(toBeSortedList)
    print myList
		
