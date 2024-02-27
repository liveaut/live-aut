from genie.testbed import load
import cmd,sys

class LautShell(cmd.Cmd):
    intro = 'LAUT started'
    prompt = '% '
    file = None

    def do_execute(self, arg):
        print("execute")

'''
Testbed load
'''
testbed_file = input("Enter testbed file path: ")
testbed = load(testbed_file)

'''
Device connection
'''
if len(testbed.devices.keys()) == 0:
    sys.exit()

for device in testbed.devices.keys():
    dev = testbed.devices[device]
    dev.connect()

'''
Start LAUT shell
'''
LautShell().cmdloop()
