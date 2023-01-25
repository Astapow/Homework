atm = int(input("Enter the desired amount: "))
rest = atm


result = ""
UAH1000 = 0
UAH500 = 0
UAH200 = 0
UAH100 = 0
UAH50 = 0
UAH20 = 0
UAH10 = 0


if rest - 1000 >= 0:
    while True:
        rest = rest - 1000
        if rest >= 0:
            UAH1000 = UAH1000 + 1
        else:
            rest = rest + 1000
            break
if rest - 500 >= 0:
    while True:
        rest = rest - 500
        if rest >= 0:
            UAH500 = UAH500 + 1
        else:
            rest = rest + 500
            break
if rest - 200 >= 0:
    while True:
        rest = rest - 200
        if rest >= 0:
            UAH200 = UAH200 + 1
        else:
            rest = rest + 200
            break
if rest - 100 >= 0:
    while True:
        rest = rest - 100
        if rest >= 0:
            UAH100 = UAH100 + 1
        else:
            rest = rest + 100
            break
if rest - 50 >= 0:
    while True:
        rest = rest - 50
        if rest >= 0:
            UAH50 = UAH50 + 1
        else:
            rest = rest + 50
            break
if rest - 20 >= 0:
    while True:
        rest = rest - 20
        if rest >= 0:
            UAH20 = UAH20 + 1
        else:
            rest = rest + 20
            break
if rest - 10 >= 0:
    while True:
        rest = rest - 10
        if rest >= 0:
            UAH10 = UAH10 + 1
        else:
            rest = rest + 10
            break
    result = f"{UAH1000}*1000 {UAH500}*500 {UAH200}*200 {UAH100}*100 {UAH50}*50 {UAH20}*20 {UAH10}*10"


print(result)