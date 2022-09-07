class Sorting:
    def __init__(self, data):
        self.data = data


class BubbleSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def start_sorting(array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


class SelectionSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def start_sorting(array):
        size = len(array)
        for ind in range(size):
            min_idx = ind
            for i in range(ind + 1, size):
                if array[i] < array[min_idx]:
                    min_idx = i
            array[ind], array[min_idx] = array[min_idx], array[ind]


class BubbleSortWithBrake(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def start_sorting(array):
        for i in range(len(array)):
            swapped = False
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            if not swapped:
                break


class InsertionSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def start_sorting(array):
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key


class MergeSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    def start_sorting(self, array):
        if len(array) > 1:

            r = len(array) // 2
            L = array[:r]
            M = array[r:]

            self.start_sorting(L)
            self.start_sorting(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = M[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                array[k] = M[j]
                j += 1
                k += 1


class QuickSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def partition(array, low, high):

        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)

            self.quick_sort(array, low, pi - 1)

            self.quick_sort(array, pi + 1, high)

    def start_sorting(self, data):
        size = len(data)
        self.quick_sort(data, 0, size - 1)


class RadixSort(Sorting):
    def __init__(self, data):
        super().__init__(data)

    @staticmethod
    def counting_sort(array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]

    # Main function to implement radix sort
    def start_sorting(self, array):
        # Get maximum element
        max_element = max(array)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            self.counting_sort(array, place)
            place *= 10