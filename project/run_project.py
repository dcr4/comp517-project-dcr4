import subprocess
import sys
import os

def install_dependencies():
    # Check if Poetry is installed
    try:
        subprocess.run(["poetry", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Poetry is not installed. Please install Poetry before running this script.")
        sys.exit(1)

    # Install project dependencies using Poetry
    subprocess.run(["poetry", "install"], check=True)

def run_project():
    subprocess.Popen(["poetry", "run", "python", "vagabond.py"])

if __name__ == "__main__":
    os.chdir("vagabond")
    install_dependencies()
    run_project()