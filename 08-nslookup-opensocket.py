#!/usr/bin/env python3

# pip install dnspython

import socket
import dns.resolver

# Lambda function to perform NSLOOKUP for a website
nslookup = lambda website: dns.resolver.resolve(website, 'A')

# Lambda function to try opening a socket connection to a website
open_socket = lambda ip_address, port: socket.create_connection((ip_address, port), timeout=5)

def main(website, port=80):
    try:
        # Perform NSLOOKUP to get IP address
        answers = nslookup(website)
        ip_address = answers[0].to_text()
        print(f"nslookup answer: {answers}")
        print(f"{website} resolves to {ip_address}")

        # Open socket connection
        sock = open_socket(ip_address, port)
        print(f"Successfully opened socket connection to {website} on port {port}")
        sock.close()
    except Exception as e:
        print(f"Failed to open socket connection to {website} on port {port}: {e}")

# Example usage:
# Replace 'example.com' with the website you want to perform NSLOOKUP and socket connection to
# Replace 80 with the port you want to try opening the socket connection to
main('example.com', 80)


