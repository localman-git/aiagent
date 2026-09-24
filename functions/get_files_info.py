import os

from functions.validation import valid_path


def get_files_info(working_directory: str, directory: str = ".") -> str:
    valid_dir = valid_path(working_directory, directory, "list_dir")
    if not valid_dir[0]:
        return valid_dir[1]
    try:
        files = os.listdir(valid_dir[0])
    except (ValueError, TypeError, OSError) as e:
        return f"Error: {e}"
    output_string = ""
    for file in files:
        file_path = os.path.join(valid_dir[0])
        file_size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        output_string += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return f"{valid_dir[1]}\nResult for current directory ({valid_dir[0]}):\n{output_string}"
