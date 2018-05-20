def main():
	string = input("Enter string to see if it's a palindrome: ")
	if string[:len(string)//2] == string[len(string)//2:]:
		print("True")
main()