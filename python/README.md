# Building the Python extension (ipc)

Requirements:
- A working Python development environment with a C compiler (MSVC on Windows or gcc/clang on Unix).
- setuptools (pip install --upgrade setuptools wheel)

Important Windows note (avoid linker failures):
- Make sure you open the matching 64-bit Visual Studio developer shell before building if your Python is 64-bit.
  - Open "Developer PowerShell for VS" (x64) or "x64 Native Tools Command Prompt for VS".
  - Confirm Python bitness:
	python -c "import struct; print(struct.calcsize('P')*8)"  # prints 64 or 32
  - If Python is 64-bit, build in the x64 shell; if 32-bit, use the 32-bit shell.

Build and install locally (Windows example using the x64 dev shell):

1) python -m pip install --upgrade pip setuptools wheel
2) python windows_make.py

The extension module is provided as the compiled SWIG wrapper _IPC plus the pure-Python wrapper IPC; import with:

  import IPC

If you need to customize the selected sources, edit setup.py's BASENAMES list.

