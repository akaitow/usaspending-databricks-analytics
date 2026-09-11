# Data and provenance

These are small aggregate exports from the saved HTML table outputs in Julio Hernandez's supplied Databricks notebooks. No clinical visit records, participant contact information, raw procurement rows, or Databricks credentials are included.

| File | Original notebook and zero-based cell | Contents |
|---|---|---|
| `column_missingness.csv` | `bronze_wrangling.ipynb`, cell 3 | Saved null counts by source column |
| `column_dominance.csv` | `bronze_wrangling.ipynb`, cell 4 | Most-common-value share among non-null values |
| `agency_obligations.csv` | `KPI_definition.ipynb`, cell 7 | Top 10 agencies by transaction obligations |
| `award_type_transactions.csv` | `KPI_definition.ipynb`, cell 14 | Transaction counts by award type, including missing type |
| `industry_obligations.csv` | `KPI_definition.ipynb`, cell 18 | Top 10 industries by transaction obligations |
| `summary.json` | Source mappings in `provenance.json` | Saved counts, dimensions, total obligations, and competition-category share |
| `provenance.json` | Original input-file hashes and cell references | Traceability for the exports |

Original `contract_count` columns were renamed to `transaction_count` in CSV exports. Values were not changed. Missing award-type labels are retained as `null` in the CSV and displayed as `Missing award type` in the chart.

The source code references the pattern `FY2025_All_Contracts_Full_20251108_*.csv` in a Databricks volume. The raw files, exact download settings, and source execution time were not supplied. See [USAspending's award archive](https://www.usaspending.gov/download_center/award_data_archive) for source access and [reproduction instructions](../docs/reproduce.md) for setup.

CSV float serialization may differ in the final displayed decimal from the original HTML; no extra numeric precision should be inferred. Currency displays are rounded explicitly.
