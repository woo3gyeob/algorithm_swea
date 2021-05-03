def perm(month, price):
    global min_price
    if price >= min_price:
        return
    if month >= 12:
        min_price = price
        return
    if plan[month] == 0: perm(month_togo[month], price)
    perm(month+1, price + daily*plan[month])
    perm(month+1, price + monthly)
    if month <= 9:
        perm(month+3, price + three_month)
    return


for tc in range(1, int(input()) + 1):
    daily, monthly, three_month, annually = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = annually
    month_togo = [0] * 12
    fill_month = 12
    for i in range(11,-1,-1):
        month_togo[i] = fill_month
        if plan[i] > 0:
            fill_month = i

    perm(0, 0)
    print('#%d %d' %(tc, min_price))