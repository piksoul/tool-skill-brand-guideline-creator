---
name: [SKILL-SLUG]
description: Applies [CLIENT_NAME]'s official brand colors, typography, and visual identity to documents, presentations, and web artifacts. Use when creating any [CLIENT_NAME]-branded content, when the user requests [CLIENT_NAME] branding, or when working on materials for [CLIENT_NAME] that need visual consistency.
license: Proprietary - For [CLIENT_NAME] use only
---

# [CLIENT_NAME] Brand Guidelines

## Overview

Apply [CLIENT_NAME]'s brand identity to all artifacts including presentations, documents, reports, and web pages. This skill ensures visual consistency across all [CLIENT_NAME] materials.

**Keywords**: [CLIENT_NAME], [CLIENT_NAME] branding, corporate identity, brand colors, [CLIENT_NAME] typography, visual identity

## Brand Assets

### Logo

Available logos in `assets/`:
- `logo.png` - Primary logo for light backgrounds
- `logo-white.png` - Logo for dark backgrounds
- `logo-horizontal.png` - Horizontal orientation for headers (if applicable)

**Logo Usage:**
- Minimum size: 50px height for digital, 0.5" for print
- Always maintain clearspace of [CLEARSPACE_RULE]
- Never distort, rotate, or add effects to the logo

For comprehensive logo usage rules, see `references/logo-usage.md`

### Colors

**Primary Colors:**
- **[CLIENT_NAME] [COLOR_NAME]**: `[HEX_CODE]` (RGB: [R], [G], [B])
  - Use for: [USAGE_DESCRIPTION]
  - Primary brand color - use prominently

**Secondary Colors:**
- **[CLIENT_NAME] [COLOR_NAME]**: `[HEX_CODE]` (RGB: [R], [G], [B])
  - Use for: [USAGE_DESCRIPTION]

**Neutral Colors:**
- **Dark**: `#1A1A1A` (RGB: 26, 26, 26)
  - Use for: Body text, dark backgrounds
- **Light**: `#F5F5F5` (RGB: 245, 245, 245)
  - Use for: Light backgrounds, subtle sections

**Color Application:**
- Headings: [PRIMARY_COLOR] or white (on dark backgrounds)
- Body text: Dark neutral
- Backgrounds: Light neutral or white
- Accents: [ACCENT_COLOR] sparingly

For comprehensive color usage rules, see `references/color-system.md`

### Typography

**Fonts:**
- **Headings**: [HEADING_FONT]
- **Subheadings**: [SUBHEADING_FONT]
- **Body Text**: [BODY_FONT]
- **Fallbacks**: Arial/Helvetica for headings, sans-serif for body

**Font Sizes:**
- H1: 36-48pt
- H2: 28-32pt
- H3: 20-24pt
- Body: 14-16pt

For detailed typography guidelines, see `references/typography.md`

## Artifact-Specific Guidelines

### Presentations (PowerPoint/PPTX)

**Slide Structure:**
- Title slide: [PRIMARY_COLOR] background with white text and logo
- Content slides: White background with [PRIMARY_COLOR] headings
- Section dividers: Dark background with white text

### Documents (Word/DOCX)

**Document Structure:**
- Cover page: [PRIMARY_COLOR] header with logo
- Headers: [PRIMARY_COLOR], [HEADING_FONT]
- Body: Dark text, [BODY_FONT]
- Footers: Small logo (right-aligned) with page numbers

### Web Content (HTML/JSX)

**CSS Variables to Use:**
```css
:root {
  --primary-color: [HEX_CODE];
  --secondary-color: [HEX_CODE];
  --dark: #1A1A1A;
  --light: #F5F5F5;

  --font-heading: '[HEADING_FONT]', Arial, sans-serif;
  --font-body: '[BODY_FONT]', Helvetica, sans-serif;
}
```

## Implementation Guidelines

### For Simple Branding Requests

When user asks for "[CLIENT_NAME] branding" or "use our brand colors":
1. Apply [PRIMARY_COLOR] to all headings
2. Apply dark neutral to body text
3. Use light neutral for backgrounds
4. Add logo from `assets/logo.png` to header/footer

### For Comprehensive Branding

When creating from scratch or user requests "full [CLIENT_NAME] brand treatment":
1. Read relevant reference files for detailed guidance
2. Use templates from `assets/templates/` if available
3. Follow all logo usage rules
4. Ensure proper color contrast and accessibility

### Quality Checklist

Before delivering branded artifacts, verify:
- [ ] Logo is present and properly sized
- [ ] Primary colors are used correctly
- [ ] Typography follows specified fonts
- [ ] Accent colors are used sparingly
- [ ] Text has sufficient contrast (4.5:1 minimum)
- [ ] Visual hierarchy is clear and consistent

## Reference Files

For detailed specifications, consult:
- `references/color-system.md` - Comprehensive color palette and usage
- `references/typography.md` - Font specifications and pairing rules
- `references/logo-usage.md` - Logo clearspace and placement guidelines

## Customization Instructions

To customize this template:

1. **Replace all [PLACEHOLDERS]** with actual brand information:
   - `[CLIENT_NAME]` - Client/brand name
   - `[SKILL-SLUG]` - URL-friendly skill name
   - `[PRIMARY_COLOR]`, `[SECONDARY_COLOR]` - Hex color codes
   - `[HEADING_FONT]`, `[BODY_FONT]` - Font names
   - `[COLOR_NAME]` - Descriptive color names
   - `[USAGE_DESCRIPTION]` - How/when to use colors

2. **Add logo files** to `assets/`:
   - `logo.png` (required)
   - `logo-white.png` (recommended)
   - `logo.svg` (recommended)

3. **Customize reference files** in `references/`:
   - Add detailed brand specifications
   - Include examples and guidelines
   - Document edge cases and special rules

4. **Add templates** (optional) in `assets/templates/`:
   - Pre-branded PowerPoint templates
   - Pre-branded Word templates
   - Other branded assets

5. **Add scripts** (optional) in `scripts/`:
   - Brand application automation
   - Asset validation scripts
   - Custom tooling

**TIP**: Use the `init_brand_skill.py` script for faster setup:
```bash
python scripts/init_brand_skill.py "[CLIENT_NAME]" --primary-color "#HEXCODE" --font-heading "FontName"
```
