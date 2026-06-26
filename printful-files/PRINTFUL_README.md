# Paws & Threads — Printful Print-Ready Files

## Overview
Four print-ready PNG files prepared for Printful's DTG (Direct-to-Garment) printing service. Each file is a single-color design on a transparent background, centered on the product canvas at 300 DPI.

## File Specifications

| Spec | Value |
|------|-------|
| **Format** | PNG (lossless) |
| **Canvas Size** | 4500 × 5400 px (15" × 18" at 300 DPI) |
| **Color Mode** | RGBA (transparent background) |
| **Resolution** | 300 DPI |
| **Max File Size** | Under 25 MB (all under 500 KB) |

## Files Created

| File | Design | Product Type | Placement | Size |
|------|--------|-------------|-----------|------|
| `whisker_pullover-hoodie_print.png` | Whisker (cat line art) | Premium Pullover Hoodie | Center chest | 181 KB |
| `paw_zip-hoodie_print.png` | Paw (abstract geometric) | Premium Zip-Up Hoodie | Center chest | 444 KB |
| `best-friend_pullover-hoodie_print.png` | Best Friend (person+dog) | Premium Pullover Hoodie | Upper chest | 225 KB |
| `type-lockup_crewneck-tee_print.png` | Type Lockup (typography) | Crewneck T-Shirt | Upper chest | 309 KB |

## How to Upload to Printful

1. Log in to your Printful Dashboard
2. Go to **Store → Add Product**
3. Select the appropriate product:
   - **Whisker / Best Friend**: Gildan 18000 Unisex Heavy Blend Hoodie (or similar premium pullover)
   - **Paw**: Gildan 18500 Unisex Heavy Blend Zip Hoodie (or similar premium zip-up)
   - **Type Lockup**: Gildan 5000 Unisex T-Shirt (or similar premium crewneck)
4. In the Design Maker, upload the corresponding PNG file
5. Select print method: **DTG (Direct-to-Garment)** — 1 color (black ink)
6. No white underbase needed (all designs are black/charcoal on light garment colors)
7. Position: **Centered on chest** at approximately 4.5" × 5.5" print size

## Recommended Garment Colors

| Design | Recommended base color |
|--------|----------------------|
| Whisker | Cream / Warm White (#F5F0EB) |
| Paw | Charcoal / Dark Grey (#2D2D2D) |
| Best Friend | Dusty Rose / Blush (#C98474) |
| Type Lockup | Warm White (#F5F0EB) |

## Re-generating Files

If you need to regenerate or modify the files, run:
```bash
cd /home/team/shared
python3 printful-files/create_print_ready.py
```

The script processes the source designs from `/home/team/shared/designs/` and outputs to this directory. It:
- Converts white backgrounds to transparent
- Scales designs to appropriate size on the 4500×5400 canvas
- Positions designs for proper chest-level placement

---

*Created: June 2026 | Last verified: all files pass 300 DPI check*