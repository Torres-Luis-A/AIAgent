import os
import google.genai.types as types


def get_files_info(working_directory, directory="."):
    absolute_path = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(absolute_path, directory))
    valid_target_dir = os.path.commonpath([absolute_path, target_directory]) == absolute_path
    lines = []

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_directory):
        return f'Error: The path "{directory}" is not a directory.'
    
    for item in os.listdir(target_directory):
        item_path = os.path.join(target_directory,item)

        try:
            item_size = os.path.getsize(item_path)
        except OSError:
            item_size = "Unknown"
        try:
            is_dir = os.path.isdir(item_path)
        except OSError:
            Is_dir = "Unknown"
        lines.append(f"- {item}: file_size={item_size}, is_dir={is_dir}")
    return "\n".join(lines)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        required=["directory"],
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)