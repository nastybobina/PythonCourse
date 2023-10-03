square_side = int(input("Введите длину стороны квадрата: "))
square_perimeter = square_side * 4
square_area = square_side ** 2
square_diagonal = round(square_side * (2 ** 0.5), 2)
print(square_perimeter, square_area, square_diagonal)