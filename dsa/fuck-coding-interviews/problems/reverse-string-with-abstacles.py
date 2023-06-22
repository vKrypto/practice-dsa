# from turing tets.


# time complexity: o(n), space complexity: o(n)
def reverse_string(s):
    new_s = list(s)
    left, right = 0 , len(s)-1
    while left < right:
        skip = False
        left_ord = ord(s[left].lower())
        right_ord = ord(s[right].lower())
        if ord('a') >  left_ord or left_ord > ord('z'):
            skip = True
            new_s[left] = s[left]
            left += 1
        if ord('a') >  right_ord or right_ord > ord('z'):
            skip = True
            new_s[right] = s[right]
            right -= 1
            
        if not skip:
            new_s[left], new_s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(new_s)



tests = [
    'ab-cd',
    'j-lh-gfE=dCba!!'
]
for test in tests:
    print( test, ">>>>", reverse_string(test))