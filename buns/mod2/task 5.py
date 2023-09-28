user_minutes = int(input("Введите время в минутах: "))
user_hours = user_minutes // 60
user_left_minutes = user_minutes % 60
print("Время в часах:", user_hours, ", оставшиеся минуты:", user_left_minutes)
