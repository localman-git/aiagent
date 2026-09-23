import os

from functions.validation import validate_write_file


def write_file(working_directory: str, file_path: str, content: str) -> str:
    valid_write_path = validate_write_file(working_directory, file_path)
    if not valid_write_path[0]:
        return valid_write_path[1]
    try:
        os.makedirs(os.path.dirname(valid_write_path[0]), exist_ok = True)
        with open(valid_write_path[0], "w") as f:
            f.write(content)
    except (ValueError, TypeError, OSError) as e:
        return f"Error: {e}"
    return f'Success: wrote to "{file_path}" ({len(content)} characters written)'
