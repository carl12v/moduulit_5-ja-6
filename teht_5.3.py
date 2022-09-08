def get_int_input(prompt: str = 'Enter an integer number: ') -> int:
    number = -1
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print('Error: Enter an integer, try again...')
    return number

def is_prime(number: int) -> bool:
    """Checks if a number is a prime by division"""
    if number < 2:
        return False
    if number == 2:
        return True
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

def display_prime(prime_status: bool) -> None:
    """Displays a message if the number is prime or not"""
    if prime_status:
        print('The number is a prime.')
    else:
        print('The number is not a prime.')

def main() -> None:
    number = get_int_input()
    status = is_prime(number)
    display_prime(status)

if __name__ == '__main__':
    main()