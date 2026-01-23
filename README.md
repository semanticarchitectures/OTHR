# OTHR Framework

This repository contains research, models, and reference materials for the OTHR
(Over-the-Horizon Radar) parametric framework. Documents are marked
**UNCLASSIFIED // PUBLIC RELEASE**.

## File Summaries

- `OTHR_Executive_Summary.md`: program overview with key findings. Highlights
  a $1.7B acquisition estimate for a 3-site system, a 10.1-year timeline to
  full capability, performance ranges (1,000-3,000 km), and top risks.
- `OTHR_Research_Summary.md`: comprehensive research base covering reference
  systems (ROTHR, JORN), OTHR fundamentals, Arctic environment impacts, threat
  context, and cost/schedule baselines.
- `OTHR_System_Architecture.md`: high-level system architecture with a Mermaid
  diagram, component descriptions, interfaces, and data-flow detail.
- `OTHR_User_Guide.md`: full operator/analyst guide with usage steps, parameter
  update procedures, interpretation guidance, and transition guidance to a
  government-refined version.
- `OTHR_coverage_model.py`: parametric Python model (numpy/matplotlib) that
  computes coverage, simulates performance impacts (aurora degradation), and
  generates plots and summaries.
- `OTHR_Coverage_Map.png`: generated coverage map showing site overlap and
  coverage zones across the Arctic.
- `OTHR_Performance_Curves.png`: generated detection probability curves across
  range and conditions (clear vs auroral).
- `OTHR_Cost_Model.csv`: parametric cost model with a WBS, Arctic multiplier,
  and FY2026 cost roll-ups (baseline total acquisition ~ $1,735M).
- `OTHR_Schedule_Model.csv`: program schedule with phases, dependencies, and
  critical path markers (baseline 121 months to FOC).
- `OTHR_Risk_Register.csv`: 36-risk register with likelihood/impact scoring,
  priorities, and mitigation owners.

## Quick Start

1. Review the summaries in `OTHR_Executive_Summary.md` and `OTHR_Research_Summary.md`.
2. Open `OTHR_User_Guide.md` for usage details.
3. Run the coverage model (optional):

```
python3 OTHR_coverage_model.py
```

## Notes

- CSV files are intended to be opened in a spreadsheet or imported into analysis tools.
- PNG files are static outputs referenced by the documentation.

