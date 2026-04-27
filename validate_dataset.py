import json
from pathlib import Path


DATASET_PATH = Path("training_data/stock_qa_dataset_v1.jsonl")


def validate_dataset():
    """
    Validate the stock fine-tuning dataset.

    Checks:
    - file exists
    - each line is valid JSON
    - each record contains instruction, input, output
    - output contains the expected structured sections
    """
    if not DATASET_PATH.exists():
        print(f"Dataset file not found: {DATASET_PATH}")
        return

    total_lines = 0
    valid_lines = 0
    errors = []

    with DATASET_PATH.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()

            if not line:
                continue

            total_lines += 1

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"Line {line_number}: Invalid JSON -> {exc}")
                continue

            # Required keys
            required_keys = {"instruction", "input", "output"}
            missing_keys = required_keys - record.keys()

            if missing_keys:
                errors.append(
                    f"Line {line_number}: Missing key(s) -> {', '.join(sorted(missing_keys))}"
                )
                continue

            output_text = str(record["output"])

            # Check structure of output
            if "Direct Answer:" not in output_text:
                errors.append(f"Line {line_number}: Missing 'Direct Answer:' section")
                continue

            if "Explanation:" not in output_text:
                errors.append(f"Line {line_number}: Missing 'Explanation:' section")
                continue

            if "Relevant Table(s):" not in output_text:
                errors.append(f"Line {line_number}: Missing 'Relevant Table(s):' section")
                continue

            valid_lines += 1

    print("----- DATASET VALIDATION REPORT -----")
    print(f"Dataset file: {DATASET_PATH}")
    print(f"Total non-empty lines checked: {total_lines}")
    print(f"Valid lines: {valid_lines}")
    print(f"Invalid lines: {len(errors)}")

    if errors:
        print("\nErrors found:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nNo structural errors found. Dataset looks ready for the next step.")


if __name__ == "__main__":
    validate_dataset()