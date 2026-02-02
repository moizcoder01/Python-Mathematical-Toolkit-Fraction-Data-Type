# Fraction DataType
class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def __str__(self):
        return '{}/{}'.format(self.num, self.den)
    
    def __add__(self, another):
        new_num = (self.num * another.den) + (another.num * self.den)
        new_den = self.den * another.den
        return '{}/{}'.format(new_num, new_den)
    
    def __sub__(self, another):
        new_num = (self.num * another.den) - (another.num * self.den)
        new_den = self.den * another.den
        return '{}/{}'.format(new_num, new_den)
    
    def __mul__(self, another):
        new_num = self.num * another.num
        new_den = self.den * another.den
        return '{}/{}'.format(new_num, new_den)
    
    def __truediv__(self, another):
        new_num = self.num * another.den
        new_den = self.den * another.num
        return '{}/{}'.format(new_num, new_den)

while True: 
    print("============CHOOSE OPERATION=============") 
    user_input = input("""
Enter 1 for Addition.
Enter 2 for Subtration.
Enter 3 for Multiplication.
Enter 4 for Division.
Enter 5 to Exit.
Select: """)
    
    if user_input == '5':
        print("Exiting.... Done")
        break

    elif user_input in ['1', '2', '3', '4', '5']:
        f1 = input("Enter first fraction (e.g: a/b): ")
        f2 = input("Enter second fraction (e.g: a/b): ")
        try: 
            n1,d1 = map(int, f1.split('/'))
            n2,d2 = map(int, f2.split('/'))

            if d1 == 0 or d2 == 0:
                print("ERROR: Denominator should not be zero")
                continue
            fr1 = Fraction(n1, d1)
            fr2 = Fraction(n2, d2)
        
        except (ValueError, IndexError):
            print("Invalid Input! Your input should be in the form of a/b")
            continue
        
        if user_input == '1':
            print("===========ADDITION==============")
            print(f"Addition: {fr1 + fr2}")

        elif user_input == '2':
            print("==========SUBTRACTION============")
            print(f"Subtraction: {fr1 - fr2}")
        
        elif user_input == '3':
            print("==========MULTIPLICATION============")
            print(f"Multiplication: {fr1 * fr2}")
        
        elif user_input == '4':
            print("==============DIVISION===============")
            print(f"Division: {fr1 / fr2}")
        
    else:
        print("Invalid Input")