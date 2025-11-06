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
| Missing module/function docstrings | pylint | No docstrings for module or functions | Multiple missing | Added descriptive docstrings | ✅ Fixed |
| Function naming style | pylint | Used CamelCase instead of snake_case | 7 occurrences | Renamed all to snake_case | ✅ Fixed |
| Mutable default argument | pylint | Default `[]` used in function param | Present | Replaced with `None` + init inside | ✅ Fixed |
| Bare except clause | pylint | Generic `except:` block | Present | Replaced with `except (ValueError, KeyError)` | ✅ Fixed |
| File handling | pylint | `open()` without context or encoding | Present | Used `with open(..., encoding="utf-8")` | ✅ Fixed |
| Global statement | pylint | Used unnecessary `global` | Present | Simplified usage, documented necessity | ✅ Fixed |
| Unsafe eval usage | bandit | `eval()` found in code | Present | Replaced with `ast.literal_eval()` | ✅ Fixed |
| String formatting | pylint | Used old `%` formatting | Present | Converted to f-strings | ✅ Fixed |
| Unused import | pylint | `logging` imported but unused | Present | Removed unused import | ✅ Fixed |
| Missing input validation | pylint | No validation on user input | Missing | Added try/except and type checks | ✅ Fixed |
| **Overall pylint score** | pylint | Code quality rating | **4.80 / 10** | **9.89 / 10** | ✅ Improved |

