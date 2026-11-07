# research-figure-kit Maintenance Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve maintenance confidence for research-figure-kit while preserving its public API and runtime behavior.

**Architecture:** Keep the two existing helpers in the current module. Add pytest coverage for their documented behavior, use Ruff for linting and formatting, and run these checks in GitHub Actions on the minimum supported Python and a current compatible stable Python.

**Tech Stack:** Python 3.9+, Matplotlib, cycler, pytest, Ruff, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-07-research-figure-kit-maintenance-design.md`

## Global Constraints

- Preserve `requires-python = ">=3.9"`.
- Preserve runtime dependencies `matplotlib>=3.7` and `cycler>=0.11`.
- Preserve public functions `figure_size(width_mm=89.0, height_ratio=0.62)` and `paper_style(font_size=8.0, line_width=1.2, save_dpi=300)`.
- Do not add plotting or export features, change the license, or publish to PyPI.
- Keep the README bilingual and aligned with the existing API.

## Review Focus

- `figure_size()` with `width_mm <= 0` must raise `ValueError` — Task 1 test `test_figure_size_rejects_non_positive_width`.
- `figure_size()` with `height_ratio <= 0` must raise `ValueError` — Task 1 test `test_figure_size_rejects_non_positive_height_ratio`.
- `paper_style()` with non-positive font size, line width, or DPI must raise `ValueError` — Task 1 test `test_paper_style_rejects_non_positive_values`.
- `paper_style()` must restore pre-existing Matplotlib settings after normal context exit — Task 1 test `test_paper_style_restores_rcparams`.
- The palette must be active inside `paper_style()` — Task 1 test `test_paper_style_sets_default_palette`.

---

### Task 1: Add behavior tests and developer tooling

**Files:**
- Modify: `pyproject.toml`
- Modify: `src/research_figure_kit/__init__.py`
- Create: `tests/test_figure_size.py`
- Create: `tests/test_paper_style.py`
- Modify: `README.md`

**Interfaces:**
- Consumes: `figure_size(width_mm: float = 89.0, height_ratio: float = 0.62) -> tuple[float, float]` and `paper_style(font_size: float = 8.0, line_width: float = 1.2, save_dpi: int = 300)`.
- Produces: development extra `.[dev]` containing pytest and Ruff; no runtime API changes.

- [ ] Add `test_figure_size_converts_mm_to_inches` for the default and an explicit width, asserting width divided by 25.4 and the requested height ratio.
- [ ] Add parametrized rejection tests for zero and negative width and height ratio.
- [ ] Add `test_paper_style_applies_settings_inside_context` for font size, line width, save DPI, and hidden top/right spines.
- [ ] Add `test_paper_style_sets_default_palette` to compare the active color cycle with `DEFAULT_PALETTE`.
- [ ] Add `test_paper_style_restores_rcparams` by saving prior values, entering and leaving the context, then comparing the restored values.
- [ ] Add parametrized rejection tests for non-positive `font_size`, `line_width`, and `save_dpi`.
- [ ] Add pytest and Ruff as development-only optional dependencies in `pyproject.toml`; configure Ruff for Python 3.9, 88-character lines, and E/F/I lint rules.
- [ ] Run `python -m pip install -e '.[dev]'`.
- [ ] Run `pytest -q` and confirm the new behavior tests pass against the existing API.
- [ ] Apply Ruff formatting to the Python module and tests; tidy README spacing while preserving its bilingual text and example behavior.
- [ ] Run `ruff check .`, `ruff format --check .`, and `pytest -q`.
- [ ] Commit Task 1 as `test: cover plotting helper behavior`.

### Task 2: Add continuous integration and project notes

**Files:**
- Create: `.github/workflows/ci.yml`
- Create: `docs/superpowers/specs/2026-11-07-research-figure-kit-maintenance-design.md`
- Create: `docs/superpowers/plans/2026-11-07-research-figure-kit-maintenance.md`

**Interfaces:**
- Consumes: the `.[dev]` extra and the commands verified in Task 1.
- Produces: a CI job that checks Python 3.9 and Python 3.14 on pushes and pull requests.

- [ ] Create a workflow triggered by `push` and `pull_request`, running on `ubuntu-latest` with a Python matrix of `['3.9', '3.14']`.
- [ ] Use `actions/checkout@v7` and `actions/setup-python@v7`.
- [ ] Install the package with `python -m pip install -e '.[dev]'`.
- [ ] Run `ruff check .`, `ruff format --check .`, and `pytest -q` in CI.
- [ ] Add the approved design and this plan to the two paths above.
- [ ] Review the final diff for API, runtime dependency, and README scope changes.
- [ ] Commit Task 2 as `ci: add maintenance checks`.
- [ ] Check the resulting GitHub Actions run and report its result.
