import re

print("Введите текст (несколько строк). Для окончания введите пустую строку:")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

# Объединяем все строки в один текст
text = '\n'.join(lines)

# Ищем отдельно стоящее слово "я" с учетом регистра (можно добавить lower() при необходимости)
matches = re.findall(r'\b[Яя]\b', text)

# Выводим результат
print(len(matches))




