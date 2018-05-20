def main():
    iterations = eval(input("Number of interations: "))
    while iterations - int(iterations) != 0:
       iterations = eval(input("Number of interations: "))

    for i in range(1, iterations + 1):
        for j in range(1, i + 1):
           print("*", end = " ")
           if i == j:
              print()
    while (iterations > 0):
        for i in range(1, iterations):
           print("*", end = " ")
           if i == iterations - 1:
              print()
        iterations -= 1

main()