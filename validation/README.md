# Technical Validation

This directory contains executable C17 validation fixtures derived from the official student materials.

The validation workflow checks:

- GCC and Clang compilation with `-std=c17 -Wall -Wextra -Wformat=2 -pedantic -Werror`
- expected output and exit status for complete examples
- expected compile or link failure for intentionally incorrect examples
- multi-file compilation and linking
- representative boundary, invalid-input, allocation, file, pointer, recursion, and string cases
- material navigation links and bilingual Unit pairing

The fixtures are validation evidence, not additional student assignments. The student materials remain the source of explanation and learning activities.

Run locally:

```bash
python3 validation/run_validation.py --compiler gcc
python3 validation/run_validation.py --compiler clang
python3 validation/check_materials.py
```
