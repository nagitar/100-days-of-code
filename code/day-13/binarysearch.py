def binarySearch(theList, value, low, high):

    if high < low:

        return -1

    mid = (low + high)/2

    if theList[mid] > value:

        return binarySearch(theList, value, low, mid-1)

    elif theList[mid] < value:

        return binarySearch(theList, value, mid+1, high)

    else:

        return 1
