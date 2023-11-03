def get_generator():
    for i in range(100, 100000):
        arm_number = 0
        for y in str(i):
            arm_number += int(y) ** len(str(i))
        if i == arm_number:
            yield arm_number


generator = get_generator()

def get_something_numbers():
    return next(generator)


for i in range(8):
    print(get_something_numbers(), end=' ')
