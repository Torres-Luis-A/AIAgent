import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    full_path = os.path.join(working_directory, file_path)
    absolute_full_path = os.path.abspath(full_path)
    absolute_path = os.path.abspath(working_directory)
    valid_target_dir = os.path.commonpath([absolute_path, absolute_full_path]) == absolute_path
    try:
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
    except Exception as e:
        return f"Error: executing Python file: {e}"   
    try: 
        command = ["python", absolute_full_path]

        if args:
            command.extend(args)

        result = subprocess.run(command, cwd=working_directory,stdout=subprocess.PIPE, stderr=subprocess.PIPE,text = True,timeout=30)
    
        if result.returncode != 0:
            result = result + "Process exited with code X"
        if result.stderr and result.stdout == None:
            result = result + "no output captured"
        else:
            result = f'STDOUT:{result.stdout}STDERR:{result.stderr}'
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"

    
        
        