import os
from subprocess import Popen

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


if not os.path.exists(".fossa.yml"):
    for command in [
        ("fossa", "init"),
    ]:
        cmd = Popen(command, cwd=PROJECT_DIRECTORY)
        cmd.wait()

if not os.path.exists(".git"):
    for command in [
        ("git", "init"),
        ("pre-commit", "install"),
        ("go", "test", "./..."),
        ("go", "mod", "tidy"),
        ("git", "add", "."),
    ]:
        cmd = Popen(command, cwd=PROJECT_DIRECTORY)
        cmd.wait()
