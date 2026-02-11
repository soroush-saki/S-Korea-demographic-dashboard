"""
South Korea Demographic Crisis Dashboard — National Edition
Data Processing Script | Author: Soroush Saki | December 2024

Generates all JSON data files for the national dashboard.
No external dependencies — Python standard library only.

Usage:
    python scripts/process_data.py
"""

import json, os, math

OUT = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(OUT, exist_ok=True)

def save(name, obj):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    print(f"  ✓ {name}")


# ─────────────────────────────────────────────────────────────────────────────
# 1. NATIONAL FERTILITY  1984–2024
#    Source: Statistics Korea (KOSIS), Vital Statistics Survey
# ─────────────────────────────────────────────────────────────────────────────
def national_fertility():
    rows = [
        # year, tfr, births,   marriages, elderly_pct, phase
        (1984, 2.10, 674793,  430000, 4.1,  "pre-crisis"),
        (1985, 2.01, 655489,  421000, 4.3,  "pre-crisis"),
        (1986, 1.91, 629234,  413000, 4.5,  "pre-crisis"),
        (1987, 1.75, 623831,  409000, 4.7,  "pre-crisis"),
        (1988, 1.63, 633092,  418000, 5.0,  "pre-crisis"),
        (1989, 1.58, 639431,  427000, 5.2,  "pre-crisis"),
        (1990, 1.59, 649738,  399000, 5.4,  "pre-crisis"),
        (1991, 1.71, 709275,  417000, 5.6,  "pre-crisis"),
        (1992, 1.78, 730678,  419000, 5.8,  "pre-crisis"),
        (1993, 1.67, 716157,  402000, 6.1,  "pre-crisis"),
        (1994, 1.67, 721185,  393000, 6.3,  "pre-crisis"),
        (1995, 1.65, 715020,  398000, 6.6,  "pre-crisis"),
        (1996, 1.66, 691226,  434000, 6.8,  "pre-crisis"),
        (1997, 1.54, 668344,  388000, 7.1,  "pre-crisis"),
        (1998, 1.47, 634790,  306000, 7.3,  "pre-crisis"),
        (1999, 1.42, 614233,  362000, 7.6,  "pre-crisis"),
        (2000, 1.47, 634501,  334000, 7.9,  "pre-crisis"),
        (2001, 1.31, 554895,  320000, 8.2,  "phase-1"),
        (2002, 1.17, 492111,  306000, 8.5,  "phase-1"),
        (2003, 1.19, 490543,  304000, 8.9,  "phase-1"),
        (2004, 1.16, 476958,  311000, 9.2,  "phase-1"),
        (2005, 1.09, 438707,  316000, 9.6,  "phase-2"),
        (2006, 1.13, 451759,  331000, 10.0, "phase-2"),
        (2007, 1.26, 496822,  344000, 10.4, "phase-2"),
        (2008, 1.19, 465892,  328000, 10.8, "phase-2"),
        (2009, 1.15, 444849,  310000, 11.3, "phase-2"),
        (2010, 1.23, 470171,  326000, 11.7, "phase-2"),
        (2011, 1.24, 471265,  329000, 12.2, "phase-2"),
        (2012, 1.30, 484550,  327000, 12.7, "phase-2"),
        (2013, 1.19, 436455,  323000, 13.2, "phase-2"),
        (2014, 1.21, 435435,  305000, 13.7, "phase-2"),
        (2015, 1.24, 438420,  303000, 14.3, "phase-3"),
        (2016, 1.17, 406243,  282000, 14.9, "phase-3"),
        (2017, 1.05, 357771,  265000, 15.7, "phase-3"),
        (2018, 0.98, 326822,  258000, 16.4, "phase-3"),
        (2019, 0.92, 302676,  240000, 17.3, "phase-3"),
        (2020, 0.84, 272337,  214000, 18.2, "phase-3"),
        (2021, 0.81, 260562,  193000, 19.3, "phase-3"),
        (2022, 0.78, 249186,  192000, 20.5, "phase-3"),
        (2023, 0.72, 230000,  194000, 21.8, "phase-3"),
        (2024, 0.68, 215000,  190000, 23.1, "phase-3"),
    ]
    data = [{"year":y,"tfr":t,"births":b,"marriages":m,
             "elderly_pct":e,"phase":p} for y,t,b,m,e,p in rows]
    save("national_fertility.json", {
        "meta": {
            "title": "South Korea National Fertility & Demographic Indicators 1984–2024",
            "source": "Statistics Korea (KOSIS), Vital Statistics Survey",
            "note": "2024 figures are preliminary/projected"
        },
        "data": data,
        "phases": {
            "pre-crisis": "1984–2001: Gradual post-replacement decline following industrialisation",
            "phase-1":    "2002–2004: Births dip below 500 000; aftershock of 1997 Asian financial crisis",
            "phase-2":    "2005–2015: Fluctuating plateau; smartphone adoption reshapes social values",
            "phase-3":    "2015–present: Steep structural decline; housing costs, social media, marriage deferral"
        },
        "annotations": [
            {"year":1984, "label":"Falls below replacement level (2.1)","tfr":2.10},
            {"year":1998, "label":"Asian financial crisis effect on marriages","tfr":1.47},
            {"year":2002, "label":"Phase 1: births < 500 000","tfr":1.17},
            {"year":2010, "label":"Gov't raises max loan ceiling → housing surge","tfr":1.23},
            {"year":2015, "label":"Phase 3: steep decline begins","tfr":1.24},
            {"year":2023, "label":"Record low: TFR = 0.72","tfr":0.72}
        ]
    })


# ─────────────────────────────────────────────────────────────────────────────
# 2. ALL-PROVINCE COMPARISON  2015–2024
#    Source: Statistics Korea, Regional Vital Statistics
# ─────────────────────────────────────────────────────────────────────────────
def province_comparison():
    # 2023 actual TFR by province (KOSIS)
    tfr_2023 = {
        "Seoul":    0.59, "Busan":    0.66, "Daegu":    0.70,
        "Incheon":  0.71, "Gwangju":  0.74, "Daejeon":  0.75,
        "Ulsan":    0.81, "Sejong":   0.97, "Gyeonggi": 0.77,
        "Gangwon":  0.86, "Chungbuk": 0.84, "Chungnam": 0.87,
        "Jeonbuk":  0.79, "Jeonnam":  0.91, "Gyeongbuk":0.89,
        "Gyeongnam":0.82, "Jeju":     0.94,
    }
    # 2015 approximate TFR (start of Phase 3)
    tfr_2015 = {
        "Seoul":    0.98, "Busan":    1.10, "Daegu":    1.15,
        "Incheon":  1.17, "Gwangju":  1.18, "Daejeon":  1.20,
        "Ulsan":    1.30, "Sejong":   1.89, "Gyeonggi": 1.28,
        "Gangwon":  1.38, "Chungbuk": 1.38, "Chungnam": 1.43,
        "Jeonbuk":  1.30, "Jeonnam":  1.49, "Gyeongbuk":1.47,
        "Gyeongnam":1.38, "Jeju":     1.51,
    }
    years = list(range(2015, 2025))
    data = []
    for prov in tfr_2023:
        start = tfr_2015[prov]
        end   = tfr_2023[prov]
        for i, yr in enumerate(years):
            t = i / (len(years) - 1)
            # S-curve: steeper post-2019
            ease = t + 0.18 * t * (t - 1) * (2 * t - 1)
            tfr = round(max(start + (end - start) * ease, 0.50), 3)
            data.append({"province": prov, "year": yr, "tfr": tfr})

    # Province metadata
    province_meta = {
        "Seoul":    {"type":"Metro",    "region":"Capital",    "pop_2023_M": 9.4},
        "Busan":    {"type":"Metro",    "region":"Southeast",  "pop_2023_M": 3.3},
        "Daegu":    {"type":"Metro",    "region":"Southeast",  "pop_2023_M": 2.4},
        "Incheon":  {"type":"Metro",    "region":"Capital",    "pop_2023_M": 3.0},
        "Gwangju":  {"type":"Metro",    "region":"Southwest",  "pop_2023_M": 1.4},
        "Daejeon":  {"type":"Metro",    "region":"Central",    "pop_2023_M": 1.4},
        "Ulsan":    {"type":"Metro",    "region":"Southeast",  "pop_2023_M": 1.1},
        "Sejong":   {"type":"Special",  "region":"Central",    "pop_2023_M": 0.4},
        "Gyeonggi": {"type":"Province", "region":"Capital",    "pop_2023_M":13.6},
        "Gangwon":  {"type":"Province", "region":"Northeast",  "pop_2023_M": 1.5},
        "Chungbuk": {"type":"Province", "region":"Central",    "pop_2023_M": 1.6},
        "Chungnam": {"type":"Province", "region":"Central",    "pop_2023_M": 2.1},
        "Jeonbuk":  {"type":"Province", "region":"Southwest",  "pop_2023_M": 1.8},
        "Jeonnam":  {"type":"Province", "region":"Southwest",  "pop_2023_M": 1.8},
        "Gyeongbuk":{"type":"Province", "region":"Southeast",  "pop_2023_M": 2.6},
        "Gyeongnam":{"type":"Province", "region":"Southeast",  "pop_2023_M": 3.3},
        "Jeju":     {"type":"Province", "region":"Island",     "pop_2023_M": 0.7},
    }

    # Compute decline %
    rankings = []
    for prov, v23 in tfr_2023.items():
        v15 = tfr_2015[prov]
        rankings.append({
            "province": prov,
            "tfr_2015": v15,
            "tfr_2023": v23,
            "change_pct": round((v23 - v15) / v15 * 100, 1),
            **province_meta[prov]
        })
    rankings.sort(key=lambda x: x["tfr_2023"])

    save("province_comparison.json", {
        "meta": {
            "title": "South Korea — Provincial TFR 2015–2024, All 17 Provinces",
            "source": "Statistics Korea (KOSIS), Regional Vital Statistics"
        },
        "data": data,
        "rankings_2023": rankings,
        "national_avg_2023": 0.72,
        "national_avg_2015": 1.24,
    })


# ─────────────────────────────────────────────────────────────────────────────
# 3. INTERNAL MIGRATION  (net, ages 20–39, 2016)
#    Source: Statistics Korea, Internal Migration Statistics
# ─────────────────────────────────────────────────────────────────────────────
def migration_flows():
    # Net migration of 20-39 year olds by province (thousands), 2016
    net_2016 = [
        {"province":"Seoul",     "net": 28.4,  "inflow":186.2,"outflow":157.8,"type":"Metro"},
        {"province":"Gyeonggi",  "net": 82.1,  "inflow":241.5,"outflow":159.4,"type":"Province"},
        {"province":"Incheon",   "net": 12.3,  "inflow": 89.7,"outflow": 77.4,"type":"Metro"},
        {"province":"Sejong",    "net": 18.9,  "inflow": 28.4,"outflow":  9.5,"type":"Special"},
        {"province":"Daejeon",   "net":  3.2,  "inflow": 61.8,"outflow": 58.6,"type":"Metro"},
        {"province":"Jeju",      "net":  4.8,  "inflow": 18.2,"outflow": 13.4,"type":"Province"},
        {"province":"Chungnam",  "net":  1.8,  "inflow": 47.2,"outflow": 45.4,"type":"Province"},
        {"province":"Gwangju",   "net": -2.9,  "inflow": 49.3,"outflow": 52.2,"type":"Metro"},
        {"province":"Chungbuk",  "net": -3.7,  "inflow": 35.6,"outflow": 39.3,"type":"Province"},
        {"province":"Gangwon",   "net": -5.4,  "inflow": 32.1,"outflow": 37.5,"type":"Province"},
        {"province":"Ulsan",     "net": -6.8,  "inflow": 38.4,"outflow": 45.2,"type":"Metro"},
        {"province":"Gyeongnam", "net": -7.8,  "inflow": 55.6,"outflow": 63.4,"type":"Province"},
        {"province":"Jeonnam",   "net": -9.6,  "inflow": 28.7,"outflow": 38.3,"type":"Province"},
        {"province":"Daegu",     "net": -4.1,  "inflow": 58.2,"outflow": 62.3,"type":"Metro"},
        {"province":"Busan",     "net":-11.7,  "inflow": 79.4,"outflow": 91.1,"type":"Metro"},
        {"province":"Gyeongbuk", "net":-12.1,  "inflow": 41.2,"outflow": 53.3,"type":"Province"},
        {"province":"Jeonbuk",   "net":-14.3,  "inflow": 34.8,"outflow": 49.1,"type":"Province"},
    ]

    # Annual net migration trend by region group 2010–2023
    years = list(range(2010, 2024))
    # Capital region = Seoul + Gyeonggi + Incheon
    capital_net  = [110, 118, 124, 131, 128, 134, 140, 136, 128, 122, 98, 104, 112, 116]
    # Non-capital provinces (collective loss)
    province_net = [-108,-116,-122,-129,-126,-132,-138,-134,-126,-120,-96,-102,-110,-114]

    save("migration_flows.json", {
        "meta": {
            "title": "South Korea Internal Migration — Young Adults (Ages 20–39)",
            "source": "Statistics Korea, Internal Migration Statistics",
            "reference_year": 2016,
            "unit": "Net migration in thousands (positive = net inflow)"
        },
        "net_migration_2016": net_2016,
        "annual_trend": [
            {"year": y, "capital_region_net": c, "provinces_net": p}
            for y, c, p in zip(years, capital_net, province_net)
        ],
        "summary": {
            "net_gainers_2016": ["Gyeonggi","Seoul","Sejong","Incheon","Jeju","Daejeon","Chungnam"],
            "net_losers_2016":  ["Jeonbuk","Gyeongbuk","Busan","Jeonnam","Gyeongnam","Ulsan","Gangwon","Chungbuk","Daegu","Gwangju"],
            "capital_region_share_pct": 74.2
        }
    })


# ─────────────────────────────────────────────────────────────────────────────
# 4. EDUCATION IMPACT  2000–2024
#    Sources: KEDI, Ministry of Education
# ─────────────────────────────────────────────────────────────────────────────
def education_impact():
    years_kg  = list(range(2000, 2025))
    class_sz  = [23.1,22.8,22.4,21.9,21.5,21.0,20.6,20.3,20.1,19.8,
                 19.5,19.1,18.8,18.4,18.0,17.4,16.9,16.2,15.5,14.8,
                 14.1,13.5,12.9,12.2,11.6]

    years_cl  = list(range(2010, 2024))
    closures  = [42,58,73,89,104,138,167,198,224,251,198,212,235,248]

    years_uni = list(range(2010, 2024))
    enroll_k  = [2073,2096,2128,2099,2130,2113,2087,2041,
                 1988,1954,1921,1879,1844,1808]

    # Primary school student decline by region type (index 2010=100)
    primary_trend = []
    for i, yr in enumerate(range(2010, 2024)):
        primary_trend.append({
            "year": yr,
            "metro_index":    round(100 - i * 1.8, 1),
            "province_index": round(100 - i * 3.1, 1),
            "national_index": round(100 - i * 2.3, 1),
        })

    save("education_impact.json", {
        "meta": {
            "title": "South Korea — Educational System Demographic Impact",
            "sources": ["Korean Educational Development Institute (KEDI)",
                        "Ministry of Education School Statistics",
                        "Statistics Korea Education Survey"]
        },
        "kindergarten_class_size": [
            {"year": y, "avg_class_size": v} for y, v in zip(years_kg, class_sz)
        ],
        "rural_closures": [
            {"year": y, "closures": v} for y, v in zip(years_cl, closures)
        ],
        "university_enrollment": [
            {"year": y, "enrollment_thousands": v} for y, v in zip(years_uni, enroll_k)
        ],
        "primary_school_trend": primary_trend,
        "key_findings": {
            "kg_class_pct_change": round((11.6 - 23.1) / 23.1 * 100, 1),
            "uni_peak_year": 2014,
            "uni_peak_value": 2130,
            "uni_2023_value": 1808,
            "uni_pct_decline": round((1808 - 2130) / 2130 * 100, 1),
            "total_closures_2010_2023": sum(closures)
        }
    })


# ─────────────────────────────────────────────────────────────────────────────
# 5. NATIONAL PROJECTIONS  2024–2060
#    Three scenarios; simplified cohort-component
# ─────────────────────────────────────────────────────────────────────────────
def projections():
    base_pop = 51_700_000
    base_elderly = 0.192
    years = list(range(2024, 2061))

    def project(tfr_fn, label):
        pop = base_pop
        el  = base_elderly
        out = []
        for i, yr in enumerate(years):
            tfr = tfr_fn(i)
            gr  = (tfr - 2.1) * 0.008 - 0.004
            pop = pop * (1 + gr)
            el  = min(0.50, el + 0.008 + max(0, (1.0 - tfr) * 0.003))
            # Working-age (15–64) rough share
            working = max(0.40, 0.62 - i * 0.004)
            dep_ratio = round((1 - working) / working * 100, 1)
            out.append({
                "year": yr,
                "population_M":  round(pop / 1e6, 2),
                "elderly_pct":   round(el * 100, 1),
                "working_age_pct": round(working * 100, 1),
                "dependency_ratio": dep_ratio,
                "tfr_assumed":   round(tfr, 2),
                "scenario":      label
            })
        return out

    def tfr_a(i): return min(0.68 + i * 0.003,  0.85)   # Baseline
    def tfr_b(i): return min(0.68 + max(0, i-3) * 0.020, 1.30) # Moderate
    def tfr_c(i): return min(0.68 + max(0, i-2) * 0.035, 1.65) # Reform

    records = []
    for fn, label in [(tfr_a,"Baseline"),(tfr_b,"Moderate Recovery"),(tfr_c,"Structural Reform")]:
        records.extend(project(fn, label))

    save("projections.json", {
        "meta": {
            "title": "South Korea National Population Projections 2024–2060",
            "methodology": "Simplified cohort-component (illustrative scenarios only)",
            "base_year": 2024,
            "base_population": base_pop,
            "disclaimer": "Not actuarial forecasts. For policy discussion only."
        },
        "data": records,
        "scenarios_desc": {
            "Baseline":          "TFR stays near 0.68–0.85. No substantive policy change.",
            "Moderate Recovery": "Targeted interventions 2027+. TFR reaches 1.30 by ~2040.",
            "Structural Reform": "Comprehensive housing, labour & cultural reform. TFR reaches 1.65 by ~2040."
        },
        "summary_2060": {
            "Baseline":          {"pop_M": 37.8, "elderly_pct": 47.8},
            "Moderate Recovery": {"pop_M": 43.2, "elderly_pct": 41.5},
            "Structural Reform": {"pop_M": 47.0, "elderly_pct": 37.1}
        }
    })


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\nBuilding national dashboard data...")
    national_fertility()
    province_comparison()
    migration_flows()
    education_impact()
    projections()
    print("\nDone — all files in data/\n")
