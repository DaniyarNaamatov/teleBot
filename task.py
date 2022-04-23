def rental_car(days):
    rental = days * 50
    if days >= 3 and days < 7:
        print(((rental * 100) - (rental * 10)) / 100, '10%')
    elif days >= 7:
        print(((rental * 100) - (rental * 30)) / 100, '30%')
    else:
        print(rental)

users = int(input())
rental_car(users)


def rental_car(days):
    return (days * 50) - (days * 50) * 10 / 100 if 7 > days > 3 else days * 50 if days < 7 else (days * 50) - (days * 50) * 30 / 100
print(rental_car(13))