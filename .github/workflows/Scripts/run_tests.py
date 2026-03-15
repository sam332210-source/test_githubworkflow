import os
import json
import subprocess

working_dir = "D:\\MyProjects\\githubworkflow\\aria2\\aria2-1.37.0-win-32bit-build1"
file_path = "data.json"

file_path = os.path.join(working_dir, file_path)

with open(file_path, "r") as fp:
    data = json.load(fp)
for key, value in data.items():
    print(f"data[{key}] = {value}")


cmd = [os.path.join(working_dir, "aria2c.exe")] + ["https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.9.2/npp.8.9.2.portable.x64.zip"]
result = subprocess.run(cmd, cwd=working_dir, text=True)

print("Return code:", result.returncode)
print("Output:\n", result.stdout)
print("Errors:\n", result.stderr)

