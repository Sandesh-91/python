word=input("Enter the word to check palindrome: ")
reversed = word[::-1]
if word == reversed:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
    

