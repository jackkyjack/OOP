num = input().split()
num = list(map(int, num))
num.sort()
ans = 0
a = 1
cheak = False

for i in range(len(num)):
    if cheak == True :
        ans = ans*10 + num[i]
    else:
        if num[i] != 0 :
            ans = a * num[i]
            cheak = True
        else:
            a *= 10
print(ans)
