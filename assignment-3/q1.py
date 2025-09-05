class DifferenceCalculator:
    def calculate(self, number):
        diff = number - 17
        if number > 17:
            return 2 * abs(diff)
        else:
            return abs(diff)


calculator = DifferenceCalculator()

num1 = 20
num2 = 10

print(f"Difference for {num1}:", calculator.calculate(num1))
print(f"Difference for {num2}:", calculator.calculate(num2))
