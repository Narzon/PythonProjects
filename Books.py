#  File: Books.py

#  Description: Given two books in .txt format, print the numbers of words in each book, the numbers of unique words in each book, the ratios of unique-to-total words for each book, and compare unique word usage between both books

#  Student Name: Nicolai Antonov

#  Student UT EID: naa766

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: April 26, 2016

#  Date Last Modified: April 26, 2016

#Using the file words.txt, create a dictionary word_dict of comprehensive words (with each value set to 1)
word_dict = {}
def create_word_dict ():
	words = open("words.txt", "r")
	for line in words:
		line = line.strip()
		word_dict["%s" % line] = 1

#Create the function parseString so that given a string st, all characters which are not letters or spaces are replaced with a space, and only apostrophes(') which are followed by a non-s letter are kept
def parseString (st):

#Initilize the new string s
	s = ""

#For each character in st, check the above conditions and either add the character to s, add nothing, or add a space
	for i in range(0, len(st)):
		if st[i].isalpha() or st[i].isspace():
			s += st[i]
		elif st[i] == "'":
			if i != len(st) - 1:
				if st[i + 1] == "s" or " ":
					st += ""
				else:
					st += "'"
			else:
				st += ""
		else:
			s += " "

#Return the new string s
	return s

#Create the function getWordFreq so that given a text file, a dictionary of all common words in lowercase letters is returned along with values representing frequency of those words
def getWordFreq (file):

#Populate word_dict from words.txt
	create_word_dict()

#Open the file and assign it to variable book, then initialize dictionary book_dict
	book = open("%s" % file, "r")
	book_dict = {}

#Go through the book line by line, parsing it with function parseString, and populating book_dict with words and their frequency. Afterwards, close each book
	for line in book:
		line = line.strip()
		line = parseString(line)
		word_list = line.split()
		for word in word_list:
			if word in book_dict:
				book_dict[word] += 1
			else:
				book_dict[word] = 1
	book.close()

#Create a new list capital_letters, then create list all_words from the values of dictionary book_dict
	capital_letters = []
	all_words = list(book_dict.keys())

#Population capital_letters with all words that begin with a capital letter from list all_words
	for word in all_words:
		if word.istitle():
			capital_letters.append(word)

#For every word in capital_letters, check if the lowercase version of the word exists in book_dict and modify the frequency if it does
	for word in capital_letters:
		if word.lower() in book_dict:
			book_dict[word.lower()] += book_dict[word]

#If the word does not appear in book_dict, check if it appears in word_dict, and if so create a new key and appropriate value in book_dict
		elif word.lower() in word_dict:
			book_dict[word.lower()] = book_dict[word]

#Remove all entries for words starting with capital letters from book_dict, then return book_dict
	for word in capital_letters:
		if word in book_dict:
			del book_dict[word]
	return book_dict

#Initialize main, which will take inputs, compare the books, and print results
def main():

#Prompt user to enter name of text file for the first and second book, and then to enter the author for each
	book1 = input("Enter name of first book: ")
	book2 = input("Enter name of second book: ")
	print()

	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print()

#Create two separate dictionaries of common words wordFreq1 and wordFreq2 from function getWordFreq
	wordFreq1 = (getWordFreq (book1))
	wordFreq2 = (getWordFreq (book2))

#For each book and author, print the total number of unique words, the total number of words, and the percentage ratio of unique to total words
	print(author1)
	print("Total distinct words = %s" % len(wordFreq1))
	print("Total words (including duplicates) = %s" % sum(wordFreq1.values()))
	print("Ratio (%% of total distinct words to total words) = %.10f" % ((len(wordFreq1) / sum(wordFreq1.values())) * 100))
	print()
	print(author2)
	print("Total distinct words = %s" % len(wordFreq2))
	print("Total words (including duplicates) = %s" % sum(wordFreq2.values()))
	print("Ratio (%% of total distinct words to total words) = %.10f" % ((len(wordFreq2) / sum(wordFreq2.values())) * 100))

#Create sets D and H from the keys in the dictionaries for each book
	D = set(wordFreq1.keys())
	H = set(wordFreq2.keys())

#Create variables Rel_Freq1 and Rel_Freq2 for the frequency of words that each author uses which the other does not
	Rel_Freq1 = 0
	for word in (D - H):
		if word in wordFreq1:
			Rel_Freq1 += wordFreq1[word]
	Rel_Freq2 = 0
	for word in (H - D):
		if word in wordFreq2:
			Rel_Freq2 += wordFreq2[word]

#Print how many words each author used that the other did not, and the percentage ratio of the frequency of unique-to-author words to total words used by each author
	print()
	print("%s used %s words that %s did not use." % (author1, len(D - H), author2))
	print("Relative frequency of words used by %s not in common with %s = %.10f" % (author1, author2, ((Rel_Freq1) / sum(wordFreq1.values()) * 100)))

	print()
	print("%s used %s words that %s did not use." % (author2, len(H - D), author1))
	print("Relative frequency of words used by %s not in common with %s = %.10f" % (author2, author1, ((Rel_Freq2) / sum(wordFreq2.values()) * 100)))

main()
