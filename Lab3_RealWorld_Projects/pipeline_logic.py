def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"[DECORATOR LOG]: Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[DECORATOR LOG]: Execution of {func.__name__} completed.")
        return result
    return wrapper

def validate_telemetry(stream):
    valid = []
    invalid = []
    for item in stream:
        try:
            val = float(item)
            if val < 0:
                raise ValueError("Negative telemetry value.")
            valid.append(val)
        except (ValueError, TypeError) as e:
            invalid.append(item)
            print(f"[Exception Handled]: Skipped '{item}' -> {e}")
    return valid, invalid

def process_readings(valid_data):
    filtered_data = list(filter(lambda x: x > 0, valid_data))
    total = sum(filtered_data)
    avg = total / len(filtered_data) if filtered_data else 0.0
    return filtered_data, total, avg

def recursive_anomaly_trace(anomaly_score):
    if anomaly_score <= 5:
        print(f"[Base Condition Reached]: Anomaly score dropped to {anomaly_score}.")
        return "NORMAL CONDITION"
    print(f"Tracing Anomaly Score: {anomaly_score}")
    return recursive_anomaly_trace(anomaly_score - 7)