# Data Quality Audit Toolkit

> Reusable validation layer for analytics datasets covering schema, nulls, duplicates, ranges, business rules, and KPI reconciliation.

## Business Problem

A dashboard or report is only as trustworthy as the data feeding it. The toolkit turns common analytical failure modes into repeatable pre-publication controls.

## Analytical Questions

- Are required fields present and correctly typed?\n- How much missingness or duplication exists?\n- Do business rules and ranges hold?\n- Do source totals reconcile to reporting totals?\n- Which failures can materially change KPIs?

## Deliverables

- Schema checks\n- Missingness report\n- Duplicate detection\n- Range and business-rule tests\n- Referential-integrity checks\n- Source-to-report reconciliation\n- Pass/review/fail summary

## Suggested Repository Structure

```text
data-quality-audit-toolkit/
├── data/
├── notebooks/
├── src/
├── tests/
├── outputs/
├── README.md
└── requirements.txt
```

## Stack

Python, pandas, SQL, SQLite/DuckDB concepts, pytest

## Method

1. Define the decision context and metric definitions.
2. Profile and validate the data.
3. Build reproducible transformations and calculations.
4. Quantify the main drivers, scenarios, or failure modes.
5. Validate outputs and document limitations.
6. Produce an executive-ready decision narrative.

## Portfolio Standard

Use synthetic or public data with documented provenance. Clearly distinguish measured results from assumptions and illustrative scenarios.
