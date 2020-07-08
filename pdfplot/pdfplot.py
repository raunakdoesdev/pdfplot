import os
import subprocess
import platform
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import time
import warnings


def save_figs(filename=None, open=True, folder='.', save_latest=True):
    """

    :param filename: (optional) path to pdf file for saving.
    :param open: boolean flag for opening pdf file after saving
    :param folder: folder to save pdf files (default=current dir)
    :param save_latest: boolean flag for creating a "latest.pdf" in folder directory, symlinked to latest plots.
    :return:
    """

    if filename is None:
        filename = time.strftime("%Y%m%d-%H%M%S.pdf")
    if folder is not None:
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, filename)

    fn = os.path.join(os.getcwd(), filename)
    pp = PdfPages(fn)
    for i in plt.get_fignums():
        plt.figure(i).tight_layout()
        pp.savefig(plt.figure(i))
        plt.close(plt.figure(i))
    pp.close()

    if save_latest:
        try:
            latest_path = os.path.join(folder, 'latest.pdf')
            if os.path.exists(latest_path):
                os.remove(latest_path)

            os.symlink(filename, latest_path)
            if open:
                _open_figs(latest_path)
            return
        except OSError:
            warnings.warn('Cannot create symbolic link in Windows without administrator privileges. Skipping.')
    if open:
        _open_figs(filename)


def _open_figs(filename):
    pdf_path = os.path.abspath(filename)

    if os.path.exists(pdf_path):
        if platform.system() == 'Darwin':  # macOS
            subprocess.call(('open', pdf_path))
        elif platform.system() == 'Windows':  # Windows
            os.startfile(pdf_path)
        else:  # linux variants
            subprocess.call(('xdg-open', pdf_path))


def make_fig():
    """
    Returns figure and axis for plotting. Can easily override to adjust defaults.
    :return:
    """
    fig, ax = plt.subplots()
    fig.tight_layout()
    return fig, ax
