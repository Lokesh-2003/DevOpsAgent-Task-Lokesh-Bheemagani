import subprocess

def restart_container(container_name):
    try:
        subprocess.run(["docker", "restart", container_name], check=True)
        return True
    except Exception as e:
        print(f"Error restarting container: {e}")
        return False
