"""
list={100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
90, 89, 88, 87, 86, 85, 84, 83, 82, 81,
80, 79, 78, 77, 76, 75, 74, 73, 72, 71,
70, 69, 68, 67, 66, 65, 64, 63, 62, 61,
60, 59, 58, 57, 56, 55, 54, 53, 52, 51,
50, 49, 48, 47, 46, 45, 44, 43, 42, 41,
40, 39, 38, 37, 36, 35, 34, 33, 31, 31,
30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
10,  9,  8,  7,  6,  5,  4,  3,  2,  1,
0}

def numbers(list):
    for i in range (101):
        while i>0:
            print (i, "Bottles of Root Beer on the wall,", i,
            "Bottles of Root Beer on the wall."
            "Take one down and pass it around"
            , i-1, "Bottles of Root Beer on the wall")

        #else:
        #    print (i, "Bottles of Root Beer on the wall,", i, " Bottles of Root Beer on the wall. Take one down and pass it around")
numbers(list)
"""
term=99
counter=0
for i in range(100):
    print(term, "Bottles of Root Beer on the wall,", term, " Bottles of Root Beer on the wall. Take one down and pass it around")
    term = term-1
    counter = +1
