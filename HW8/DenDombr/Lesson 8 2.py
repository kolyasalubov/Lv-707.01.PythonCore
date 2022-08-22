import re
pattern_password = re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')

print(bool(pattern_password.match('absghk4D')))  # True
print(bool(pattern_password.match('abc123FF')))  # True
print(bool(pattern_password.match('123ABCac')))  # True
print(bool(pattern_password.match('abcFF123')))  # True
print()
print(bool(pattern_password.match('absghk4D $%#$')))  # False
print(bool(pattern_password.match('')))               # False
print(bool(pattern_password.match('bsghk4D')))        # False
print(bool(pattern_password.match('abc_aaFF')))       # False
print(bool(pattern_password.match('abcabcac')))       # False
print(bool(pattern_password.match('ABCDF!@##')))      # False