import paramiko
import os
import sys

if sys.stdout.encoding != 'utf-8':
      sys.stdout.reconfigure(encoding='utf-8')

PI_IP = "192.168.1.24"
PI_USER = "alessandro"
PI_PASS = "5281"
REMOTE_DIR = "/home/alessandro/trading_bot"
LOCAL_DIR = "."

FILES_TO_UPLOAD = [
      "main.py", "main_dashboard.py", "risk_manager.py", 
      "strategy_engine.py", "topstep_client.py", "config_manager.py", 
      "requirements.txt", "config.json"
]

def deploy():
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      try:
                ssh.connect(PI_IP, username=PI_USER, password=PI_PASS, timeout=10)
except Exception as e:
        print(f"ERRORE: {e}")
        return
    ssh.exec_command(f"rm -rf {REMOTE_DIR} && mkdir -p {REMOTE_DIR}")
    sftp = ssh.open_sftp()
    for file in FILES_TO_UPLOAD:
              local_path = os.path.join(LOCAL_DIR, file)
              remote_path = f"{REMOTE_DIR}/{file}"
              if os.path.exists(local_path):
                            sftp.put(local_path, remote_path)
                    sftp.close()
    ssh.exec_command(f"cd {REMOTE_DIR} && python3 -m venv venv && ./venv/bin/pip install -r requirements.txt && ./venv/bin/pip install pandas-ta")
    ssh.close()

if __name__ == "__main__":
      deploy()
