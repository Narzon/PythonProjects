class Person:

   population = 0

   def __init__(self, name):
      self.name = name
      print ('(Initializing {})'.format(self.name))
      Person.population += 1
        
   def leave(self):
      print ('{} says bye.'.format(self.name))

      if Person.population == 0:
         print ('The room is already empty.')
      elif Person.population == 1:
         Person.population -= 1
         print ('I was the last one.')         
      else:
         Person.population -= 1
         print ('There are still {} people left.'.format(Person.population))

   def greet(self):
      print ('Hi, my name is {}.'.format(self.name))

   def howMany(self):
      if Person.population == 1:
         print ('I am the only person here.')
      else:
         print ('We have {} people here.'.format(Person.population))

def main():
   Obama = Person("Obama")
   Bill = Person("Bill")
   Person.howMany(Obama)
   Bill.howMany()
   Obama.greet()
   Bill.greet()
   Obama.leave()


main()