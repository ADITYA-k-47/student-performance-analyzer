name = input("enter student name:")
maths = float(input("enter maths marks(0-100):"))
python = float(input("enter python marks(0-100):"))
english = float(input("enter english marks(0-100):"))
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
    grade = "f"
else:
    grade = "f"
print("grade:",grade)
if average >= 40:
    result = "pass"
else:
    result = "fail"
highest = max(maths,python,english)
lowest = min(maths,python,english)
print("\nresult")
print("student:",name)
print("average marks:",round(average,2))
print("highest marks:",highest)
print("lowest marks:",lowest)
print("please enter numbers for marks")