#!/usr/bin/env python3
"""
Brand Skill Initializer

Creates a fully scaffolded brand guideline skill with provided brand information.

Usage:
    python scripts/init_brand_skill.py "Acme Corp" --primary-color "#0066CC" --font-heading "Montserrat"
    python scripts/init_brand_skill.py "TechStart" --primary-color "#FF5733" --secondary-color "#33FF57" --font-body "Open Sans"
"""

import argparse
import os
import sys
from pathlib import Path
import re


def slugify(text):
    """Convert text to a URL-friendly slug"""
    # Convert to lowercase
    text = text.lower()
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    # Remove non-alphanumeric characters except hyphens
    text = re.sub(r'[^a-z0-9-]', '', text)
    # Remove duplicate hyphens
    text = re.sub(r'-+', '-', text)
    # Strip leading/trailing hyphens
    text = text.strip('-')
    return text


def validate_hex_color(color):
    """Validate hex color format"""
    if not color:
        return True
    pattern = r'^#?[0-9A-Fa-f]{6}$'
    if not re.match(pattern, color):
        return False
    return True


def normalize_hex_color(color):
    """Ensure hex color has # prefix"""
    if not color:
        return None
    color = color.strip()
    if not color.startswith('#'):
        color = '#' + color
    return color.upper()


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def create_skill_md(client_name, slug, args):
    """Generate SKILL.md content with brand information"""

    # Prepare color information
    colors_section = ""
    if args.primary_color:
        rgb = hex_to_rgb(args.primary_color)
        colors_section += f"""
**Primary Color:**
- **{client_name} Primary**: `{args.primary_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Headlines, primary CTAs, key UI elements
  - Primary brand color - use prominently
"""

    if args.secondary_color:
        rgb = hex_to_rgb(args.secondary_color)
        colors_section += f"""
**Secondary Color:**
- **{client_name} Secondary**: `{args.secondary_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Accents, highlights, supporting elements
"""

    if args.accent_color:
        rgb = hex_to_rgb(args.accent_color)
        colors_section += f"""
**Accent Color:**
- **{client_name} Accent**: `{args.accent_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Highlights, important callouts
  - Use sparingly for maximum impact
"""

    # Add neutral colors
    colors_section += """
**Neutral Colors:**
- **Dark**: `#1A1A1A` (RGB: 26, 26, 26)
  - Use for: Body text, dark backgrounds
- **Light**: `#F5F5F5` (RGB: 245, 245, 245)
  - Use for: Light backgrounds, subtle sections
"""

    # Prepare typography section
    typography_section = ""
    if args.font_heading or args.font_body:
        typography_section = "\n### Typography\n\n**Fonts:**\n"
        if args.font_heading:
            typography_section += f"- **Headings**: {args.font_heading}\n"
        if args.font_subheading:
            typography_section += f"- **Subheadings**: {args.font_subheading}\n"
        if args.font_body:
            typography_section += f"- **Body Text**: {args.font_body}\n"

        typography_section += """- **Fallbacks**: Arial/Helvetica for headings, sans-serif for body

**Font Sizes:**
- H1: 36-48pt
- H2: 28-32pt
- H3: 20-24pt
- Body: 14-16pt

For detailed typography guidelines, see `references/typography.md`
"""

    # Create the SKILL.md content
    content = f"""---
name: {slug}
description: Applies {client_name}'s official brand colors, typography, and visual identity to documents, presentations, and web artifacts. Use when creating any {client_name}-branded content, when the user requests {client_name} branding, or when working on materials for {client_name} that need visual consistency.
license: Proprietary - For {client_name} use only
---

# {client_name} Brand Guidelines

## Overview

Apply {client_name}'s brand identity to all artifacts including presentations, documents, reports, and web pages. This skill ensures visual consistency across all {client_name} materials.

**Keywords**: {client_name}, {client_name} branding, corporate identity, brand colors, {client_name} typography, visual identity

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

{colors_section}

**Color Application:**
- Headings: Primary brand color or white (on dark backgrounds)
- Body text: Dark neutral
- Backgrounds: Light neutral or white
- Accents: Secondary/Accent colors sparingly

For comprehensive color usage rules, see `references/color-system.md`
{typography_section}

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
:root {{
  --primary-color: {args.primary_color or '#0066CC'};
  --secondary-color: {args.secondary_color or '#FF6600'};
  --dark: #1A1A1A;
  --light: #F5F5F5;

  --font-heading: '{args.font_heading or 'Arial'}', sans-serif;
  --font-body: '{args.font_body or 'Helvetica'}', sans-serif;
}}
```

## Implementation Guidelines

### For Simple Branding Requests

When user asks for "{client_name} branding" or "use our brand colors":
1. Apply primary brand color to all headings
2. Apply dark neutral to body text
3. Use light neutral for backgrounds
4. Add logo from `assets/logo.png` to header/footer

### For Comprehensive Branding

When creating from scratch or user requests "full {client_name} brand treatment":
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

1. **Add Logo Assets**: Place {client_name}'s logo files in `assets/`
   - `logo.png` (required)
   - `logo-white.png` (for dark backgrounds)
   - `logo-horizontal.png` (alternative orientation)

2. **Customize References**: Edit files in `references/` to add detailed brand specifications

3. **Add Templates**: Place pre-branded templates in `assets/templates/` for quick starts

4. **Test**: Create sample artifacts to ensure the guidelines work as expected

5. **Iterate**: Update based on usage and feedback
"""

    return content


def create_color_system_md(client_name, args):
    """Generate references/color-system.md"""

    primary_section = ""
    if args.primary_color:
        rgb = hex_to_rgb(args.primary_color)
        primary_section = f"""## Primary Color

- **{client_name} Primary**: `{args.primary_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Primary CTAs, headings, key UI elements
  - Accessibility: WCAG AA compliant on white backgrounds (verify contrast ratio)
  - Recommended uses: Buttons, links, headlines, brand accents

**Usage Rules:**
- Always use for primary brand touchpoints
- Ensure 4.5:1 contrast ratio for text
- Pair with white or light neutral backgrounds
"""

    secondary_section = ""
    if args.secondary_color:
        rgb = hex_to_rgb(args.secondary_color)
        secondary_section = f"""## Secondary Color

- **{client_name} Secondary**: `{args.secondary_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Supporting elements, accents, highlights
  - Works well with: Primary color and neutrals
"""

    accent_section = ""
    if args.accent_color:
        rgb = hex_to_rgb(args.accent_color)
        accent_section = f"""## Accent Color

- **{client_name} Accent**: `{args.accent_color}` (RGB: {rgb[0]}, {rgb[1]}, {rgb[2]})
  - Use for: Highlights, important callouts
  - Limit to <20% of any design
  - Never use for body text
"""

    content = f"""# {client_name} Color System

This document provides comprehensive color specifications and usage guidelines.

{primary_section}
{secondary_section}
{accent_section}

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
:root {{
  /* Brand colors */
  --primary: {args.primary_color or '#0066CC'};
  --secondary: {args.secondary_color or '#FF6600'};
  --accent: {args.accent_color or '#33CC33'};

  /* Neutrals */
  --dark: #1A1A1A;
  --light: #F5F5F5;
  --white: #FFFFFF;
}}
```

### Hex vs RGB

- **Hex**: Use for CSS, design tools (e.g., `{args.primary_color or '#0066CC'}`)
- **RGB**: Use for alpha transparency, JavaScript (e.g., `rgba({hex_to_rgb(args.primary_color)[0] if args.primary_color else 0}, {hex_to_rgb(args.primary_color)[1] if args.primary_color else 102}, {hex_to_rgb(args.primary_color)[2] if args.primary_color else 204}, 0.8)`)

## Brand Evolution

When updating colors:
1. Document changes in this file
2. Update SKILL.md with new values
3. Archive old color specifications
4. Re-test accessibility compliance
5. Update all templates and examples
"""

    return content


def create_typography_md(client_name, args):
    """Generate references/typography.md"""

    fonts_section = ""
    if args.font_heading:
        fonts_section += f"""### Heading Font: {args.font_heading}

- **Usage**: H1, H2, H3 headlines
- **Weights**: Bold (700), SemiBold (600) preferred
- **Fallback**: Arial, Helvetica, sans-serif
"""

    if args.font_subheading:
        fonts_section += f"""### Subheading Font: {args.font_subheading}

- **Usage**: H4, H5, section headers
- **Weights**: SemiBold (600), Medium (500)
- **Fallback**: Arial, sans-serif
"""

    if args.font_body:
        fonts_section += f"""### Body Font: {args.font_body}

- **Usage**: Paragraphs, body text, captions
- **Weights**: Regular (400), Medium (500) for emphasis
- **Fallback**: Helvetica, Arial, sans-serif
"""

    content = f"""# {client_name} Typography Guidelines

This document specifies font usage, sizing, and pairing rules for {client_name} brand materials.

## Font Families

{fonts_section if fonts_section else "**Note**: Update this section with {client_name}'s specified fonts."}

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
body {{
  font-family: '{args.font_body or 'Helvetica'}', Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #1A1A1A;
}}

h1, h2, h3 {{
  font-family: '{args.font_heading or 'Arial'}', sans-serif;
  line-height: 1.3;
  color: {args.primary_color or '#0066CC'};
}}

h1 {{
  font-size: 36px;
  font-weight: 700;
}}

h2 {{
  font-size: 28px;
  font-weight: 600;
}}
```

### Microsoft Word

1. Create custom styles for {client_name} headings
2. Set Heading 1: {args.font_heading or 'Arial'} Bold, 36pt, {args.primary_color or '#0066CC'}
3. Set Body: {args.font_body or 'Helvetica'} Regular, 14pt, #1A1A1A
4. Save as template for reuse

### PowerPoint

1. Edit Master Slide
2. Set title: {args.font_heading or 'Arial'} Bold, 36pt
3. Set body: {args.font_body or 'Helvetica'} Regular, 18pt
4. Apply to all slide layouts

## Font Licensing

**Important**: Ensure {client_name} has proper licensing for all fonts used in brand materials.

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
"""

    return content


def create_logo_usage_md(client_name):
    """Generate references/logo-usage.md"""

    content = f"""# {client_name} Logo Usage Guidelines

This document provides detailed specifications for using {client_name}'s logo correctly.

## Available Logo Files

Place logo files in `assets/`:
- `logo.png` - Primary logo for light backgrounds
- `logo-white.png` - Logo variant for dark backgrounds
- `logo-horizontal.png` - Horizontal orientation (if applicable)
- `logo-vertical.png` - Vertical orientation (if applicable)
- `logo.svg` - Vector format for scaling (recommended)

## Logo Specifications

### Minimum Size

**Digital:**
- Minimum height: 50px
- Recommended: 80-120px for standard usage

**Print:**
- Minimum height: 0.5 inches
- Recommended: 1-2 inches for standard usage

### Clearspace

Maintain clearspace around logo equal to the height of a significant logo element:
- Minimum clearspace: 2x the height of the primary logo element
- No text, graphics, or other elements should intrude into clearspace

### File Formats

- **PNG**: Use for digital applications (web, presentations, documents)
- **SVG**: Use when scaling is important (responsive web)
- **EPS/PDF**: Use for print and professional design software
- **JPG**: Avoid (no transparency support)

## Usage Rules

### Do's

- Use official logo files only (no recreations)
- Maintain aspect ratio (no stretching or distorting)
- Place on appropriate backgrounds (light logo on dark, dark logo on light)
- Ensure sufficient contrast with background
- Leave adequate clearspace around logo
- Use high-resolution files for print

### Don'ts

- Don't rotate the logo
- Don't add effects (drop shadows, gradients, outlines)
- Don't change logo colors (unless using approved variants)
- Don't place on busy backgrounds that reduce legibility
- Don't stretch, squish, or distort proportions
- Don't recreate or redraw the logo

## Background Usage

### Light Backgrounds

Use primary logo (`logo.png`) on:
- White backgrounds
- Light gray backgrounds (#F5F5F5 or lighter)
- Light brand colors with sufficient contrast

### Dark Backgrounds

Use white logo variant (`logo-white.png`) on:
- Dark backgrounds (#333333 or darker)
- Primary brand color backgrounds
- Dark photography or imagery

### Busy Backgrounds

If placing logo on photography or complex backgrounds:
1. Add a solid background shape (white or dark)
2. Ensure minimum clearspace within shape
3. Ensure shape has sufficient contrast with photo

## Placement Guidelines

### Documents (Word/PDF)

- Header: Right-aligned or centered, small size
- Footer: Small size, right-aligned with page numbers
- Cover page: Larger, centered or left-aligned

### Presentations (PowerPoint/Keynote)

- Title slide: Larger, centered or bottom-right
- Content slides: Small, consistent position (usually top-right or bottom-right)
- Section dividers: Centered, medium size

### Web Pages

- Header: Left-aligned, medium size (80-120px height)
- Footer: Small size (40-60px height)
- Favicon: Use simplified icon version (if available)

## Color Variations

**Primary Logo**: Full color version
- Use whenever possible
- Preferred for all brand materials

**White Logo**: Reverse version for dark backgrounds
- Use on dark backgrounds
- Ensure sufficient contrast (4.5:1 minimum)

**Black Logo**: Single-color version (if available)
- Use for single-color printing
- Use when color printing is not available

## Logo Misuse Examples

### Common Mistakes to Avoid

1. **Stretching**: Logo is wider or narrower than original proportions
2. **Rotation**: Logo is tilted at an angle
3. **Low contrast**: Logo on background with insufficient contrast
4. **Effects**: Drop shadows, glows, or other effects applied
5. **Crowding**: Other elements too close to logo (violating clearspace)
6. **Color changes**: Logo colors altered from brand specifications
7. **Low resolution**: Pixelated or blurry logo

## Quality Checklist

Before using logo, verify:
- [ ] Using official logo file (not screenshot or recreation)
- [ ] Aspect ratio is maintained (no distortion)
- [ ] Logo meets minimum size requirements
- [ ] Clearspace is respected on all sides
- [ ] Sufficient contrast with background (4.5:1+)
- [ ] No effects or modifications applied
- [ ] High resolution file used (for print: 300dpi+)

## Getting Logo Files

If you need logo files for {client_name}:
1. Check the `assets/` directory in this skill
2. Contact {client_name}'s marketing/brand team
3. Download from official brand portal (if available)

**Never** recreate or modify the logo yourself.

## Updates

When logo changes:
1. Replace all logo files in `assets/`
2. Update this document with new specifications
3. Archive old logo files (for reference)
4. Update all templates and examples
5. Communicate changes to all brand users
"""

    return content


def create_readme_for_assets():
    """Generate assets/README.md"""
    return """# Brand Assets

Place brand assets in this directory:

## Logo Files

- `logo.png` - Primary logo for light backgrounds (required)
- `logo-white.png` - Logo for dark backgrounds (recommended)
- `logo-horizontal.png` - Horizontal logo orientation (optional)
- `logo-vertical.png` - Vertical logo orientation (optional)
- `logo.svg` - Vector format for scaling (recommended)

## Templates (optional)

Create `templates/` subdirectory for pre-branded templates:
- `templates/presentation-template.pptx`
- `templates/report-template.docx`
- `templates/one-pager-template.pdf`

## Fonts (optional)

If distributing custom fonts (ensure proper licensing):
- `fonts/HeadingFont-Bold.ttf`
- `fonts/BodyFont-Regular.ttf`

## Next Steps

1. Add logo files (PNG at minimum, SVG recommended)
2. Add any pre-branded templates
3. Remove this README.md file once assets are in place
"""


def create_placeholder_logo(path, logo_type="primary"):
    """Create a placeholder text file for logo"""
    content = f"""PLACEHOLDER: {logo_type.upper()} LOGO

Replace this file with the actual logo image file.

Recommended formats:
- PNG (with transparency)
- SVG (vector, scalable)

Minimum requirements:
- Digital: 50px height minimum
- Print: 300 DPI, 0.5" height minimum

For detailed logo specifications, see:
references/logo-usage.md
"""
    with open(path, 'w') as f:
        f.write(content)


def init_brand_skill(client_name, args):
    """Initialize a new brand skill with the given parameters"""

    # Create slug for directory name
    slug = slugify(client_name)

    # Determine base path
    if args.path:
        base_path = Path(args.path)
    else:
        base_path = Path('brand-skills')

    skill_path = base_path / slug

    # Check if directory already exists
    if skill_path.exists():
        if not args.force:
            print(f"Error: Skill directory '{skill_path}' already exists.")
            print(f"Use --force to overwrite.")
            return 1
        print(f"Warning: Overwriting existing skill at '{skill_path}'")

    # Create directory structure
    print(f"Creating brand skill: {client_name}")
    print(f"Skill slug: {slug}")
    print(f"Location: {skill_path}")
    print()

    skill_path.mkdir(parents=True, exist_ok=True)
    (skill_path / 'assets').mkdir(exist_ok=True)
    (skill_path / 'references').mkdir(exist_ok=True)
    (skill_path / 'scripts').mkdir(exist_ok=True)

    # Create SKILL.md
    print("Creating SKILL.md...")
    skill_md_content = create_skill_md(client_name, slug, args)
    with open(skill_path / 'SKILL.md', 'w') as f:
        f.write(skill_md_content)

    # Create reference files
    print("Creating reference documentation...")

    color_system_content = create_color_system_md(client_name, args)
    with open(skill_path / 'references' / 'color-system.md', 'w') as f:
        f.write(color_system_content)

    typography_content = create_typography_md(client_name, args)
    with open(skill_path / 'references' / 'typography.md', 'w') as f:
        f.write(typography_content)

    logo_usage_content = create_logo_usage_md(client_name)
    with open(skill_path / 'references' / 'logo-usage.md', 'w') as f:
        f.write(logo_usage_content)

    # Create assets README
    print("Creating assets directory...")
    assets_readme = create_readme_for_assets()
    with open(skill_path / 'assets' / 'README.md', 'w') as f:
        f.write(assets_readme)

    # Create placeholder logo files
    create_placeholder_logo(skill_path / 'assets' / 'logo.png.placeholder', 'primary')
    create_placeholder_logo(skill_path / 'assets' / 'logo-white.png.placeholder', 'white')

    # Create a simple example script
    print("Creating example script...")
    example_script = f"""#!/usr/bin/env python3
\"\"\"
Example script for applying {client_name} brand colors

This is a placeholder - customize based on your needs.
\"\"\"

# {client_name} brand colors
PRIMARY_COLOR = "{args.primary_color or '#0066CC'}"
SECONDARY_COLOR = "{args.secondary_color or '#FF6600'}"
DARK = "#1A1A1A"
LIGHT = "#F5F5F5"

def apply_brand_colors():
    \"\"\"Example function to apply brand colors\"\"\"
    print(f"Applying {client_name} brand colors...")
    print(f"Primary: {{PRIMARY_COLOR}}")
    print(f"Secondary: {{SECONDARY_COLOR}}")
    # Add your implementation here

if __name__ == "__main__":
    apply_brand_colors()
"""
    with open(skill_path / 'scripts' / 'example_brand_script.py', 'w') as f:
        f.write(example_script)

    # Create success summary
    print()
    print("=" * 60)
    print(f"✓ Brand skill created successfully!")
    print("=" * 60)
    print()
    print(f"Skill name: {client_name}")
    print(f"Skill slug: {slug}")
    print(f"Location: {skill_path.absolute()}")
    print()
    print("Created files:")
    print(f"  • SKILL.md (pre-populated with brand info)")
    print(f"  • references/color-system.md")
    print(f"  • references/typography.md")
    print(f"  • references/logo-usage.md")
    print(f"  • assets/README.md")
    print(f"  • assets/logo.png.placeholder")
    print(f"  • assets/logo-white.png.placeholder")
    print(f"  • scripts/example_brand_script.py")
    print()
    print("Next steps:")
    print(f"  1. Add logo files to: {skill_path / 'assets'}/")
    print(f"  2. Review and customize: {skill_path / 'SKILL.md'}")
    print(f"  3. Add detailed specs to files in: {skill_path / 'references'}/")
    print(f"  4. Run validation: python scripts/validate_brand_assets.py {slug}")
    print()

    # Show brand info summary
    if args.primary_color or args.font_heading or args.font_body:
        print("Brand information:")
        if args.primary_color:
            print(f"  • Primary color: {args.primary_color}")
        if args.secondary_color:
            print(f"  • Secondary color: {args.secondary_color}")
        if args.accent_color:
            print(f"  • Accent color: {args.accent_color}")
        if args.font_heading:
            print(f"  • Heading font: {args.font_heading}")
        if args.font_subheading:
            print(f"  • Subheading font: {args.font_subheading}")
        if args.font_body:
            print(f"  • Body font: {args.font_body}")
        print()

    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Initialize a new brand guideline skill',
        epilog='Example: python init_brand_skill.py "Acme Corp" --primary-color "#0066CC" --font-heading "Montserrat"'
    )

    # Required arguments
    parser.add_argument('client_name', help='Client/brand name (e.g., "Acme Corp")')

    # Color arguments
    parser.add_argument('--primary-color', help='Primary brand color (hex format, e.g., "#0066CC")')
    parser.add_argument('--secondary-color', help='Secondary brand color (hex format)')
    parser.add_argument('--accent-color', help='Accent color (hex format)')

    # Typography arguments
    parser.add_argument('--font-heading', help='Heading font name (e.g., "Montserrat")')
    parser.add_argument('--font-subheading', help='Subheading font name (e.g., "Montserrat SemiBold")')
    parser.add_argument('--font-body', help='Body text font name (e.g., "Open Sans")')

    # Path arguments
    parser.add_argument('--path', help='Base path for skill (default: ./brand-skills/)')
    parser.add_argument('--force', action='store_true', help='Overwrite existing skill directory')

    args = parser.parse_args()

    # Validate colors
    colors_to_validate = [
        ('primary-color', args.primary_color),
        ('secondary-color', args.secondary_color),
        ('accent-color', args.accent_color)
    ]

    for color_name, color_value in colors_to_validate:
        if color_value and not validate_hex_color(color_value):
            print(f"Error: Invalid hex color for --{color_name}: {color_value}")
            print(f"Color must be in format: #RRGGBB (e.g., #0066CC)")
            return 1

    # Normalize colors
    if args.primary_color:
        args.primary_color = normalize_hex_color(args.primary_color)
    if args.secondary_color:
        args.secondary_color = normalize_hex_color(args.secondary_color)
    if args.accent_color:
        args.accent_color = normalize_hex_color(args.accent_color)

    # Initialize the skill
    return init_brand_skill(args.client_name, args)


if __name__ == '__main__':
    sys.exit(main())
