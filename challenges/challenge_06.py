# Store two numeric values of your choice in variables, and if the sum is odd, print "ODD". If not, print "EVEN".
from utils.is_even import is_even

bignumber = 400000
smallnumber = 1

if is_even(bignumber + smallnumber):
    print('even')
else:
    print('odd')

# if (bignumber + smallnumber) % 2 == 0:
#     print('even')
# else:
#     print('odd')