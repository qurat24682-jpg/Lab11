def calculate_sum(items):
    return sum(items)

def apply_tax(total, tax_percent):
    return total + (total * tax_percent / 100)

def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"