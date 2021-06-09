def inch_to_sm():
  dm = int(input("Enter a value: "))
  sm = dm * 2.54
  return f'{dm} dm is {sm} sm'

print(inch_to_sm())


def sm_to_dm():
  sm = int(input("Enter a value: "))
  dm = sm / 2.54
  return f'{sm} sm is {dm} dm'

print(sm_to_dm())


def miles_to_km():
  miles = int(input("Enter a value: "))
  km = miles * 1.6
  return f'{miles} miles is {km} km'

print(miles_to_km())


def km_to_miles():
  km = int(input("Enter a value: "))
  miles = km / 1.6
  return f'{km} km is {miles} miles'

print(km_to_miles())


def f_to_kg():
  f = int(input("Enter a value: "))
  kg = f * 0.45
  return f'{f} f is {kg} kg'

print(f_to_kg())


def kg_to_f():
  kg = int(input("Enter a value: "))
  f = kg / 0.45
  return f'{kg} kg is {f} f'

print(kg_to_f())


def un_to_g():
  un = int(input("Enter a value: "))
  g = un * 28.3
  return f'{un} un is {g} g'

print(un_to_g())


def g_to_un():
  g = int(input("Enter a value: "))
  un = g / 28.3
  return f'{g} g is {un} un'

print(g_to_un())