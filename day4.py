marks = {"Maths":88,"science":92,"English":79,"History":85}
print(marks)

for i,j in marks.items():
    print(i,j)

def top_marks(marks):
    print(max(marks.values()))

top_marks(marks)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5 + 32))

print(celsius_to_fahrenheit(22.98))

def is_fever(temp):
    if temp > 37.5:
        return True
    else:
        return False

def describe_temp(c):
    f = celsius_to_fahrenheit(c)
    fever = is_fever(f)
    print(f"Temperature in Fahrenheit: {f}")
    print(f"Is fever: {fever}")

describe_temp(38)