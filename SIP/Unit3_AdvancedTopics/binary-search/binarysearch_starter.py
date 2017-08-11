import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

#length = len(countries)
#print(countries[1])
#print(countries)

# Start your search algorithm here.
ans=input("What country are you looking for: ")
#def binarySearch(array, x):
length = len(array)
len2 = length-1
found = False
	while length < len2 and found == False:
		mid =((length+lenght) /2)
# Check if x is present at mid
		if array[mid] == x:
			found =True
			print(ans+ "is found in this list.")
		# If x is greater, ignore left half
		else:
			if array[mid] < x:
				len2 = mid - 1
				print (ans+ "is found in this list.")
			else :
				length = mid + 1
				print ("didnt find"+ans)

#binarySearch(countries, ans)
