def palindrome(word):
    if len(word) < 2: 
        return True
    if word[0] != word[-1]: 
        return False
    return palindrome(word[1:-1])

a = input('Enter Input : ')
if palindrome(a):
    print("'"+a+ "'" +  ' is palindrome')
else:
    print("'"+a+ "'" + ' is not palindrome')