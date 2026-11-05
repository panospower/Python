import mpmath as mp

def digit_counter(num):
    text = str(num).lower().split('e')[0]

    digits = sum(1 for char in text if char.isdigit())

    print(digits)


number = input("Enter number:")

digit_counter(number)

# Convert it to an mpmath number for calculations
number = mp.mpf(number)