def sum_two_numbers():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print(f"Sum =", first + second)

def square_area():
    side = float(input("Enter square side: "))
    print(f"Area =", side ** 2)

def average_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Average =", (a + b) / 2)

def compare_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Is first number less than or equal to second", a <= b)

if __name__ == "__main__":
    sum_two_numbers()
    square_area()
    average_two_numbers()
    compare_numbers()

