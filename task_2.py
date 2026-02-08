import random
def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    if min_num < 1 or max_num > 1000:
        return []

    if quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)