import os
import subprocess

from functions.validation import valid_path


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    valid_file = valid_path(working_directory, file_path, "run_python")
    if not valid_file[0]:
        return valid_file[1]
    try:
        command = ["python", valid_file[0]]
        if args:
            command.extend(args)
        execute = subprocess.run(
            command,
            cwd = os.path.abspath(working_directory),
            capture_output = True,
            text = True,
            timeout = 30,
            check = False
        )
        output_string = valid_file[1] + "\n"
        if execute.returncode != 0:
            output_string += f"Process exited with code {execute.returncode}.\n"
        if not execute.stdout and not execute.stderr:
            output_string += "No output produced.\n"
        else:
            output_string += f"STDOUT: {execute.stdout}\n"
            output_string += f"STDERR: {execute.stderr}\n"
        return output_string
    except (subprocess.TimeoutExpired, OSError, UnicodeDecodeError) as e:
        return f"Error: executing Python file: {e}"
