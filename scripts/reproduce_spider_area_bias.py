#!/usr/bin/env python3
"""
Reproduce Closed Spider/Radar Chart 1.99x Axis-Permutation Area Distortion
vs. Orthogonal Polar Rose Area Invariance.

Communication Growth Map 1.0 (CL-WP-2026-01)
Author: Zhang Ling — Communication Lab (https://do.link)
License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
"""

import itertools
import math

PROFILE_ALT = [0.88, 0.20, 0.88, 0.20, 0.88, 0.20, 0.88, 0.20]
PROFILE_CLUSTERED = [0.88, 0.88, 0.88, 0.88, 0.20, 0.20, 0.20, 0.20]


def spider_polygon_area(values: list[float]) -> float:
    """Euclidean enclosed area of a regular n-axis closed radar polygon."""
    n = len(values)
    sin_theta = math.sin(2.0 * math.pi / n)
    adj_sum = sum(values[i] * values[(i + 1) % n] for i in range(n))
    return 0.5 * sin_theta * adj_sum


def polar_rose_area(values: list[float]) -> float:
    """Total area of n orthogonal polar rose sectors (radius r_i, angle 2*pi/n)."""
    n = len(values)
    sector_angle = 2.0 * math.pi / n
    return sum(0.5 * sector_angle * (r ** 2) for r in values)


def main() -> None:
    area_alt = spider_polygon_area(PROFILE_ALT)
    area_clustered = spider_polygon_area(PROFILE_CLUSTERED)
    ratio = area_clustered / area_alt

    rose_alt = polar_rose_area(PROFILE_ALT)
    rose_clustered = polar_rose_area(PROFILE_CLUSTERED)

    # Exhaustive check over unique permutations of 4x0.88 + 4x0.20
    unique_perms = set(itertools.permutations(PROFILE_ALT))
    spider_areas = [spider_polygon_area(list(p)) for p in unique_perms]
    rose_areas = [polar_rose_area(list(p)) for p in unique_perms]

    print("Communication Growth Map 1.0 — Spider vs Polar Rose Geometric Verification")
    print("=" * 74)
    print(f"Profile multiset         : 4 x 0.88 + 4 x 0.20 (8 orthogonal dimensions)")
    print(f"Unique axis permutations : {len(unique_perms)}")
    print("-" * 74)
    print(f"Spider area (Alternating): {area_alt:.6f}  (sum r_i*r_(i+1) = 1.4080)")
    print(f"Spider area (Clustered)  : {area_clustered:.6f}  (sum r_i*r_(i+1) = 2.7952)")
    print(f"Exact distortion ratio   : {ratio:.6f}x  (rounded: {ratio:.2f}x)")
    print(f"Global spider min / max  : {min(spider_areas):.6f} / {max(spider_areas):.6f}")
    print("-" * 74)
    print(f"Polar Rose (Alternating) : {rose_alt:.6f}")
    print(f"Polar Rose (Clustered)   : {rose_clustered:.6f}")
    print(f"Polar Rose max drift     : {max(rose_areas) - min(rose_areas):.2e} (exact invariance)")


if __name__ == "__main__":
    main()
