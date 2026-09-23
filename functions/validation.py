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
        return (target_dir, f'Success: "{directory}" is within the working directory.')
    except (ValueError, TypeError, OSError) as e:
        return (None, f"Error: {e}")

def validate_file(working_directory: str, file_path: str) -> tuple[str | None, str]:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([target_file, working_dir_abs]) == working_dir_abs
        if not valid_target_file:
            return (None, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.')
        if not os.path.isfile(target_file):
            return (None, f'Error: File not found or is not a regular file: "{file_path}".')
        return (target_file, f'Success: "{file_path}" has been found and can be read.')
    except (ValueError, TypeError, OSError) as e:
        return (None, f"Error: {e}")

def validate_write_file(working_directory: str, file_path: str) -> tuple[str | None, str]:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([target_file, working_dir_abs]) == working_dir_abs
        if not valid_target_file:
            return (None, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory.')
        if os.path.isdir(target_file):
            return (None, f'Error: Cannot write to "{file_path}" as it is a directory.')
        return (target_file, f'Success: "{file_path}" is valid and can be written to.')
    except (ValueError, TypeError, OSError) as e:
        return (None, f"Error: {e}")
