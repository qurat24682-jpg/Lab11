from main_code import calculate_sum, apply_tax

# Unit Tests
print("Unit Sum:", calculate_sum([10, 20, 30]))
print("Unit Tax:", apply_tax(100, 10))

# Integration Test
items = [50, 100, 150]
total = calculate_sum(items)
final = apply_tax(total, 10)

print("Integration Result:", final)