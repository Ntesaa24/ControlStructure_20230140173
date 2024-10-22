def evaluate_performance(percentage): #membuat fungsi evaluate_performance dengan dengan kata kunci def
    if percentage >= 90:              #jika persentasi lebih dari sama dengan 90
        return "Excellent performance"  #maka akan tampil tulisan "Excellent performance"
    elif percentage >= 80:              #jika persentasi lebih dari sama dengan 80
        return "Very Good performance"  #maka akan tampil tulisan "Very Good performance"
    elif percentage >= 70:              #jika persentasi lebih dari sama dengan 70
        return "Good performance"       #maka akan tampil tulisan "Good performance"
    elif percentage >= 60:              #jika persentasi lebih dari sama dengan 60
        return "Average performance"    #maka akan tampil tulisan "Average performance"
    else:                               #jika persentasi kurang dari 60
        return "Below Average performance"  #maka akan tampil tulisan "Below Average performance"
    
student_percentage = float(input("Enter the student's percentage: "))  #menginput nilai siswa tersebut
performance = evaluate_performance(student_percentage)                 
print("The student's performance is:",performance)                      #menampilkan nilai siswa tersebut

def find_largest(num1, num2, num3):         #membuat fungsi find_largest dengan dengan kata kunci def          
    if num1 >= num2 and num1 >= num3:       #jika number1 lebih besar sama dengan number2 dan jika number1 lebih besar sama dengan number3
        return num1                         #maka yang akan muncul number1
    elif num2 >= num1 and num2 >= num3:     #jika number2 lebih besar sama dengan number1 dan jika number2 lebih besar sama dengan number3
        return num2                         #maka yang akan muncul number2
    else:                                   #jika number3 yang lebih besar
        return num3                         #maka yang akan muncul number3  
   
number1 = float(input("Enter the first number: "))  #masukkan angka pertama
number2 = float(input("Enter the second number: ")) #masukkan angka kedua
number3 = float(input("Enter the third number: "))  #masukkan angka ketiga 

largest = find_largest(number1, number2, number3)   #untuk mencari angka yang lebih besar(antara 1, 2, 3)
print("The largest number is:",largest)             #cetak angka yang paling besar

def fibonacci_series(n):            #membuat fungsi deret fibonacci_series dengan kata kunci def
    a, b = 0, 1
    while a <= n:                   #ketika a kurang dari sama dengan n
        print(a, end=" ")           #cetak 
        a, b = b, a + b             #a, b=b, a + b
    print()                         #untuk menampilkan garis baru

n = int(input("Enter the value of n: "))        #masukkan angka nya
fibonacci_series(n)                             #cetak

def print_odd_numbers(n):                       #membuat fungsi print_odd_numbers dengan kata kunci def
    print("Odd numbers up to", n, "are:")       #cetak "Odd numbers up to"
    for i in range(1, n + 1, 2):                #untuk i di antara(1, n + 1, 2)
        print(i, end=" ")                       #cetak(i dan angka ganjil )
    print()  

n = int(input("Enter the value of n: "))        #masukkan n - nya
print_odd_numbers(n)                            #tampilkan angka ganjil sebelum n - nya

def print_pattern(n):                           #untuk mencetak pola angka berdasarkan nilai n yang diinputkan pengguna
    for i in range(1, n + 1):
        print((str(i) + " ") * i)

n = int(input("Enter the value of n: "))
print_pattern(n)