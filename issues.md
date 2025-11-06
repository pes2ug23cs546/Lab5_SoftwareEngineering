# Static Code Analysis – Issues & Fixes

| Issue | Tool | Line(s) | Description | Fix Implemented | Status |
|-------|------|----------|--------------|------------------|--------|
| Mutable default argument | pylint | 15 | Function uses list as default parameter | Changed to None default | ✅ Fixed |
| Bare except clause | pylint/flake8 | 45 | Catches all exceptions | Handled specific exceptions | ✅ Fixed |
| Insecure subprocess usage | bandit | 80 | Used shell=True | Changed to safe subprocess call | ✅ Fixed |
| Long line >120 chars | flake8 | 102 | Style issue | Broke into two lines | ✅ Fixed |

# Static Code Analysis – Final Fix Summary

| Issue | Tool | Description | Before Fix | After Fix | Status |
|-------|------|--------------|-------------|------------|--------|
| Missing docstrings | pylint | No docstrings for module/functions | 12 warnings | 0 warnings | ✅ Fixed |
| Function naming | pylint | CamelCase names used | 7 occurrences | 0 occurrences | ✅ Fixed |
| Mutable default list | pylint | Used [] as default param | Present | Replaced with None default | ✅ Fixed |
| Bare except | pylint | Caught all exceptions | Present | Specific exceptions used | ✅ Fixed |
| Unsafe eval | bandit | Use of eval() | Present | Replaced with `ast.literal_eval()` | ✅ Fixed |
| File handling | pylint | open() without encoding/context | Present | Added `with open(..., encoding='utf-8')` | ✅ Fixed |
| Unused import | pylint | logging not used | Present | Removed | ✅ Fixed |
| String formatting | pylint | Used `%` instead of f-string | Present | Replaced with f-string | ✅ Fixed |

