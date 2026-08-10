import time

def measure_execution_time(task_duration):
    """Simulates a task and measures actual elapsed time."""
    start_time = time.time()
    time.sleep(task_duration)
    end_time = time.time()
    return round(end_time - start_time, 2)

# Program execution
elapsed = measure_execution_time(1.5)
print(f"Task completed in {elapsed} seconds.")