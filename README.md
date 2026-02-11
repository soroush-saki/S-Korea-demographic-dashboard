# South Korea Demographic Crisis — National Interactive Dashboard

**Research by Soroush Saki · December 2024**  
**Live:** `https://soroush-saki.github.io/sk-demographic-dashboard/`

---

## Abstract

An interactive national dashboard analysing South Korea's demographic crisis — the steepest
fertility collapse ever recorded in a peacetime economy. The dashboard extends Phase 1 static
research findings across five domains: national trend analysis, all-province comparison,
internal migration patterns, educational system impacts, and long-term population projections.

**Key findings:**
- TFR of **0.72** (2023) is globally unprecedented — Germany's 1994 post-reunification low
  was 0.77, and that decline was temporary; South Korea's is structural
- All 17 provinces are below replacement level; Seoul is the lowest at **0.59**
- 10 of 17 provinces experienced net youth outmigration in 2016, feeding capital concentration
- Kindergarten class sizes are down **49.8%** since 2000; university enrolment down **15.1%** from 2014 peak
- Under a no-change baseline, national population falls to **~37.8M by 2060** with 47.8% elderly share

---

## Dashboard Sections

| § | Title | Content |
|---|-------|---------|
| 1 | National Overview | TFR 1984–2024, marriages, aging — with three-phase framework |
| 2 | All Provinces | TFR rankings, interactive province line chart, full heatmap (all 17) |
| 3 | Internal Migration | Net migration bar (all provinces), Capital vs. provinces trend |
| 4 | Education Impact | Kindergarten class sizes, rural closures, university enrolment, primary school index |
| 5 | Future Outlook | Three population scenarios 2024–2060, elderly share, TFR assumptions |

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/soroush-saki/sk-demographic-dashboard.git
cd sk-demographic-dashboard

# 2. Generate data
python scripts/process_data.py

# 3. Preview locally
python -m http.server 8000
# → http://localhost:8000
```

**No npm. No pip installs. No build step.** Python standard library only.

---

## Deploy to GitHub Pages

```bash
git add .
git commit -m "Deploy national dashboard"
git push origin main
# GitHub → Settings → Pages → Source: main / root → Save
```

---

## Repository Structure

```
sk-demographic-dashboard/
├── index.html              ← Self-contained dashboard
├── README.md
├── .gitignore
├── data/                   ← Pre-generated JSON (commit these)
│   ├── national_fertility.json
│   ├── province_comparison.json
│   ├── migration_flows.json
│   ├── education_impact.json
│   └── projections.json
├── scripts/
│   └── process_data.py
└── docs/
    └── methodology.md
```

---

## Data Sources

| Data | Source |
|------|--------|
| National TFR, births, marriages | Statistics Korea (KOSIS), Vital Statistics Survey |
| Provincial TFR (all 17) | Statistics Korea, Regional Vital Statistics |
| Internal migration | Statistics Korea, Internal Migration Statistics |
| Kindergarten statistics | Korean Educational Development Institute (KEDI) |
| University enrolment | KEDI, Higher Education Statistics |
| Housing policy context | IMF, Republic of Korea Article IV 2010 |

---

## Citation

```
Saki, S. (2024). South Korea's Demographic Crisis: National Interactive Dashboard.
GitHub. https://github.com/soroush-saki/sk-demographic-dashboard

@misc{saki2024dashboard,
  author = {Saki, Soroush},
  title  = {South Korea's Demographic Crisis: National Interactive Dashboard},
  year   = {2024},
  url    = {https://github.com/soroush-saki/sk-demographic-dashboard}
}
```

---

*Code: MIT License · Data: Statistics Korea and KEDI terms of use*  
*Soroush Saki · github.com/soroush-saki*
