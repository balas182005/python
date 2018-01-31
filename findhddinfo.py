#program to find hdd information on the machine

import commands
output = commands.getoutput('lsblk')
print output
