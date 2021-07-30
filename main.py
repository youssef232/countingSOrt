def countingSort(inputArray, outputArray, k):

    """

    :param inputArray: the input array to be sorted
    :param outputArray: the sorted array
    :param k: the largest number in the input array
    :return: sorted array
    """
    c = [0] * (k + 1)
    for i in range(0, len(inputArray)):
        """
        counting the iteration of each number in the array
        """
        c[inputArray[i]] += 1
    for i in range(1, k + 1):
        """
        the sum of the elements less than x.
        it's used to know where to start to put the range of this number
        """
        c[i] += c[i-1]

    for i in range(len(inputArray) - 1, -1, -1):
        """
        put the sorted elements in the output array.
        """
        outputArray[c[inputArray[i]] - 1] = inputArray[i]
        c[inputArray[i]] -= 1
    return outputArray


iArray = [2, 5, 3, 0, 2, 3, 0, 3]
oArray = [0] * len(iArray)
print(countingSort(iArray, oArray, max(iArray)))
