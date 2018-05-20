


def main():
   data = open("usepass.txt", "r")
   dictdata = {}
   for line in data:
      line = line.replace(":"," ")
      line = line.split()
      dictdata[line[0]] = line[1]

   user = input("Enter username: ")
   passw = input("Enter password: ")
   if dictdata[user] == passw:
      print ("Success")
   else:
      print ("Error")

main()