# Copyright (c) 2026 x1nv.
# Licensed under the MIT License.

import sys
import os
from pathlib import Path

LICENSE_HEADER = (
    "// Copyright (c) <YEAR> <COPYRIGHT HOLDER>.\n"
    "// Licensed under the MIT License.\n\n"
)

# generate define guard header
def create_guard_define(filename: str):
    project_name = Path.cwd().name.upper().replace("-", "_")
    path = Path(filename)
    path_prefix = str(path.with_suffix("")).replace(os.sep, "_").upper()
    guard_name = f"{project_name}_{path_prefix}_H_"
    return (
        f"#ifndef {guard_name}\n"
        f"#define {guard_name}\n"
        "\n\n\n"
        f"#endif  // {guard_name}\n"
    )

# create .cc and .h files
def create_files(filename: str):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    h_path = path.parent / f"{path.name}.h"
    cc_path = path.parent / f"{path.name}.cc"
    with open(h_path, "w") as f:
        f.write(LICENSE_HEADER)
        f.write(f"{create_guard_define(filename)}")
    with open(cc_path, "w") as f:
        f.write(LICENSE_HEADER)
        f.write(f"#include \"{path.name}.h\"")
    print(f"created file: {h_path.resolve()}")
    print(f"created file: {cc_path.resolve()}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Create file failed, Usage: python tools/newcc.py <filename>")
    create_files(sys.argv[1])
