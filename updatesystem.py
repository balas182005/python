#This program is to update the system with latest updates

import commands
output = commands.getoutput('sudo apt-get update')
print output
