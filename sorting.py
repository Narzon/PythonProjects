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

#Define functions to return various list types (rev for reversed, ran for random, fullsorted for sorted, and alsorted for almost sorted) given list length n

def rev(n):
    listLength = n
    myList = [i for i in range(listLength)]
    myList.reverse()
    return myList

def ran(n):
    listLength = n
    myList = [i for i in range(listLength)]
    random.shuffle(myList)
    return myList

def fullsorted(n):
    listLength = n
    myList = [i for i in range(listLength)]
    return myList

def alsorted(n):
    listLength = n
    myList = [i for i in range(listLength)]
    pairsSwapped = n // 10
    for i in range (pairsSwapped):
        ranIndex1 = random.randint(0,len(myList) - 1)
        savedVal = myList[ranIndex1] 
        ranIndex2 = random.randint(0,len(myList) - 1)
        myList[ranIndex1] = myList[ranIndex2]
        myList[ranIndex2] = savedVal
    return myList

#Define functions to return the average execution time of 5 iterations of sorting through lists listType of length n using the six sorting algorithms defined above 

def findTimeBubble(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeInsertion(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeSelection(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  


def findTimeShell(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeMerge(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        avgElapsedTime += elapsedTime
    avgElapsedTime = avgElapsedTime / 5
    return avgElapsedTime  

def findTimeQuick(n, listType):
    avgElapsedTime = 0
    for i in range(5):

        myList = listType(n)

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
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubble(10, ran),findTimeBubble(100, ran),findTimeBubble(1000, ran)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelection(10, ran),findTimeSelection(100, ran),findTimeSelection(1000, ran)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertion(10, ran),findTimeInsertion(100, ran),findTimeInsertion(1000, ran)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShell(10, ran),findTimeShell(100, ran),findTimeShell(1000, ran)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMerge(10, ran),findTimeMerge(100, ran),findTimeMerge(1000, ran)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuick(10, ran),findTimeQuick(100, ran),findTimeQuick(1000, ran)))
    print()

    print("Input type = Sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubble(10, fullsorted),findTimeBubble(100, fullsorted),findTimeBubble(1000, fullsorted)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelection(10, fullsorted),findTimeSelection(100, fullsorted),findTimeSelection(1000, fullsorted)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertion(10, fullsorted),findTimeInsertion(100, fullsorted),findTimeInsertion(1000, fullsorted)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShell(10, fullsorted),findTimeShell(100, fullsorted),findTimeShell(1000, fullsorted)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMerge(10, fullsorted),findTimeMerge(100, fullsorted),findTimeMerge(1000, fullsorted)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuick(10, fullsorted),findTimeQuick(100, fullsorted),findTimeQuick(1000, fullsorted)))
    print()
    print()

    print("Input type = Reverse")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubble(10, rev),findTimeBubble(100, rev),findTimeBubble(1000, rev)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelection(10, rev),findTimeSelection(100, rev),findTimeSelection(1000, rev)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertion(10, rev),findTimeInsertion(100, rev),findTimeInsertion(1000, rev)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShell(10, rev),findTimeShell(100, rev),findTimeShell(1000, rev)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMerge(10, rev),findTimeMerge(100, rev),findTimeMerge(1000, rev)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuick(10, rev),findTimeQuick(100, rev),findTimeQuick(1000, rev)))
    print()
    print()

    print("Input type = Almost sorted")
    print("                    avg time   avg time   avg time")
    print("   Sort function     (n=10)    (n=100)    (n=1000)")
    print("-----------------------------------------------------")
    print("      bubbleSort    %.6f   %.6f   %.6f" % (findTimeBubble(10, alsorted),findTimeBubble(100, alsorted),findTimeBubble(1000, alsorted)))
    print("   selectionSort    %.6f   %.6f   %.6f" % (findTimeSelection(10, alsorted),findTimeSelection(100, alsorted),findTimeSelection(1000, alsorted)))
    print("   insertionSort    %.6f   %.6f   %.6f" % (findTimeInsertion(10, alsorted),findTimeInsertion(100, alsorted),findTimeInsertion(1000, alsorted)))
    print("       shellSort    %.6f   %.6f   %.6f" % (findTimeShell(10, alsorted),findTimeShell(100, alsorted),findTimeShell(1000, alsorted)))
    print("       mergeSort    %.6f   %.6f   %.6f" % (findTimeMerge(10, alsorted),findTimeMerge(100, alsorted),findTimeMerge(1000, alsorted)))
    print("       quickSort    %.6f   %.6f   %.6f" % (findTimeQuick(10, alsorted),findTimeQuick(100, alsorted),findTimeQuick(1000, alsorted)))
main()