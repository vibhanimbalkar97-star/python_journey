1. First try
python --version

If that doesn't work, try:

py --version
2. If python works

Instead of:

pip install numpy jupyter

use:

python -m pip install numpy jupyter
3. If only py works

Use:

py -m pip install numpy jupyter

This is often the easiest solution on Windows.

4. Check NumPy

After installation:

python -c "import numpy; print(numpy.__version__)"

Or if you used py:

py -c "import numpy; print(numpy.__version__)"
5. Check Jupyter
jupyter --version

=============================================

py -m pip install numpy jupyter

check version = py -c "import numpy; print(numpy.__version__)"
check version = py -m jupyter --version

In companies, there isn't one single environment. For Python projects, the common practice is to use a **project-specific virtual environment** or a dependency-managed environment.

For your situation, the important idea is:

```text
Company Project
      ↓
Python Environment
      ↓
Dependencies
      ↓
Code / Notebook
```

### 1. Most common: `.venv`

A typical project might look like:

```text
my-project/
├── .venv/              ← Python environment
├── src/
├── notebooks/
│   └── analysis.ipynb
├── requirements.txt
└── README.md
```

The `.venv` folder is **not pushed to GitHub**. Usually `.gitignore` contains:

```text
.venv/
```

The team shares the dependencies through:

```text
requirements.txt
```

For example:

```text
numpy
pandas
matplotlib
jupyter
```

A new developer can create their own environment and install the same dependencies:

```bash
python -m venv .venv
```

Then:

```bash
.venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

---

## 2. How companies run notebooks in VS Code

Suppose the company project has:

```text
company-project/
├── .venv/
├── notebooks/
│   └── analysis.ipynb
└── requirements.txt
```

Open `company-project` in VS Code.

Then open:

```text
analysis.ipynb
```

At the top-right of the notebook:

**Select Kernel → Python Environment → `.venv`**

Then:

```python
import numpy as np
import pandas as pd
```

Click **▶ Run Cell**.

That's basically it.

---

## 3. What is the "Kernel"?

This is important for interviews and practical work.

The **kernel is the running Python process that executes your notebook code**.

For example:

```text
VS Code
   ↓
analysis.ipynb
   ↓
Select Kernel
   ↓
Python 3.x (.venv)
   ↓
NumPy / Pandas
```

If you select the wrong kernel, you might get:

```text
ModuleNotFoundError: No module named 'numpy'
```

even though you installed NumPy somewhere else.

---

## 4. What do companies actually use?

It depends on the project.

| Environment                | Common usage                                                        |
| -------------------------- | ------------------------------------------------------------------- |
| `venv` / `.venv`           | Very common Python projects                                         |
| Conda                      | Data Science / ML environments                                      |
| Poetry                     | Dependency/project management                                       |
| `pip` + `requirements.txt` | Very common                                                         |
| `uv`                       | Increasingly used for fast Python dependency/environment management |
| Docker                     | Deployment and reproducible environments                            |

For **your current NumPy → Pandas → AI learning**, don't worry about all of these yet.

### Learn this workflow first:

```text
VS Code
   ↓
Project folder
   ↓
.venv
   ↓
NumPy / Pandas / Jupyter
   ↓
.ipynb
   ↓
Select .venv as Kernel
   ↓
Run Cell ▶
```

That's a very good foundation for working with Python projects professionally.
