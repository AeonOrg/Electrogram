from __future__ import annotations

import sys
from pathlib import Path

# Add the current directory to sys.path to allow importing from compiler
sys.path.insert(0, str(Path(__file__).parent))

from compiler.api.compiler import start as compile_api
from compiler.errors.compiler import start as compile_errors

if __name__ == "__main__":
    print("Generating raw API files...")
    compile_api()
    print("Generating error exceptions...")
    compile_errors()
    print("Done!")
