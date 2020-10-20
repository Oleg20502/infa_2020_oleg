class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if isinstance(other, Vector):
             return Vector(self.x+other.x, self.y+other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x+other, self.y+other)
        else:
            raise TypeError(f'cannot add {other.__class__.__name__} to Vector')
    
class MyList(list):
    def __getitem__(self, index):
        if isinstance(index, tuple):
            return [self[i] for i in index]
        else:
            return super().__getitem__(index)
    
    
    pass