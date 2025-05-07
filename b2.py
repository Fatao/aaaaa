import re

def normalize_string(s):
    """Удаляет пунктуацию, приводит к нижнему регистру, нормализует пробелы."""
    s = re.sub(r'[^\w\s]', '', s)
    s = s.lower()
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def jaccard_similarity(s1, s2):
    """Вычисляет коэффициент Жаккара между двумя строками"""
    set1 = set(s1.split())
    set2 = set(s2.split())
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union) if union else 0.0

if __name__ == "__main__":
    print("Введите первую строку:")
    s1 = input("> ")
    print("Введите вторую строку:")
    s2 = input("> ")

    # Нормализация
    norm_s1 = normalize_string(s1)
    norm_s2 = normalize_string(s2)

    # Расчёт коэффициента Жаккара
    jaccard = jaccard_similarity(norm_s1, norm_s2)

    print(f"\nКоэффициент Жаккара: {jaccard:.6f}")
