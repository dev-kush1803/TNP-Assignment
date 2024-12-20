#Exception Handlilng

# error
try: 

    file = open("example.txt",'a')
    import sys

except ZeroDivisionError as e: 

    print("Error: Cannot divide by zero") 

except ValueError as e: 

    print("Error: Invalid input. Please enter a valid number.")
except:
    print("ALL type of error")
else:
    try:
        user_input = int(input("Enter a number: ")) 

        result = 10 / user_input
        file.write(result)
    except TypeError as e:
        print(f"ERROR1 : {e}")
    except ValueError as e:
        print(f"ERROR : {e}")
finally:
    print("ALWAYS")

