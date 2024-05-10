#!/usr/bin/env python3

# Similar to 08-nslookup-opensocket.py but make it AWS lambda friendly
# pip install dnspython

import socket
import dns.resolver

def lambda_handler(event, context):
    try:
        website = event['website']
        port = event.get('port', 80)
        
        # Lambda function to perform NSLOOKUP for a website
        nslookup = lambda website: dns.resolver.resolve(website, 'A')
        
        # Lambda function to try opening a socket connection to a website
        open_socket = lambda ip_address, port: socket.create_connection((ip_address, port), timeout=5)

        # Perform NSLOOKUP to get IP address
        answers = nslookup(website)
        ip_address = answers[0].to_text()

        # Open socket connection
        sock = open_socket(ip_address, port)
        print(f"Successfully opened socket connection to {website} on port {port}")
        sock.close()
        return {
            'statusCode': 200,
            'body': f"Successfully opened socket connection to {website} on port {port}"
        }
    except Exception as e:
        error_message = f"Failed to open socket connection to {website} on port {port}: {e}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': error_message
        }

