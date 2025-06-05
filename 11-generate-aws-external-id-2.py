#!/usr/bin/env python3

# Generate an AWS external ID for IAM roles (UUID uuid) 
# External IDs are often used to prevent the "confused deputy" problem when setting up trust relationships between AWS accounts.

import uuid
print(str(uuid.uuid4()))
# Example: '550e8400-e29b-41d4-a716-446655440000'
