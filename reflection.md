# Reflection – Static Code Analysis Lab

**1. What were the easiest and hardest issues to fix?**  
- Easiest: Style and naming warnings from flake8.  
- Hardest: Security issues from bandit (required rewriting logic).

**2. Any false positives or warnings you disagreed with?**  
- Example: Pylint warning for variable naming where readability was fine.

**3. How could you use these tools in real development?**  
- Integrate pylint/flake8 as pre-commit hooks.  
- Run bandit in CI to prevent insecure code from merging.

**4. What improvements did you notice after fixing the issues?**  
- Cleaner, more readable, and safer code.

