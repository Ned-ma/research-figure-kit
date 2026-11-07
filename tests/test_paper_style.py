import matplotlib as mpl
import pytest

from research_figure_kit import DEFAULT_PALETTE, paper_style

def test_paper_style_applies_settings_inside_context():
    with paper_style(font_size=10.0, line_width=2.0, save_dpi=600):
        assert mpl.rcParams["font.size"] == 10.0
        assert mpl.rcParams["axes.labelsize"] == 10.0
        assert mpl.rcParams["lines.linewidth"] == 2.0
        assert mpl.rcParams["savefig.dpi"] == 600
        assert mpl.rcParams["axes.spines.top"] is False
        assert mpl.rcParams["axes.spines.right"] is False

def test_paper_style_sets_default_palette():
    with paper_style():
        assert mpl.rcParams["axes.prop_cycle"].by_key()["color"] == list(
            DEFAULT_PALETTE
        )

def test_paper_style_restores_rcparams():
    keys = ("font.size", "axes.labelsize", "axes.prop_cycle", "savefig.dpi")
    before = {key: mpl.rcParams[key] for key in keys}
    with paper_style(font_size=14.0, line_width=2.5, save_dpi=900):
        pass
    assert {key: mpl.rcParams[key] for key in keys} == before

@pytest.mark.parametrize(
    "kwargs",
    [
        {"font_size": 0},
        {"font_size": -1},
        {"line_width": 0},
        {"line_width": -1},
        {"save_dpi": 0},
        {"save_dpi": -1},
    ],
)
def test_paper_style_rejects_non_positive_values(kwargs):
    with pytest.raises(ValueError):
        with paper_style(**kwargs):
            pass
