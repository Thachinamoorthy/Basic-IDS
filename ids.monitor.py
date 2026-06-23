import re
from collections import defaultdict

def monitor_logs(log_file_path, alert_threshold=3):
    # Dictionary to keep track of how many times an IP fails
    failed_attempts = defaultdict(int)

    try:
        with open(log_file_path, 'r') as file:
            for line in file:
                # Look for lines indicating a failed login
                if "Failed password" in line:
                    # Use a Regular Expression (Regex) to extract the IP address
                    ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                    
                    if ip_match:
                        attacker_ip = ip_match.group()
                        failed_attempts[attacker_ip] += 1
        
        print("\n=== IDS Security Report ===")
        if not failed_attempts:
            print("Status: SECURE. No failed logins detected.")
        
        # Check the dictionary to see if any IP crossed the threshold
        for ip, count in failed_attempts.items():
            if count >= alert_threshold:
                print(f"[CRITICAL ALERT] Brute-force attack detected from IP: {ip} ({count} attempts)")
            else:
                print(f"[WARNING] Suspicious login failure from IP: {ip} ({count} attempts)")
        print("===========================\n")

    except FileNotFoundError:
        print(f"Error: Could not find the log file at '{log_file_path}'.")

if __name__ == "__main__":
    print("Starting IDS Log Monitor...")
    # Point the script to the mock log file we created
    monitor_logs("server_auth.log", alert_threshold=3)