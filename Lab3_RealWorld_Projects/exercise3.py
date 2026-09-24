from pipeline_logic import log_execution, validate_telemetry, process_readings, recursive_anomaly_trace

LAST_NAME = "DACUA"
SEED_NUM = 1
FAVORITE_ARTIST = "MYMP"

def telemetry_generator():
    raw_stream = [SEED_NUM * 20, len(LAST_NAME) * 8, "CORRUPT", -15, len(FAVORITE_ARTIST) * 10, 35.5]
    for reading in raw_stream:
        yield reading

print("--- INTELLIGENT EQUIPMENT MONITORING PIPELINE ---")
stream_data = list(telemetry_generator())
print(f"Generated Telemetry Data: {stream_data}")

@log_execution
def run_pipeline():
    valid, invalid = validate_telemetry(stream_data)
    processed, total, average = process_readings(valid)
    anomaly_check = recursive_anomaly_trace(int(average) * 2)
    return valid, invalid, processed, total, average, anomaly_check

valid_res, invalid_res, processed_res, total_res, avg_res, final_status = run_pipeline()

print("\n--- ASSESSMENT DATA (Exercise 3) ---")
print(f"Student-Specific Inputs: Last Name: {LAST_NAME}, Seed: {SEED_NUM}, Artist: {FAVORITE_ARTIST}")
print(f"Generated Telemetry Data: {stream_data}")
print(f"Valid/Invalid Results: Valid: {valid_res} | Invalid: {invalid_res}")
print(f"Processed Results: Total = {total_res}, Average = {round(avg_res, 2)}")
print(f"Recursive Analysis: Completed trace with result {final_status}")
print(f"Final Output: {final_status}")