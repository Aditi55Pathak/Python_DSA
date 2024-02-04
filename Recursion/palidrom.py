def isPalindrome(strng):
    if strng is int:
        return int(strng[::-1])
    return strng == strng[::-1]


print(isPalindrome("awesome"))  # false
print(isPalindrome("foobar"))  # false
print(isPalindrome("tacocat"))  # true
print(isPalindrome("amanaplanacanalpanama"))  # true
print(isPalindrome("amanaplanacanalpandemonium"))  # false
