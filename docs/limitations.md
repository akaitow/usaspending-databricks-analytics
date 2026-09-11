# Limitations and validation

## What was checked for this portfolio edition

- Read the Python/SQL code and original saved outputs in both supplied Databricks notebooks.
- Extracted the featured aggregate tables without changing numeric values. Renamed `contract_count` to `transaction_count` in the CSV exports to reflect the actual row grain.
- Checked that saved award-type counts sum to the saved total of 5,804,212 transactions.
- Checked that the source and projected row counts agree.
- Executed notebook 03's Python cells sequentially against the included aggregates and inspected the resulting charts.
- Checked notebook JSON structure, Python syntax, local links, and the packaged file inventory. A Jupyter kernel/schema-library validation was unavailable in the authoring environment; notebook 03 was executed through the included Python runner.
- Inspected both generated chart images. A full rendered notebook-viewer inspection was unavailable; open the notebooks in GitHub or Jupyter to confirm the final notebook presentation.

The original Databricks transformations and SQL queries were **not rerun** during portfolio preparation. Their saved outputs are evidence of the original execution, not independent verification of source completeness or current results.

## Four exploratory KPIs excluded from the featured notebook

| Original KPI | Why it needs more work |
|---|---|
| Average contract value | Averaging award totals across transaction rows weights awards with more transactions more heavily. Define the award grain and select a defensible award snapshot first. |
| Total potential award value | Adding award-level ceiling values across transactions can repeatedly count the same award. No defensible government-wide exposure total follows from that sum. |
| Average offers received | The saved average is approximately 99.36. Before interpreting it, inspect field codes, nulls, special values, and distribution; a successful numeric cast is insufficient validation. |
| Days from solicitation to action | The action date can describe an amendment or other transaction, so this is not automatically solicitation-to-initial-award cycle time. Define eligible actions and check date validity. |

## Preparation and source boundaries

- The source managed table retains all columns. The projected table drops award and transaction identifiers; use the source table to check uniqueness and to calculate distinct-award metrics.
- The null exclusion threshold is an absolute count of 4,000,000. It is specific to the original snapshot and should be revisited when volume changes.
- Dropping low-variance columns or all columns containing `_id`/`_code` can remove valuable fields. These are original project rules, not a universal cleaning policy.
- No transaction-key deduplication, full source reconciliation, schema-drift check, or coded-missing-value audit was supplied.
- Rare saved award-type labels such as `GA-02`, `GA-12`, `B`, and `AL-02` need validation against the original records. Possible explanations include malformed values or CSV parsing/schema issues; none is established from aggregate outputs alone. Check quoted multiline fields, delimiters, and row alignment during source re-ingestion.
- The source filename references FY2025 and contains `20251108`. That token does not establish exact query execution time, completeness, or all download filters.
- Agency and industry outputs are top-10 extracts. They cannot independently reproduce the grand total or the long tail.
- The 59.38% competition measure covers one exact category. Its numerator cannot be reconstructed exactly from the saved rounded percentage alone.
- No realized cost savings, improved accuracy, or performance speedup was measured in the supplied notebooks.

## Next validation steps in Databricks

1. Confirm source download filters, schema, transaction grain, and the original snapshot.
2. Check null and duplicate transaction keys in the full source table; investigate duplicates before deciding whether to exclude them.
3. Confirm competition-category semantics and offers-received codes from the data dictionary.
4. For award-level metrics, define a snapshot rule and validate repeated award totals before aggregation.
5. Re-execute notebooks 01 and 02 in a dedicated project namespace, then refresh the aggregate CSVs and notebook 03 outputs together.
