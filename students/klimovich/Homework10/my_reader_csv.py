def my_reader(s: str, delimiter=';'):
    text = s.splitlines()
    result = []
    for i in range(len(text)):
        temp_var = text[i].split(delimiter)
        result.append(temp_var)
    return result