#!/usr/bin/env python3
"""
Reorganize testimonial images from best to worst results
Based on tier analysis: TOP -> HIGH -> MID -> EARLY STAGE
"""

import os
import shutil
from pathlib import Path

# Define the new order based on tier analysis
# Format: [old_number] = position in new order
NEW_ORDER = {
    # TOP TIER (€100K+/month) - Positions 1-5
    89: 1,    # ~$143K/month
    62: 2,    # €100K/month
    64: 3,    # $150K/month
    71: 4,    # $100K/month
    83: 5,    # $200K-$300K/month

    # HIGH TIER (€10K-€100K/month) - Positions 6-18
    3: 6,     # €12,850/period
    37: 7,    # €20K-30K/month
    50: 8,    # €38,479.74 (€38K/month)
    51: 9,    # €25K/month
    54: 10,   # $24K net/month
    57: 11,   # £122K/month
    58: 12,   # €25K/month
    59: 13,   # $200K/month
    61: 14,   # $70K/month
    63: 15,   # €41K/month
    75: 16,   # €25K net/month (€156k total)
    92: 17,   # $250K/month

    # MID TIER (€2K-€10K/month) - Positions 19-40
    2: 19,
    4: 20,
    5: 21,
    6: 22,
    7: 23,
    10: 24,
    23: 25,
    34: 26,
    36: 27,
    44: 28,
    46: 29,
    49: 30,
    52: 31,
    56: 32,
    60: 33,
    66: 34,
    76: 35,
    79: 36,
    81: 37,
    86: 38,
    87: 39,
    90: 40,

    # EARLY STAGE (<€2K or first sales) - Positions 41-92
    1: 41,
    8: 42,
    9: 43,
    11: 44,
    12: 45,
    13: 46,
    14: 47,
    15: 48,
    16: 49,
    17: 50,
    18: 51,
    19: 52,
    20: 53,
    21: 54,
    22: 55,
    24: 56,
    25: 57,
    26: 58,
    27: 59,
    28: 60,
    29: 61,
    30: 62,
    31: 63,
    32: 64,
    33: 65,
    35: 66,
    38: 67,
    39: 68,
    40: 69,
    41: 70,
    42: 71,
    43: 72,
    45: 73,
    47: 74,
    48: 75,
    53: 76,
    55: 77,
    65: 78,
    67: 79,
    68: 80,
    69: 81,
    70: 82,
    72: 83,
    73: 84,
    74: 85,
    77: 86,
    78: 87,
    80: 88,
    82: 89,
    84: 90,
    85: 91,
    88: 92,
    91: 92,  # Last one
}

def reorganize_testimonials():
    """Rename all testimonial files in order from best to worst results"""

    testimonials_dir = Path('/home/user/Simo-Landing-Page/assets/testimonials')

    if not testimonials_dir.exists():
        print(f"Error: Directory {testimonials_dir} not found")
        return False

    print("📋 Starting testimonial reorganization...")
    print("   Organizing from BEST results (Top Tier) to earliest sales (Early Stage)\n")

    # Step 1: Create temporary names to avoid conflicts
    temp_files = {}
    for old_num, new_num in NEW_ORDER.items():
        old_file = testimonials_dir / f"testimonial-{old_num:03d}.png"
        temp_file = testimonials_dir / f"temp-{new_num:03d}.png"

        if old_file.exists():
            shutil.copy2(old_file, temp_file)
            temp_files[old_num] = new_num
            print(f"   ✓ Copied {old_num:03d} → temp-{new_num:03d}")
        else:
            print(f"   ⚠ Missing: testimonial-{old_num:03d}.png")

    # Step 2: Rename temp files to final names
    print("\n   Finalizing new numbering...")
    for new_num in sorted(temp_files.values()):
        temp_file = testimonials_dir / f"temp-{new_num:03d}.png"
        final_file = testimonials_dir / f"testimonial-{new_num:03d}.png"

        if temp_file.exists():
            if final_file.exists():
                final_file.unlink()
            shutil.move(temp_file, final_file)
            print(f"   ✓ Finalized: testimonial-{new_num:03d}.png")

    # Step 3: Clean up any remaining temp files
    for temp_file in testimonials_dir.glob("temp-*.png"):
        temp_file.unlink()
        print(f"   ✓ Cleaned up: {temp_file.name}")

    print("\n✨ Testimonial reorganization complete!")
    print("\n📊 New Order:")
    print("   Positions 001-005: TOP TIER (€100K+/month)")
    print("   Positions 006-017: HIGH TIER (€10K-€100K/month)")
    print("   Positions 018-040: MID TIER (€2K-€10K/month)")
    print("   Positions 041-092: EARLY STAGE (<€2K or first sales)")

    return True

if __name__ == '__main__':
    reorganize_testimonials()
