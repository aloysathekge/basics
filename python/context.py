import json
import time


class SimpleTracker:
    def __init__(self, name):
        self.name = name
        self.start_time = None

    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        status = "ERROR" if exc_type else "SUCCESS"
        print(f"Finished {self.name}: {status} in {duration:.2f}s")
        return False  # Don't suppress exceptions


# Test it
with SimpleTracker("test_script"):
    user_input = input("enter your name: ")
    print(user_input)
