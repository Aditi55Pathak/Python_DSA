def reverse(strng):
    if strng is int:
        return int(strng[::-1])
    return strng[::-1]

print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'