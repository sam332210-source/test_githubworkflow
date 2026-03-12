import os
import json
import subprocess

working_dir = "D:\\MyProjects\\githubworkflow\\notepad"
file_path = "data.json"

file_path = os.path.join(working_dir, file_path)

with open(file_path, "r") as fp:
    data = json.load(fp)
for key, value in data.items():
    print(f"data[{key}] = {value}")


cmd = [os.path.join(working_dir, "notepad++.exe")] + ["data.json"]
result = subprocess.run(cmd, cwd=working_dir, text=True)

print("Return code:", result.returncode)
print("Output:\n", result.stdout)
print("Errors:\n", result.stderr)

