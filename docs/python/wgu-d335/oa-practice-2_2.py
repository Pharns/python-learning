# Input
oz_in = int(input())

# 1 ton = 2000 pounds = 2000 * 16 = 32000 ounces

# Calculate tons, pounds, and ounces using integer division and modulus
total_tons = oz_in // 32000  # how many whole tons
remaining_oz_after_tons = oz_in % 32000  # leftover ounces after tons
total_lbs = remaining_oz_after_tons // 16  # how many whole pounds
oz_remain = remaining_oz_after_tons % 16  # leftover ounces

# Output
print(f"Tons: {total_tons}")
print(f"Pounds: {total_lbs}")
print(f"Ounces: {oz_remain}")

# 1 ton = 2000 lbs = *16 = 3200 ounces
