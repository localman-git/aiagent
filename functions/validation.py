import os


def valid_path(working_directory: str, path: str, validation_type: str) -> tuple[str | None, str]:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(working_dir_abs, path))
        valid_target = os.path.commonpath([target, working_dir_abs]) == working_dir_abs
        target_dir = os.path.isdir(target)
        target_file = os.path.isfile(target)

        if validation_type == "list_dir":
            if not valid_target:
                return (None, f'Error: Cannot list "{path}" as it is outside the permitted working directory.')
            if not target_dir:
                return (None, f'Error: "{path}" is not a directory.')
            return (target, f'Success: "{path}" is within the working directory. Reading directory contents...')

        if validation_type == "read_file":
            if not valid_target:
                return (None, f'Error: Cannot read "{path}" as it is outside the permitted working directory.')
            if not target_file:
                return (None, f'Error: File not found or is not a regular file: "{path}".')
            return (target, f'Success: "{path}" has been found and can be read. Reading file contents...')

        if validation_type == "write_file":
            if not valid_target:
                return (None, f'Error: Cannot write to "{path}" as it is outside the permitted working directory.')
            if target_dir:
                return (None, f'Error: Cannot write to "{path}" as it is a directory.')
            return (target, f'Success: "{path}" is valid and can be written to. Writing file contents...')

        if validation_type == "run_python":
            if not valid_target:
                return (None, f'Error: Cannot execute "{path}" as it is outside the permitted working directory.')
            if not target_file:
                return (None, f'Error: "{path}" does not exist or is not a regular file.')
            if not target.endswith(".py"):
                return (None, f'Error: "{path}" is not a Python file.')
            return (target, f'Success: "{path}" is a valid python file and can be executed. Executing python file...')

    except (ValueError, TypeError, OSError) as e:
        return (None, f"Error: {e}")

    return (None, f"Error: {validation_type} validation failed without exception.")
