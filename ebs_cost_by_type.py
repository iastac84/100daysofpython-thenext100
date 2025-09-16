import boto3
import csv
from datetime import datetime, timedelta
from botocore.exceptions import BotoCoreError, ClientError

# ==============================
# Configuration
# ==============================
DAYS_BACK = 30  # Look back window for cost analysis
OUTPUT_CSV = "ebs_storage_cost_by_type.csv"

# AWS Cost Explorer client
ce = boto3.client('ce')

# ==============================
# Fetch EBS Storage Costs
# ==============================
def get_ebs_storage_costs(days_back=30):
    """Fetch only EBS storage costs (gp2, gp3, etc.)"""
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
                "And": [
                    # Service must be Amazon EBS
                    {
                        'Dimensions': {
                            'Key': 'SERVICE',
                            'Values': ['Amazon Elastic Block Store']
                        }
                    },
                    # Only include volume usage costs (storage)
                    {
                        'Dimensions': {
                            'Key': 'USAGE_TYPE',
                            'Values': [
                                # gp2, gp3, io1, io2, st1, sc1
                                'EBS:VolumeUsage.gp2',
                                'EBS:VolumeUsage.gp3',
                                'EBS:VolumeUsage.io1',
                                'EBS:VolumeUsage.io2',
                                'EBS:VolumeUsage.st1',
                                'EBS:VolumeUsage.sc1'
                            ]
                        }
                    }
                ]
            },
            GroupBy=[
                {"Type": "DIMENSION", "Key": "USAGE_TYPE"}
            ]
        )
        return response['ResultsByTime']
    except (BotoCoreError, ClientError) as e:
        print(f"Error fetching cost data: {e}")
        return None

# ==============================
# Process and Summarize Data
# ==============================
def process_results(results):
    """Summarize costs by EBS volume type (storage only)."""
    summary = {}

    for day in results:
        for group in day['Groups']:
            usage_type = group['Keys'][0]  # e.g., 'EBS:VolumeUsage.gp2'
            amount = float(group['Metrics']['UnblendedCost']['Amount'])

            # Extract just the type: gp2, gp3, etc.
            volume_type = usage_type.split('.')[-1]
            summary[volume_type] = summary.get(volume_type, 0.0) + amount

    return summary

# ==============================
# Save to CSV
# ==============================
def save_to_csv(summary, filename):
    """Save summarized data to a CSV file."""
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Volume Type", "Total Storage Cost (USD)"])
        for volume_type, cost in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([volume_type, f"{cost:.2f}"])
    print(f"Data saved to {filename}")

# ==============================
# Main Logic
# ==============================
def main():
    print(f"Fetching EBS storage costs for the past {DAYS_BACK} days...")
    results = get_ebs_storage_costs(DAYS_BACK)

    if not results:
        print("No data returned.")
        return

    summary = process_results(results)

    # Display summary
    print("\nEBS Storage Cost Summary (Last 30 Days):")
    print("-" * 40)
    for volume_type, cost in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        print(f"{volume_type:<10} ${cost:,.2f}")

    # Save to CSV
    save_to_csv(summary, OUTPUT_CSV)


if __name__ == "__main__":
    main()

