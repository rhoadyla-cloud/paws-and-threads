#!/usr/bin/env python3
"""Create print-ready PNG files for Printful from design images."""

from PIL import Image
import os

# Printful DTG print file specs
# Template: 4500 x 5400 px at 300 DPI (15" x 18" canvas)
# Format: PNG with transparent background
# Color mode: sRGB
CANVAS_W = 4500
CANVAS_H = 5400

# Design sizes on canvas (smaller to leave margin for print area)
# Hoodie front print area is approx 14" x 16" = 4200 x 4800 at 300 DPI
# T-shirt front print area is approx 12" x 15" = 3600 x 4500 at 300 DPI

INPUT_DIR = "/home/team/shared/designs"
OUTPUT_DIR = "/home/team/shared/printful-files"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def make_transparent(img, threshold=240):
    """Make white/light background transparent."""
    img = img.convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            # If pixel is close to white, make it transparent
            if r > threshold and g > threshold and b > threshold:
                pixels[x, y] = (r, g, b, 0)
    
    return img

def create_print_file(design_path, output_path, design_size_ratio=0.65, apply_bg_transform=False):
    """Create a print-ready file from a design image."""
    print(f"  Processing: {design_path}")
    
    # Load and process design
    design = Image.open(design_path).convert("RGBA")
    
    # Make background transparent
    design = make_transparent(design)
    
    # Calculate design size on canvas
    canvas_min = min(CANVAS_W, CANVAS_H)
    design_size = int(canvas_min * design_size_ratio)
    
    # Resize design maintaining aspect ratio
    design.thumbnail((design_size, design_size), Image.LANCZOS)
    
    # Create transparent canvas (4500x5400)
    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    
    # Center the design on the canvas
    x = (CANVAS_W - design.size[0]) // 2
    y = (CANVAS_H - design.size[1]) // 2
    
    # For t-shirts, position slightly higher (chest-level)
    if apply_bg_transform:
        y = int(CANVAS_H * 0.38) - design.size[1] // 2  # Upper chest position
    
    canvas.paste(design, (x, y), design)
    
    # Save as PNG
    canvas.save(output_path, "PNG", optimize=True)
    print(f"  Saved: {output_path} ({canvas.size[0]}x{canvas.size[1]}px)")

# === Print-Ready Files ===

# File naming: designName_product_print.png

print("=" * 60)
print("Creating Print-Ready Files for Printful")
print("=" * 60)

# --- Hoodie Designs (centered, full front print) ---

# 1. Whisker - Premium Pullover Hoodie
create_print_file(
    f"{INPUT_DIR}/design-01-whisker.png",
    f"{OUTPUT_DIR}/whisker_pullover-hoodie_print.png",
    design_size_ratio=0.60
)

# 2. Paw - Premium Zip-Up Hoodie
create_print_file(
    f"{INPUT_DIR}/design-02-paw.png",
    f"{OUTPUT_DIR}/paw_zip-hoodie_print.png",
    design_size_ratio=0.65
)

# 3. Best Friend - Premium Pullover Hoodie
create_print_file(
    f"{INPUT_DIR}/design-03-best-friend.png",
    f"{OUTPUT_DIR}/best-friend_pullover-hoodie_print.png",
    design_size_ratio=0.70,
    apply_bg_transform=True  # Chest-level placement for continuous line art
)

# 4. Type Lockup - Crewneck T-Shirt
create_print_file(
    f"{INPUT_DIR}/design-04-type-lockup.png",
    f"{OUTPUT_DIR}/type-lockup_crewneck-tee_print.png",
    design_size_ratio=0.60,
    apply_bg_transform=True  # Chest-level placement for t-shirt
)

print()
print("=" * 60)
print("All print-ready files created!")
print(f"Output directory: {OUTPUT_DIR}")
print("=" * 60)

# Print file listing
for f in sorted(os.listdir(OUTPUT_DIR)):
    size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
    img = Image.open(os.path.join(OUTPUT_DIR, f))
    print(f"  {f:40s} {img.size[0]}x{img.size[1]:<8d} {size/1024:.0f} KB")