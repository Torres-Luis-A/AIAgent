import os
from functions.get_files_info import get_files_info
from config import max_chars

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    absolute_full_path = os.path.abspath(full_path)

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            file_content = f.read(max_chars)
            extra = f.read(1)

    except UnicodeDecodeError:
        return f'Error: File "{file_path}" is not a text file or contains unsupported characters.'
    try:
        absolute_path = os.path.abspath(working_directory)
        valid_target_dir = os.path.commonpath([absolute_path, absolute_full_path]) == absolute_path
    except OSError:
        return f'Error: File not found or is not a regular file: "{file_path}"'

    # After reading the first MAX_CHARS...
    if extra !=None:
        file_content += f'[...File "{file_path}" truncated at {max_chars} characters]'
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    

    return file_content