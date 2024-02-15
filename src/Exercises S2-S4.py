# SESSION 2, EXERCISES 1-3

# EXERCISE 1
def exercise_s2_1():
  print("This program illustrates a chaotic function")
  X = eval(input("Enter a number between 0 and 1 "))
  for i in range(20):
    X = 3.9 * X * (1 - X)
    print(round(X,2))

exercise_s2_1()

# EXERCISE 2
def exercise_s2_2():
  print("This program illustrates a chaotic function")
  n = eval(input("How many numbers should I print? "))
  X = eval(input("Enter a number between 0 and 1 "))
  for i in range(n):
    X = 3.9 * X * (1 - X)
    print(round(X,2))

exercise_s2_2()

# EXERCISE 3
def exercise_s2_3():
  print("This program illustrates a chaotic function")
  X = eval(input("Enter a number between 0 and 1: "))
  Y = eval(input("Enter a number between 0 and 1: "))
  n = eval(input("How many numbers should I print?: "))
  for i in range(n):
    X = 3.9 * X * (1 - X)
    Y = 3.9 * Y * (1-Y)
    rounded_X = round(X,2)
    rounded_Y = round(Y,2)
    print(rounded_X,"\t",rounded_Y)

exercise_s2_3()


# SESSION 3, EXERCISES 1-7

# EXERCISE 1 AND 2
def exerciseS3_12():
  print("This is a program that transforms Celsius degrees into Fahrenheit degrees")

  for i in range(5):
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")

exerciseS3_12()

# EXERCISE 3
def exerciseS3_3():
  print("This is a program that transforms Celsius degrees into Fahrenheit degrees")

  for celsius in range(0,101,10):
    fahrenheit = (9/5) * celsius + 32
    print("Temperature in Celsius ",celsius,"\t","Temperature in Fahrenheit ", fahrenheit)

exerciseS3_3()

# EXERCISE 4
def exerciseS3_4():
    print("This program calculates the future value of your investment depending on the years you hold it.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years of your investment: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print ("The value in", years, "years is ", round(principal,2))

exerciseS3_4()

# EXERCISE 5
def exerciseS3_5():
    print("This program calculates the future value of a fixed amount invested every year depending on the years holded.")

    annual_investment = float(input("Enter your annual investment: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years of your investment: "))
    future = 0


    for i in range(years,0,-1):
        annual_investment = annual_investment * (1 + apr)
        future = future + annual_investment

    print ("The value of your annual investment in", years, "years is ", round(future,2))

exerciseS3_5()

# EXERCISE 6
def exerciseS3_6():
  print("This is a program that converts Fahrenheit degrees into Celsius")

  fahrenheit = float(input("What is the temperature in Fahrenheit?: "))
  Celsius = fahrenheit/(9/5) - 32/(9/5)
  print("Celsius temperature is: ", round(Celsius,1))

exerciseS3_6()

# EXERCISE 7
def exerciseS3_7():
  print("This is a program that transforms distance in Kilometers into distances in Miles")
  km = float(input("What is the distance in KM? "))
  miles = km * 0.62

  print("The distance in miles is ", round(miles,2))

exerciseS3_7()


# SESSION 4, EXERCISES 1-6

# EXERCISE 1
def exerciseS4_1():
  print("This program calculates the Volume and Area of a sphere when its radius is known")
  r = float(input("What is the radius of the sphere? "))
  pi = 3.14159
  V = (4/3) * pi * r**3
  A = 4 * pi * r**2

  print("The Volume of the sphere is ", round(V,2), "and the Area is", round(A,2))

exerciseS4_1()

# EXERCISE 1 WITH MATH LIBRARY
# You can also do it importing the math library.
import math
def exerciseS4_1():
  print("This program calculates the Volume and Area of a sphere when its radius is known")
  r = float(input("What is the radius of the sphere? "))
  V = (4/3) * math.pi * r**3
  A = 4 * math.pi * r**2

  print("The Volume of the sphere is ", round(V,2), "and the Area is", round(A,2))

exerciseS4_1()

# EXERCISE 2
def exerciseS4_2():
  print("This program calculates the cost per square inch of a circular pizza knowing its diameter and price")

  diam = float(input("What is the diameter of the pizza? "))
  p = float(input("What is the price of the pizza? "))
  pi = 3.14159    # --> You can also use math.pi instead of defining the pi variable yourself.
  r = diam/2
  a = pi * r**2
  cost_per_inch = p/a

  print("The cost per square inch of this pizza is: ", round(cost_per_inch,2))

exerciseS4_2()

# EXERCISE 3
def exerciseS4_3():
  print("This is a program that finds the sum of the first natural numbers of the number that you enter")

  n = int(input("Enter the numbers whose sum you want to find: "))
  fact = 1

  for factor in range(n,1,-1):
    fact = fact + factor

  print("The sum of the first",n,"natural numbers is", fact)

exerciseS4_3()

# EXERCISE 4
def exerciseS4_4():
  print("This is a program that finds the sum of the cubes of the numbers you enter")

  n = int(input("Enter a number: "))
  f = 0

  for i in range(1,n+1):
    cube = i**3
    f = f + cube

  print("The sum of the cubes of the first",n, "natural numbers is", f)

exerciseS4_4()

# EXERCISE 5
def exerciseS4_5():
  print("This is a program that finds the sum of the numbers you enter")

  n = int(input("How many numbers do you want to sum: "))
  sum = 0

  for i in range(1,n+1):
    d = int(input("Enter the numbers you want to sum: "))
    sum = sum + d

  print("The sum of the numbers entered is ", sum)

exerciseS4_5()

# EXERCISE 6
def exerciseS4_6():
  print("This is a program that finds the average of the numbers you enter")

  n = int(input("How many numbers do you want to sum: "))
  sum = 0


  for i in range(1,n+1):
    d = int(input("Enter the numbers whose average you want to know: "))
    sum = (sum + d)
    final = sum / n

  print("The average of the numbers you have summed up is ", final)

exerciseS4_6()

# EXERCISE 7
def exerciseS4_7():
  import random
  print("This program finds the sum of the first n natural integer random numbers from 1 to 10")

  n = int(input("Enter the number whose sum you want to find: "))
  fact = 0

  for i in range(1,n+1):
    r = random.randrange(1,10+1)
    print(r)
    fact = fact + r

  print("The solution for this exercise is ", fact)

exerciseS4_7()

# EXERCISE 8
def exerciseS4_8():
  import random
  print("This program finds the sum of the first n natural float random numbers from 1 to 10")

  n = int(input("Enter the float number whose sum you want to find: "))
  fact = 0

  for i in range(1, n + 1):
    r = random.random()
    print(r)
    fact = fact + r

  print("The solution for this exercise is ", fact)

exerciseS4_8()