nric = input('Enter an NRIC number: ')

# Type your code below
sum = 0
digit_weight = [2, 7, 6, 5, 4, 3, 2]
prefixes = ['S', 'T', 'F', 'G']
check_digit_ST = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
check_digit_FG = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
valid = False
if len(nric) == 9 and nric[0] in prefixes and nric[8].isalpha and nric[1:8].isdecimal:
    prefix, suffix, digits = nric[0], nric[8], nric[1:8]
    for i in range(7):
        sum += int(digits[i]) * digit_weight[i]
    if prefix in ['T', 'G']:
        sum += 4
    if prefix in ['S', 'T']:
        if suffix == check_digit_ST[sum % 11]:
            valid = True
    if prefix in ['F', 'G']:
        if suffix == check_digit_FG[sum % 11]:
            valid = True
if valid:
    print("NRIC is valid.")
else:
    print("NRIC is invalid.")