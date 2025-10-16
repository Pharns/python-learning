# Employee A: 15.62 miles
# Employee B: 41.85 miles
# Employee C: 32.67 miles

# input = 3,10,5
# total =  628.71 miles
# solution accepts three integer inputs representing the number of times an employe
# solution outputs "Distance: " followed by the total value to two decimal places
# accept three integer inputs

print("Enter the number of days Employee A travels to job:")
Employee_A = int(input())

print("Enter the number of days Employee B travels to job:")
Employee_B = int(input())

print("Enter the number of days Employee C travels to job:")
Employee_C = int(input())

# calculate total distance
total_miles_traveled = (
    (Employee_A * 15.62) + (Employee_B * 41.85) + (Employee_C * 32.67)
)

# output combined mileage

print(f"Distance: {total_miles_traveled:.2f} miles")
