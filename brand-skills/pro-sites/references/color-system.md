# Pro Sites Color System

This document provides comprehensive color specifications and usage guidelines for Pro Sites (https://www.pro-sites.com.au), a professional web development and design company based in Australia.

**Brand Context**: These colors are optimized for web use, with particular attention to digital accessibility, responsive design, and modern web UI patterns.

## Primary Color

- **Pro Sites Primary**: `#0052CC` (RGB: 0, 82, 204)
  - Use for: Primary CTAs, headings, key UI elements
  - Accessibility: WCAG AA compliant on white backgrounds (verify contrast ratio)
  - Recommended uses: Buttons, links, headlines, brand accents

**Usage Rules:**
- Always use for primary brand touchpoints
- Ensure 4.5:1 contrast ratio for text
- Pair with white or light neutral backgrounds

## Secondary Color

- **Pro Sites Secondary**: `#FF5630` (RGB: 255, 86, 48)
  - Use for: Supporting elements, accents, highlights
  - Works well with: Primary color and neutrals

## Accent Color

- **Pro Sites Accent**: `#36B37E` (RGB: 54, 179, 126)
  - Use for: Highlights, important callouts
  - Limit to <20% of any design
  - Never use for body text


## Neutral Colors

- **Dark**: `#1A1A1A` (RGB: 26, 26, 26)
  - Use for: Body text, dark backgrounds
  - Primary text color

- **Light**: `#F5F5F5` (RGB: 245, 245, 245)
  - Use for: Light backgrounds, subtle sections
  - Background color for content areas

- **White**: `#FFFFFF` (RGB: 255, 255, 255)
  - Use for: Main backgrounds, text on dark backgrounds

## Color Combinations

### Recommended Pairings

1. **Headers**: Primary color on white background
2. **Body**: Dark text on white/light background
3. **CTAs**: White text on primary color background
4. **Accents**: Accent color sparingly on white background

### Avoid

- Low contrast combinations (ensure 4.5:1 minimum for text)
- Clashing color combinations
- Overuse of accent colors (keep under 20% of design)

## Accessibility

All color combinations should meet WCAG 2.1 Level AA standards:
- Normal text: 4.5:1 contrast ratio minimum
- Large text (18pt+): 3:1 contrast ratio minimum
- UI components: 3:1 contrast ratio minimum

Test all combinations with tools like:
- WebAIM Contrast Checker
- Adobe Color Accessibility Tools
- Chrome DevTools Accessibility Inspector

## Implementation

### CSS Variables

```css
:root {
  /* Brand colors */
  --primary: #0052CC;
  --secondary: #FF5630;
  --accent: #36B37E;

  /* Neutrals */
  --dark: #1A1A1A;
  --light: #F5F5F5;
  --white: #FFFFFF;
}
```

### Hex vs RGB

- **Hex**: Use for CSS, design tools (e.g., `#0052CC`)
- **RGB**: Use for alpha transparency, JavaScript (e.g., `rgba(0, 82, 204, 0.8)`)

## Web-Specific Color Usage

As a web development company, Pro Sites materials often include web UI examples. Use these color applications:

### Interactive States

**Primary Button States:**
- Default: `#0052CC`
- Hover: `#003d99` (darker shade)
- Active/Pressed: `#002b66`
- Disabled: `rgba(0, 82, 204, 0.4)`

**Link States:**
- Default: `#0052CC`
- Hover: `#003d99`
- Visited: `#5243AA` (purple tint)

### Semantic Colors

- **Success**: Use accent green `#36B37E` for success messages, confirmations
- **Warning**: Use secondary `#FF5630` sparingly for important alerts
- **Error**: Use darker red `#DE350B` (derived from secondary)
- **Info**: Use primary `#0052CC` for informational messages

### Code Syntax Highlighting

When showing code examples in Pro Sites materials:
- Comments: `#6B778C` (muted gray)
- Keywords: `#0052CC` (primary)
- Strings: `#36B37E` (accent green)
- Functions: `#FF5630` (secondary)
- Background: `#F4F5F7` (light neutral)

### UI Component Colors

**Forms:**
- Input border: `#DFE1E6` (light gray)
- Input focus: `#0052CC` (primary)
- Error state: `#DE350B`
- Success state: `#36B37E`

**Backgrounds:**
- Primary surface: `#FFFFFF`
- Secondary surface: `#F4F5F7`
- Elevated surface: `#FFFFFF` with shadow
- Code blocks: `#F4F5F7`

## Brand Evolution

When updating colors:
1. Document changes in this file
2. Update SKILL.md with new values
3. Archive old color specifications
4. Re-test accessibility compliance
5. Update all templates and examples
