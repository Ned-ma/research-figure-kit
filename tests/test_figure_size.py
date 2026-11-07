import pytest

from research_figure_kit import figure_size

def test_figure_size_converts_mm_to_inches():
    assert figure_size() == pytest.approx((3.5039370078740157, 2.17244094488189))
    assert figure_size(100.0, 0.5) == pytest.approx(
        (3.937007874015748, 1.968503937007874)
    )

@pytest.mark.parametrize("width_mm", [0.0, -1.0])
def test_figure_size_rejects_non_positive_width(width_mm):
    with pytest.raises(ValueError, match="width_mm"):
        figure_size(width_mm=width_mm)

@pytest.mark.parametrize("height_ratio", [0.0, -0.5])
def test_figure_size_rejects_non_positive_height_ratio(height_ratio):
    with pytest.raises(ValueError, match="height_ratio"):
        figure_size(height_ratio=height_ratio)
