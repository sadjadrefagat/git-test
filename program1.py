# محاسبه مقسوم علیه ها
n = int(input("Enter n: "))
for i in range(1, n+1):
    if n % i == 0:
        s = 1
        print(i, end=" ")
