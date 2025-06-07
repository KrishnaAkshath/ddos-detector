
import time
import scapy.all as scapy

def detect_ddos(packet_counts, threshold=100):
    for ip, count in packet_counts.items():
        if count > threshold:
            print(f"⚠️ Possible DDoS attack detected from IP: {ip} with {count} packets")

def sniff_packets(interface="eth0", duration=10):
    print("[*] Sniffing packets...")
    packet_counts = {}
    start_time = time.time()

    def process_packet(packet):
        if packet.haslayer(scapy.IP):
            src_ip = packet[scapy.IP].src
            packet_counts[src_ip] = packet_counts.get(src_ip, 0) + 1

    scapy.sniff(iface=interface, prn=process_packet, timeout=duration, store=False)
    detect_ddos(packet_counts)

if __name__ == "__main__":
    sniff_packets()
