import math

class Vector:
    def __init__(self, *args):
        self.components = list(args)
        
    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __bool__(self):
        return any(c != 0 for c in self.components)

    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length for addition.")
        return Vector(*(x + y for x, y in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length for subtraction.")
        return Vector(*(x - y for x, y in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same length for multiplication.")
            return Vector(*(x * y for x, y in zip(self.components, other.components)))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*(x * other for x in self.components))
        else:
            raise TypeError("Operand must be a Vector or a scalar (int/float).")
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Operand must be a scalar (int/float).")
        if scalar == 0:
            raise ValueError("Cannot divide by zero.")
        return Vector(*(x / scalar for x in self.components))
    
    def __eq__(self, other):
        return self.components == other.components
    
    def __getitem__(self, index):
        return self.components[index]
    
    def __setitem__(self, index, value):
        self.components[index] = value
    
    def __len__(self):
        return len(self.components)
    
    def __abs__(self):
        return math.sqrt(sum(x**2 for x in self.components))
    
    def __neg__(self):
        return Vector(*(-x for x in self.components))


# Instantiation
v1 = Vector(1, 4, 6)
print(v1)              # Expected Output: Vector(1, 4, 6)

# Boolean Evaluation
print(bool(v1))               # Expected Output: True
print(bool(Vector(0, 0)))     # Expected Output: False

# Length
print(len(v1))               # Expected Output: 3

# Indexing and Slicing
print(v1[1])                # Expected Output: 4
v1[1] = 10
print(v1)              # Expected Output: Vector(1, 10, 6)

# Vector Arithmetic
v2 = Vector(3, 7, 2)
print(v1 + v2)            # Expected Output: Vector(4, 17, 8)
print(v1 - v2)                # Expected Output: Vector(-2, 3, 4)
print(v1 * v2)                # Expected Output: Vector(3, 70, 12)

# Scalar Multiplication and Division
print(v1 * 3)                 # Expected Output: Vector(3, 30, 18)
print(v1 / 2)                 # Expected Output: Vector(0.5, 5, 3)

# Absolute Value (Norm)
print(abs(v1))                # Expected Output: √(1^2 + 10^2 + 6^2) = 11.66...

# Equality Comparison
print(v1 == Vector(1, 10, 6)) # Expected Output: True

# Negation
print( -v1 )                   # Expected Output: Vector(-1, -10, -6)

"""output:
Vector(1, 4, 6)
True
False
3
4
Vector(1, 10, 6)
Vector(4, 17, 8)
Vector(-2, 3, 4)
Vector(3, 70, 12)
Vector(3, 30, 18)
Vector(0.5, 5.0, 3.0)
11.704699910719626
True
Vector(-1, -10, -6)
"""