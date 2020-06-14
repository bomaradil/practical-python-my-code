# bounce.py
#
# Exercise 1.5
bounce = 1

#first methode using while

height = 100

while bounce < 11 :
    height = (height * 3) / 5
    print(round(height, 4))
    bounce = bounce + 1

print("\n####################\n")
#seconde methode using for and range

h = 100

for b in range(1,11):
    h = (h * 3) / 5
    print(round(h, 4))