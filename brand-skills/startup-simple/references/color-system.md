# Startup Simple Color System

This document provides comprehensive color specifications and usage guidelines.

## Primary Color

- **Startup Simple Primary**: `#FF5733` (RGB: 255, 87, 51)
  - Use for: Primary CTAs, headings, key UI elements
  - Accessibility: WCAG AA compliant on white backgrounds (verify contrast ratio)
  - Recommended uses: Buttons, links, headlines, brand accents

**Usage Rules:**
- Always use for primary brand touchpoints
- Ensure 4.5:1 contrast ratio for text
- Pair with white or light neutral backgrounds




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
  --primary: #FF5733;
  --secondary: #FF6600;
  --accent: #33CC33;

  /* Neutrals */
  --dark: #1A1A1A;
  --light: #F5F5F5;
  --white: #FFFFFF;
}
```

### Hex vs RGB

- **Hex**: Use for CSS, design tools (e.g., `#FF5733`)
- **RGB**: Use for alpha transparency, JavaScript (e.g., `rgba(255, 87, 51, 0.8)`)

## Brand Evolution

When updating colors:
1. Document changes in this file
2. Update SKILL.md with new values
3. Archive old color specifications
4. Re-test accessibility compliance
5. Update all templates and examples
