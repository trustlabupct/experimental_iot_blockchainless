import matplotlib.pyplot as plt
import re
from collections import defaultdict

# Define the filenames and corresponding IoT devices
log_files = {
    'iot_device_log1.log': 'IoT_1',
    'iot_device_log2.log': 'IoT_2',
    'iot_device_log3.log': 'IoT_3',
    'iot_device_log4.log': 'IoT_4'
}

# Define colors for each IoT device
colors = {
    'IoT_1': 'blue',
    'IoT_2': 'orange',
    'IoT_3': 'green',
    'IoT_4': 'red'
}

# Regular expression to match log lines
log_line_regex = re.compile(r'Published transaction')

# Function to process each log file and count the transactions
def count_transactions(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if log_line_regex.search(line):
                count += 1
    return count

# Count transactions for each IoT device
transaction_counts = {device_id: count_transactions(log_file) for log_file, device_id in log_files.items()}

# Print the transaction counts
for device_id, count in transaction_counts.items():
    print(f"{device_id}: {count} transactions")

# Create a bar plot for the transaction counts
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(transaction_counts.keys(), transaction_counts.values(), color=[colors[device_id] for device_id in transaction_counts.keys()])

# Customize the plot
ax.set_xlabel('IoT Devices', fontsize=30)
ax.set_ylabel('Number of Transactions', fontsize=30)
ax.set_title('Number of Transactions Generated by Each IoT Device', fontsize=25)
ax.tick_params(axis='both', which='major', labelsize=25)

# Save the plot as an image file
output_file_path = 'iot_transactions_count.png'
plt.savefig(output_file_path)
plt.show()
plt.close()
