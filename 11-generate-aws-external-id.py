#!/usr/bin/env python3

# Generate an AWS external ID for IAM roles (UUID uuid) 
# External IDs are often used to prevent the "confused deputy" problem when setting up trust relationships between AWS accounts.

import secrets
import string

def generate_external_id(length=32):
    """
    Generate a secure, random external ID suitable for AWS IAM roles.
    
    Args:
        length (int): Length of the external ID string (default: 32).
    
    Returns:
        str: A securely generated external ID.
    """
    characters = string.ascii_letters + string.digits + '-_'
    external_id = ''.join(secrets.choice(characters) for _ in range(length))
    return external_id

if __name__ == "__main__":
    external_id = generate_external_id()
    print(f"Generated External ID: {external_id}")
