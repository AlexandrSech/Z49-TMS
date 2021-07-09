import csv

FILENAME = "users.csv"
 
users = [
    ["Tim", "Benington", 19],
    ["Andrey", "Benington", 43],
    ["Bob", "Benington", 34],
    ["Mary", "Benington", 10],
    ["Sergey", "Benington", 5],
    ["Paul", "Benington", 16],
    ["Sally", "Benington", 18],
    ["Tom", "Benington", 46],
]
 
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
     
 
with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, "a", newline="") as file:
    user = ["Alina", 22]
    writer = csv.writer(file)
    writer.writerow(user)