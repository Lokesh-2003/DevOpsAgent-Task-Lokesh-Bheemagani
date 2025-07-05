def get_recent_logs(log_path="/var/log/syslog", lines=100):
    try:
        with open(log_path, 'r') as f:
            return ''.join(f.readlines()[-lines:])
    except Exception as e:
        return f"Error reading logs: {e}"
