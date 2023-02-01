def is_plusone_dictionary(d):
    total = 0
    before = 0
    for i in d.keys():
            total += 1 if d[i]-i == 1 and i - before == 1 else total == 2
            before = d[i] if d[i]-i == 1 and i - before == 1 else before == 0
    return True if total == len(d) else False