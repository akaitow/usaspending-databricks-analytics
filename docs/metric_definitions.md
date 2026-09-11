# Metric definitions

All metrics refer to the source snapshot in the supplied notebooks. A record is a procurement transaction. Missing values are not automatically zero.

| Metric | Calculation and unit | Interpretation and limitation |
|---|---|---|
| Transaction volume | `COUNT(*)`; rows | Measures recorded activity, not distinct awards. The original alias `number_of_contracts` is historical. |
| Transaction obligations | `SUM(federal_action_obligation)`; USD | Includes negative adjustments. Measures obligations, not outlays. Duplicate transaction checks are still required. |
| Agency obligations | Sum transaction obligations by `awarding_agency_name`; USD | The saved output contains only the top 10 groups. |
| Full/open competition category share | Rows with `extent_competed = 'FULL AND OPEN COMPETITION'` divided by all rows, multiplied by 100 | An exact-category transaction share. Does not include every possible competed category. Missing/other categories remain in the denominator. |
| Award-type activity | Count rows by `award_type` | Retains missing categories. Award type and contract pricing type are different attributes. |
| Industry obligations and activity | Sum obligations and count rows by `naics_description` | Saved output is top 10 industries by obligations; count aliases refer to transaction rows. |

## Data-preparation diagnostics

**Null count:** SQL `IS NULL` count per column. Empty strings and coded missing values are not automatically included.

**Dominant-value share:** Frequency of the most common non-null value divided by the count of non-null observations. A share above 95% triggered exclusion in the original projection. Rare values may still matter for a business question.

**Column reduction:** 297 source columns to 48 projected columns. This demonstrates selection, not a measured gain in model quality, runtime, or data accuracy.
