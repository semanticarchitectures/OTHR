# OVER-THE-HORIZON RADAR (OTHR) RESEARCH SUMMARY
## Framework Model for Arctic Strategic Defense Acquisition

**Date:** January 21, 2026  
**Purpose:** Unclassified framework to support OTHR acquisition for northern US/Canada Arctic defense  
**Classification:** UNCLASSIFIED // PUBLIC RELEASE  

---

## EXECUTIVE SUMMARY

This research phase compiled open-source information on OTHR technology, reference systems (AN/TPS-71 ROTHR and Jindalee OTHR), Arctic operational challenges, and acquisition baselines to support development of a parametric modeling framework for a new Arctic OTHR system.

**Key Findings:**
- **Reference Systems Identified:** AN/TPS-71 ROTHR (US Navy) and JORN (Australia) provide validated architectural patterns
- **Technology Maturity:** OTHR is mature technology with 40+ years operational experience; Arctic-specific challenges are well-documented
- **Cost Range:** Historical data suggests $100M-$1B+ per site depending on capability and infrastructure
- **Schedule Range:** 5-10 years from program initiation to initial operational capability (IOC)
- **Arctic Challenges:** High-latitude ionospheric variability requires sophisticated frequency management and tolerates 30-50% performance degradation during auroral events
- **Threat Context:** Cruise missiles and low-flying aircraft are primary detection targets; commercial polar routes provide realistic target profiles

---

## 1. REFERENCE SYSTEM ANALYSIS

### 1.1 AN/TPS-71 ROTHR (US Navy)

**System Overview:**
- Designation: Relocatable Over-The-Horizon Radar
- Developer: US Navy with Raytheon
- Status: Three operational systems (Virginia, Texas, Puerto Rico)
- Primary Mission: Counter-narcotics surveillance, maritime domain awareness

**Technical Specifications:**
- **Frequency Band:** HF (5-28 MHz), 3-30 MHz range
- **Coverage:** 64-degree wedge-shaped area
- **Range:** 500-1,600 nautical miles (925-2,963 km)
- **Surveillance Area:** >2.2 million square miles (example: Virginia system)
- **Architecture:** Bistatic (separate transmitter and receiver sites)
- **Receiver Array:** 2.58 km long, 372 twin-monopole elements
- **Beamforming:** 18 simultaneous beams, digital beamformer
- **Resolution:** ~6 km range, ~15 km azimuth (at operational ranges)
- **Angular Resolution:** 0.5 degrees azimuth
- **Waveform:** 25 kHz continuous frequency-modulated (FM-CW)
- **Dwell Regions:** Up to 12 simultaneous Dwell Illumination Regions (DIRs)
- **Dwell Duration:** Up to 49 seconds per DIR

**Operational History:**
- Prototype: Amchitka Island, Alaska (1991-1993) - Russia surveillance
- P1 (Virginia): Operational April 1993 - Caribbean coverage
- P2 (Texas): Operational July 1995 - Caribbean/Pacific coverage
- P3 (Puerto Rico): Extended coverage into South America

**Cost/Schedule Data:**
- FY2026 Operations Budget (3 sites): $89M
- Support Contract (2024-2029): $34.5M over 5 years
- Historical construction cost estimate: ~£10M + $90M for radar/computers (UK system, never built)

**Lessons Learned:**
- Successful counter-drug mission demonstrates maritime/air surveillance capability
- Long operational life (30+ years) validates technology maturity
- Adaptive waveforms developed to handle Spread Doppler Clutter
- Real-time ionospheric sounding essential for frequency management

### 1.2 Jindalee Operational Radar Network (JORN) - Australia

**System Overview:**
- Operator: Royal Australian Air Force (RAAF)
- Status: Three operational radars + command center
- Primary Mission: Air and maritime surveillance of northern approaches to Australia
- Recognition: World's most sophisticated OTHR system

**Technical Specifications:**
- **Range:** 1,000-3,000 km operational
- **Coverage:** 37,000 square kilometers total
- **Frequency Band:** HF (5.7-33 MHz typical)
- **Architecture:** Three radar sites, each with separate TX/RX locations
- **Site Locations:**
  - Radar 1: Longreach, Queensland (TX: 23°39'29"S, RX: Stonehenge) - 90° coverage
  - Radar 2: Laverton, Western Australia (TX: Leonora, RX: Laverton) - 180° coverage  
  - Radar 3: Alice Springs, Northern Territory (TX: Harts Range, RX: Mt Everard) - 90° coverage
- **Control Center:** RAAF Base Edinburgh, South Australia (JORN Coordination Centre)
- **Waveform:** FMCW with intro tone, 3-15 kHz bandwidth typical
- **Supporting Infrastructure:** Extensive ionospheric sounder network

**Development Timeline:**
- Stage A (Jindalee): 1974-1979 - Feasibility demonstration
- Stage B: 1978-1985 - Larger prototype, real-time processing
- Phase 3 (Construction): 1991-2003 - Initial JORN deployment
- Phase 5 (Upgrade): 2004-2014 - Commonization across three sites
- Phase 6 (Major Upgrade): 2018-2028 - Modernization, open architecture

**Cost Data:**
- **Total Program (Phases 1-5):** ~$1.8 billion AUD
- **Phase 3 (Construction):** $1.1 billion AUD
- **Phase 5 (Upgrade):** $70 million AUD
- **Phase 6 (Modernization):** $1.2 billion AUD over 10 years
- **Export to Canada (2025):** $6 billion CAD ($4 billion USD) - Arctic deployment
- **Future Canadian Polar Radar:** Up to $5 billion CAD additional

**Key Innovations:**
- Open software architecture (Phase 6)
- Enhanced signal processing for sensitivity
- Integration with broader defense surveillance system
- Ionospheric model integration (E-CHAIM for high latitudes)
- Regular Over-sampled Sparse Array (ROSA) receiver architecture in development

**Lessons Learned:**
- Government ownership + industry partnership model successful
- Continuous evolution over 50+ years maintains capability edge
- Dedicated R&D facility (Alice Springs) critical for advancement
- Integration with ionospheric monitoring infrastructure essential
- Program challenges: contractor experience gaps, schedule overruns in early phases

### 1.3 Comparative Analysis

| Parameter | ROTHR (US) | JORN (Australia) |
|-----------|-----------|------------------|
| Range | 500-1,600 nm | 1,000-3,000 km |
| Coverage Angle | 64° wedge | 90° or 180° sectors |
| Frequency | 5-28 MHz | 5.7-33 MHz |
| Architecture | Bistatic | Bistatic |
| Mission | Tactical/Counter-drug | Strategic Defense |
| Sites Operational | 3 | 3 |
| Technology Generation | 1980s baseline | Continuously upgraded |
| Cost per Site | ~$100-300M (est) | ~$300-600M AUD |

**Architectural Commonalities:**
- Separate transmitter/receiver sites (bistatic configuration)
- HF band operation (3-30 MHz)
- Large phased array antennas (km-scale)
- Real-time frequency management systems
- Ionospheric sounding for propagation prediction
- Digital beamforming and signal processing
- Multiple simultaneous surveillance regions
- Centralized operations control center

---

## 2. OTHR TECHNOLOGY FUNDAMENTALS

### 2.1 Propagation Principles

**Ionospheric Refraction:**
- HF signals (3-30 MHz) refract off ionosphere layers
- E-layer (90-150 km altitude) and F-layer (150-500 km) provide reflection
- Signal path: Ground → Ionosphere → Target → Ionosphere → Receiver
- "Skip" distance creates coverage gap near radar (typically <500 km)

**Frequency Selection:**
- Lower frequencies (3-10 MHz): Better long-range propagation, lower resolution
- Higher frequencies (20-30 MHz): Better resolution, limited by ionospheric conditions
- Maximum Usable Frequency (MUF) varies with: time of day, season, solar activity, geomagnetic activity
- Frequency Management System (FMS) essential for real-time selection

**Propagation Challenges:**
- Multipath propagation causes bearing/range errors
- Ionospheric motion introduces Doppler shifts
- Ground clutter from surface reflections
- Sea clutter (especially problematic for maritime surveillance)
- Spread Doppler clutter from ionospheric irregularities

### 2.2 System Architecture Components

**Transmitter Site:**
- High-power HF transmitters (typically MW-class)
- Large transmit antenna array (typically linear, 1-3 km)
- Frequency synthesizers and waveform generators
- Ionospheric sounders for propagation assessment
- Environmental monitoring systems

**Receiver Site:**
- Large receive antenna array (typically 2-3 km linear array)
- Hundreds of individual receiver elements
- Digital receiver per element
- High-dynamic-range A/D converters
- Digital beamforming processors

**Operations Control Center:**
- Mission planning and tasking systems
- Real-time signal processing (clutter rejection, target detection, tracking)
- Frequency Management System (FMS)
- Ionospheric models and prediction tools
- Display systems and operator interfaces
- Data fusion and track management
- External system interfaces (NORAD, etc.)

**Supporting Infrastructure:**
- Ionospheric monitoring network (sounders, GPS TEC, etc.)
- Communications links (typically satellite)
- Power systems (on-grid or backup generation)
- Environmental control systems
- Maintenance facilities

### 2.3 Performance Parameters

**Detection Performance:**
- Aircraft detection: 1-10 m² RCS targets at 1,000-3,000 km
- Maritime detection: Ships at similar ranges
- Probability of Detection (Pd): Typically 0.5-0.9 depending on conditions
- False Alarm Rate: Managed through adaptive thresholds

**Measurement Accuracy:**
- Range: ±5-10 km (limited by ionospheric variability)
- Azimuth: ±0.5-2° (antenna beamwidth dependent)
- Velocity: ±10-50 m/s (Doppler measurement)
- Update Rate: 10-60 seconds per surveillance region

**Operational Limitations:**
- No altitude measurement (2D radar)
- Dead zone near radar (<500 km typically)
- Maximum range limited by ionosphere (typically 3,000 km)
- Performance degrades during ionospheric disturbances
- Cannot penetrate through ionosphere (satellite blind)

---

## 3. ARCTIC OPERATIONAL ENVIRONMENT

### 3.1 High-Latitude Ionospheric Challenges

**Ionospheric Variability:**
- Arctic ionosphere significantly more variable than mid-latitudes
- Standard models (IRI) perform poorly - up to 80% error in TEC
- Empirical Canadian High Arctic Ionospheric Model (E-CHAIM) developed specifically for Arctic
- Assimilative CHAIM (A-CHAIM) provides near-real-time modeling

**Auroral Effects:**
- Auroral precipitation creates enhanced E-region electron density
- Impact on OTHR performance during auroral events:
  - Maximum Usable Frequency: Can increase from 8.5 MHz to 26 MHz
  - Median range: Can decrease from 2,541 km to 1,226 km
  - Coverage area: -50% to +58% variation
  - Target interception: 33-115% variation for tested flight paths
- Auroral Electrojet Index (AE) > 100 nT causes substantial modifications
- Two distinct propagation modes observed: F-E ducted and Auroral E-mode

**Sporadic-E Layers:**
- Thin enhancements in E-region (90-150 km) electron density
- Common in high latitudes
- Can significantly improve or degrade propagation:
  - Establish additional propagation paths
  - Particularly beneficial at night
  - Enable broader frequency range
  - Require lower elevation angles
- Must be included in propagation models for accurate frequency management

**Polar Cap Absorption (PCA):**
- Solar proton events cause absorption in D-region
- Can black out HF communications for hours to days
- More frequent and severe at high latitudes
- Major operational constraint for Arctic OTHR

**Off-Great-Circle Propagation:**
- Solar terminator (dawn/dusk) creates large ionospheric gradients
- Causes lateral deviations from great-circle path
- Leads to positioning errors if not corrected
- Coordination registration systems must account for this

### 3.2 Geomagnetic Disturbances

**Space Weather Impacts:**
- Geomagnetic storms create convection patterns in ionospheric plasma
- Especially severe near geomagnetic poles
- Radar clutter increases dramatically
- Detection performance degrades
- Can render radar temporarily ineffective

**Magnetic Field Considerations:**
- Magnetic compass unreliable near magnetic North Pole
- Modern navigation systems required
- Ionospheric structure aligned with magnetic field lines
- Affects propagation characteristics

### 3.3 Environmental Constraints

**Arctic Geography:**
- Vast distances between infrastructure
- Limited road access to potential sites
- Permafrost challenges for construction
- Extreme temperature range (-50°C to +30°C)
- Seasonal accessibility issues

**Climate Impacts:**
- Long winter darkness
- Severe weather events
- Ice accumulation on structures
- Wind loading on large antenna arrays
- Temperature effects on electronics

**Remote Site Operations:**
- Limited local support infrastructure
- Difficult logistics for personnel/supplies
- Satellite communications primary link
- Autonomous operations required
- Harsh conditions for maintenance

### 3.4 Sovereignty and Coordination Issues

**US-Canada Bilateral Considerations:**
- NORAD framework provides existing coordination structure
- Potential sites in both US (Alaska) and Canada (territories)
- Data sharing and command/control integration
- Overflight notification procedures
- Site access and security arrangements

**Indigenous Considerations:**
- Consultations with indigenous communities
- Land use agreements
- Employment opportunities
- Environmental impact assessments
- Cultural heritage protection

---

## 4. STRATEGIC DEFENSE CONTEXT

### 4.1 NORAD Modernization

**Current System - North Warning System:**
- 47 radar stations across northern Canada (11 manned)
- Constructed 1985-1989 (late 1980s technology)
- Designed for high-altitude bomber detection
- Inadequate for modern threats:
  - Low-flying cruise missiles
  - Stealth aircraft
  - UAVs/drones
  - Hypersonic weapons

**Modernization Requirements:**
- Replace/augment North Warning System
- Northern Approaches Surveillance System planned
- Layered defense architecture:
  1. Space-based sensors (missile warning, AMTI)
  2. OTHR (early detection, wide-area surveillance)
  3. Airborne platforms (E-7 Wedgetail, fighters)
  4. Terminal defenses

**Canadian Investment:**
- $38.6 billion CAD over 20 years for NORAD modernization
- $6 billion CAD for Arctic OTHR (JORN technology)
- $5 billion CAD for Polar OTHR (future)
- F-35 fighter procurement
- Command, control, and communications upgrades

**US Investment:**
- Four OTHR systems planned for NORAD/NORTHCOM
- Additional systems for other COCOMs
- Tactical Multi-Mission Over-the-Horizon Radar (TACMOR): Palau deployment ongoing

### 4.2 Threat Environment

**Cruise Missile Threat:**
- Russian KH-101 cruise missiles: Low-altitude, long-range (>2,500 km)
- Can be launched from bombers over Arctic, return undetected
- Hypersonic development ongoing (warning time <60 minutes)
- Current systems inadequate for detection

**Attack Scenarios:**
- Bombers launch cruise missiles from standoff range
- Submarine-launched cruise missiles from Arctic waters
- Low-altitude penetration by stealth aircraft
- Hypersonic glide vehicles
- Coordinated saturation attacks

**Detection Gaps:**
- North Warning System: "solid fence shrinking to picket fence"
- Missiles could remain undetected until impact
- Less than 60 minutes warning for hypersonic weapons
- Significant coverage gaps over Arctic Ocean

### 4.3 Operational Concept

**Mission:**
- Persistent wide-area surveillance of Arctic approaches
- Detection and tracking of air and maritime threats
- Early warning to NORAD command structure
- Cueing for interceptors and other sensors
- Frequency deconfliction with authorized users

**Integration:**
- Data fusion with space-based sensors
- Coordination with airborne early warning (E-7, E-3)
- Link to NORAD command and control
- Cooperation with Canadian systems
- Information sharing with allies

**Target Set (Generic Profiles):**
- **Commercial Aviation (Background Traffic):**
  - Polar routes: NYC-Tokyo, London-Tokyo, etc.
  - Typical speeds: 450-550 mph (220-270 m/s)
  - Altitudes: 35,000-41,000 feet
  - RCS: 10-100 m² (large jets)
  
- **Cruise Missiles:**
  - Speeds: 500-2,000+ mph (subsonic to hypersonic)
  - Altitudes: 50-200 feet (low-altitude penetration)
  - RCS: 0.1-1 m² (reduced signature)
  
- **Bombers:**
  - Speeds: 500-1,500 mph
  - Altitudes: Variable (high/low mix)
  - RCS: 0.1-100 m² (stealth to conventional)

---

## 5. COST AND SCHEDULE BASELINES

### 5.1 Historical Program Costs

**ROTHR (US Navy):**
- Per-site construction: ~$100-300M (estimated, 1990s dollars)
- Annual operations (3 sites): ~$89M (FY2026)
- Support services: ~$7M per year per site
- Infrastructure development: Variable by location

**JORN (Australia):**
- Phase 3 Construction (2 sites): $1.1 billion AUD (~$550M per site, 1990s)
- Phase 5 Upgrade: $70 million AUD
- Phase 6 Modernization: $1.2 billion AUD over 10 years
- **Total program cost:** ~$1.8 billion AUD
- Export to Canada: $6 billion CAD ($4B USD) for Arctic system

**Comparable Systems:**
- UK ROTHR (cancelled): £10M construction + $90M radar
- TACMOR (Palau): $25M infrastructure (2026)

**Cost Scaling Factors:**
- Technology maturity: Mature tech reduces R&D costs
- Site preparation: Arctic sites 2-5x multiplier over temperate
- Number of sites: Economies of scale after first site
- Performance requirements: Higher sensitivity = higher cost
- Remote location: Logistics and infrastructure costs significant

### 5.2 Schedule Considerations

**Program Phases:**
1. **Concept Development:** 1-2 years
2. **Technology Development:** 2-3 years (if needed)
3. **Engineering & Manufacturing Development:** 2-3 years
4. **Production & Deployment:** 2-4 years per site
5. **Test & Evaluation:** 1-2 years overlap with deployment

**Historical Timelines:**
- ROTHR: ~4 years concept to first deployment (benefited from OTH-B work)
- JORN: 12+ years from decision to operational (1986-2003), included significant delays
- JORN Phase 6: 10 years for major upgrade (2018-2028)

**Arctic-Specific Schedule Impacts:**
- Environmental assessments: +1-2 years
- Site surveys and permitting: +1-2 years
- Limited construction season: +1-2 years overall
- Logistics and mobilization: +6-12 months
- Indigenous consultations: Ongoing throughout

**Critical Path Items:**
- Site selection and acquisition
- Environmental impact statements
- Ionospheric characterization at sites
- Long-lead antenna components
- Power infrastructure installation
- Communications infrastructure

### 5.3 Risk Factors

**Technical Risks:**
- Arctic ionospheric modeling accuracy
- Clutter rejection performance in auroral conditions
- Permafrost foundation stability
- Extreme cold impacts on electronics
- Integration with legacy systems

**Schedule Risks:**
- Environmental approval delays
- Indigenous consultation outcomes
- Weather-limited construction windows
- Supply chain issues for remote sites
- Contractor experience with Arctic operations

**Cost Risks:**
- Site preparation costs (permafrost, remote access)
- Infrastructure development (power, communications)
- Scope creep in requirements
- Exchange rate fluctuations (if using foreign technology)
- Operations and maintenance costs

**Programmatic Risks:**
- Changing threat environment
- Budget constraints and priorities
- Political support and continuity
- Interagency coordination (DOD, FAA, etc.)
- International coordination (US-Canada)

---

## 6. KEY TAKEAWAYS FOR PARAMETRIC MODELING

### 6.1 Critical Parameters to Model

**System Architecture:**
- Number of sites (recommend 2-3 for northern coverage)
- Transmitter/receiver separation (50-200 km typical)
- Antenna array size (2-3 km for mature performance)
- Frequency band allocation (5-30 MHz HF)
- Power levels (MW-class transmitters)

**Performance:**
- Detection range: 1,000-3,000 km baseline
- Coverage angle: 60-180° per site
- Update rate: 10-60 seconds
- Probability of detection: 0.5-0.9 (target and conditions dependent)
- Measurement accuracy: ±10 km range, ±1° bearing

**Cost Drivers:**
- Site preparation: $50-200M per site (Arctic multiplier)
- Radar hardware: $100-300M per site
- Infrastructure: $50-150M per site (power, comms, facilities)
- Integration: $50-100M (command/control, NORAD interfaces)
- Operations: $20-40M per site per year

**Schedule Drivers:**
- Concept to IOC: 7-10 years (Arctic environment)
- Per-site deployment: 3-4 years
- Parallel construction: Can overlap after first site validation

### 6.2 Assumptions for Framework Model

**Technology Maturity:**
- Leverage existing ROTHR/JORN technology base
- No fundamental R&D required
- Arctic-specific adaptations needed but achievable
- Mature supply chain for HF components

**Operational Requirements:**
- 24/7 persistent surveillance
- Automated operations with remote monitoring
- Integration with NORAD architecture
- Coordination with Canadian systems
- Civilian frequency deconfliction

**Performance Assumptions:**
- Baseline capability: JORN-equivalent
- Arctic degradation: 30-50% during auroral storms
- Graceful degradation with space weather
- Frequency agility for interference avoidance

**Site Assumptions:**
- Government land or agreements in place
- Infrastructure available within 100 km
- Permafrost engineering solutions applied
- Environmental clearances achievable
- Indigenous support obtained

### 6.3 Model Sensitivity Analysis Needs

The parametric model should enable sensitivity analysis on:
- Number of sites vs. coverage completeness
- Site location optimization
- Performance vs. cost trades
- Schedule acceleration options (risk/cost impact)
- Technology insertion opportunities
- Operations concept (manned vs. automated)

---

## 7. INFORMATION GAPS AND CLASSIFIED REFINEMENTS

The following areas require classified refinement in the government-internal model:

**Technical:**
- Specific threat profiles (cruise missile RCS, speeds, altitudes)
- Detailed detection performance requirements
- Desired classification of tracks
- Integration specifications with classified systems
- Frequency allocation and deconfliction details

**Operational:**
- Exact coverage requirements and gaps analysis
- NORAD operational procedures and interfaces
- Rules of engagement and response times
- Specific site locations (candidate evaluation)
- Canadian coordination details and cost sharing

**Programmatic:**
- Budget profiles and funding sources
- Acquisition strategy and contracting approach
- Industry partners and technology sources
- Security classification requirements
- International agreements (ITAR, etc.)

---

## 8. REFERENCES AND SOURCES

**Primary Sources:**
- FAS.org - AN/TPS-71 ROTHR documentation
- Australian Department of Defence - JORN fact sheets
- Wikipedia - Over-the-horizon radar, JORN, ROTHR articles
- Academic papers - Arctic ionospheric effects on OTHR (Ruck et al., Themens et al.)
- Trade press - Breaking Defense, Defense Security Monitor, Australian Aviation

**Key Technical Papers:**
- "Impacts of Auroral Precipitation on HF Propagation: A Hypothetical OTHR Case Study" (Ruck & Themens, 2021)
- "Frequency Management System for Over-the-Horizon Radar using E-CHAIM" (Themens et al.)
- Various JORN upgrade documentation (ANAO reports)

**Recent News:**
- Canada JORN purchase announcement (March 2025)
- Mitchell Institute Arctic defense policy papers (2023-2025)
- NORAD modernization announcements

**Note:** All information compiled from publicly available sources. No classified or export-controlled information included.

---

## NEXT STEPS: PHASE 2 - PARAMETRIC MODEL DEVELOPMENT

With this research foundation, Phase 2 will develop:

1. **System Architecture Model** - Component breakdown, interfaces, data flows
2. **Coverage & Performance Model** - Python-based parametric calculator with geographic visualization
3. **Cost Model** - Spreadsheet-based with parametric scaling factors  
4. **Schedule Model** - Gantt-style with critical path identification
5. **Risk Assessment Framework** - Likelihood/impact/mitigation for key risks
6. **Trade Study Framework** - Tool for evaluating design alternatives
7. **User Documentation** - Instructions for updating parameters and interpreting results

The deliverable will be a complete, portable, parametric modeling framework that program office personnel can easily update with classified/refined parameters to produce detailed acquisition planning products.

---

**END OF RESEARCH PHASE**
