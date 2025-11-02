# Brand Guideline Skill Generator

A specialized repository for rapidly creating brand guideline skills for different clients. This toolkit enables you to quickly scaffold, validate, and package professional brand skills that help AI assistants apply client branding consistently.

## ⚠️ Important: Repository Purpose

**This is a GENERATOR repository - for creating and packaging brand skills.**

**You do NOT use skills here for actual work. Instead:**

1. **CREATE skills here** → Generate and package brand skills
2. **DEPLOY skills elsewhere** → Install in client-specific repositories
3. **USE skills there** → Create branded content in client repos

```
┌─────────────────────────┐
│ THIS REPO (Factory)     │  →  CREATE & PACKAGE skills
│ tool-skill-brand-*      │
└─────────────────────────┘
           │
           │ .skill files
           ↓
┌─────────────────────────┐
│ CLIENT REPOS (Usage)    │  →  INSTALL & USE skills
│ pro-sites-brand/        │
│ acme-corp-brand/        │
│ startup-xyz-brand/      │
└─────────────────────────┘
```

📖 **See [ARCHITECTURE.md](./ARCHITECTURE.md) for the complete multi-repository pattern.**

## Overview

This repository provides tools and templates to create **brand guideline skills** - packaged instructions and assets that enable AI assistants to correctly apply a client's brand identity to documents, presentations, websites, and other artifacts.

**Key Features:**
- 🚀 **Rapid Setup**: Create a fully-scaffolded brand skill in minutes
- ✅ **Validation**: Automated checking of assets, colors, and structure
- 📦 **Templates**: Reusable templates with industry best practices
- 🎨 **Examples**: Three sample skills at different complexity levels
- 🛠️ **Scripts**: Python tooling for initialization and validation

## Repository Structure

```
tool-skill-brand-guideline-creator/
├── brand-skills/              # Client brand guideline skills
│   ├── startup-simple/        # Example: Minimal brand skill
│   ├── midsize-standard/      # Example: Standard brand skill
│   └── enterprise-complex/    # Example: Comprehensive brand skill
├── templates/                 # Reusable templates
│   └── brand-skill-template/  # Base template with placeholders
├── scripts/                   # Automation tools
│   ├── init_brand_skill.py    # Create new brand skill
│   └── validate_brand_assets.py  # Validate brand assets
├── dist/                      # Packaged .skill files (generated)
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Quick Start: Create a Brand Skill in 5 Minutes

### 1. Initialize a New Brand Skill

Use the `init_brand_skill.py` script to quickly scaffold a new brand skill:

```bash
python scripts/init_brand_skill.py "Acme Corp" \
  --primary-color "#0066CC" \
  --secondary-color "#FF6600" \
  --font-heading "Montserrat" \
  --font-body "Open Sans"
```

This creates:
- Complete directory structure (`brand-skills/acme-corp/`)
- Pre-populated `SKILL.md` with your brand info
- Reference documentation templates
- Asset placeholders
- Example scripts

### 2. Add Brand Assets

Add your client's logo files to `brand-skills/acme-corp/assets/`:

```bash
cp /path/to/acme-logo.png brand-skills/acme-corp/assets/logo.png
cp /path/to/acme-logo-white.png brand-skills/acme-corp/assets/logo-white.png
```

### 3. Validate the Skill

Run validation to check everything is correct:

```bash
python scripts/validate_brand_assets.py acme-corp
```

This checks:
- Logo files exist and are valid images
- Color codes are proper hex/RGB format
- Directory structure is correct
- SKILL.md has required frontmatter
- Reference files are present

### 4. Customize (Optional)

Edit the generated files to add more detail:
- `SKILL.md` - Core instructions and workflows
- `references/color-system.md` - Detailed color specifications
- `references/typography.md` - Font pairing and sizing rules
- `references/logo-usage.md` - Logo placement guidelines

### 5. Package and Deploy

*(Future: Add packaging script)*

Your brand skill is ready to use!

## Scripts

### init_brand_skill.py

Create a new brand guideline skill with pre-populated content.

**Usage:**
```bash
python scripts/init_brand_skill.py "Client Name" [OPTIONS]
```

**Required Arguments:**
- `client_name` - Client or brand name (e.g., "Acme Corp")

**Optional Arguments:**
- `--primary-color HEX` - Primary brand color (e.g., "#0066CC")
- `--secondary-color HEX` - Secondary brand color
- `--accent-color HEX` - Accent color for highlights
- `--font-heading NAME` - Heading font name (e.g., "Montserrat")
- `--font-subheading NAME` - Subheading font name
- `--font-body NAME` - Body text font name (e.g., "Open Sans")
- `--path PATH` - Base path for skills (default: `./brand-skills/`)
- `--force` - Overwrite existing skill directory

**Examples:**

Minimal setup (just colors):
```bash
python scripts/init_brand_skill.py "TechStart" --primary-color "#FF5733"
```

Standard setup (colors + fonts):
```bash
python scripts/init_brand_skill.py "Midsize Co" \
  --primary-color "#0066CC" \
  --secondary-color "#FF6600" \
  --font-heading "Montserrat" \
  --font-body "Open Sans"
```

Complete setup (all options):
```bash
python scripts/init_brand_skill.py "Enterprise Corp" \
  --primary-color "#1E3A8A" \
  --secondary-color "#10B981" \
  --accent-color "#F59E0B" \
  --font-heading "Playfair Display" \
  --font-subheading "Source Sans Pro" \
  --font-body "Source Sans Pro"
```

### validate_brand_assets.py

Validate brand skill assets and structure.

**Usage:**
```bash
python scripts/validate_brand_assets.py SKILL_NAME [OPTIONS]
```

**Arguments:**
- `skill_name` - Skill directory name (e.g., "acme-corp")
- `--path PATH` - Base path to skills directory (default: `./brand-skills/`)
- `--strict` - Treat warnings as errors

**Examples:**

Basic validation:
```bash
python scripts/validate_brand_assets.py acme-corp
```

Strict validation (warnings = errors):
```bash
python scripts/validate_brand_assets.py acme-corp --strict
```

Custom path:
```bash
python scripts/validate_brand_assets.py my-client --path /custom/path/to/skills
```

**What It Checks:**
- ✅ Directory structure (required folders present)
- ✅ SKILL.md exists and has valid YAML frontmatter
- ✅ Logo files exist and are valid image formats
- ✅ Image dimensions meet minimum requirements
- ✅ Color codes are valid hex/RGB format
- ✅ Reference documentation exists
- ✅ File sizes are reasonable
- 💡 Suggestions for optimal formats (SVG logos, etc.)

## Brand Asset Checklist

When onboarding a new client, collect:

### Required
- [ ] **Client name** - Official company/brand name
- [ ] **Primary brand color** - Hex code (e.g., #0066CC)
- [ ] **Primary logo** - PNG format, transparent background, minimum 100px height

### Recommended
- [ ] **Secondary/accent colors** - Hex codes for additional colors
- [ ] **Logo variants** - White version, horizontal orientation, SVG format
- [ ] **Font names** - Heading and body fonts
- [ ] **Existing brand guidelines** - PDF or document with official specs

### Optional (For Comprehensive Skills)
- [ ] **Color usage rules** - When to use each color
- [ ] **Font weights and pairings** - Specific font specifications
- [ ] **Logo clearspace rules** - Minimum spacing around logo
- [ ] **Pre-branded templates** - PowerPoint, Word, or other templates
- [ ] **Brand photography guidelines** - Image style and treatment
- [ ] **Accessibility requirements** - Contrast ratios, WCAG compliance

## Example Skills

This repository includes three example brand skills at different complexity levels:

### 1. Startup Simple (`brand-skills/startup-simple/`)

**Use Case**: Small companies, simple branding, quick setup

**Contents:**
- Minimal SKILL.md with colors and fonts
- Basic reference documentation
- Logo placeholders

**Best For:**
- Startups with simple brand guidelines
- Quick proof-of-concept
- Learning the skill structure

### 2. Midsize Standard (`brand-skills/midsize-standard/`)

**Use Case**: Most companies, standard branding needs

**Contents:**
- Comprehensive SKILL.md
- Detailed reference documentation
- Primary + secondary colors
- Multiple font specifications
- Logo variants

**Best For:**
- Established companies with brand guidelines
- Standard corporate branding
- Typical client engagements

### 3. Enterprise Complex (`brand-skills/enterprise-complex/`)

**Use Case**: Large organizations, comprehensive branding

**Contents:**
- Complete SKILL.md with all sections
- Extensive reference documentation
- Full color palette (primary, secondary, accent)
- Complete typography system
- Multiple logo variants
- *(Future: Pre-branded templates, automation scripts)*

**Best For:**
- Enterprise clients
- Complex brand systems
- Multiple use cases and artifact types

## Workflow: Onboarding a New Client

Follow this workflow to create a brand skill for a new client:

### Step 1: Gather Information

Collect brand assets and information from the client:
- Request brand guidelines document
- Get logo files (PNG, SVG if available)
- Ask for brand colors (hex codes)
- Identify primary fonts

**Questions to Ask:**
- "What types of documents do you create?" (presentations, reports, websites)
- "Can you provide examples of branded materials?"
- "What would a typical request for branded content look like?"

### Step 2: Initialize the Skill

Run `init_brand_skill.py` with collected information:

```bash
python scripts/init_brand_skill.py "Client Name" \
  --primary-color "#HEXCODE" \
  --secondary-color "#HEXCODE" \
  --font-heading "Font Name" \
  --font-body "Font Name"
```

### Step 3: Add Assets

Copy logo files to the `assets/` directory:

```bash
# Add primary logo
cp client-logo.png brand-skills/client-name/assets/logo.png

# Add white logo variant
cp client-logo-white.png brand-skills/client-name/assets/logo-white.png

# Add SVG version (if available)
cp client-logo.svg brand-skills/client-name/assets/logo.svg
```

### Step 4: Customize Content

Review and enhance the generated files:

1. **SKILL.md** - Review and adjust:
   - Verify color descriptions and usage
   - Add any specific brand rules
   - Include concrete examples
   - Customize artifact-specific guidelines

2. **references/color-system.md** - Add details:
   - Color accessibility information
   - Specific usage rules (when to use each color)
   - Approved color combinations

3. **references/typography.md** - Enhance:
   - Font pairing rules
   - Specific size requirements
   - Line height and spacing specs

4. **references/logo-usage.md** - Specify:
   - Clearspace requirements
   - Minimum sizes
   - Placement guidelines

### Step 5: Validate

Run validation to ensure everything is correct:

```bash
python scripts/validate_brand_assets.py client-name
```

Fix any errors or warnings reported.

### Step 6: Test

Create sample artifacts using the skill:
- Generate a test presentation
- Create a test document
- Build a sample webpage

Verify outputs match client expectations.

### Step 7: Iterate

Based on usage, improve the skill:
- Add missing information
- Clarify ambiguous guidelines
- Add templates for common use cases
- Create scripts for repetitive tasks

## Templates

### Brand Skill Template (`templates/brand-skill-template/`)

A complete template with `[PLACEHOLDERS]` for manual customization.

**Use this when:**
- You prefer manual setup over scripted generation
- You need a starting point for complex customization
- You want to understand the full structure

**How to use:**
1. Copy the template: `cp -r templates/brand-skill-template brand-skills/new-client`
2. Replace all `[PLACEHOLDERS]` with actual values
3. Add logo files to `assets/`
4. Customize reference documentation
5. Validate with `validate_brand_assets.py`

**Placeholders to replace:**
- `[CLIENT_NAME]` - Client/brand name
- `[SKILL-SLUG]` - URL-friendly skill name
- `[PRIMARY_COLOR]`, `[SECONDARY_COLOR]` - Hex codes
- `[HEADING_FONT]`, `[BODY_FONT]` - Font names
- `[COLOR_NAME]` - Descriptive color names
- `[HEX_CODE]`, `[R]`, `[G]`, `[B]` - Color values
- `[USAGE_DESCRIPTION]` - Color usage descriptions

## Best Practices

### 1. Start Simple, Enhance Later

- Begin with minimal information (colors + logo)
- Test with real use cases
- Add detail based on actual needs
- Iterate based on feedback

### 2. Use Concrete Examples

Instead of:
> "Use appropriate colors for slides"

Write:
> "Title slide: #0066CC background with white text and logo"

### 3. Progressive Disclosure

- **SKILL.md**: Core workflows and quick reference (keep < 500 lines)
- **references/**: Detailed specifications and edge cases
- **assets/**: Files used in outputs

### 4. Keep Assets Current

When client branding changes:
- Update assets immediately
- Revise SKILL.md and references
- Archive old versions for reference
- Re-validate

### 5. Document Common Issues

Add notes about:
- Frequent mistakes
- Edge cases
- Platform-specific quirks
- Workarounds

## Handling Brand Updates

When a client updates their branding:

### Minor Updates (Color tweaks, font changes)

1. Update the affected values in SKILL.md
2. Update corresponding reference files
3. Re-validate
4. Test with existing artifacts

### Major Updates (New logo, complete rebrand)

1. Archive the old skill:
   ```bash
   mv brand-skills/client-name brand-skills/client-name-legacy-2024
   ```

2. Create new skill with updated information
3. Document what changed
4. Notify users of the update

## Troubleshooting

### Validation Fails: "Missing logo files"

**Problem**: Logo placeholders haven't been replaced with actual images.

**Solution**: Add logo files to `assets/`:
```bash
cp logo.png brand-skills/client-name/assets/logo.png
```

### Validation Warning: "Image dimensions too small"

**Problem**: Logo file is below recommended minimum (100px height).

**Solution**: Provide higher resolution logo or acknowledge if it's intentional.

### Colors Look Wrong in Output

**Problem**: Using hex codes when RGB values needed (or vice versa).

**Solution**: Provide both formats in SKILL.md (script does this automatically).

### Skill Doesn't Trigger When Expected

**Problem**: Description in frontmatter isn't comprehensive enough.

**Solution**: Add more trigger phrases to description:
- Client name variations
- Common request phrases
- Synonym terms

### Too Slow / Uses Too Many Tokens

**Problem**: SKILL.md is too long or everything is in one file.

**Solution**: Move detailed specs to `references/`, keep SKILL.md under 500 lines.

## Advanced: Custom Scripts

Add custom scripts to `scripts/` directory for automation:

### Example: Apply Brand Colors to PowerPoint

```python
#!/usr/bin/env python3
"""Apply brand colors to PowerPoint presentations"""

from pptx import Presentation
from pptx.dml.color import RGBColor

BRAND_PRIMARY = RGBColor(0, 102, 204)
BRAND_SECONDARY = RGBColor(255, 102, 0)

def apply_colors(pptx_path, output_path):
    prs = Presentation(pptx_path)

    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text_frame"):
                # Apply brand colors based on text size
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if run.font.size and run.font.size >= 240000:  # 24pt
                            run.font.color.rgb = BRAND_PRIMARY

    prs.save(output_path)

if __name__ == "__main__":
    import sys
    apply_colors(sys.argv[1], sys.argv[2])
```

Make it executable:
```bash
chmod +x brand-skills/client-name/scripts/apply_brand_colors.py
```

## Requirements

### Python

- Python 3.7+
- No external dependencies required for basic usage

### Optional Dependencies

For enhanced image validation:
```bash
pip install Pillow
```

For PowerPoint automation:
```bash
pip install python-pptx
```

For Word document automation:
```bash
pip install python-docx
```

## Contributing

This is a specialized internal tool. When adding new features:

1. Update scripts with new functionality
2. Update this README with documentation
3. Add examples demonstrating the feature
4. Test with real brand skills

## FAQ

### Q: How long does it take to create a brand skill?

**A**: 5-15 minutes with the scripts:
- 1 minute: Run `init_brand_skill.py`
- 2 minutes: Add logo files
- 2-10 minutes: Customize SKILL.md and references
- 1 minute: Validate

### Q: Can I create skills without the scripts?

**A**: Yes! Copy `templates/brand-skill-template/` and replace placeholders manually.

### Q: What if the client doesn't have official brand guidelines?

**A**: Start with what you have:
1. Get logo files
2. Extract colors from logo using design tools
3. Identify fonts from existing materials
4. Create basic skill and iterate

### Q: How do I handle multiple logo variants?

**A**: Add all variants to `assets/`:
- `logo.png` - Primary
- `logo-white.png` - For dark backgrounds
- `logo-horizontal.png` - Horizontal orientation
- `logo-vertical.png` - Vertical orientation
- `logo-icon.png` - Icon/favicon version

Document when to use each in `references/logo-usage.md`.

### Q: Should I commit client logos to git?

**A**: It depends:
- **Public logos**: Yes, safe to commit
- **Proprietary/confidential**: Add to `.gitignore` or use separate private repo
- **Large files**: Consider using Git LFS

### Q: How do I share a skill with someone?

**A**: *(Future: Packaging feature)*
Currently: Share the entire skill directory or zip it.

## Roadmap

Future enhancements:

- [ ] **Packaging script** - Create distributable `.skill` files
- [ ] **Skill installation script** - Deploy skills to AI assistant
- [ ] **Web interface** - Browser-based skill creator
- [ ] **Asset optimization** - Automatic logo resizing/optimization
- [ ] **Template generator** - Create branded templates automatically
- [ ] **Version management** - Track skill versions over time
- [ ] **Skill testing framework** - Automated testing of brand application
- [ ] **Multi-brand support** - Handle clients with multiple brands

## License

*(Add your license here)*

## Support

For issues or questions:
- Review example skills in `brand-skills/`
- Check troubleshooting section above
- Consult template documentation in `templates/brand-skill-template/`

---

**Last Updated**: 2024
**Version**: 1.0.0
