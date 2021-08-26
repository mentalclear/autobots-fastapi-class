def greeting(name: str) -> str:
    """ This function expects to have argument name of type string"""
    return 'Hello ' + name

print(greeting('Tester'))


# A type alias is defined by assigning the type to the alias. In this example, 
# Vector and list[float] will be treated as interchangeable synonyms

Vector = list[float]
def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])
print(new_vector)