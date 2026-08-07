#!/usr/bin/env bash
set -euo pipefail

CC="${CC:-cc}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

BASE_FLAGS=(-std=c17 -Wall -Wextra -pedantic)
CLEAN_FLAGS=(-std=c17 -Wall -Wextra -pedantic -Werror)

compile_clean() {
  local src="$1"
  local out="$2"
  "$CC" "${CLEAN_FLAGS[@]}" "$ROOT/$src" -o "$TMP/$out"
}

assert_exact() {
  local expected="$1"
  local actual="$2"
  local label="$3"
  if [[ "$actual" != "$expected" ]]; then
    printf 'FAIL: %s\nExpected:\n%s\nActual:\n%s\n' "$label" "$expected" "$actual" >&2
    exit 1
  fi
}

run_success() {
  local program="$1"
  local input="$2"
  local expected="$3"
  local label="$4"
  local actual
  actual="$(printf '%s' "$input" | "$TMP/$program")"
  assert_exact "$expected" "$actual" "$label"
}

run_failure() {
  local program="$1"
  local input="$2"
  local expected="$3"
  local label="$4"
  local actual status
  set +e
  actual="$(printf '%s' "$input" | "$TMP/$program")"
  status=$?
  set -e
  if [[ $status -eq 0 ]]; then
    printf 'FAIL: %s unexpectedly exited successfully\n' "$label" >&2
    exit 1
  fi
  assert_exact "$expected" "$actual" "$label"
}

echo "Compiler: $($CC --version | head -n 1)"

# Correct references must be warning-clean for the supported GCC/Clang CI targets.
compile_clean unit-01/hello.c hello
compile_clean unit-02/average.c average
compile_clean unit-03/score-statistics.c score-statistics
compile_clean unit-04/max-of-three.c max-of-three

# Intentional defects have explicit, different expectations.
if "$CC" "${BASE_FLAGS[@]}" "$ROOT/unit-01/defects/missing-semicolon.c" -o "$TMP/missing-semicolon" >"$TMP/missing-semicolon.log" 2>&1; then
  echo 'FAIL: missing-semicolon.c unexpectedly translated successfully' >&2
  exit 1
fi

compile_clean unit-02/defects/integer-division.c integer-division
compile_clean unit-03/defects/infinite-loop.c infinite-loop

# This defect is diagnostic/contract material only. Do not execute it; its relevant call has undefined behavior.
set +e
"$CC" "${BASE_FLAGS[@]}" "$ROOT/unit-04/defects/missing-return.c" -o "$TMP/missing-return" >"$TMP/missing-return.log" 2>&1
missing_return_status=$?
set -e
printf 'missing-return.c diagnostic compile status: %d\n' "$missing_return_status"
cat "$TMP/missing-return.log"

# Correct-reference runtime cases.
run_success hello '' 'Hello, C!' 'unit-01 hello'

run_success average $'5 2\n' 'Average: 2.50' 'unit-02 average 5/2'
run_success average $'0 3\n' 'Average: 0.00' 'unit-02 average zero total'
run_failure average $'5 0\n' 'Count must be positive' 'unit-02 zero count'
run_failure average $'5 -2\n' 'Count must be positive' 'unit-02 negative count'
run_failure average $'x 2\n' 'Invalid input' 'unit-02 malformed input'

run_success score-statistics $'80 90 -1\n' $'Count: 2\nSum: 170\nAverage: 85.00' 'unit-03 normal scores'
run_success score-statistics $'0 100 -1\n' $'Count: 2\nSum: 100\nAverage: 50.00' 'unit-03 boundary scores'
run_success score-statistics $'-1\n' 'No valid score' 'unit-03 empty valid sequence'
run_success score-statistics $'120 80 -1\n' $'Count: 1\nSum: 80\nAverage: 80.00' 'unit-03 ignored out-of-range score'

run_success max-of-three $'3 8 5\n' 'Maximum: 8' 'unit-04 normal maximum'
run_success max-of-three $'9 9 1\n' 'Maximum: 9' 'unit-04 tied maximum'
run_success max-of-three $'-3 -8 -5\n' 'Maximum: -3' 'unit-04 negative values'
run_failure max-of-three $'x 8 5\n' 'Invalid input' 'unit-04 malformed input'

# Logic defect may be run in a controlled test because its behavior is defined; the wrong result is the lesson.
run_success integer-division '' 'Average: 2.00' 'unit-02 intentional integer-division defect'

# Never execute infinite-loop.c here. CI verifies only that it translates cleanly.

echo 'C17 example verification passed.'
