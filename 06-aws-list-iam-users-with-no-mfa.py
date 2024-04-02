import boto3

def list_iam_users_without_mfa():
    # Create IAM client
    iam = boto3.client('iam')
    
    # List IAM users
    response = iam.list_users()
    
    # Print IAM users without MFA
    print("IAM Users without MFA enabled:")
    for user in response['Users']:
        mfa_devices = iam.list_mfa_devices(UserName=user['UserName'])
        if not mfa_devices['MFADevices']:
            print(f"Username: {user['UserName']}, UserID: {user['UserId']}")

if __name__ == "__main__":
    list_iam_users_without_mfa()
