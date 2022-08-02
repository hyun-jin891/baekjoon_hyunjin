password = [0]
string = input()

for s in string:
    password.append(int(s))

dp = [0] * (len(password))
dp[0] = 1
dp[1] = 1

for i in range(2, len(password)):
    if password[i] < 0:
        dp[-1] = 0
        break
    if password[i] == 0:
        if password[i - 1] == 0:
            dp[-1] = 0
            break
        if password[i - 1] == 1 or password[i - 1] == 2:
            dp[i] = dp[i - 2] % 1000000
            continue
        else:
            dp[i] = 0
            break
        
    if password[i - 1] == 1:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
    elif password[i - 1] == 2:
        if password[i] <= 6:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
        else:
            dp[i] = dp[i - 1] % 1000000
    else:
        dp[i] = dp[i - 1] % 1000000


if string[0] == "0":
    print(0)
else:        
    print(dp[-1])