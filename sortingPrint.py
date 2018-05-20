#  File: sorting.py
#  Description: List the average time it takes to sort various lists using various algorithms
#  Student's Name: Nicolai Antonov
#  Student's UT EID: naa766
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: November 17, 2016
#  Date Last Modified: November 18, 2016


#Import the various packages needed, and define the sort methods (Bubble, Selection, Insertion, Shell, Merge, and Quick)
import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


#Create functions to return the average elapsed time for 5 cycles of sorting Random lists of integers of size n, using the six different algorithms

def findTimeBubbleRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        print("Random list:",myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeInsertionRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeSelectionRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeShellRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeMergeRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeQuickRandom(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

#Create functions to return the average elapsed time for 5 cycles of sorting Sorted lists of integers of size n, using the six different algorithms

def findTimeBubbleSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeInsertionSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeSelectionSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeShellSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeMergeSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeQuickSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

#Create functions to return the average elapsed time for 5 cycles of sorting Reversed lists of integers of size n, using the six different algorithms

def findTimeBubbleRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeInsertionRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeSelectionRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeShellRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeMergeRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeQuickRev(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        myList.reverse()
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

#Create functions to return the average elapsed time for 5 cycles of sorting Almost sorted lists of integers of size n, using the six different algorithms

def findTimeBubbleAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeInsertionAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeSelectionAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeShellAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeMergeAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeQuickAlSort(n):
    avgElapsedTime = 0
    for i in range(5):

        listLength = n
        myList = [i for i in range(listLength)]
        pairsSwapped = n // 10
        for i in range (pairsSwapped):
            ranIndex1 = random.randint(0,len(myList) - 1)
            savedVal = myList[ranIndex1] 
            ranIndex2 = random.randint(0,len(myList) - 1)
            myList[ranIndex1] = myList[ranIndex2]
            myList[ranIndex2] = savedVal

        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  


#Define the main function

def main():
    

#Print tables for each type of list, displaying the average execution time for lists of size 10, 100, and 1000

    print("Input type = Random")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubbleRandom(10),findTimeBubbleRandom(100),findTimeBubbleRandom(1000)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelectionRandom(10),findTimeSelectionRandom(100),findTimeSelectionRandom(1000)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertionRandom(10),findTimeInsertionRandom(100),findTimeInsertionRandom(1000)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShellRandom(10),findTimeShellRandom(100),findTimeShellRandom(1000)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMergeRandom(10),findTimeMergeRandom(100),findTimeMergeRandom(1000)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuickRandom(10),findTimeQuickRandom(100),findTimeQuickRandom(1000)))
    print()
    print()

    print("Input type = Sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubbleSort(10),findTimeBubbleSort(100),findTimeBubbleSort(1000)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelectionSort(10),findTimeSelectionSort(100),findTimeSelectionSort(1000)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertionSort(10),findTimeInsertionSort(100),findTimeInsertionSort(1000)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShellSort(10),findTimeShellSort(100),findTimeShellSort(1000)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMergeSort(10),findTimeMergeSort(100),findTimeMergeSort(1000)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuickSort(10),findTimeQuickSort(100),findTimeQuickSort(1000)))
    print()
    print()

    print("Input type = Reverse")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubbleRev(10),findTimeBubbleRev(100),findTimeBubbleRev(1000)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelectionRev(10),findTimeSelectionRev(100),findTimeSelectionRev(1000)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertionRev(10),findTimeInsertionRev(100),findTimeInsertionRev(1000)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShellRev(10),findTimeShellRev(100),findTimeShellRev(1000)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMergeRev(10),findTimeMergeRev(100),findTimeMergeRev(1000)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuickRev(10),findTimeQuickRev(100),findTimeQuickRev(1000)))
    print()
    print()

    print("Input type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubbleAlSort(10),findTimeBubbleAlSort(100),findTimeBubbleAlSort(1000)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelectionRev(10),findTimeSelectionRev(100),findTimeSelectionAlSort(1000)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertionAlSort(10),findTimeInsertionAlSort(100),findTimeInsertionAlSort(1000)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShellAlSort(10),findTimeShellAlSort(100),findTimeShellAlSort(1000)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMergeAlSort(10),findTimeMergeAlSort(100),findTimeMergeAlSort(1000)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuickAlSort(10),findTimeQuickAlSort(100),findTimeQuickAlSort(1000)))
main()