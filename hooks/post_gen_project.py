import os
from subprocess import Popen

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if not os.path.exists(".git"):
    for command in [
        ("git", "init"),
        ("pre-commit", "install"),
        ("go", "test", "./..."),
        ("go", "mod", "tidy"),
        ("git", "add", "."),
    ]:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()
