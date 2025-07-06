from monitor import check_cpu_spike
from logs import get_recent_logs
from analyze import analyze_logs
from remediate import restart_container
from notify import send_slack_alert


def main():
    alert, usage = check_cpu_spike()
    if alert:
        logs = get_recent_logs()
        analysis = analyze_logs(logs)

        if "infinite loop" in analysis.lower() or "memory leak" in analysis.lower():
            restarted = restart_container("your_container_name")
            status = " Container restarted successfully" if restarted else " Failed to restart container"
        else:
            status = " No confident remediation step detected"

        send_alert(f"""
 *CPU Spike Detected* – Usage: {usage:.2f}%
 *LLM Analysis*:
{analysis}
🔧 *Remediation*: {status}
        """)


if __name__ == "__main__":
    main()
