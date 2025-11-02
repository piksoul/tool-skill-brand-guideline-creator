# Brand Assets Directory

Place all brand assets in this directory.

## Required Files

### Logo Files (Required)

- `logo.png` - Primary logo for light backgrounds
  - Format: PNG with transparency
  - Minimum: 50px height, 300 DPI for print
  - Recommended: 100-200px height for digital use

### Logo Variants (Recommended)

- `logo-white.png` - Logo for dark backgrounds
- `logo.svg` - Vector format (scalable, recommended)
- `logo-horizontal.png` - Horizontal orientation
- `logo-vertical.png` - Vertical orientation

## Optional Subdirectories

### templates/

Pre-branded templates for quick starts:
- `templates/presentation-template.pptx` - Branded PowerPoint template
- `templates/report-template.docx` - Branded Word document
- `templates/one-pager-template.pdf` - Single-page branded layout

### fonts/

Custom brand fonts (if redistributable and licensed):
- `fonts/HeadingFont-Bold.ttf`
- `fonts/BodyFont-Regular.ttf`

**Important**: Only include fonts if you have proper redistribution rights.

### images/

Additional brand imagery:
- `images/brand-patterns.png` - Background patterns
- `images/icon-set.svg` - Brand icon collection
- `images/photography-samples/` - Approved photography styles

## File Naming Conventions

- Use lowercase with hyphens: `logo-white.png` (not `Logo_White.PNG`)
- Be descriptive: `presentation-template-2024.pptx`
- Version when necessary: `logo-v2.svg`

## Next Steps

1. Add required logo files (at minimum `logo.png`)
2. Add logo variants for different use cases
3. Optional: Add templates for common document types
4. Optional: Add fonts (if licensed for redistribution)
5. Delete this README.md once assets are in place

---

**Note**: After adding assets, run validation:
```bash
python scripts/validate_brand_assets.py [skill-name]
```
