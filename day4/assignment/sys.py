import sys

def get_python_environment_info():
    """Returns the current Python version and operating system platform."""
    return {
        "python_version": sys.version.split()[0],
        "platform": sys.platform
    }

info = get_python_environment_info()
print(f"Python Version: {info['python_version']} on {info['platform']}")