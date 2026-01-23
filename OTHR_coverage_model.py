#!/usr/bin/env python3
"""
Arctic OTHR Coverage and Performance Model
Parametric calculator for Over-the-Horizon Radar system

UNCLASSIFIED // PUBLIC RELEASE
Version: 1.0 Framework
Date: January 21, 2026

PURPOSE: Parametric model framework for Arctic OTHR acquisition planning.
         Parameters should be updated with actual requirements in government version.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle
import json

# ============================================================================
# PARAMETRIC INPUTS - EASILY ADJUSTABLE
# ============================================================================

class OTHRParameters:
    """
    All key parameters in one place for easy modification
    """
    
    # SYSTEM PARAMETERS (based on JORN Phase 6 baseline)
    def __init__(self):
        # Detection Performance
        self.min_range_km = 500          # Minimum detection range (skip zone)
        self.max_range_km = 3000         # Maximum detection range
        self.nominal_range_km = 2000     # Nominal operational range
        
        # Coverage
        self.coverage_angle_deg = 120    # Coverage angle per site (degrees)
        self.probability_detection = 0.7 # Nominal Pd (clear conditions)
        
        # Measurement Accuracy
        self.range_accuracy_km = 10      # Range measurement error (±km)
        self.bearing_accuracy_deg = 1.0  # Bearing measurement error (±deg)
        self.velocity_accuracy_mps = 25  # Velocity measurement error (±m/s)
        
        # Update Rate
        self.update_rate_sec = 30        # Track update rate (seconds)
        
        # Arctic Performance Degradation
        self.aurora_degradation_factor = 0.65  # Performance multiplier during aurora
        self.aurora_occurrence_rate = 0.20     # Fraction of time auroral
        
        # Site Locations (lat, lon, coverage azimuth center)
        # These are notional - actual sites require detailed analysis
        self.sites = [
            {
                'name': 'Site 1 - Western Arctic',
                'lat': 65.0,
                'lon': -165.0,
                'azimuth_center': 0,    # Degrees true (0=North)
                'coverage_angle': 120
            },
            {
                'name': 'Site 2 - Central Arctic',
                'lat': 70.0,
                'lon': -110.0,
                'azimuth_center': 350,
                'coverage_angle': 120
            },
            {
                'name': 'Site 3 - Eastern Arctic',
                'lat': 68.0,
                'lon': -85.0,
                'azimuth_center': 340,
                'coverage_angle': 120
            }
        ]
        
        # Target Profiles (generic, based on commercial aviation)
        self.target_profiles = {
            'Large Commercial Aircraft': {
                'rcs_m2': 50,
                'speed_mps': 250,
                'altitude_m': 11000,
                'pd_modifier': 1.0
            },
            'Medium Aircraft': {
                'rcs_m2': 10,
                'speed_mps': 200,
                'altitude_m': 9000,
                'pd_modifier': 0.9
            },
            'Small Aircraft': {
                'rcs_m2': 2,
                'speed_mps': 150,
                'altitude_m': 7000,
                'pd_modifier': 0.7
            },
            'Generic Cruise Missile': {
                'rcs_m2': 0.5,
                'speed_mps': 250,
                'altitude_m': 100,
                'pd_modifier': 0.5
            }
        }
        
        # Major Commercial Routes (for threat model baseline)
        self.commercial_routes = [
            {'name': 'JFK-NRT (New York-Tokyo)', 
             'waypoints': [(40.6, -73.8), (65.0, -170.0), (75.0, 170.0), (35.8, 139.8)]},
            {'name': 'LAX-NRT (Los Angeles-Tokyo)', 
             'waypoints': [(33.9, -118.4), (55.0, 170.0), (35.8, 139.8)]},
            {'name': 'ORD-PEK (Chicago-Beijing)', 
             'waypoints': [(41.98, -87.9), (70.0, -150.0), (77.0, 180.0), (40.1, 116.6)]},
            {'name': 'YVR-HKG (Vancouver-Hong Kong)', 
             'waypoints': [(49.2, -123.2), (60.0, 175.0), (22.3, 114.2)]}
        ]

# ============================================================================
# COVERAGE CALCULATION FUNCTIONS
# ============================================================================

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate great circle distance between two points on Earth
    Returns distance in kilometers
    """
    R = 6371  # Earth radius in km
    
    lat1_rad = np.radians(lat1)
    lat2_rad = np.radians(lat2)
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    
    a = np.sin(dlat/2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return R * c

def bearing_from_to(lat1, lon1, lat2, lon2):
    """
    Calculate initial bearing from point 1 to point 2
    Returns bearing in degrees (0-360, where 0=North)
    """
    lat1_rad = np.radians(lat1)
    lat2_rad = np.radians(lat2)
    dlon = np.radians(lon2 - lon1)
    
    x = np.sin(dlon) * np.cos(lat2_rad)
    y = np.cos(lat1_rad) * np.sin(lat2_rad) - \
        np.sin(lat1_rad) * np.cos(lat2_rad) * np.cos(dlon)
    
    bearing = np.degrees(np.arctan2(x, y))
    return (bearing + 360) % 360

def point_in_coverage(target_lat, target_lon, site_lat, site_lon, 
                      azimuth_center, coverage_angle, min_range, max_range):
    """
    Determine if a point is within radar coverage
    Returns (in_coverage, range_km, bearing_deg)
    """
    range_km = haversine_distance(site_lat, site_lon, target_lat, target_lon)
    bearing = bearing_from_to(site_lat, site_lon, target_lat, target_lon)
    
    # Check range
    if range_km < min_range or range_km > max_range:
        return False, range_km, bearing
    
    # Check azimuth coverage
    # Calculate angular difference accounting for wrap-around
    angle_diff = abs(bearing - azimuth_center)
    if angle_diff > 180:
        angle_diff = 360 - angle_diff
    
    if angle_diff <= coverage_angle / 2:
        return True, range_km, bearing
    else:
        return False, range_km, bearing

def calculate_coverage_map(params, resolution_deg=1.0):
    """
    Calculate coverage map showing which areas are covered by each site
    Returns grid of coverage (lat/lon grid with coverage indicators)
    """
    # Define grid
    lat_range = np.arange(50, 85, resolution_deg)
    lon_range = np.arange(-180, -60, resolution_deg)
    
    coverage_grid = np.zeros((len(lat_range), len(lon_range)))
    
    for i, lat in enumerate(lat_range):
        for j, lon in enumerate(lon_range):
            num_sites_covering = 0
            for site in params.sites:
                in_cov, _, _ = point_in_coverage(
                    lat, lon, 
                    site['lat'], site['lon'],
                    site['azimuth_center'], site['coverage_angle'],
                    params.min_range_km, params.max_range_km
                )
                if in_cov:
                    num_sites_covering += 1
            
            coverage_grid[i, j] = num_sites_covering
    
    return lat_range, lon_range, coverage_grid

# ============================================================================
# PERFORMANCE CALCULATION FUNCTIONS
# ============================================================================

def calculate_detection_probability(params, target_type, range_km, conditions='clear'):
    """
    Calculate probability of detection for given target at given range
    
    conditions: 'clear' or 'auroral'
    """
    base_pd = params.probability_detection
    target_modifier = params.target_profiles[target_type]['pd_modifier']
    
    # Range degradation (simple model: linear decrease beyond nominal range)
    if range_km > params.nominal_range_km:
        range_factor = 1 - 0.3 * (range_km - params.nominal_range_km) / \
                       (params.max_range_km - params.nominal_range_km)
    else:
        range_factor = 1.0
    
    pd = base_pd * target_modifier * range_factor
    
    if conditions == 'auroral':
        pd *= params.aurora_degradation_factor
    
    return np.clip(pd, 0, 1)

def estimate_detection_range(params, target_type, pd_threshold=0.5, conditions='clear'):
    """
    Estimate maximum detection range for given target type and Pd threshold
    """
    for range_km in range(params.min_range_km, params.max_range_km, 50):
        pd = calculate_detection_probability(params, target_type, range_km, conditions)
        if pd < pd_threshold:
            return range_km
    return params.max_range_km

def calculate_track_accuracy(params, range_km):
    """
    Calculate position and velocity accuracy at given range
    Returns dict with accuracy estimates
    """
    # Accuracy degrades with range (simple model)
    range_factor = range_km / params.nominal_range_km
    
    return {
        'range_error_km': params.range_accuracy_km * range_factor,
        'bearing_error_deg': params.bearing_accuracy_deg * range_factor,
        'velocity_error_mps': params.velocity_accuracy_mps * np.sqrt(range_factor),
        'cross_range_error_km': range_km * np.radians(params.bearing_accuracy_deg * range_factor)
    }

# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def plot_coverage_map(params, save_path=None):
    """
    Create coverage map visualization
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Calculate coverage
    lat_range, lon_range, coverage_grid = calculate_coverage_map(params, resolution_deg=2.0)
    
    # Plot coverage
    coverage_plot = ax.contourf(lon_range, lat_range, coverage_grid, 
                                levels=[0, 0.5, 1.5, 2.5, 3.5],
                                colors=['white', 'lightblue', 'blue', 'darkblue'],
                                alpha=0.6)
    
    # Add colorbar
    cbar = plt.colorbar(coverage_plot, ax=ax, ticks=[0, 1, 2, 3])
    cbar.set_label('Number of Sites Covering', rotation=270, labelpad=20)
    cbar.set_ticklabels(['0', '1', '2', '3'])
    
    # Plot radar sites
    for site in params.sites:
        ax.plot(site['lon'], site['lat'], 'r*', markersize=20, label=site['name'])
        
        # Add coverage wedge (simplified, not accounting for Earth curvature)
        # This is approximate visualization only
        ax.text(site['lon'], site['lat']+1, site['name'], 
               ha='center', fontsize=8, weight='bold')
    
    # Plot commercial routes
    for route in params.commercial_routes:
        lons = [wp[1] for wp in route['waypoints']]
        lats = [wp[0] for wp in route['waypoints']]
        ax.plot(lons, lats, 'g--', linewidth=1, alpha=0.5)
        ax.text(lons[0], lats[0], route['name'], fontsize=7, color='green')
    
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title('Arctic OTHR Coverage Map\n(Unclassified Framework - Notional Site Locations)', 
                fontsize=14, weight='bold')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-180, -60)
    ax.set_ylim(50, 85)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Coverage map saved to {save_path}")
    
    return fig

def plot_performance_curves(params, save_path=None):
    """
    Plot detection performance curves for different target types and conditions
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ranges = np.arange(params.min_range_km, params.max_range_km, 50)
    
    # Plot 1: Pd vs Range for different targets (clear conditions)
    for target_type in params.target_profiles.keys():
        pds = [calculate_detection_probability(params, target_type, r, 'clear') 
               for r in ranges]
        ax1.plot(ranges, pds, label=target_type, linewidth=2)
    
    ax1.axhline(y=0.5, color='r', linestyle='--', alpha=0.5, label='Pd=0.5 threshold')
    ax1.set_xlabel('Range (km)', fontsize=12)
    ax1.set_ylabel('Probability of Detection (Pd)', fontsize=12)
    ax1.set_title('Detection Performance vs Range\n(Clear Conditions)', fontsize=12, weight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 1.05)
    
    # Plot 2: Pd vs Range for Large Aircraft (clear vs auroral)
    target = 'Large Commercial Aircraft'
    pds_clear = [calculate_detection_probability(params, target, r, 'clear') for r in ranges]
    pds_aurora = [calculate_detection_probability(params, target, r, 'auroral') for r in ranges]
    
    ax2.plot(ranges, pds_clear, label='Clear Conditions', linewidth=2, color='blue')
    ax2.plot(ranges, pds_aurora, label='Auroral Conditions', linewidth=2, color='red')
    ax2.fill_between(ranges, pds_clear, pds_aurora, alpha=0.2, color='yellow', 
                     label='Performance Degradation')
    ax2.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
    
    ax2.set_xlabel('Range (km)', fontsize=12)
    ax2.set_ylabel('Probability of Detection (Pd)', fontsize=12)
    ax2.set_title(f'Arctic Performance Impact\n({target})', fontsize=12, weight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 1.05)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Performance curves saved to {save_path}")
    
    return fig

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

def generate_performance_summary(params):
    """
    Generate summary statistics for reporting
    """
    summary = {
        'System Configuration': {
            'Number of Sites': len(params.sites),
            'Coverage Angle per Site (deg)': params.coverage_angle_deg,
            'Minimum Range (km)': params.min_range_km,
            'Maximum Range (km)': params.max_range_km,
            'Nominal Range (km)': params.nominal_range_km,
            'Update Rate (sec)': params.update_rate_sec
        },
        'Detection Performance (Clear Conditions)': {},
        'Detection Performance (Auroral Conditions)': {},
        'Arctic Degradation': {
            'Performance Factor': params.aurora_degradation_factor,
            'Occurrence Rate (%)': params.aurora_occurrence_rate * 100,
            'Average Performance Impact (%)': (1 - params.aurora_degradation_factor) * 
                                             params.aurora_occurrence_rate * 100
        },
        'Measurement Accuracy': {
            'Range (km)': f'±{params.range_accuracy_km}',
            'Bearing (deg)': f'±{params.bearing_accuracy_deg}',
            'Velocity (m/s)': f'±{params.velocity_accuracy_mps}'
        }
    }
    
    # Calculate detection ranges for each target type
    for target_type in params.target_profiles.keys():
        range_clear = estimate_detection_range(params, target_type, 0.5, 'clear')
        range_aurora = estimate_detection_range(params, target_type, 0.5, 'auroral')
        
        summary['Detection Performance (Clear Conditions)'][target_type] = f"{range_clear} km"
        summary['Detection Performance (Auroral Conditions)'][target_type] = f"{range_aurora} km"
    
    return summary

def print_summary(summary):
    """
    Print formatted summary to console
    """
    print("\n" + "="*80)
    print("ARCTIC OTHR PERFORMANCE SUMMARY")
    print("="*80 + "\n")
    
    for section, data in summary.items():
        print(f"\n{section}:")
        print("-" * 60)
        for key, value in data.items():
            print(f"  {key:40s}: {value}")
    
    print("\n" + "="*80)
    print("NOTE: This is a parametric framework. Update parameters in OTHRParameters")
    print("      class for refined analysis with actual requirements.")
    print("="*80 + "\n")

def export_summary_json(summary, filepath):
    """
    Export summary to JSON file
    """
    with open(filepath, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Summary exported to {filepath}")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("Arctic OTHR Coverage and Performance Model")
    print("Initializing parameters...")
    
    # Create parameter set
    params = OTHRParameters()
    
    # Generate summary statistics
    summary = generate_performance_summary(params)
    print_summary(summary)
    
    # Create visualizations
    print("Generating coverage map...")
    fig1 = plot_coverage_map(params, save_path='/home/claude/OTHR_Coverage_Map.png')
    
    print("Generating performance curves...")
    fig2 = plot_performance_curves(params, save_path='/home/claude/OTHR_Performance_Curves.png')
    
    # Export summary
    export_summary_json(summary, '/home/claude/OTHR_Performance_Summary.json')
    
    print("\n" + "="*80)
    print("AI FACILITATOR TEAM NOTE:")
    print("-" * 80)
    print("This parametric model was generated through AI-assisted systems engineering.")
    print("Time saved: ~1-2 weeks of manual analysis and coding")
    print("")
    print("To update parameters:")
    print("1. Edit the OTHRParameters class at the top of this file")
    print("2. Run the script again to regenerate outputs")
    print("")
    print("For government version:")
    print("- Replace notional site locations with actual candidates")
    print("- Update target profiles with classified threat data")
    print("- Refine performance models with actual test data")
    print("- Add ionospheric models specific to selected sites")
    print("="*80 + "\n")
    
    print("Analysis complete. Files generated:")
    print("  - OTHR_Coverage_Map.png")
    print("  - OTHR_Performance_Curves.png")
    print("  - OTHR_Performance_Summary.json")
