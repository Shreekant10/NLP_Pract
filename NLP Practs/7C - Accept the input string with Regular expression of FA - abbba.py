def FA(s):
    if not s:
        return "Rejected (Empty string)"
    for char in s:
        if char not in ('a', 'b'):
            return "Rejected (Contains characters other than 'a' and 'b')"
        
        if not s.endswith('bba'):
            return "Rejected (Doesn't end with 'bba')"
        return "Accepted (Matches (a+b)*bba)"

inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', '']
for i in inputs:
    print(FA(i))