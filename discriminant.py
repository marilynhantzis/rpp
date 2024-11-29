def calculate_discriminant(a, b, c):  # Функция для расчета дискриминанта
    return b**2 - 4*a*c  

if __name__ == "__main__":  # Проверяем, является ли скрипт основным
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))  
    c = float(input("Введите коэффициент c: "))  
    discriminant = calculate_discriminant(a, b, c)  
    print(f"Дискриминант: {discriminant}")  

