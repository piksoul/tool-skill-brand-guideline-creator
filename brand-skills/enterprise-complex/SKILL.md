---
name: enterprise-complex
description: Applies Enterprise Complex's official brand colors, typography, and visual identity to documents, presentations, and web artifacts. Use when creating any Enterprise Complex-branded content, when the user requests Enterprise Complex branding, or when working on materials for Enterprise Complex that need visual consistency.
license: Proprietary - For Enterprise Complex use only
---

# Enterprise Complex Brand Guidelines

## Overview

Apply Enterprise Complex's brand identity to all artifacts including presentations, documents, reports, and web pages. This skill ensures visual consistency across all Enterprise Complex materials.

**Keywords**: Enterprise Complex, Enterprise Complex branding, corporate identity, brand colors, Enterprise Complex typography, visual identity

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
- **Enterprise Complex Primary**: `#1E3A8A` (RGB: 30, 58, 138)
  - Use for: Headlines, primary CTAs, key UI elements
  - Primary brand color - use prominently

**Secondary Color:**
- **Enterprise Complex Secondary**: `#10B981` (RGB: 16, 185, 129)
  - Use for: Accents, highlights, supporting elements

**Accent Color:**
- **Enterprise Complex Accent**: `#F59E0B` (RGB: 245, 158, 11)
  - Use for: Highlights, important callouts
  - Use sparingly for maximum impact

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
- **Headings**: Playfair Display
- **Subheadings**: Source Sans Pro
- **Body Text**: Source Sans Pro
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
  --primary-color: #1E3A8A;
  --secondary-color: #10B981;
  --dark: #1A1A1A;
  --light: #F5F5F5;

  --font-heading: 'Playfair Display', sans-serif;
  --font-body: 'Source Sans Pro', sans-serif;
}
```

## Implementation Guidelines

### For Simple Branding Requests

When user asks for "Enterprise Complex branding" or "use our brand colors":
1. Apply primary brand color to all headings
2. Apply dark neutral to body text
3. Use light neutral for backgrounds
4. Add logo from `assets/logo.png` to header/footer

### For Comprehensive Branding

When creating from scratch or user requests "full Enterprise Complex brand treatment":
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

1. **Add Logo Assets**: Place Enterprise Complex's logo files in `assets/`
   - `logo.png` (required)
   - `logo-white.png` (for dark backgrounds)
   - `logo-horizontal.png` (alternative orientation)

2. **Customize References**: Edit files in `references/` to add detailed brand specifications

3. **Add Templates**: Place pre-branded templates in `assets/templates/` for quick starts

4. **Test**: Create sample artifacts to ensure the guidelines work as expected

5. **Iterate**: Update based on usage and feedback
