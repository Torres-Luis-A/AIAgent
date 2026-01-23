from functions.get_files_info import get_files_info

def get_file_content(working_directory, file_path):
    absolute_path = os.path.abspath(working_directory)
    valid_target_dir = os.path.commonpath([absolute_path, target_directory]) == absolute_path

    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'