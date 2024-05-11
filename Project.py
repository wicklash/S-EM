import re

def read_and_parse_logs(file_path):
    # Log pattern updated for the new log format
    log_pattern = re.compile(
        r'Timestamp: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}), IP: ([\d.]+), UserName: (\w+), Event-ID: (\d+), '
        r'Message: (.*), Machine: (\w+)'
    )

    # Read the log file
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                date, ip, username, log_id, message, machine = match.groups()
                logs.append({
                    "date": date,
                    "ip": ip,
                    "username": username,
                    "id": log_id,
                    "message": message,
                    "machine": machine
                })
    return logs


def print_all_logs(logs):
    for log in logs:
        print(
            f"Date: {log['date']}, IP: {log['ip']}, UserName: {log['username']}, ID: {log['id']}, Machine: {log['machine']}, Message: {log['message']}")


def print_log_with_specific_id(logs, specific_id):
    # Convert specific_id to string to match the parsed IDs
    specific_id = str(specific_id)
    # Find and print the log with the specific ID
    found = False
    for log in logs:
        if log['id'] == specific_id:
            print(
                f"Date: {log['date']}, IP: {log['ip']}, UserName: {log['username']}, ID: {log['id']}, Machine: {log['machine']}, Message: {log['message']}")
            found = True
    if not found:
        print(f"No logs found with ID: {specific_id}")


def check_three_consecutive_ids(logs, target_id):
    # Initialize the counter for consecutive occurrences
    consecutive_count = 0

    # Loop through the list of logs
    for log in logs:
        if log['id'] == str(target_id):  # Check if the current log's ID matches the target ID
            consecutive_count += 1
        else:
            consecutive_count = 0  # Reset the counter if the sequence is broken

        # Check if we have found three consecutive logs with the target ID
        if consecutive_count == 3:
            print("Hata1")
            return  # Exit the function after printing the message


def check_consecutive_ids(logs, first_id, second_id):
    # Convert IDs to string for matching
    first_id = str(first_id)
    second_id = str(second_id)

    # Iterate over logs, checking pairs of consecutive entries
    for i in range(len(logs) - 1):  # We stop at len(logs) - 1 to avoid index error
        if logs[i]['id'] == first_id and logs[i + 1]['id'] == second_id:
            print("Hata2")
            return  # Print "Hata" and exit the function if the pattern is found


file_path = 'source_logs.txt'
logs = read_and_parse_logs(file_path)
print_all_logs(logs)
specific_id = 7
check_three_consecutive_ids(logs, 3)
check_consecutive_ids(logs, 3, 4)
