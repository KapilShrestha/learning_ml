import os
import sys
import subprocess

def create_project(project_name, title):
    base_path = os.getcwd()
    project_path = os.path.join(base_path, project_name)

    if os.path.exists(project_path):
        print(f"Project {project_name} already exists.")
        return

    # 1️⃣ Create project folder
    os.makedirs(project_path)

    # 2️⃣ Create dataset folder
    os.makedirs(os.path.join(project_path, "dataset"))

    # 3️⃣ Create README.md
    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write("## Overview\n")
        f.write("Short project description here.\n")

    # 4️⃣ Create virtual environment
    env_name = f"{project_name}_env"
    subprocess.run(["python", "-m", "venv", env_name], cwd=project_path)

    # 5️⃣ Define base packages
    base_packages = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "jupyter"
    ]

    # 6️⃣ Install packages using venv python
    venv_python = os.path.join(project_path, env_name, "Scripts", "python.exe")

    if not os.path.exists(venv_python):  # Mac/Linux fallback
        venv_python = os.path.join(project_path, env_name, "bin", "python")

    subprocess.run([venv_python, "-m", "pip", "install"] + base_packages)

    # 7️⃣ Generate requirements.txt
    req_path = os.path.join(project_path, "requirements.txt")
    with open(req_path, "w") as req_file:
        subprocess.run([venv_python, "-m", "pip", "freeze"], stdout=req_file)

    print(f"\nProject {project_name} created successfully! 🚀")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_project.py <project_name> <title>")
    else:
        create_project(sys.argv[1], sys.argv[2])