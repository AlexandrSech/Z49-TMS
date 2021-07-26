

# сделать функцию которая возвращает
# из входной строки палиндром

def get_pal(inp_str):
    inp_str = str(inp_str)
    n = 0
    while inp_str[n:] != inp_str[n:][::-1]:
        n += 1
    return inp_str + inp_str[:n][::-1]

