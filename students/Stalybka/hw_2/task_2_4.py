"""Создать строку равную введенной строку без последних двух символов."""

your_str = input()
new_str = your_str[0:len(your_str)-2]
print(new_str)