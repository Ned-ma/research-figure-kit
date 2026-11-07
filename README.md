# research-figure-kit

Small Matplotlib helpers for scientific figure sizing and consistent defaults.

## Install

```bash
python -m pip install git+https://github.com/Ned-ma/research-figure-kit.git
```

## Quick start

```python
import matplotlib.pyplot as plt
from research_figure_kit import figure_size, paper_style

with paper_style():
    fig, ax = plt.subplots(figsize=figure_size(width_mm=89, height_ratio=0.62))
    ax.plot([0, 1, 2], [0, 1, 0], label="Example")
    ax.set(xlabel="X", ylabel="Y")
    ax.legend(frameon=False)
    fig.savefig("figure.pdf")
```

paper_style() temporarily applies compact plotting defaults and restores the previous Matplotlib settings when the context manager exits. figure_size() converts a width in millimeters to a (width, height) pair in inches. The defaults are starting points; adjust them to fit your target journal or use case.

## API

- figure_size(width_mm=89.0, height_ratio=0.62) returns figure dimensions in inches.
- paper_style(font_size=8.0, line_width=1.2, save_dpi=300) provides a temporary style context.
- DEFAULT_PALETTE is the default sequence of plot colors.

## License

MIT. See [LICENSE](LICENSE).

---

# research-figure-kit（中文）

为 Matplotlib 科研绘图提供画布尺寸换算和简洁统一的绘图默认值。

```bash
python -m pip install git+https://github.com/Ned-ma/research-figure-kit.git
```

```python
import matplotlib.pyplot as plt
from research_figure_kit import figure_size, paper_style

with paper_style():
    fig, ax = plt.subplots(figsize=figure_size(width_mm=89, height_ratio=0.62))
    ax.plot([0, 1, 2], [0, 1, 0], label="示例")
    ax.set(xlabel="X", ylabel="Y")
    ax.legend(frameon=False)
    fig.savefig("figure.pdf")
```

paper_style() 只在上下文管理器内生效，退出后恢复原来的 Matplotlib 设置。figure_size() 根据毫米宽度计算英寸单位的画布尺寸。默认值只是起点，请按目标期刊或实际用途调整。
