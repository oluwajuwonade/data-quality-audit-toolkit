from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from validate import validate_table

ROOT = Path(__file__).resolve().parents[1]
DATA, OUTPUTS = ROOT / "data", ROOT / "outputs"
DATA.mkdir(exist_ok=True); OUTPUTS.mkdir(exist_ok=True)


def main() -> None:
    # Illustrative audit fixture: deliberately includes one null, one duplicate, and one invalid amount.
    raw = pd.DataFrame({
        "order_id": [1001, 1002, 1003, 1003, 1005, 1006, 1007, 1008],
        "customer_id": ["C01", "C02", "C03", "C03", "C05", "C06", "C07", "C08"],
        "order_date": pd.to_datetime(["2026-01-03", "2026-01-05", "2026-01-08", "2026-01-08", "2026-01-12", "2026-01-14", "2026-01-17", "2026-01-19"]),
        "region": ["North", "South", "East", "East", "West", "North", None, "South"],
        "order_value": [1200.0, 850.0, 640.0, 640.0, -90.0, 1100.0, 735.0, 920.0],
    })
    raw.to_csv(DATA / "illustrative_orders.csv", index=False)
    required = {"order_id", "customer_id", "order_date", "region", "order_value"}
    base = validate_table(raw, required)
    checks = [
        {"check": "Required columns", "status": "PASS" if not base["missing_required_columns"] else "REVIEW", "issue_count": len(base["missing_required_columns"])},
        {"check": "Duplicate rows", "status": "PASS" if base["duplicate_rows"] == 0 else "REVIEW", "issue_count": base["duplicate_rows"]},
        {"check": "Null cells", "status": "PASS" if base["null_cells"] == 0 else "REVIEW", "issue_count": base["null_cells"]},
        {"check": "Positive order value", "status": "PASS" if (raw["order_value"] > 0).all() else "REVIEW", "issue_count": int((raw["order_value"] <= 0).sum())},
        {"check": "Unique order IDs", "status": "PASS" if raw["order_id"].is_unique else "REVIEW", "issue_count": int(raw["order_id"].duplicated().sum())},
    ]
    check_df = pd.DataFrame(checks)
    check_df.to_csv(OUTPUTS / "audit_checks.csv", index=False)
    profile = pd.DataFrame({"metric": ["rows", "columns", "null_cells", "duplicate_rows", "failed_checks"], "value": [len(raw), len(raw.columns), base["null_cells"], base["duplicate_rows"], int((check_df.status == "REVIEW").sum())]})
    profile.to_csv(OUTPUTS / "audit_profile.csv", index=False)
    (OUTPUTS / "audit_summary.md").write_text(f"""# Executive Summary — Illustrative Data Quality Audit\n\n**Scope:** Deliberately imperfect synthetic order data used to demonstrate pre-publication controls.\n\n## Result\n\n- **{len(check_df[check_df.status == 'PASS'])} checks passed** and **{len(check_df[check_df.status == 'REVIEW'])} checks require review**.\n- The fixture contains **{base['null_cells']} null cell**, **{base['duplicate_rows']} duplicate row**, and **{int((raw['order_value'] <= 0).sum())} non-positive order value**.\n\n## Decision readout\n\nThe dataset should not feed a production KPI report until the duplicate order, missing region, and invalid order value are resolved or explicitly quarantined. The audit is intentionally designed to show both pass and review states rather than only a clean happy path.\n\n## Limitations\n\nThis is an illustrative synthetic fixture. It does not cover referential integrity against a customer master, date freshness, currency consistency, or source-to-report reconciliation.\n""")

    plt.style.use("seaborn-v0_8-whitegrid")
    colors = ["#15803D" if x == "PASS" else "#C2413B" for x in check_df.status]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.barh(check_df["check"], check_df["issue_count"], color=colors)
    ax.set_title("Illustrative Data Quality Audit Findings", loc="left", weight="bold")
    ax.set_xlabel("Issue count (zero indicates pass)")
    for i, (count, status) in enumerate(zip(check_df.issue_count, check_df.status)):
        ax.text(max(count, 0.03) + 0.05, i, status, va="center", weight="bold", color="#334155")
    fig.tight_layout(); fig.savefig(OUTPUTS / "audit_findings.png", dpi=180); plt.close(fig)

    region_nulls = raw.assign(region=raw.region.fillna("Missing")).groupby("region", dropna=False).size()
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.bar(region_nulls.index, region_nulls.values, color="#2563EB")
    ax.set_title("Illustrative Orders by Region", loc="left", weight="bold")
    ax.set_ylabel("Rows"); ax.set_xlabel("")
    fig.tight_layout(); fig.savefig(OUTPUTS / "orders_by_region.png", dpi=180); plt.close(fig)


if __name__ == "__main__":
    main()
