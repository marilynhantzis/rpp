def calculate_discriminant(a, b, c):  # Функция для расчета дискриминанта
    return b**2 - 4*a*c  

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))  
c = float(input("Введите коэффициент c: "))  
discriminant = calculate_discriminant(a, b, c)  
print(f"Дискриминант: {discriminant}")  
