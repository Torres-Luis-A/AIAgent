import os
import google.genai.types as types

def write_file(working_directory, file_path, content):
    absolute_path = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)
    absolute_full_path = os.path.abspath(full_path)
    valid_target_dir = os.path.commonpath([absolute_path, absolute_full_path]) == absolute_path

    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(absolute_full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as file:
            file.write(content)
    except Exception as e:
        return f'Error: Failed to write to "{file_path}" due to: {str(e)}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory",
    parameters=types.Schema(
        required=["file_path", "content"],
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
    ),
)