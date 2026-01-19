import os


def get_files_info(working_directory, directory="."):
    absolute_path = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(absolute_path, directory))
    valid_target_dir = os.path.commonpath([absolute_path, target_directory]) == absolute_path
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_directory):
        return f'Error: The path "{directory}" is not a directory.'