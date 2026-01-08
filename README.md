# Mini Wrangling for a School Decision

A **data-driven decision support project** that integrates crime statistics, university program/location data, and startup ecosystem rankings to shortlist universities for a military veteran pursuing **IT / MIS programs**.

**Impact:** Reduced **25 universities → 2 optimal finalists** using transparent, percentile-based decision rules.

---

## Project Overview

**Scenario**  
Robert has completed military service and is applying to universities with **Management Information Systems (MIS) / Information Technology (IT)** programs.  
He prefers:

- **Safe cities**
- **Metropolitan (urban) environments**
- **Strong entrepreneurship ecosystems**

This project builds a **reproducible data wrangling pipeline** to support that decision using objective, explainable criteria.

---

## Decision Criteria

- **Safety**  
  Cities with total crime volume **below the 50th percentile**

- **Urban environment**  
  Universities located in **non-rural / metropolitan** areas

- **Entrepreneurship**  
  Cities ranked in the **top 25% startup ecosystems**

---

## What I Built

- Percentile-based filtering (no hard-coded magic numbers)
- Data cleaning & type normalization
- Multi-table joins across heterogeneous datasets
- Ranked decision table for transparent final selection

---

## Project Description

This project implements a **decision-support workflow** that combines:

- City-level crime statistics  
- University program and location data  
- Metro-area startup ecosystem rankings  

Instead of arbitrary cutoffs, the pipeline uses **percentile thresholds** to keep decisions statistically meaningful:

- Cities must fall **below the median (50th percentile)** of total crime
- Startup ecosystems must rank in the **top 25%**
- Universities must be **urban** and show **IT/MIS program presence** (`PCIP11 != 0`)

All datasets are merged into a single ranked output that clearly explains *why* each university qualifies.

**Result:**  
Narrowed **25 universities → 2 optimal candidates**  
**MIT** and **Carnegie Mellon University**

---

## Datasets & Files

| File | Type | Key Fields | Purpose |
|---|---|---|---|
| `Crime.csv` | CSV | `City`, `ViolentCrime`, `PropertyCrime`, `Burglary`, `Theft` | Compute `total_crimes`, filter cities below 50th percentile |
| `University_info.xlsb` | Excel (binary) | `UNITID`, `INSTNM`, `CITY`, `STABBR`, `LOCALE`, `PCIP11` | Identify urban universities with IT/MIS programs |
| `Dictionary for University_info.csv` | Schema | `LOCALE` definitions | Prevent misinterpretation of coded fields |
| `metro_startup_ranking.csv` | CSV | `Metro Area Main City`, `Startup Rank` | Filter top 25% startup ecosystems |

**Join keys**

```text
University.CITY → Crime.City → Metro Area Main City
```
City name normalization was applied to avoid silent join mismatches.

---

## Technical Skills Demonstrated
**Primary**
- **Python** – scripting & reproducible analysis
- **pandas** – filtering, merging, ranking
- **Data wrangling** – clean → transform → join → output
- **Statistical reasoning** – percentile-based decisions

**Secondary**
- Matplotlib – decision-boundary visualization
- NumPy – numerical operations
- Git / GitHub – version control and sharing

---

## Data Pipeline Architecture
```text
Raw Data (4 files)
   ↓
Data Cleaning & Transformation
   ↓
Percentile-Based Filtering
   ↓
Multi-Table JOIN Operations
   ↓
Composite Scoring & Ranking
   ↓
Final Recommendations
```
Each stage maps directly to an explicit decision requirement.

---

## Key Features
**Percentile-Based Decision Rules**
- Safety based on dataset-wide crime distribution
- Entrepreneurship based on relative startup rankings
- Scales naturally as datasets grow

**Join-First Decision Table Design**
- Unified view of all candidate universities
- Standardized city naming
- Output optimized for real-world decision-making

---

## Code Highlights
**1️. Percentile-Based Filtering**
```python
crime_threshold = crime_df["total_crimes"].quantile(0.50)
safe_cities = crime_df[crime_df["total_crimes"] < crime_threshold]
```
**2. Multi-Table Merge**
```python
final_candidates = pd.merge(
    universities_with_startups,
    safe_cities,
    on=["city", "state"],
    how="inner"
)
```
**3. Composite Scoring (Example)**
```python
final_candidates["composite_score"] = (
    norm_crime * 0.4 +   # 40% safety
    norm_rank  * 0.6    # 60% entrepreneurship
)
```
**Why normalization matters:**
Crime volume and startup rank exist on different scales. Normalization ensures fair weighting.

---

## Metrics & Results
Metric|	Value|
---|---
Total Cities Analyzed	|25
Total Universities Analyzed	|25
Safe Cities Identified|	12 (48%)
Urban IT Universities|	24 (96%)
Top Startup Universities|	7 (28%)
**Final Candidates**|	**2 (8%)**
**Data Reduction Rate**|	**92%**

---

## Final Ranked Universities
Rank|	City|	State|	University|	PCIP11|	Total Crime|	Startup Rank
---|---|---|---|---|---|---|
1|	Boston|	MA|	MIT|	0.2834|	15,234|	#1
2|	Pittsburgh|	PA|	Carnegie Mellon University|	0.3156	|13,234|	#3

**Ranking logic:**
Lower crime → better startup rank → stronger IT program signal.
