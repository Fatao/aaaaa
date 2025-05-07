import re

def is_leap_year(year):
    """Проверка на високосный год"""
    year = int(year)
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

def is_valid_date(day, month, year):
    """Проверка корректности даты"""
    day, month, year = int(day), int(month), int(year)
    
    # Проверка месяца
    if month < 1 or month > 12:
        return False
    
    # Проверка дня
    max_days = 31
    if month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        max_days = 29 if is_leap_year(year) else 28
    
    if day < 1 or day > max_days:
        return False
    
    return True

def extract_and_filter_dates(text):
    # Регулярные выражения
    pattern_ddmmyyyy = r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b'
    pattern_yyyymmdd = r'\b(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])\b'
    
    # Находим все совпадения
    dates_ddmmyyyy = re.findall(pattern_ddmmyyyy, text)
    dates_yyyymmdd = re.findall(pattern_yyyymmdd, text)
    
    valid_dates = []
    
    # Проверяем даты в формате DD.MM.YYYY
    for day, month, year in dates_ddmmyyyy:
        if is_valid_date(day, month, year):
            valid_dates.append(f"{day}.{month}.{year}")
    
    # Проверяем даты в формате YYYY-MM-DD
    for year, month, day in dates_yyyymmdd:
        if is_valid_date(day, month, year):
            valid_dates.append(f"{year}-{month}-{day}")
    
    return valid_dates if valid_dates else ["-1"]

if __name__ == "__main__":
    text = input("Введите текст с датами (в одной строке): ")
    result = extract_and_filter_dates(text)
    print("\nНайденные корректные даты:")
    for date in result:
        print(date)
