import subprocess

def run_shell_command(command):
    """Executes a system command and returns the output."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout.strip()

# Program execution
output = run_shell_command("echo Hello from the system shell")
print("Command Output:", output)