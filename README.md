# Data Quality & Analytics Assurance Framework

> **Control problem:** Can a dashboard, report, or KPI be trusted before it reaches a decision-maker?

A reusable validation layer for analytics datasets covering schema, missingness, duplicates, ranges, business rules, referential integrity, and KPI reconciliation.

## Why it matters

A polished dashboard can still be wrong when the underlying data contains structural defects. This toolkit converts common analytical failure modes into repeatable pre-publication controls.

## Validation workflow

`Decision context → Profile → Validate → Reconcile → PASS / REVIEW / FAIL → KPI reliability`

## Controls

- Schema validation
- Missingness analysis
- Duplicate detection
- Range and business-rule checks
- Referential-integrity checks
- Source-to-report reconciliation
- Check-level PASS / REVIEW / FAIL classification

## Analytical questions

1. Are required fields present and correctly typed?
2. How much missingness or duplication exists?
3. Do ranges and business rules hold?
4. Do source totals reconcile to reporting totals?
5. Which failures can materially change reported KPIs?

## Reproducible outputs

Run:

```bash
python src/generate_outputs.py
```

The project includes a deliberately imperfect synthetic order dataset so that both PASS and REVIEW states can be demonstrated.

Outputs include:

- Audit summary
- Check-level results
- Data profile
- Findings visualizations
- Executive decision guidance

## Important limitations

- The fixture is synthetic and intentionally imperfect.
- The checks cover common analytical-quality risks but are not a complete data-governance or observability system.
- Reconciliation controls depend on the availability and correctness of the comparison source and metric definitions.
- Production use would require source-specific rules, ownership, alerting, and ongoing monitoring.

## Technical stack

Python · pandas · SQL concepts · SQLite/DuckDB concepts · pytest

## Portfolio role

**Tier 2 — Analytics Infrastructure / Governance**

This project supports the broader portfolio by demonstrating that analytical results should be validated before interpretation or publication.

## Related projects

- [Business Metrics & KPI Engine](https://github.com/oluwajuwonade/business-kpi-calculator)
- [AI-Powered Retail Sales Diagnostic](https://github.com/oluwajuwonade/AI-Powered-Retail-Sales-Diagnostic)
- [AI Research & Evaluation Framework](https://github.com/oluwajuwonade/ai-research-evaluation-system)

## Author

**Oluwajuwon Adediji**  
Data & Quantitative Analyst | Analytics Quality & Decision Intelligence
