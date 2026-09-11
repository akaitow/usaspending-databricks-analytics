# Reproduce the project

## Local charts from included aggregates

Install Python 3.10 or later, then run the commands in the repository README. The authoring run used Python 3.12. The runner uses the repository root as its working directory and executes only notebook 03. It writes notebook cell outputs and regenerates `images/agency_obligations.png` and `images/award_type_transactions.png`.

For a Jupyter interface, install `jupyterlab`, open notebook 03, and run all cells. To validate all notebook schemas, install `nbformat` and run:

```bash
python -c "import pathlib, nbformat; [nbformat.validate(nbformat.read(p, as_version=4)) for p in pathlib.Path('notebooks').glob('*.ipynb')]; print('Notebook schemas validated')"
```

## Full source workflow in Databricks

1. Obtain the FY2025 contract CSV snapshot used in the original project. The filename pattern was `FY2025_All_Contracts_Full_20251108_*.csv`. Start with the [USAspending award data archive](https://www.usaspending.gov/download_center/award_data_archive). Current downloads may differ; the raw source files and exact download filters are not included here.
2. Create a dedicated writable Databricks catalog/schema and a volume for the CSV parts. Use a Databricks environment with Spark, SQL notebooks, and the required table/volume permissions. The original runtime version was not recorded.
3. Import notebooks 01 and 02 into your workspace using [Databricks notebook import](https://docs.databricks.com/aws/en/notebooks/notebook-export-import).
4. In notebook 01, replace the `/Volumes/workspace/usaspending/usa_cvs/...` input path and both `workspace.usaspending` output-table references with your dedicated namespace. The original code uses `overwrite` writes.
5. Run notebook 01 from top to bottom. Review dimensions, null counts, dominant-value fractions, and exclusions. Retain the full source table for key-based validation.
6. Update notebook 02 to the same prepared-table namespace, then run all SQL cells. Compare metric definitions with `docs/metric_definitions.md` before interpreting outputs.
7. Export the selected aggregate results to the corresponding `data/` CSVs. Update `summary.json` and provenance with the new source date and filters; do not mix a new table extract with old summary values.
8. Run notebook 03 or `python scripts/run_showcase.py` to regenerate charts.

Notebooks 01 and 02 cannot be fully reproduced from this repository alone because the raw 5.8-million-row CSV extract and Databricks environment are not included. A later source download may legitimately produce different counts and values.
