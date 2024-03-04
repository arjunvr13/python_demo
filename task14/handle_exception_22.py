try:
    n1 = int(input("Enter the number:"))
    n2 = int(input("Enter the number:"))
    if n2 == 0:
        raise ZeroDivisionError
    
    elif isinstance(n1,int) and isinstance(n2,int):
        div = n1 / n2
        print(div)

    else:
        raise ValueError
except ZeroDivisionError:
    print("Second Number Should Not Be Zero division by zero is not possible")
except ValueError:
    print("Pls Input Integer Only invalid literal for int() with base 10: {n2}")
except Exception as e:
    print(e)