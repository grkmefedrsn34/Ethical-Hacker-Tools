import scapy.all as scapy
import optparse as opt

# 1-) ARP Table Request
# 2-) Broadcast
# 3-) ARP Table Response

def user_get_input():
    object = opt.OptionParser()
    object.add_option("-t", "--target", dest="target" ,help="Target IP / IP range")

    (user_input, arguments) = object.parse_args()

    if not user_input.target:
        object.error("[-] Please specify an IP / IP range, use --help for more info.")

    return user_input.target

def scan_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)

    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packet = broadcast_packet / arp_request_packet

    (answer_list , unanswer_list) = scapy.srp(combined_packet, timeout=1)
    answer_list.summary()



user_ip = user_get_input()
scan_network(user_ip.target)