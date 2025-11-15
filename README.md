# OQ - Objects Quickly

Quick access to popular data science and machine learning libraries.

## Overview

OQ (Objects Quickly) is a convenience package that provides instant access to commonly used objects and functions from popular Python data science and machine learning libraries. It eliminates the need for repetitive imports and gives you quick access to the tools you need.

## Key Features

- **Optional Dependencies**: All scientific/ML libraries are optional - only import what you have installed
- **Flexible Imports**: Use module-specific imports (`import oq.pd`) or get everything at once (`import oq`)
- **Configurable**: Control which modules are imported and in what order
- **Zero Setup**: Works out of the box with intelligent defaults
- **Name Collision Handling**: Import order determines precedence when function names overlap

## Installation

### Basic Installation

```bash
pip install oq
```

This installs only the core package with configuration support.

### With Optional Dependencies

Install specific libraries:

```bash
# Data science essentials
pip install oq[datascience]  # numpy, pandas, scipy, matplotlib, seaborn

# Machine learning
pip install oq[ml]  # scikit-learn, xgboost, lightgbm

# Deep learning
pip install oq[deeplearning]  # torch, tensorflow

# Visualization
pip install oq[viz]  # matplotlib, seaborn, plotly

# Everything
pip install oq[all]
```

Or install individual libraries:

```bash
pip install oq[numpy]
pip install oq[pandas]
pip install oq[sklearn]
# etc.
```

Available individual extras: `numpy`, `pandas`, `scipy`, `matplotlib`, `seaborn`, `plotly`, `sklearn`, `xgboost`, `lightgbm`, `torch`, `tensorflow`, `statsmodels`

## Usage

### Module-Specific Imports

Import and use objects from specific libraries:

```python
# Import pandas utilities
from oq import pd

# Use pandas objects directly
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(pd.concat([df, df]))

# Import numpy utilities
from oq import np

# Use numpy objects directly
arr = np.array([1, 2, 3])
print(np.mean(arr))
```

### Root-Level Import (Auto-Import)

Import everything from all installed libraries at once:

```python
import oq

# All objects from installed libraries are available directly
df = oq.DataFrame({'a': [1, 2, 3]})  # from pandas
arr = oq.array([1, 2, 3])  # from numpy
model = oq.RandomForestClassifier()  # from sklearn
```

## Module Abbreviations

OQ uses intuitive abbreviations for popular libraries:

| Abbreviation | Library | Description |
|--------------|---------|-------------|
| `np` | numpy | Numerical computing |
| `pd` | pandas | Data manipulation and analysis |
| `sp` | scipy | Scientific computing |
| `plt` | matplotlib.pyplot | Plotting and visualization |
| `sns` | seaborn | Statistical visualization |
| `sk` | sklearn | Machine learning (scikit-learn) |
| `xgb` | xgboost | Gradient boosting |
| `lgb` | lightgbm | Light gradient boosting |
| `torch` | torch | Deep learning (PyTorch) |
| `tf` | tensorflow | Deep learning (TensorFlow) |
| `px` | plotly.express | Interactive visualization |
| `sm` | statsmodels | Statistical modeling |

## Configuration

### Default Behavior

By default, OQ:
- Auto-imports all available modules to the root namespace
- Imports in this order: `np`, `pd`, `sp`, `plt`, `sns`, `sk`, `xgb`, `lgb`, `torch`, `tf`, `px`, `sm`
- Later imports take precedence in case of name conflicts

### Custom Configuration

You can customize OQ's behavior by creating a configuration file. OQ uses the `config2py` package for configuration management.

Create a config file at one of these locations:
- `~/.config/oq/config.json`
- Custom location set via `OQ_APP_DATA_DIR` environment variable

Example configuration:

```json
{
  "import_config": {
    "auto_import_to_root": true,
    "module_order": [
      "pd",
      "np",
      "sk"
    ],
    "enabled_modules": {
      "np": true,
      "pd": true,
      "sp": false,
      "plt": true,
      "sns": false,
      "sk": true,
      "xgb": false,
      "lgb": false,
      "torch": false,
      "tf": false,
      "px": false,
      "sm": false
    }
  }
}
```

Configuration options:
- `auto_import_to_root`: Whether to auto-import modules to `oq` namespace (default: `true`)
- `module_order`: Order in which modules are imported (determines precedence for name conflicts)
- `enabled_modules`: Which modules to import when using `import oq`

### Handling Name Conflicts

When multiple libraries define functions with the same name, the import order determines which one is used:

```python
import oq

# If both numpy and torch are installed, and numpy comes first in module_order:
oq.tensor  # This will be torch.tensor (later in import order wins)
```

To avoid conflicts, use module-specific imports:

```python
from oq import np, torch

np_array = np.array([1, 2, 3])
torch_tensor = torch.tensor([1, 2, 3])
```

## How It Works

OQ uses dynamic introspection to extract callable objects from installed libraries:

1. Conditionally imports libraries (fails gracefully if not installed)
2. Uses the `guide` package to extract all public callables
3. Injects them into the module namespace
4. Makes them available for your use

This means:
- No manual maintenance of exported functions
- Always up-to-date with the latest library versions
- Only imports what you have installed
- Zero overhead if you don't use certain libraries

## Examples

### Data Analysis Workflow

```python
import oq

# Load data
df = oq.read_csv('data.csv')

# Analyze
print(df.describe())

# Transform
arr = oq.array(df['column'])
normalized = oq.scale(arr)  # sklearn's scale

# Visualize
oq.figure(figsize=(10, 6))
oq.plot(df['x'], df['y'])
oq.show()
```

### Machine Learning Pipeline

```python
from oq import pd, np, sk

# Load data
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

# Train model
model = sk.RandomForestClassifier()
model.fit(X, y)

# Predict
predictions = model.predict(X)
accuracy = sk.accuracy_score(y, predictions)
print(f'Accuracy: {accuracy}')
```

### Quick Exploration

```python
import oq

# Just start working with your data
data = oq.array([[1, 2], [3, 4], [5, 6]])
df = oq.DataFrame(data, columns=['A', 'B'])
print(df.corr())

# Plot
oq.scatter(df['A'], df['B'])
```

## Development

### Running Tests

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Author

Thor Whalen

## Links

- GitHub: https://github.com/thorwhalen/oq
- PyPI: https://pypi.org/project/oq/

## Related Projects

- [config2py](https://github.com/i2mint/config2py) - Configuration management
- [guide](https://github.com/thorwhalen/guide) - Introspection tools
