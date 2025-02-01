import socket
import struct

def send_wol(mac_address: str):
    mac_address = mac_address.replace("-", ":").replace(".", ":").lower()
    mac_bytes = bytes.fromhex(mac_address.replace(":", ""))
    if len(mac_bytes) != 6:
        raise ValueError("Invalid MAC address format")
    
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ('<broadcast>', 9))
    
    print(f"Magic packet sent to {mac_address}")

try:
    with open("mac_address.txt", "r") as file:
        mac_address = file.read().strip()
        send_wol(mac_address)
except FileNotFoundError:
    print("Error: mac_address.txt not found")
except Exception as e:
    print(f"Error: {e}")