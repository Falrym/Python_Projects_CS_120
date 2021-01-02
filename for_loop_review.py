# numbers = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
# number = "Number"
# square = "Square"
# print(f"{number}{square:>7}")
# print("-------------")
# for n,s in numbers.items():
#     print(f"{n:3}{s:8}")

# conversions = {60:37.3,70:43.4,80:49.7,90:55.9,100:62.1,110:68.4,120:74.6}
# kph = "KPH"
# mph = "MPH"
# print(f"{kph}{mph:>7}")
# print("-----------")
# for k,m in conversions.items():
#     print(f"{k:3}{m:7}")

hours = []
count = 6
for i in range(count):
    WeeklyHours = float(input(f"\nEnter the hours worked by employee {i+1}\n>>"))
    hours.append(WeeklyHours)
payrate = float(input("Enter the hourly rate\n>> "))
for i,v in enumerate(hours):
    print(f"Gross pay for employee {i+1} is ${v * payrate}")


