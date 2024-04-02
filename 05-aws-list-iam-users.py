import boto3

def list_iam_users():
    # Create IAM client
    iam = boto3.client('iam')
    
    # List IAM users
    response = iam.list_users()
    
    # Print IAM users
    print("IAM Users:")
    for user in response['Users']:
        print(f"Username: {user['UserName']}, UserID: {user['UserId']}")

if __name__ == "__main__":
    list_iam_users()

