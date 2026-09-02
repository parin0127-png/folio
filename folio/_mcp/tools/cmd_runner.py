import subprocess
import tempfile
import shutil
import os

def run_command(command: str):
    """execute and run terminal commands, shell scripts, bash commands, or system operations in a sandbox"""    
    temp_dir = None
    try:
        temp_dir = tempfile.mkdtemp()

        subprocess.run(["git", "init"], cwd = temp_dir, capture_output = True)

        result = subprocess.run(
            command,
            shell = True,
            cwd = temp_dir,
            capture_output = True,
            timeout = 10  
        )

        return  {
            "Status": "Success",
            "Output": result.stdout.strip(),
            "Error": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "command killed after 10 seconds"}

    except Exception as e:
        return f"> run_command failed: {str(e)}"

    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors = True)
