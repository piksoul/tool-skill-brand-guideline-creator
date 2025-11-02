---
name: pro-sites
description: Applies Pro Sites's official brand colors, typography, and visual identity to documents, presentations, and web artifacts. Use when creating any Pro Sites-branded content, when the user requests Pro Sites branding, or when working on materials for Pro Sites that need visual consistency.
license: Proprietary - For Pro Sites use only
---

# Pro Sites Brand Guidelines

## Overview

Apply Pro Sites's brand identity to all artifacts including presentations, documents, reports, and web pages. Pro Sites (https://www.pro-sites.com.au) is a professional web development and design company. This skill ensures visual consistency across all Pro Sites materials, with special attention to web-focused deliverables.

**Keywords**: Pro Sites, Pro Sites branding, corporate identity, brand colors, Pro Sites typography, visual identity, web development, professional sites, Australian web agency

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
- **Pro Sites Primary**: `#0052CC` (RGB: 0, 82, 204)
  - Use for: Headlines, primary CTAs, key UI elements
  - Primary brand color - use prominently

**Secondary Color:**
- **Pro Sites Secondary**: `#FF5630` (RGB: 255, 86, 48)
  - Use for: Accents, highlights, supporting elements

**Accent Color:**
- **Pro Sites Accent**: `#36B37E` (RGB: 54, 179, 126)
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
- **Headings**: Inter
- **Body Text**: Inter
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
  --primary-color: #0052CC;
  --secondary-color: #FF5630;
  --accent-color: #36B37E;
  --dark: #1A1A1A;
  --light: #F5F5F5;

  --font-heading: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;
}
```

**Web-Specific Guidelines:**

Since Pro Sites specializes in professional web development, pay special attention to:

1. **Responsive Design**: Ensure brand colors work on all screen sizes
2. **Accessibility**: Maintain WCAG AA standards (4.5:1 contrast minimum)
3. **Call-to-Actions**: Use primary color (#0052CC) for primary CTAs, secondary (#FF5630) for urgent actions
4. **Success States**: Use accent green (#36B37E) for success messages and confirmations
5. **Interactive Elements**:
   - Buttons: Primary color with hover state using darker shade
   - Links: Primary color with underline on hover
   - Forms: Primary color for focus states

**Modern Web Patterns:**
```css
/* Primary Button */
.btn-primary {
  background: #0052CC;
  color: white;
  border-radius: 4px;
  padding: 12px 24px;
}

.btn-primary:hover {
  background: #003d99;
}

/* Secondary Button */
.btn-secondary {
  background: #FF5630;
  color: white;
}

/* Success State */
.success {
  color: #36B37E;
  border-color: #36B37E;
}
```

## Implementation Guidelines

### For Simple Branding Requests

When user asks for "Pro Sites branding" or "use our brand colors":
1. Apply primary brand color to all headings
2. Apply dark neutral to body text
3. Use light neutral for backgrounds
4. Add logo from `assets/logo.png` to header/footer

### For Comprehensive Branding

When creating from scratch or user requests "full Pro Sites brand treatment":
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

1. **Add Logo Assets**: Place Pro Sites's logo files in `assets/`
   - `logo.png` (required)
   - `logo-white.png` (for dark backgrounds)
   - `logo-horizontal.png` (alternative orientation)

2. **Customize References**: Edit files in `references/` to add detailed brand specifications

3. **Add Templates**: Place pre-branded templates in `assets/templates/` for quick starts

4. **Test**: Create sample artifacts to ensure the guidelines work as expected

5. **Iterate**: Update based on usage and feedback
