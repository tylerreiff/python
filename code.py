import os
import csv

# Function to validate if the path is valid or not. 
def validate(path):
	return os.path.isdir(path) 

def main():

	directory = input("Enter the path of the directory where you want to add the file: ")
	filename = input("Enter the name of the file you want to add: ")

	print()

	if not validate(directory):
		print("Invalid directory.")
		exit()
	else:
		filepath = directory + "\\"+ filename

	name = input("Enter your name: ")
	address = input("Enter your address: ")
	phone = input("Enter your phone number: ")



	with open(filepath, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(['Name', 'Address', 'Phone Number'])
		csvwriter.writerow([name, address, phone])


main()
