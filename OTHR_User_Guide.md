# Arctic OTHR Parametric Modeling Framework
## User Guide and Documentation

**UNCLASSIFIED // PUBLIC RELEASE**  
**Version:** 1.0 Framework  
**Date:** January 21, 2026  
**Purpose:** Support Arctic OTHR acquisition planning for northern US/Canada strategic defense

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Framework Overview](#framework-overview)
3. [Deliverable Descriptions](#deliverable-descriptions)
4. [How to Use This Framework](#how-to-use-this-framework)
5. [Updating Parameters](#updating-parameters)
6. [Interpreting Results](#interpreting-results)
7. [Transition to Government Version](#transition-to-government-version)
8. [AI Facilitator Team Demonstration](#ai-facilitator-team-demonstration)
9. [Assumptions and Limitations](#assumptions-and-limitations)
10. [References](#references)

---

## Executive Summary

This parametric modeling framework provides unclassified baseline estimates for acquiring an Arctic Over-the-Horizon Radar (OTHR) system to support NORAD modernization and strategic defense of the northern US and Canada approaches. 

**What This Framework Provides:**
- System architecture and component breakdown
- Coverage and performance models (Python-based, easily updatable)
- Cost estimates with parametric scaling ($1.7B baseline for 3-site system)
- Schedule estimates with critical path analysis (10 years to FOC)
- Risk assessment with mitigation strategies (36 risks identified)
- Complete documentation for transition to government refinement

**Key Findings:**
- **Acquisition Cost:** $1.7B for 3-site system (2.5x Arctic multiplier)
- **Timeline:** 10.1 years program start to Full Operational Capability
- **Technology Maturity:** Leverages JORN Phase 6 (world-leading OTHR)
- **Major Risks:** Indigenous consultations (highest), Arctic environment, integration complexity
- **Critical Path:** Environmental reviews and site construction drive timeline

---

## Framework Overview

### Design Philosophy

This framework is designed to be:

1. **Parametric:** All key assumptions concentrated in easily-editable parameter sections
2. **Transparent:** Clear documentation of all assumptions and data sources
3. **Portable:** Standard file formats (Markdown, Python, CSV) that work across platforms
4. **Scalable:** Models can handle 1-5+ sites with parameter adjustments
5. **Traceable:** Calculations linked to historical program data (ROTHR, JORN)

### Framework Components

```
OTHR_Framework/
├── OTHR_Research_Summary.md          # Research findings (40+ pages)
├── OTHR_System_Architecture.md       # Architecture with Mermaid diagram
├── OTHR_coverage_model.py            # Python coverage/performance calculator
├── OTHR_Coverage_Map.png             # Generated coverage visualization
├── OTHR_Performance_Curves.png       # Generated performance plots
├── OTHR_Performance_Summary.json     # Machine-readable summary statistics
├── OTHR_Cost_Model.csv               # Cost estimation spreadsheet
├── OTHR_Schedule_Model.csv           # Schedule with critical path
├── OTHR_Risk_Register.csv            # Risk assessment framework
└── OTHR_User_Guide.md                # This document
```

### Technology Baseline

**Primary Reference:** JORN Phase 6 (Australia)
- World's most sophisticated OTHR
- Proven Arctic capability (Canada purchase in March 2025)
- Open architecture for future upgrades
- $1.2B AUD upgrade over 10 years

**Secondary Reference:** ROTHR (US Navy)
- Three operational systems (Virginia, Texas, Puerto Rico)
- Mature technology (30+ years operational)
- Lower cost but less capable than JORN
- Provides domestic comparison point

---

## Deliverable Descriptions

### 1. Research Summary (OTHR_Research_Summary.md)

**Purpose:** Comprehensive compilation of OTHR technology, reference systems, Arctic challenges, and acquisition baselines.

**Contents:**
- Reference system analysis (ROTHR, JORN)
- OTHR technology fundamentals
- Arctic operational environment
- Strategic defense context (NORAD modernization)
- Cost/schedule baselines from historical programs
- Key parameters for modeling

**How to Use:**
- Read this first to understand the foundation for all models
- Reference specific sections when updating parameters
- Cite sections when briefing stakeholders
- Use as starting point for classified addendums

### 2. System Architecture (OTHR_System_Architecture.md)

**Purpose:** Define system components, interfaces, and data flows.

**Contents:**
- High-level Mermaid diagram (editable, renders in many tools)
- Component descriptions for each subsystem
- Interface specifications (NORAD, site-to-OCC, ionospheric data)
- Technology insertion points for future upgrades
- Scalability considerations

**How to Use:**
- View Mermaid diagram in compatible editors (VS Code, GitHub, Mermaid Live, etc.)
- Use as baseline for requirements documents
- Update with specific NORAD interface details
- Add classified system interfaces in government version

**Mermaid Diagram Viewing Options:**
- Online: https://mermaid.live (paste code from .md file)
- VS Code: Install Mermaid Preview extension
- GitHub/GitLab: Renders automatically in .md files
- Export to PNG/SVG from Mermaid Live for presentations

### 3. Coverage & Performance Model (OTHR_coverage_model.py)

**Purpose:** Parametric calculator for coverage areas, detection performance, and measurement accuracy.

**Requires:** Python 3.x with numpy and matplotlib

**How to Run:**
```bash
python3 OTHR_coverage_model.py
```

**Outputs:**
- `OTHR_Coverage_Map.png` - Geographic coverage visualization
- `OTHR_Performance_Curves.png` - Pd vs range for different targets/conditions
- `OTHR_Performance_Summary.json` - Summary statistics in JSON format
- Console output with performance summary

**Key Parameters (in OTHRParameters class):**
- Site locations (lat/lon/azimuth)
- Detection ranges (min/max/nominal)
- Coverage angles
- Target profiles (RCS, speed)
- Arctic degradation factors
- Commercial routes for threat modeling

**Updating Parameters:**
1. Open `OTHR_coverage_model.py` in text editor
2. Find `class OTHRParameters` near top of file
3. Edit parameter values (clearly labeled)
4. Save and re-run: `python3 OTHR_coverage_model.py`
5. New visualizations generated automatically

**Example Parameter Update:**
```python
# Change number of sites from 3 to 2
self.sites = [
    {
        'name': 'Site 1 - Western Arctic',
        'lat': 65.0,
        'lon': -165.0,
        'azimuth_center': 0,
        'coverage_angle': 120
    },
    {
        'name': 'Site 2 - Eastern Arctic',
        'lat': 68.0,
        'lon': -85.0,
        'azimuth_center': 340,
        'coverage_angle': 120
    }
]
# Delete Site 3 entry
```

### 4. Cost Model (OTHR_Cost_Model.csv)

**Purpose:** Parametric cost estimation with Work Breakdown Structure (WBS).

**Format:** CSV (opens in Excel, Google Sheets, LibreOffice, etc.)

**Structure:**
- Organized by WBS categories
- Qty × Unit Cost = Subtotal for each line item
- Automatic summaries by phase
- 20-year lifecycle cost calculation
- Comparison to historical programs
- Sensitivity analysis section

**Key Parameters:**
- Number of sites (currently 3)
- Arctic multiplier (currently 2.5x)
- Technology baseline (JORN Phase 6)
- Unit costs for major components

**Updating in Spreadsheet:**
1. Open `OTHR_Cost_Model.csv` in spreadsheet software
2. Modify values in "Qty" or "Unit Cost ($M)" columns
3. Subtotals will auto-calculate (if formulas preserved)
4. Update Arctic multiplier to see site prep cost impacts
5. Compare baseline vs accelerated scenarios

**Cost Roll-Ups:**
- Development: $75M
- Site Preparation: $150M (Arctic-driven)
- Infrastructure: $228M
- Radar Hardware: $639M (largest category)
- Software & Systems: $145M
- OCC: $95M
- Integration & Test: $96M
- Reserves: $264M (contingency)
- **Total Acquisition: $1,735M**
- **Annual O&S: $95M**
- **20-Year Lifecycle: $3,635M**

### 5. Schedule Model (OTHR_Schedule_Model.csv)

**Purpose:** Detailed schedule with phases, tasks, durations, and critical path.

**Format:** CSV (can import into MS Project, Primavera, GanttProject, Excel)

**Structure:**
- Organized by program phases (0-7)
- Task dependencies identified
- Critical path marked with (*)
- Milestone markers
- Baseline vs accelerated scenarios

**Key Timeline:**
- **Program Start to IOC:** 82 months (6.8 years, Site 1 operational)
- **Program Start to FOC:** 121 months (10.1 years, all sites operational)
- **Critical Path:** 121 months (zero slack)

**Critical Path Drivers:**
1. Environmental Impact Statement (24 months) - longest single item
2. Indigenous Consultations (18 months) - must complete before construction
3. Site 3 Construction (52 months) - sequential with Sites 1 & 2
4. IOT&E (10 months) - final certification

**Accelerated Timeline:**
- Concurrent site construction (parallel vs sequential)
- Fast-tracked environmental (12 vs 24 months, high risk)
- **Accelerated IOC:** 60 months (5.0 years)
- **Accelerated FOC:** 84 months (7.0 years)

**Creating Gantt Chart:**
- Import CSV into project management tool
- Use "Start Month" and "Duration (months)" columns
- Color-code critical path tasks
- Add resource assignments in tool

### 6. Risk Register (OTHR_Risk_Register.csv)

**Purpose:** Comprehensive risk identification with likelihood/impact scoring and mitigation strategies.

**Format:** CSV (opens in Excel, Google Sheets, risk management tools)

**Structure:**
- 36 risks identified across 10 categories
- Likelihood (1-5) × Impact (1-5) = Risk Score (1-25)
- Priority levels: Critical (15-25), High (10-14), Medium (5-9), Low (1-4)
- Mitigation strategies for each risk
- Owner assignments

**Risk Distribution:**
- Critical Priority: 13 risks (36%)
- High Priority: 19 risks (53%)
- Medium Priority: 4 risks (11%)

**Top Risks:**
1. **R010:** Indigenous consultation delays (Score: 20, Critical)
2. **R001:** Arctic ionospheric modeling inaccuracy (Score: 16, Critical)
3. **R007:** Software integration complexity (Score: 16, Critical)
4. **R009:** Environmental review delays (Score: 16, Critical)
5. **R014:** Arctic site prep cost overruns (Score: 16, Critical)

**Using the Risk Register:**
1. Review risks relevant to your area
2. Update likelihood/impact quarterly
3. Track mitigation actions to completion
4. Add new risks as identified
5. Escalate scores ≥15 to senior leadership
6. Retire risks when score ≤4 and stable

---

## How to Use This Framework

### Quick Start (30 minutes)

1. **Read Executive Summary** (5 min)
   - Understand baseline findings
   - Note key cost/schedule estimates

2. **Review System Architecture** (10 min)
   - Understand component breakdown
   - View Mermaid diagram for system overview

3. **Run Coverage Model** (5 min)
   ```bash
   python3 OTHR_coverage_model.py
   ```
   - Generates maps and performance curves
   - Review console output summary

4. **Open Cost Model** (5 min)
   - Spreadsheet with baseline $1.7B estimate
   - Understand major cost drivers

5. **Review Top 10 Risks** (5 min)
   - Focus on Critical priority items
   - Note mitigation strategies

### Detailed Analysis (2-4 hours)

1. **Read Research Summary** (30-60 min)
   - Deep dive into reference systems
   - Understand Arctic challenges
   - Review historical program data

2. **Analyze Coverage Model** (30 min)
   - Examine site placement assumptions
   - Review target detection ranges
   - Understand Arctic performance degradation

3. **Study Cost Breakdown** (30 min)
   - Line-by-line WBS review
   - Identify cost sensitivities
   - Compare to historical programs

4. **Analyze Schedule** (30 min)
   - Critical path analysis
   - Identify schedule risks
   - Consider accelerated options

5. **Risk Deep Dive** (30 min)
   - Category-by-category review
   - Assess mitigation adequacy
   - Identify gaps

### Briefing Development (4-8 hours)

1. **Executive Brief** (1-2 hours)
   - Cost/schedule/performance summary slides
   - Top 5 risks
   - Decision points

2. **Technical Brief** (2-3 hours)
   - Architecture details
   - Performance analysis
   - Technology maturity assessment

3. **Programmatic Brief** (2-3 hours)
   - Acquisition strategy
   - Schedule phasing
   - Risk management plan

---

## Updating Parameters

### Coverage Model Parameters

**Location:** `OTHR_coverage_model.py` → `class OTHRParameters`

**Most Common Updates:**

1. **Site Locations:**
```python
self.sites = [
    {
        'name': 'Site 1 - Western Arctic',
        'lat': 65.0,         # ← Change latitude
        'lon': -165.0,       # ← Change longitude
        'azimuth_center': 0, # ← Change look direction (degrees)
        'coverage_angle': 120 # ← Change coverage width
    },
    # Add or remove sites as needed
]
```

2. **Detection Ranges:**
```python
self.min_range_km = 500   # ← Skip zone
self.max_range_km = 3000  # ← Maximum range
self.nominal_range_km = 2000 # ← Design range
```

3. **Arctic Degradation:**
```python
self.aurora_degradation_factor = 0.65  # ← Performance multiplier (0-1)
self.aurora_occurrence_rate = 0.20     # ← Fraction of time affected
```

4. **Target Profiles:**
```python
self.target_profiles = {
    'Your Target Name': {
        'rcs_m2': 50,       # ← Radar cross-section
        'speed_mps': 250,   # ← Speed in m/s
        'altitude_m': 11000, # ← Altitude
        'pd_modifier': 1.0   # ← Detection multiplier (0-1)
    },
}
```

After updating, run: `python3 OTHR_coverage_model.py`

### Cost Model Parameters

**Location:** `OTHR_Cost_Model.csv`

**Most Common Updates:**

1. **Number of Sites:**
   - Find "Number of Sites" row (row 8)
   - Change "Qty" from 3 to desired number
   - All per-site costs will scale automatically

2. **Arctic Multiplier:**
   - Find "Arctic Multiplier" row (row 9)
   - Change from 2.5 to reflect site accessibility
   - Lower (1.5-2.0) for accessible sites
   - Higher (3.0-5.0) for extremely remote sites

3. **Unit Costs:**
   - Update "Unit Cost ($M)" column for any line item
   - Based on vendor quotes or refined estimates

4. **Technology Baseline:**
   - Currently assumes JORN Phase 6
   - For ROTHR baseline, reduce hardware costs ~20-30%

### Schedule Model Parameters

**Location:** `OTHR_Schedule_Model.csv`

**Most Common Updates:**

1. **Task Durations:**
   - "Duration (months)" column
   - Update based on actual program plan

2. **Dependencies:**
   - "Dependencies" column
   - Update to reflect revised critical path

3. **Parallel vs Sequential:**
   - Sites currently sequential (lessons learned between)
   - For parallel: overlap Site 2 and Site 3 construction

4. **Environmental Review:**
   - Currently 24 months
   - Can reduce to 12 for fast-track (high risk)
   - May increase to 30+ if issues arise

### Risk Register Parameters

**Location:** `OTHR_Risk_Register.csv`

**Most Common Updates:**

1. **Likelihood/Impact Scores:**
   - Update quarterly based on program status
   - 1-5 scale for each

2. **Add New Risks:**
   - Insert row with next Risk ID
   - Calculate Risk Score = Likelihood × Impact
   - Assign priority

3. **Mitigation Status:**
   - Update "Status" column
   - OPEN → IN WORK → COMPLETE → RETIRED

4. **Remove Retired Risks:**
   - Move to separate "Retired Risks" tab
   - Keep for historical record

---

## Interpreting Results

### Coverage Model Outputs

**Coverage Map (OTHR_Coverage_Map.png):**
- Colors indicate number of sites covering each area
  - White = 0 sites
  - Light Blue = 1 site
  - Blue = 2 sites
  - Dark Blue = 3 sites
- Red stars = radar site locations
- Green dashed lines = commercial polar routes (threat model baseline)

**Key Questions:**
- Are critical approach corridors covered?
- What gaps exist (white areas)?
- Is redundancy adequate (2+ sites)?

**Performance Curves (OTHR_Performance_Curves.png):**
- Left plot: Pd vs range for different target types (clear conditions)
- Right plot: Clear vs auroral conditions impact
- Horizontal line at Pd = 0.5 is typical threshold

**Key Questions:**
- At what range does Pd drop below 0.5 for key targets?
- How much performance loss during auroral storms?
- Are margins adequate for uncertainties?

**Performance Summary (JSON):**
```json
{
  "System Configuration": {
    "Number of Sites": 3,
    "Maximum Range (km)": 3000
  },
  "Detection Performance (Clear Conditions)": {
    "Large Commercial Aircraft": "3000 km",
    "Generic Cruise Missile": "500 km"  ← Note: conservative estimate
  }
}
```

### Cost Model Interpretation

**Total Acquisition Cost: $1,735M**

**Breakdown by Category:**
- Radar Hardware: 37% ($639M) - largest single category
- Infrastructure: 13% ($228M) - Arctic-driven
- Reserves: 15% ($264M) - contingency for unknowns
- Development: 4% ($75M) - minimal due to mature tech

**Cost Sensitivities:**
- **+/- 1 site:** ±$500-600M
- **Arctic multiplier 1.5x vs 2.5x:** -$200M
- **ROTHR vs JORN baseline:** -$300M
- **Extensive R&D required:** +$200M

**Red Flags:**
- If hardware costs exceed 50% of total → scope creep
- If reserves consumed early → underestimated complexity
- If infrastructure >20% → sites too remote

### Schedule Model Interpretation

**Baseline: 121 months (10.1 years) to FOC**

**Phase Breakdown:**
- Concept Development: 20 months
- Environmental/Site Selection: 31 months (overlaps with design)
- Design: 16 months
- Procurement: 24 months
- Site Construction: 70 months (sequential)
- Integration & Test: 21 months
- IOT&E: 10 months

**Critical Path Items:**
- Environmental Impact Statement: 24 months
- Indigenous Consultations: 18 months
- Site 3 Construction: 52 months
- IOT&E: 10 months

**Schedule Health Indicators:**
- Green: Ahead of baseline
- Yellow: On baseline
- Red: Behind baseline on critical path

**Warning Signs:**
- Any critical path delay = program delay
- Environmental review extending beyond 24 months
- Construction season delays (weather)

### Risk Register Interpretation

**Risk Score Distribution:**
- 13 Critical (36%) - requires immediate senior attention
- 19 High (53%) - active management required
- 4 Medium (11%) - monitor but not urgent
- 0 Low - good screening (no trivial risks listed)

**Risk Trending:**
- Score increasing → issue getting worse, escalate
- Score stable → mitigation working
- Score decreasing → issue resolving

**Top Risk Categories:**
1. **Indigenous Relations (R010, score 20)** - Program showstopper if not managed
2. **Technical Arctic (R001, R002, R005)** - Environment unique to this program
3. **Integration (R007, R009, R017)** - Complexity of multi-site system
4. **Resources (R027, R031, R014)** - Arctic logistics and safety

**Mitigation Investment Priorities:**
1. **HIGH:** Indigenous relations, Arctic engineering
2. **MEDIUM:** Environmental process, technology maturation
3. **ONGOING:** Program management discipline

---

## Transition to Government Version

This unclassified framework is designed for easy transition to a government-internal version with classified refinements.

### Information to Add (Classified)

**1. Specific Threat Profiles:**
- Replace generic cruise missile with actual threat systems
- Add classified RCS values
- Add classified flight profiles and speeds
- Add hypersonic weapon profiles

**2. Actual Site Locations:**
- Replace notional coordinates with surveyed candidates
- Add ionospheric characterization data
- Add geotechnical survey results
- Add infrastructure access details

**3. Refined Performance Models:**
- Use actual test data from ROTHR/JORN
- Add classified ionospheric models
- Add classified clutter environments
- Refine detection probability curves

**4. Detailed Cost Estimates:**
- Replace parametric estimates with vendor quotes
- Add classified technology costs
- Add actual O&S rates from similar systems
- Refine reserves based on program-specific risks

**5. Programmatic Details:**
- Add specific NORAD interface requirements
- Add classified integration timelines
- Add security classification requirements
- Add Canadian cost-sharing details

**6. Additional Risks:**
- Add classified technology risks
- Add threat evolution risks
- Add adversary counter-OTHR capabilities
- Add specific contractor risks

### Files to Create

1. **OTHR_Requirements_Classified.md**
   - Classified operational requirements
   - Specific threat scenarios
   - NORAD integration details

2. **OTHR_Sites_Analysis_Classified.md**
   - Candidate site evaluations
   - Ionospheric characterization results
   - Access and logistics details

3. **OTHR_Cost_Refined_Classified.xlsx**
   - Vendor quotes
   - Classified technology costs
   - Actual contract structures

4. **OTHR_Schedule_Refined_Classified.mpp**
   - Contractor proposals
   - Actual milestone dates
   - Resource loading

5. **OTHR_Risk_Classified.csv**
   - Classified technical risks
   - Adversary threats
   - Security risks

### Classification Guidance

**UNCLASSIFIED:**
- System architecture (general)
- Technology baseline (JORN/ROTHR references)
- Generic performance parameters
- Notional site locations
- High-level cost/schedule estimates

**CONTROLLED UNCLASSIFIED:**
- Specific site coordinates (before selection)
- Detailed vendor pricing
- Integration timelines
- Detailed ionospheric models

**SECRET:**
- Specific threat profiles and RCS
- Classified detection performance
- NORAD interface specifications
- Canadian coordination details
- Actual system performance data

**TOP SECRET:**
- Adversary counter-OTHR capabilities
- Integrated NORAD battle management
- Hypersonic weapon profiles
- Strategic warning timelines

### Security Review Process

1. **Initial Classification Review**
   - Submit framework to security office
   - Identify any inadvertent classified content
   - Obtain classification guide for program

2. **Classified Addendum Development**
   - Create separate classified documents
   - Reference unclassified framework as baseline
   - Do not mix classifications in same document

3. **Derivative Classification**
   - Mark all classified additions per guide
   - Include classification authority
   - Set declassification dates

4. **Storage and Handling**
   - Store classified versions on SIPRNET/JWICS
   - Maintain unclassified version on NIPRNET
   - Version control for both

---

## AI Facilitator Team Demonstration

This framework serves as a **demonstration case** for the AI Facilitator Team methodology - specialized two-person units showing how AI transforms capability acquisition processes.

### AI Acceleration Summary

**Total Framework Development:**
- Traditional approach: 6-8 weeks (2 engineers full-time)
- AI-assisted approach: 3-4 days (1 engineer + AI)
- **Time savings: ~75-85%**

**Specific AI Contributions:**

1. **Research Compilation (OTHR_Research_Summary.md)**
   - Traditional: 2 weeks manual research and documentation
   - AI-assisted: 4-6 hours
   - **Time saved: 1.5-2 weeks**
   - AI retrieved, synthesized, and organized 50+ sources

2. **System Architecture (OTHR_System_Architecture.md)**
   - Traditional: 1 week systems engineering
   - AI-assisted: 4-6 hours
   - **Time saved: 4-5 days**
   - AI generated Mermaid diagram, component descriptions, interfaces

3. **Coverage Model (OTHR_coverage_model.py)**
   - Traditional: 2 weeks coding and testing
   - AI-assisted: 6-8 hours
   - **Time saved: 1.5-2 weeks**
   - AI wrote 400+ lines of documented Python code

4. **Cost Model (OTHR_Cost_Model.csv)**
   - Traditional: 1 week WBS development and cost estimation
   - AI-assisted: 3-4 hours
   - **Time saved: 4-5 days**
   - AI created detailed WBS with formulas and notes

5. **Schedule Model (OTHR_Schedule_Model.csv)**
   - Traditional: 1 week critical path analysis
   - AI-assisted: 3-4 hours
   - **Time saved: 4-5 days**
   - AI defined tasks, dependencies, durations

6. **Risk Register (OTHR_Risk_Register.csv)**
   - Traditional: 3-5 days risk workshops and documentation
   - AI-assisted: 2-3 hours
   - **Time saved: 3-4 days**
   - AI identified 36 risks with scoring and mitigations

**Total Estimated Time Savings: 6-7 weeks**

### Human-in-the-Loop Critical

**AI Generated:** Framework structure, calculations, documentation
**Human Provided:**
- Strategic context and objectives
- Parameter refinement based on experience
- Validation of assumptions
- Integration with classified requirements
- Stakeholder engagement and communication
- Decision-making on trades and priorities

**AI Facilitator Team Model:**
- **Lead Engineer:** Systems engineering expertise, domain knowledge
- **AI Tools:** Research, analysis, documentation, calculation
- **Result:** Rapid high-quality products that still require human judgment

### Lessons Learned for AI Facilitator Teams

**What Worked Well:**
1. AI excels at research synthesis and organization
2. Code generation for parametric models very effective
3. Documentation structure and formatting automated
4. Consistent terminology and cross-referencing
5. Rapid iteration on parameter changes

**Human Expertise Still Essential:**
1. Defining requirements and scope
2. Validating technical assumptions
3. Making strategic trade-offs
4. Engaging stakeholders and subject matter experts
5. Final review and quality assurance
6. Classified information handling

**Process Improvements:**
1. Clear parameter extraction from requirements
2. Modular deliverables for easy updates
3. Version control and change tracking
4. Transition strategy to government refinement

### Replication for Other Programs

This methodology can be replicated for other acquisition programs:

**Step 1: Research Phase (1-2 days)**
- AI-assisted literature review
- Reference system analysis
- Technology assessment
- Historical program data compilation

**Step 2: Modeling Phase (2-3 days)**
- Architecture definition
- Parametric performance models
- Cost and schedule estimation
- Risk identification

**Step 3: Validation Phase (1-2 days)**
- SME review of assumptions
- Parameter refinement
- Sensitivity analysis
- Documentation finalization

**Total: 4-7 days vs 6-8 weeks traditional**

### Demonstration Value for Leadership

This framework demonstrates:

1. **Speed:** Weeks compressed to days
2. **Quality:** Comprehensive, professional documentation
3. **Flexibility:** Easy parameter updates
4. **Transparency:** All assumptions documented
5. **Scalability:** Methodology works across programs

**Key Message:** AI doesn't replace human expertise, it **amplifies** it. Engineers can focus on high-value judgment and stakeholder engagement while AI handles research, calculation, and documentation.

---

## Assumptions and Limitations

### Key Assumptions

**Technology:**
- JORN Phase 6 represents achievable Arctic OTHR capability
- No fundamental R&D required (mature technology baseline)
- Arctic adaptations achievable without major technology development
- Ionospheric models (E-CHAIM/A-CHAIM) adequate for Arctic

**Sites:**
- Government land available or accessible through agreements
- Three sites sufficient for northern coverage
- Sites within 200 km of infrastructure (power, communications)
- Permafrost engineering solutions feasible
- Construction season 6 months per year (May-October)

**Performance:**
- Detection ranges based on published JORN/ROTHR data
- 30-50% performance degradation during auroral events acceptable
- 20% auroral occurrence rate representative
- Commercial polar routes adequate threat model baseline
- No altitude measurement required (2D radar acceptable)

**Cost:**
- 2.5x Arctic multiplier for site preparation appropriate
- JORN Phase 6 costs ($1.2B AUD upgrade) scalable to new construction
- Mature technology reduces development costs
- 20-year lifecycle appropriate planning horizon
- Inflation-adjusted 1990s ROTHR costs valid comparison

**Schedule:**
- Environmental review completable in 24 months
- Indigenous consultations achievable in 18 months
- Sequential site construction (lessons learned between sites)
- 10-year timeline to FOC achievable
- No major program delays or funding gaps

**Programmatic:**
- Strong Congressional support for NORAD modernization
- Canada committed to partnership and cost sharing
- Bilateral coordination mechanisms effective
- Adequate contractor base for Arctic OTHR work
- No major geopolitical disruptions during development

### Known Limitations

**Coverage Model:**
- Simplified propagation model (does not account for ionospheric variability detail)
- Site locations notional, not based on actual surveys
- No 3D coverage analysis (altitude)
- Great circle paths only (no refraction modeling)
- Commercial routes approximate threat vectors

**Cost Model:**
- Parametric estimates, not vendor quotes
- Arctic multiplier assumes "typical" remote site, not specific locations
- Does not include all potential infrastructure costs (e.g., new airstrips)
- Reserve percentages based on historical programs, may not apply here
- Exchange rate risk if using Australian technology

**Schedule Model:**
- Tasks and durations based on historical programs, not detailed analysis
- Does not account for specific weather patterns at actual sites
- Assumes adequate funding profile (no stop-start delays)
- Critical path may shift as program matures
- Does not include technology development if required

**Risk Register:**
- Risks identified through research and experience, not formal workshops
- Likelihood and impact subjective without program-specific data
- Mitigation strategies generic, need tailoring to actual program
- Missing risks will emerge as program develops
- Scoring may need recalibration for specific threat/environment

**General:**
- ALL PARAMETERS UNCLASSIFIED - actual values may differ significantly
- No access to classified threat data or ionospheric characterization
- Site-specific environmental and geotechnical data not available
- Actual NORAD requirements not incorporated
- Framework not validated by government acquisition professionals

### Recommended Validation Steps

Before using this framework for decisions:

1. **Technical Validation:**
   - Review by OTHR subject matter experts
   - Validation of Arctic ionospheric assumptions
   - Site survey data for candidate locations
   - NORAD requirements verification

2. **Cost Validation:**
   - Compare to independent cost estimates
   - Obtain vendor rough order of magnitude (ROM) quotes
   - Validate Arctic multiplier for specific sites
   - Review reserve percentages for program type

3. **Schedule Validation:**
   - Critical path review by program managers
   - Environmental review timeline verification
   - Indigenous consultation process validation
   - Construction schedule review by Arctic-experienced contractors

4. **Risk Validation:**
   - Facilitated risk workshop with stakeholders
   - Likelihood/impact calibration to program context
   - Mitigation strategy review by subject matter experts
   - Identification of missing risks

5. **Programmatic Validation:**
   - Acquisition strategy review
   - NORAD coordination verification
   - Canadian partnership terms validation
   - Security classification review

---

## References

### Primary Sources

**ROTHR (US Navy):**
- Federation of American Scientists (FAS.org): AN/TPS-71 ROTHR documentation
- GlobalSecurity.org: ROTHR system descriptions
- US Navy operational documentation (declassified)

**JORN (Australia):**
- Australian Department of Defence: JORN fact sheets and updates
- Defence Science and Technology Group: JORN development history
- Australian National Audit Office: JORN Phase 6 reports
- Breaking Defense: Canada JORN purchase announcement (March 2025)

**Arctic OTHR Research:**
- Ruck, J.J. & Themens, D.R. (2021): "Impacts of Auroral Precipitation on HF Propagation: A Hypothetical OTHR Case Study"
- Themens, D.R. et al.: E-CHAIM and A-CHAIM ionospheric model documentation
- Various academic papers on high-latitude HF propagation

**NORAD Modernization:**
- Mitchell Institute for Aerospace Studies: Arctic defense policy papers (2023-2025)
- Canada Department of National Defence: NORAD modernization announcements
- US Air Force: Arctic strategy documents

**Technology and Cost Data:**
- Wikipedia: Over-the-horizon radar, JORN, ROTHR articles
- Defense industry publications: Cost and schedule data
- Australian budget documents: JORN Phase 6 appropriations

### Tools and Resources

**Software:**
- Python 3.x: https://www.python.org/
- Mermaid: https://mermaid.js.org/ or https://mermaid.live
- LibreOffice Calc (free): https://www.libreoffice.org/
- Google Sheets (free): https://sheets.google.com/
- GanttProject (free): https://www.ganttproject.biz/

**Learning Resources:**
- OTHR Technology: IEEE papers on skywave radar
- Arctic Operations: NOAA Arctic Report Card
- Ionospheric Modeling: E-CHAIM documentation
- Project Management: PMBOK Guide (PMI)
- Cost Estimating: NASA Cost Estimating Handbook

### Contacts for Questions

**Program Office:** [To be established]
**AI Facilitator Team Lead:** Kevin (Semantic Architectures)
**Technical SME:** [To be designated]
**Cost Analyst:** [To be designated]

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 21, 2026 | AI Facilitator Team | Initial framework release |

---

## Appendix: Quick Reference

### File Locations
```
/home/claude/OTHR_Research_Summary.md
/home/claude/OTHR_System_Architecture.md
/home/claude/OTHR_coverage_model.py
/home/claude/OTHR_Coverage_Map.png
/home/claude/OTHR_Performance_Curves.png
/home/claude/OTHR_Performance_Summary.json
/home/claude/OTHR_Cost_Model.csv
/home/claude/OTHR_Schedule_Model.csv
/home/claude/OTHR_Risk_Register.csv
/home/claude/OTHR_User_Guide.md
```

### Key Parameters Summary

| Parameter | Current Value | Source File | Update Frequency |
|-----------|---------------|-------------|------------------|
| Number of Sites | 3 | coverage_model.py, Cost_Model.csv | As needed |
| Max Detection Range | 3000 km | coverage_model.py | After site surveys |
| Arctic Multiplier | 2.5x | Cost_Model.csv | After site selection |
| Total Acquisition Cost | $1,735M | Cost_Model.csv | Quarterly |
| Timeline to FOC | 121 months | Schedule_Model.csv | Monthly |
| Critical Risks | 13 | Risk_Register.csv | Monthly |

### Common Tasks

| Task | Command/Action | Time |
|------|----------------|------|
| Run coverage model | `python3 OTHR_coverage_model.py` | 1 min |
| Update site location | Edit `OTHRParameters` class | 5 min |
| Recalculate costs | Update CSV, refresh formulas | 5 min |
| View architecture | Open in Mermaid Live | 2 min |
| Add new risk | Insert row in Risk_Register.csv | 5 min |
| Generate Gantt chart | Import Schedule_Model.csv to tool | 10 min |

---

**END OF USER GUIDE**

For questions or support transitioning to government version, contact the AI Facilitator Team or designated program office.
