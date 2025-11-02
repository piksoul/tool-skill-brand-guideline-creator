---
name: startup-simple
description: Applies Startup Simple's official brand colors, typography, and visual identity to documents, presentations, and web artifacts. Use when creating any Startup Simple-branded content, when the user requests Startup Simple branding, or when working on materials for Startup Simple that need visual consistency.
license: Proprietary - For Startup Simple use only
---

# Startup Simple Brand Guidelines

## Overview

Apply Startup Simple's brand identity to all artifacts including presentations, documents, reports, and web pages. This skill ensures visual consistency across all Startup Simple materials.

**Keywords**: Startup Simple, Startup Simple branding, corporate identity, brand colors, Startup Simple typography, visual identity

## Brand Assets

### Logo

Available logos in `assets/`:
- `logo.png` - Primary logo for light backgrounds
- `logo-white.png` - Logo for dark backgrounds (if applicable)
- `logo-horizontal.png` - Horizontal orientation for headers (if applicable)

**Logo Usage:**
- Minimum size: 50px height for digital, 0.5" for print
- Always maintain clearspace
- Never distort, rotate, or add effects to the logo

For comprehensive logo usage rules, see `references/logo-usage.md`

### Colors


**Primary Color:**
- **Startup Simple Primary**: `#FF5733` (RGB: 255, 87, 51)
  - Use for: Headlines, primary CTAs, key UI elements
  - Primary brand color - use prominently

**Neutral Colors:**
- **Dark**: `#1A1A1A` (RGB: 26, 26, 26)
  - Use for: Body text, dark backgrounds
- **Light**: `#F5F5F5` (RGB: 245, 245, 245)
  - Use for: Light backgrounds, subtle sections


**Color Application:**
- Headings: Primary brand color or white (on dark backgrounds)
- Body text: Dark neutral
- Backgrounds: Light neutral or white
- Accents: Secondary/Accent colors sparingly

For comprehensive color usage rules, see `references/color-system.md`

### Typography

**Fonts:**
- **Headings**: Inter
- **Body Text**: Roboto
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
- Title slide: Primary brand color background with white text and logo
- Content slides: White background with primary color headings
- Section dividers: Dark background with white text

### Documents (Word/DOCX)

**Document Structure:**
- Cover page: Primary brand color header with logo
- Headers: Primary brand color, heading font
- Body: Dark text, body font
- Footers: Small logo (right-aligned) with page numbers

### Web Content (HTML/JSX)

**CSS Variables to Use:**
```css
:root {
  --primary-color: #FF5733;
  --secondary-color: #FF6600;
  --dark: #1A1A1A;
  --light: #F5F5F5;

  --font-heading: 'Inter', sans-serif;
  --font-body: 'Roboto', sans-serif;
}
```

## Implementation Guidelines

### For Simple Branding Requests

When user asks for "Startup Simple branding" or "use our brand colors":
1. Apply primary brand color to all headings
2. Apply dark neutral to body text
3. Use light neutral for backgrounds
4. Add logo from `assets/logo.png` to header/footer

### For Comprehensive Branding

When creating from scratch or user requests "full Startup Simple brand treatment":
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

## Next Steps

To complete this brand skill:

1. **Add Logo Assets**: Place Startup Simple's logo files in `assets/`
   - `logo.png` (required)
   - `logo-white.png` (for dark backgrounds)
   - `logo-horizontal.png` (alternative orientation)

2. **Customize References**: Edit files in `references/` to add detailed brand specifications

3. **Add Templates**: Place pre-branded templates in `assets/templates/` for quick starts

4. **Test**: Create sample artifacts to ensure the guidelines work as expected

5. **Iterate**: Update based on usage and feedback
