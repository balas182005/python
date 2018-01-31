#program to find the primary user of the machine

import commands
output = commands.getoutput('cat /etc/amazon/50primary_user.json')
print output
