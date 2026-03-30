def if_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number"
    else:
        return f"{number} is an odd number"
    
def main():
    try:
        user_input = int(input("Enter a number: "))
        print(if_even_or_odd(user_input))
    except ValueError:
        print("Invalid. Enter a valid number")

if __name__ == "__main__":  main()
