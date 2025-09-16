import boto3
import csv
from datetime import datetime, timedelta
from botocore.exceptions import BotoCoreError, ClientError

# ==============================
# Configuration
# ==============================
# Number of past days to fetch
DAYS_BACK = 30
# Output CSV filename
OUTPUT_CSV = "ebs_cost_by_type.csv"
# AWS Cost Explorer client
ce = boto3.client('ce')

def get_ebs_costs(days_back=30):
    """Fetch EBS cost data grouped by volume type."""
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days_back)

    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost'],
            Filter={
                'Dimensions': {
                    'Key': 'SERVICE',
                    'Values': ['Amazon Elastic Block Store']
                }
            },
            GroupBy=[
                {"Type": "DIMENSION", "Key": "USAGE_TYPE"}
            ]
        )
        return response['ResultsByTime']
    except (BotoCoreError, ClientError) as e:
        print(f"Error fetching cost data: {e}")
        return None


def process_results(results):
    """Summarize results by EBS volume type."""
    summary = {}

    for day in results:
        for group in day['Groups']:
            usage_type = group['Keys'][0]  # e.g., 'EBS:VolumeUsage.gp2'
            amount = float(group['Metrics']['UnblendedCost']['Amount'])

            # Extract just the volume type, e.g., 'gp2' from 'EBS:VolumeUsage.gp2'
            if "VolumeUsage" in usage_type:
                volume_type = usage_type.split('.')[-1]
            else:
                volume_type = usage_type

            summary[volume_type] = summary.get(volume_type, 0.0) + amount

    return summary


def save_to_csv(data, filename):
    """Save summarized data to a CSV file."""
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Volume Type", "Total Cost (USD)"])
        for volume_type, cost in sorted(data.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([volume_type, f"{cost:.2f}"])
    print(f"Data saved to {filename}")


def main():
    print(f"Fetching EBS costs for the past {DAYS_BACK} days...")
    results = get_ebs_costs(DAYS_BACK)

    if not results:
        print("No data returned.")
        return

    summary = process_results(results)

    # Display summary
    print("\nEBS Cost Summary by Volume Type:")
    print("-" * 40)
    for volume_type, cost in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        print(f"{volume_type:<10} ${cost:,.2f}")

    # Save to CSV
    save_to_csv(summary, OUTPUT_CSV)


if __name__ == "__main__":
    main()

