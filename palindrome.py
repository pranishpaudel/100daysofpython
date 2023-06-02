def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Compare the original and reversed strings
    if num_str == reversed_str:
        return True
    else:
        return False

# Example usage
number = 12321
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
