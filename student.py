def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(m1, m2, m3):
    return calculate_total(m1, m2, m3) / 3

def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 35:
        return "C"
    else:
        return "Fail"

m1 = 80
m2 = 75
m3 = 90

total = calculate_total(m1, m2, m3)
avg = calculate_average(m1, m2, m3)

print("Student Total:", total)
print("Average:", avg)
print("Grade:", get_grade(avg))