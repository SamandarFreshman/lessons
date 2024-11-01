universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(primitive:list):
    students = []
    fees = []
    for i in range(0,len(primitive)):
        students.append(primitive[i][1])
        fees.append(primitive[i][2])
    return students, fees
def mean(list1:list):
    sum = 0
    for i in range(len(list1)):
        sum+=list1[i]
    mean = sum/len(list1)
    return mean
def median(list1:list):
    list1.sort()
    if len(list1)%2==1:
        median= list1[(len(list1)+1)//2]
    else:
        median = (list1[(len(list1)+2)//2]+list1[(len(list1))//2])/2
    return median

num_students,titutions = enrollment_stats(universities)
print("Number of students:",sum(num_students))
print("Total tuition: $",sum(titutions))
print("\nStudent mean:",round(mean(num_students),2))
print("Student median:",median(num_students))
print("\nTitutions mean:",round(mean(titutions),2))
print("Titutions median:",median(titutions))