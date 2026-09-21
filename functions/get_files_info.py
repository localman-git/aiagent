import os


def validate_dir(working_directory: str, directory: str = ".") -> tuple[str | None, str]:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([target_dir, working_dir_abs]) == working_dir_abs
        if not valid_target_dir:
            return (None, f'Error: Cannot list "{directory}" as it is outside the permitted working directory.')
        if not os.path.isdir(target_dir):
            return (None, f'Error: "{directory}" is not a directory.')
        else:
            return (target_dir, f'Success: "{directory}" is within the working directory.')
    except (ValueError, TypeError, OSError) as e:
        return (None, f"Error: {e}")

def get_files_info(working_directory: str, directory: str = ".") -> str:
    valid_dir = validate_dir(working_directory, directory)
    if not valid_dir[0]:
        return valid_dir[1]
    try:
        files = os.listdir(valid_dir[0])
    except (ValueError, TypeError, OSError) as e:
        return f"Error: {e}"
    output_string = ""
    for file in files:
        file_size = os.path.getsize(os.path.join(valid_dir[0], file))
        is_dir = os.path.isdir(os.path.join(valid_dir[0], file))
        output_string += f"- {file}: file_size={file_size} bytes, is_dir={is_dir}\n"
    return f"Result for current directory ({valid_dir[0]}):\n{output_string}"
