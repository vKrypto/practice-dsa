class CircularArray:

    def __init__(self, capacity=10) -> None:
        self._size = capacity
        self._capacity = capacity
        self._front = 0
        self._array = [None for _ in range(capacity)]

    def _actual_index(self, index):
        if index >= 0:
            if index > self._size:
                raise IndexError
            return  index
        if abs(index) > self._size:
            raise IndexError
        return index


    def __getitem__(self, index):
        return self._array[self._actual_index(index)]


    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass

    def __add__(self, value):
        pass

    def __eq__(self, __value: object) -> bool:
        pass


    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __sub__(self, other:object) -> object:
        pass


    def pop(self):
        pass