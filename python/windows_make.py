from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
import os

py_dir = os.path.dirname(__file__)
src_dir = os.path.join(os.path.dirname(py_dir), "src")

class build_ext_local(_build_ext):
    def finalize_options(self):
        super().finalize_options()
        self.build_lib = os.path.join(py_dir, "lib")
        self.build_temp = os.path.join(py_dir, "build")


# Collect all .c files from src/ to build a self-contained extension.
# Exclude files that are build scripts or platform-specific mains.
exclude_basenames = {
    'centralMain.c', 'GNUmakefile', 'makefile.os2', 'makefile.pc', 'ipcLisp.c', 'mcl-console.c',
    'ipcFFI.c'
}

sources = []
for fname in os.listdir(src_dir):
    if not fname.endswith('.c'):
        continue
    if fname in exclude_basenames:
        continue
    # Skip files in Windows subfolders (if any) referenced in src path
    if os.path.sep + 'Windows' + os.path.sep in os.path.join(src_dir, fname):
        continue
    sources.append(os.path.join(src_dir, fname))

# Prefer python/IPC_wrap.c if it exists (user asked for it); fall back to python/ipcPython.c
wrap_candidates = [os.path.join(py_dir, "IPC_wrap.c"), os.path.join(py_dir, "ipcPython.c")]
wrap = None
for p in wrap_candidates:
    if os.path.exists(p):
        wrap = p
        break
if not wrap:
    raise FileNotFoundError("No Python wrapper found. Expected python/IPC_wrap.c or python/ipcPython.c")
sources.append(wrap)

ext_modules = [
    Extension(
        "_IPC",
        sources=sources,
        include_dirs=[src_dir, py_dir],
        define_macros=[("PYTHON_EXTENSION", "1")],
        libraries=(['Ws2_32'] if os.name == 'nt' else []),
        language="c",
    )
]

long_description = (
    "Builds the IPC native extension (_IPC) from selected src/*.c files and a Python wrapper.\n"
    "The SWIG-generated compiled module is named '_IPC' and the pure-Python wrapper imports it as 'IPC'.\n"
    "Usage: python -m pip install .\n"
    "After install, import the package as 'import IPC'."
)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("build_ext")

setup(
    name="ipc",
    version="0.1",
    description="IPC native extension for Python",
    long_description=long_description,
    project_urls={"Homepage": "https://example.com/ipc"},
    ext_modules=ext_modules,
    cmdclass = {"build_ext": build_ext_local},
)
