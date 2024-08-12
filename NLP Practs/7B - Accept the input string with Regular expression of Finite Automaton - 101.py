def FA(s):
    if len(s) < 3:
        return "Rejected (String too short)"
    
    if s[0] == '1' and s[1] == '0' and s[2] == '1':
        for i in range(3, len(s)):
            if s[i] != '1':
                return "Rejected (Not 101 followed by 1s)"
            return "Accepted (Matches 101+)"
    else:
        return "Rejected (Doesn't start with 101)"

inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111']
for i in inputs:
    print(FA(i))