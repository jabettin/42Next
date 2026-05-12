def helper(current, days):
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    helper(current + 1, days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(1, days)
