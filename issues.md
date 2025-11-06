# Static Code Analysis – Issues & Fixes

| Issue | Tool | Line(s) | Description | Fix Implemented | Status |
|-------|------|----------|--------------|------------------|--------|
| Mutable default argument | pylint | 15 | Function uses list as default parameter | Changed to None default | ✅ Fixed |
| Bare except clause | pylint/flake8 | 45 | Catches all exceptions | Handled specific exceptions | ✅ Fixed |
| Insecure subprocess usage | bandit | 80 | Used shell=True | Changed to safe subprocess call | ✅ Fixed |
| Long line >120 chars | flake8 | 102 | Style issue | Broke into two lines | ✅ Fixed |

