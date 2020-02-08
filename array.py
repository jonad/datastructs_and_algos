class Array:
    def __init__(self, capacity:int) -> None:
        self.capacity = capacity
        self.arr = []
        self.size = 0
    
    @property
    def size(self):
        return self._size
    
    @property
    def capacity(self):
        return self._capacity
    
    @size.setter
    def size(self, new_size):
        if not isinstance(new_size, int):
            raise TypeError('Size must be int')
        if new_size < 0:
            raise ValueError('size must be >= 0')
        if len(self.arr) != new_size:
            raise ValueError('Size must be equal to the number of item in the array')
        self._size = new_size
        
    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity<0:
            raise ValueError('Capacity must be greater than 0')
        self._capacity = new_capacity
    
    def __getitem__(self, item):
        return self.arr[item]
    
    def __setitem__(self, key, value):
        self.arr[key] = value
    
    def clear(self):
        self.arr.clear()
        self.size = 0
    
    def is_full(self):
        return self.size == self.capacity
        
    def add(self, elt):
        if not self.is_full():
            self.arr.append(elt)
            self.size += 1
        else:
            self.capacity *= 2
            self.add(elt)
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.arr.__iter__()
    
    def __str__(self):
        return f'Array of capacity {self.capacity!r}, with {self.size!r} element(s): {self.arr!r}'
    
    def __repr__(self):
        return f'Array of capacity {self.capacity!r}, with {self.size!r} element(s): {self.arr!r}'
    
    def remove(self, value):
        self.arr.remove(value)
    
    def remove_at(self, key):
        self.arr.__delitem__(key)
        
    
    
        
        
    