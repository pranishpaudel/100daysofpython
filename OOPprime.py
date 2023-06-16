class Number:
    def __init__(self, value):
        self.value = value

    def is_prime(self):
        if self.value < 2:
            return False

        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def is_composite(self):
        return not self.is_prime()


# Example usage
number1 = Number(7)
print(number1.is_prime())      # Output: True
print(number1.is_composite())  # Output: False

number2 = Number(12)
print(number2.is_prime())      # Output: False
print(number2.is_composite())  # Output: True
