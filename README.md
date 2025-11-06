# Lab 5 – Static Code Analysis

This repository contains:
- `inventory_system.py`: the program under analysis
- Static analysis reports: `pylint_report.txt`, `flake8_report.txt`, and `bandit_report.txt`
- Documentation: `issues.md` (fix summary) and `reflection.md` (post-lab reflections)
- Original handout: `Lab_5_Static_code_analysis_Student_handout.docx`

## How to reproduce
```bash
pip install pylint flake8 bandit
pylint inventory_system.py
flake8 inventory_system.py
bandit -r inventory_system.py

