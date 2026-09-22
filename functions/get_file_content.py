from config import MAX_CHARACTERS
from functions.validation import validate_file


def get_file_content(working_directory: str, file_path: str) -> str:
    valid_file = validate_file(working_directory, file_path)
    if not valid_file[0]:
        return valid_file[1]
    try:
        with open(valid_file[0], "r") as f:
            content = f.read(MAX_CHARACTERS)
            if f.read(1):
                content += f' [...File "{file_path}" truncated at {MAX_CHARACTERS} characters]'
    except (ValueError, TypeError, OSError) as e:
        return f"Error: {e}"
    return f"{valid_file[1]}\n{content}"
