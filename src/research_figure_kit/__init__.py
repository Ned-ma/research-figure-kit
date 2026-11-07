"""Helpers for consistent Matplotlib scientific figures."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import matplotlib as mpl
from cycler import cycler

__all__ = ["DEFAULT_PALETTE", "figure_size", "paper_style"]
DEFAULT_PALETTE = (
    "#0072B2",
    "#D55E00",
    "#009E73",
    "#CC79A7",
    "#E69F00",
    "#56B4E9",
    "#F0E442",
    "#000000",
)


def figure_size(
    width_mm: float = 89.0, height_ratio: float = 0.62
) -> tuple[float, float]:
    """Return a figure size in inches for a width in millimeters."""
    if width_mm <= 0:
        raise ValueError("width_mm must be greater than zero")
    if height_ratio <= 0:
        raise ValueError("height_ratio must be greater than zero")
    width_in = width_mm / 25.4
    return width_in, width_in * height_ratio


@contextmanager
def paper_style(
    font_size: float = 8.0,
    line_width: float = 1.2,
    save_dpi: int = 300,
) -> Iterator[None]:
    """Temporarily apply compact plotting defaults inside a context manager."""
    if font_size <= 0 or line_width <= 0 or save_dpi <= 0:
        raise ValueError(
            "font_size, line_width, and save_dpi must be greater than zero"
        )
    params = {
        "axes.prop_cycle": cycler(color=DEFAULT_PALETTE),
        "axes.linewidth": line_width,
        "axes.labelsize": font_size,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "figure.dpi": 120,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans"],
        "font.size": font_size,
        "legend.fontsize": max(font_size - 1, 1),
        "lines.linewidth": line_width,
        "savefig.dpi": save_dpi,
        "xtick.direction": "out",
        "xtick.labelsize": max(font_size - 1, 1),
        "ytick.direction": "out",
        "ytick.labelsize": max(font_size - 1, 1),
    }
    with mpl.rc_context(params):
        yield
