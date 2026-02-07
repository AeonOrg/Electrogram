from __future__ import annotations

from compiler.api.compiler import start as compile_api
from compiler.errors.compiler import start as compile_errors

if __name__ == "__main__":
    print("Generating raw API files...")
    compile_api()
    print("Generating error exceptions...")
    compile_errors()
    print("Done!")
