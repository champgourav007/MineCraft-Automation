from dependency import dependency
import subprocess

def install_python_requirements():
   subprocess.run(["pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
   install_python_requirements()
   isDone = dependency.check_java()
   isDone = dependency.check_rclone()