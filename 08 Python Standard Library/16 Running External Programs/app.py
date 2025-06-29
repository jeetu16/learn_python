import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
# completed = subprocess.run(["ls", "-l"],
#                            capture_output=True,
#                            text=True)
# completed = subprocess.run(["python3", "other.py"],
#                            capture_output=True,
#                            text=True)
try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)
    print(type(completed))
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
