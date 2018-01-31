#program to find users who have sudo permissions on the machine

import commands
output = commands.getoutput('sudo getent group sudo')
print output
