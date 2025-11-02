# Startup Simple Typography Guidelines

This document specifies font usage, sizing, and pairing rules for Startup Simple brand materials.

## Font Families

### Heading Font: Inter

- **Usage**: H1, H2, H3 headlines
- **Weights**: Bold (700), SemiBold (600) preferred
- **Fallback**: Arial, Helvetica, sans-serif
### Body Font: Roboto

- **Usage**: Paragraphs, body text, captions
- **Weights**: Regular (400), Medium (500) for emphasis
- **Fallback**: Helvetica, Arial, sans-serif


## Font Sizing

### Desktop/Print

- **H1**: 36-48pt (Headlines, major sections)
- **H2**: 28-32pt (Subsections)
- **H3**: 20-24pt (Minor headings)
- **Body**: 14-16pt (Paragraph text)
- **Caption**: 12-14pt (Image captions, footnotes)

### Mobile/Responsive

- **H1**: 28-32pt
- **H2**: 22-26pt
- **H3**: 18-20pt
- **Body**: 16-18pt (minimum for readability)
- **Caption**: 14pt

## Line Height & Spacing

- **Headlines**: 1.2-1.3 line height
- **Body text**: 1.5-1.6 line height
- **Paragraph spacing**: 1em between paragraphs
- **Letter spacing**: 0 for body, slight increase (0.02-0.05em) for uppercase headings

## Font Pairing Rules

1. **Contrast**: Headings and body should have clear visual distinction
2. **Hierarchy**: Use size, weight, and color to establish information hierarchy
3. **Consistency**: Stick to 2-3 font families maximum per document
4. **Readability**: Ensure sufficient contrast between text and background

## Best Practices

### Do's

- Use heading font for all headlines and titles
- Maintain consistent sizing across similar document types
- Ensure sufficient contrast for readability
- Use bold/medium weights for emphasis rather than different fonts

### Don'ts

- Don't mix more than 3 font families in one document
- Don't use decorative fonts for body text
- Don't use font sizes below 12pt for body text
- Don't set body text in all caps

## Implementation Examples

### CSS

```css
body {
  font-family: 'Roboto', Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #1A1A1A;
}

h1, h2, h3 {
  font-family: 'Inter', sans-serif;
  line-height: 1.3;
  color: #FF5733;
}

h1 {
  font-size: 36px;
  font-weight: 700;
}

h2 {
  font-size: 28px;
  font-weight: 600;
}
```

### Microsoft Word

1. Create custom styles for Startup Simple headings
2. Set Heading 1: Inter Bold, 36pt, #FF5733
3. Set Body: Roboto Regular, 14pt, #1A1A1A
4. Save as template for reuse

### PowerPoint

1. Edit Master Slide
2. Set title: Inter Bold, 36pt
3. Set body: Roboto Regular, 18pt
4. Apply to all slide layouts

## Font Licensing

**Important**: Ensure Startup Simple has proper licensing for all fonts used in brand materials.

- Web fonts: Verify license allows web embedding
- Desktop fonts: Ensure license covers all users
- Custom fonts: Document where/how to obtain fonts

## Updates

When typography changes:
1. Update this document with new specifications
2. Update SKILL.md with new font families
3. Update all templates (Word, PowerPoint, etc.)
4. Archive old typography specifications
5. Communicate changes to all brand users
