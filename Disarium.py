def disarium():
    for i in range (1, 100):
        arr = [int(num) for num in str(i)]
        sum = 0
        for j, n in enumerate (arr):
            sum = sum + n ** (j+1)
        if sum == int (i):
            print (sum)

# print("Srineeta  1MJ19CS163")
disarium()