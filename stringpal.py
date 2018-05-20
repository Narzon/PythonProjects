def main():
   string = str(input())
   count = 0
   for i in range(len(string) // 2):
      if string[i] == string [- (i + 1)]:
         count += 1
   if count == (len(string) // 2):
      print("Yes!")




main()