
# pdfplot ![PyPI - License](![GitHub](https://img.shields.io/github/license/sauhaardac/pdfplot))

pdfplot is a Python library for easily managing your matplotlib figures as PDF files.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pdfplot.

```bash
pip install pdfplot
```

## Usage

```python
import pdfplot

fig, ax = pdfplot.make_fig()
ax.plot([0, 1, 2, 3], [4, 3, 2, 1])
ax.set_title('First Plot plot!')

fig, ax = pdfplot.make_fig()
ax.plot([0, 1, 2, 3], [1, 2, 3, 4])
ax.set_title('Second plot!')

pdfplot.save_figs(folder='figures')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)