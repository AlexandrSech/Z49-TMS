# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова палиндромы.)

def palindrom(words: list):
  for word in words:
    if word == word[::-1]:
      print(f'{word} is palindrom')
    else:
      print(f'{word} is not palindrom')


palindrom(['ollo', 'course', 'maybe'])