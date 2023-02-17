import sys
from cx_Freeze import setup, Executable

setup(
    name = "cst",
    version = "0.1",
    description = "Watch your file and excute the script after the files modified.",
    executables = [Executable("main.py", targetName="cst" , base=None)]
)