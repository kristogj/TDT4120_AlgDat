

class Heap:

    def __init__(self,A):
        self.liste = A
        self.lengde = len(A)
        self.heap_size = len(A)-1

    def Max_Heapify(self,A,i):
        l = Left(i)
        r = Right(i)
        if l <= self.heap_size and A[l] > A[i]:
            largest = l
        else: largest = i
        if r <= self.heap_size and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i],A[largest] = A[largest],A[i]
            self.Max_Heapify(A,largest)

    def Heapsort(self):
        # Build Max-Heap
        self.build_max_heap(self.liste)
        print("Start:" + str(self.liste))
        c = 1
        for i in range(len(self.liste) - 1, 0, -1):
            self.liste[0], self.liste[i] = self.liste[i], self.liste[0]
            self.heap_size -= 1
            self.Max_Heapify(self.liste, 0)
            print("Iterasjon " + str(c) + ": " + str(self.liste))
            c +=1
        return self.liste

    def build_max_heap(self,A):
        for i in range(self.lengde//2,-1,-1):
            self.Max_Heapify(A,i)

def Left(i):
    return 2*i +1

def Right(i):
    return 2*i + 2

def Parent(i):
    return i//2

liste = [4,1,3,2,16,9,10,14,8,7]
heap = Heap(liste)
heap.Heapsort()
