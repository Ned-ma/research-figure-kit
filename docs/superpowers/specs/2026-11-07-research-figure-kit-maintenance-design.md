# research-figure-kit Maintenance Upgrade

## Intent

Make the existing Matplotlib helper package easier to maintain and safer to change, without expanding its user-facing API.

## Goals

- Reformat the Python module and README for normal project readability.
- Add focused tests for `figure_size()` conversion and validation, and for `paper_style()` applying settings only within its context and restoring prior Matplotlib settings afterward.
- Add development-only tooling and a GitHub Actions workflow that installs the package, runs formatting/lint checks, and runs the test suite on the minimum supported Python version plus a current stable version.

## Non-goals

- No new plotting or export functions.
- No changes to the public function names, signatures, runtime dependencies, or MIT license.
- No PyPI release or publishing workflow.
- No claims that the defaults meet any journal's submission requirements.

## Approaches

1. **Maintenance base (chosen):** clean up formatting, add focused tests, and run them with lint checks in CI. This improves change confidence without adding a new feature surface.
2. **Feature expansion:** add an export helper such as `save_figure()`. This would add a new public API and needs separate decisions about formats, naming, and save options.
3. **Package release setup:** prepare a PyPI release workflow. This adds publishing configuration and account setup that are outside the selected maintenance scope.

## Constraints and implementation calls

- Preserve Python `>=3.9` and current runtime dependencies.
- Use `pytest` and Ruff as development tools only.
- Test existing documented behavior: millimeter-to-inch conversion, rejection of non-positive dimensions/style values, style values inside the context, and restoration after exit.
- CI will test Python 3.9 and a current stable Python release; the workflow will run on pushes and pull requests.
- Keep the public README bilingual and make its code examples match the tested API.

## Acceptance

The public API and runtime dependency set remain unchanged; the focused test suite and Ruff checks pass locally; GitHub Actions reports success for the supported Python matrix.
