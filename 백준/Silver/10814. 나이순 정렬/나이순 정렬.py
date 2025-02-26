import sys

n = int(sys.stdin.readline().strip())

people = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    people.append((int(age),name))

sorted_people = sorted(people, key=lambda x:x[0])

for person in sorted_people:
    print(person[0],person[1])
