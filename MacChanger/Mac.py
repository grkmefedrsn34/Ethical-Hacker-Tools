import subprocess as sub
import optparse as op


object = op.OptionParser()
object.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
object.add_option("-m", "--mac", dest="mac_address", help="New MAC address")

(options, arguments) = object.parse_args()

print(object.parse_args())

print("Mac Changer is running...")
print("MAC address changer is a tool that allows you to change the MAC address of your network interface. This can be useful for privacy, security, or testing purposes.")

'''
print("Changing MAC address of " + options.interface + " to " + options.mac_address)

interface = options.interface
mac_address = options.mac_address

sub.call(["ifconfig", interface, "down"])
sub.call(["ifconfig", interface, "hw", "ether", mac_address])
sub.call(["ifconfig", interface, "up"])
'''