def convert_cel_to_far(cel:float):
    far = cel*(5/9)+32
    return far
def convert_far_to_cel(far: float):
    cel = (far-32)*(9/5)
a = float(input("Enter a temperature in degrees F: "))
print(a,"degrees F =",convert_far_to_cel(a),"degrees C")
b= float(input("Enter a temperature in degrees C: "))
print(b,"degrees C =",convert_cel_to_far(b),"degrees F")