# Executive Summary — Illustrative Data Quality Audit

**Scope:** Deliberately imperfect synthetic order data used to demonstrate pre-publication controls.

## Result

- **1 checks passed** and **4 checks require review**.
- The fixture contains **1 null cell**, **1 duplicate row**, and **1 non-positive order value**.

## Decision readout

The dataset should not feed a production KPI report until the duplicate order, missing region, and invalid order value are resolved or explicitly quarantined. The audit is intentionally designed to show both pass and review states rather than only a clean happy path.

## Limitations

This is an illustrative synthetic fixture. It does not cover referential integrity against a customer master, date freshness, currency consistency, or source-to-report reconciliation.
