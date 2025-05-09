import sys

for line in sys.stdin:
    line = line.strip()

    # Rule 1: Contains a dot
    if '.' in line:
        print(line)
        continue

    # Rule 2: Two or more spaces
    if line.count(' ') >= 2:
        print(line)
        continue

    # Rule 3: Surname starts with D/d and salary > 60000
    parts = line.split(';')
    if len(parts) == 4:
        surname = parts[0]
        try:
            salary = int(parts[3])
            if surname.lower().startswith('d') and salary > 60000:
                print(line)
        except ValueError:
            pass
