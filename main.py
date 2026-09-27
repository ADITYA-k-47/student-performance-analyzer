print("student performance analyzer")
name = input("enter student name:")
maths = float(input("enter maths marks(0-100):"))
while maths<0 or maths>100:
    print("please enter marks between 0 and 100")
python = float(input("enter python marks(0-100):"))
while python<0 or python>100:
    print("please enter marks between 0 and 100:")
english = float(input("enter english marks(0-100):"))
while english<0 or english>100:
    print("please enter marks between 0 and 100:")
average = (maths+python+english)/3
if average >= 90:
    grade = "a+"
elif average >= 80:
    grade = "b"
elif average >= 70:
    grade = "c"
elif average >= 60:
    grade = "d"
elif average >= 50:
    grade = "e"
print("grade:",grade)
if average >= 40:
    result = "pass"
else:
    result = "fail"
highest = max(maths,python,english)
lowest = min(maths,python,english)
print("result:",result)
print("student:",name)
print("average marks:",round(average,2))
print("highest marks:",highest)
print("lowest marks:",lowest)