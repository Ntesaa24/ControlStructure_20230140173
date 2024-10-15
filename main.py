#Program untuk mengevaluasi kinerja siswa berdasarkan  persentase 1 
def evaluate_perfomance(percentage):  #def untuk medefinisikan fungsi 
    if percentage >= 90:
        return("Excellent performance")
    elif percentage >= 80: 
        return("Very Good perfomance")
    elif percentage >= 70: 
        return("Good performance")
    elif percentage >= 60:
        return("Averange performance")
    else: 
        return("Needs Impovement")
    
def find_largest(num1, num2, num3): #mencari nilai terbesar dari sekumpulan data.
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3 #membandingkan ketiga angka dan mengembalikan nilai terbesar di antara mereka.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

largest = find_largest(number1, number2, number3)
print("The largest number is:", largest)

def fibonacci_series(n): # untuk mencetak deret Fibonacci hingga bilangan 10
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  

n = int(input("Enter the value of n: "))
fibonacci_series(n)

def print_odd_numbers(n):
    print("Odd numbers up to", n, "are:")
    for i in range(1, n + 1, 2):  
        print(i, end=" ")
    print()  

n = int(input("Enter the value of n: "))
print_odd_numbers(n)

def print_pattern(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

n = int(input("Enter the value of n: "))
print_pattern(n)