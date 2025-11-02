# Brand Skill Usage Playbook

This playbook explains how to **use** brand skills after creating them with the generator tools.

## Table of Contents

1. [Understanding Brand Skills](#understanding-brand-skills)
2. [Workflow Overview](#workflow-overview)
3. [Packaging Skills](#packaging-skills)
4. [Installing Skills](#installing-skills)
5. [Using Skills in Practice](#using-skills-in-practice)
6. [Distribution to Teams](#distribution-to-teams)
7. [Best Practices](#best-practices)
8. [Troubleshooting](#troubleshooting)

---

## Understanding Brand Skills

### What is a Brand Skill?

A **brand skill** is a packaged set of instructions and assets that teaches Claude (or other AI assistants) how to apply a specific brand's identity consistently across different types of content.

**Components:**
- `SKILL.md` - Core instructions with YAML metadata
- `assets/` - Logo files, templates, fonts
- `references/` - Detailed specifications
- `scripts/` - Optional automation tools

### How Skills Work

When a skill is installed:

1. **Discovery**: Claude reads the skill's YAML frontmatter (name, description, keywords)
2. **Triggering**: When user requests match the skill's description/keywords, Claude loads the skill
3. **Execution**: Claude follows the instructions in SKILL.md and uses bundled assets
4. **Output**: Branded content that follows the guidelines

**Example Flow:**
```
User: "Create a Pro Sites branded presentation slide"
  ↓
Claude detects "Pro Sites" matches pro-sites skill
  ↓
Claude loads SKILL.md + assets/logo.png
  ↓
Claude creates slide with:
  - Primary color #0052CC background
  - White text in Inter font
  - Pro Sites logo from assets/
  ↓
User receives branded content
```

---

## Workflow Overview

### Development vs Deployment

**This Repository (Development):**
- ✅ Create and edit brand skills
- ✅ Validate assets and structure
- ✅ Test and iterate on guidelines
- ❌ NOT where you use skills in actual work

**Target Repositories (Deployment):**
- ✅ Install packaged skills
- ✅ Use skills for actual branded content
- ✅ Reference skills in projects
- ❌ NOT where you edit skills

### The Complete Lifecycle

```
1. CREATE (this repo)
   └─> scripts/init_brand_skill.py "Client Name"

2. CUSTOMIZE (this repo)
   └─> Edit SKILL.md, add logos, enhance references

3. VALIDATE (this repo)
   └─> scripts/validate_brand_assets.py client-name

4. PACKAGE (this repo)
   └─> scripts/package_skill.py client-name
   └─> Output: dist/client-name.skill

5. DISTRIBUTE (copy .skill file)
   └─> Share client-name.skill file with team

6. INSTALL (target repo/project)
   └─> Copy to ~/.claude/skills/ or project skills/

7. USE (target repo/project)
   └─> Request branded content from Claude

8. ITERATE (back to this repo)
   └─> Update skill based on feedback
   └─> Re-package and redistribute
```

---

## Packaging Skills

### Manual Packaging (Current Method)

Since the packaging script isn't built yet, package skills manually:

**Step 1: Prepare the Skill**

```bash
cd brand-skills/pro-sites

# Ensure validation passes
python ../../scripts/validate_brand_assets.py pro-sites

# Remove any unnecessary files
rm -f .DS_Store
rm -f */.DS_Store
```

**Step 2: Create the Package**

```bash
# From repository root
cd brand-skills

# Create a zip file with .skill extension
zip -r ../dist/pro-sites.skill pro-sites/ \
  -x "*.placeholder" \
  -x "*/__pycache__/*" \
  -x "*/.DS_Store"

# Verify the package
unzip -l ../dist/pro-sites.skill
```

**Step 3: Verify Package Contents**

The .skill file should contain:
```
pro-sites/
├── SKILL.md                    # Required
├── assets/
│   ├── logo.png               # Logo files
│   ├── logo-white.png
│   ├── logo.svg
│   └── logo-white.svg
├── references/
│   ├── color-system.md
│   ├── typography.md
│   └── logo-usage.md
└── scripts/                    # Optional
    └── example_brand_script.py
```

### Automated Packaging (Future)

Once the packaging script is created:

```bash
# Package a single skill
python scripts/package_skill.py pro-sites

# Package all skills
python scripts/package_skill.py --all

# Output location
ls -lh dist/*.skill
```

---

## Installing Skills

### Option 1: User-Level Installation (Recommended for Personal Use)

Install skills in your Claude skills directory for use across all projects:

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Extract the skill
unzip dist/pro-sites.skill -d ~/.claude/skills/

# Verify installation
ls -la ~/.claude/skills/pro-sites/
```

**When to use:**
- You work on Pro Sites projects frequently
- You want the skill available everywhere
- Personal/individual workflow

### Option 2: Project-Level Installation (Recommended for Teams)

Install skills in a specific project repository:

```bash
# Navigate to your project
cd /path/to/your/project

# Create project skills directory
mkdir -p .claude/skills

# Extract the skill
unzip /path/to/pro-sites.skill -d .claude/skills/

# Add to .gitignore if skills contain sensitive assets
echo ".claude/skills/*/assets/*.png" >> .gitignore

# Or commit skills to git for team sharing
git add .claude/skills/pro-sites/
git commit -m "Add Pro Sites brand skill for project"
```

**When to use:**
- Team collaboration on branded projects
- Project-specific branding requirements
- Want skills version-controlled with project

### Option 3: Direct Copy (Development/Testing)

For testing during development:

```bash
# Copy skill directory directly
cp -r brand-skills/pro-sites /target/project/.claude/skills/

# Or symlink for live editing
ln -s $(pwd)/brand-skills/pro-sites /target/project/.claude/skills/pro-sites
```

**When to use:**
- Actively developing/testing the skill
- Need live updates without re-packaging
- Development workflow only

### Verification

After installation, verify Claude can find the skill:

```bash
# Check skill is in the right location
ls -la ~/.claude/skills/pro-sites/SKILL.md
# or
ls -la .claude/skills/pro-sites/SKILL.md

# Verify YAML frontmatter is valid
head -n 10 ~/.claude/skills/pro-sites/SKILL.md
```

You should see:
```yaml
---
name: pro-sites
description: Applies Pro Sites's official brand colors...
license: Proprietary - For Pro Sites use only
---
```

---

## Using Skills in Practice

### How to Invoke a Skill

Skills are triggered automatically when your request matches the skill's description and keywords.

**Trigger Phrases for Pro Sites:**

Direct mentions:
- "Use Pro Sites branding"
- "Apply Pro Sites brand colors"
- "Create with Pro Sites style"

Implicit matching:
- "Create a presentation for Pro Sites"
- "Design a Pro Sites landing page"
- "Make a branded document for Pro Sites"

### Example Use Cases

#### Use Case 1: Branded Presentation Slide

**Request:**
```
Create a title slide for a Pro Sites client presentation about
our new web development services. Use Pro Sites branding.
```

**Claude will:**
1. Load the pro-sites skill
2. Apply primary color (#0052CC) background
3. Use Inter font for text
4. Place Pro Sites logo from assets/
5. Follow layout guidelines from SKILL.md

**Output:**
- HTML/SVG slide with proper branding
- Or instructions for creating in PowerPoint
- With exact color codes and logo placement

#### Use Case 2: Branded Web Component

**Request:**
```
Create a React button component using Pro Sites brand guidelines.
Include hover states.
```

**Claude will:**
1. Load pro-sites skill
2. Reference color-system.md for button states
3. Use CSS variables from SKILL.md
4. Apply Inter font family
5. Implement hover state (#003d99)

**Output:**
```jsx
import React from 'react';
import './ProSitesButton.css';

const ProSitesButton = ({ children, onClick }) => (
  <button className="btn-primary" onClick={onClick}>
    {children}
  </button>
);

// CSS with Pro Sites branding
```

#### Use Case 3: Branded Document Header

**Request:**
```
Create a Word document header for Pro Sites quarterly report.
```

**Claude will:**
1. Load pro-sites skill
2. Place logo from assets/
3. Use primary color for header background
4. Apply Inter font for title
5. Follow document guidelines from SKILL.md

#### Use Case 4: Brand-Compliant Email Template

**Request:**
```
Design an HTML email template for Pro Sites marketing campaign.
Must be responsive and follow brand guidelines.
```

**Claude will:**
1. Load pro-sites skill
2. Use web-specific guidelines from SKILL.md
3. Apply responsive color patterns
4. Include semantic colors for CTAs
5. Use proper logo placement

### Working Across Multiple Projects

If you have multiple brand skills installed:

**Explicit selection:**
```
Create a presentation using Pro Sites branding
```

**Context-based selection:**
```
# If working in a Pro Sites client project
Create a branded presentation
# Claude infers Pro Sites based on project context
```

**Multiple brands in one project:**
```
Create a Pro Sites header and an Acme Corp footer
# Claude loads both skills as needed
```

---

## Distribution to Teams

### Method 1: Shared File System

**Best for:** Small co-located teams

```bash
# Share via network drive
cp dist/pro-sites.skill /Volumes/SharedDrive/brand-skills/

# Team members install
unzip /Volumes/SharedDrive/brand-skills/pro-sites.skill \
  -d ~/.claude/skills/
```

### Method 2: Git Repository

**Best for:** Distributed teams, version control

**Option A: Include in project repos**
```bash
# In each project that needs Pro Sites branding
mkdir -p .claude/skills
unzip pro-sites.skill -d .claude/skills/
git add .claude/skills/pro-sites/
git commit -m "Add Pro Sites brand skill"
git push

# Team members get skill automatically
git pull
```

**Option B: Separate skills repository**
```bash
# Create a skills repository
mkdir company-brand-skills
cd company-brand-skills
git init

# Add packaged skills
cp /path/to/tool-skill-brand-guideline-creator/dist/*.skill ./
git add *.skill
git commit -m "Add company brand skills"
git push

# Team members clone and install
git clone company-brand-skills
cd company-brand-skills
unzip pro-sites.skill -d ~/.claude/skills/
```

### Method 3: Internal Package Registry

**Best for:** Large enterprises, automated deployment

```bash
# Upload to internal registry
aws s3 cp dist/pro-sites.skill s3://company-skills/

# Team members download
aws s3 cp s3://company-skills/pro-sites.skill .
unzip pro-sites.skill -d ~/.claude/skills/
```

### Method 4: Direct File Sharing

**Best for:** Quick distribution, small teams

1. Email the .skill file as attachment
2. Share via Slack/Teams
3. Upload to Google Drive/Dropbox

**Recipient instructions:**
```bash
# Download pro-sites.skill
# Then install:
unzip ~/Downloads/pro-sites.skill -d ~/.claude/skills/
```

### Version Management

**Track skill versions:**

```bash
# Version in filename
dist/pro-sites-v1.0.0.skill
dist/pro-sites-v1.1.0.skill

# Or use git tags in this repo
git tag -a pro-sites-v1.0.0 -m "Pro Sites skill v1.0.0"
git push --tags
```

**Communicate updates:**
```
From: Brand Team
To: Development Team
Subject: Pro Sites Brand Skill Updated to v1.1.0

Changes:
- Updated primary color to #0056D2
- Added new logo variants
- Enhanced web component guidelines

Please update your installed skill:
1. Download: https://link-to-skill/pro-sites-v1.1.0.skill
2. Remove old: rm -rf ~/.claude/skills/pro-sites
3. Install new: unzip pro-sites-v1.1.0.skill -d ~/.claude/skills/
```

---

## Best Practices

### For Skill Creators

1. **Keep Skills Updated**
   - Update when brand guidelines change
   - Test changes before distributing
   - Communicate updates to users

2. **Version Control**
   - Tag releases in git
   - Include version in skill documentation
   - Maintain changelog

3. **Documentation**
   - Include README in skill package
   - Document known issues
   - Provide usage examples

4. **Testing**
   - Test skills in real projects before distributing
   - Validate with actual use cases
   - Get feedback from users

### For Skill Users

1. **Keep Skills Current**
   - Check for updates regularly
   - Subscribe to skill update notifications
   - Test updates in non-production first

2. **Provide Feedback**
   - Report issues to skill creators
   - Suggest improvements
   - Share successful use cases

3. **Use Explicit Triggers**
   - Mention brand name explicitly in requests
   - Specify "use [Brand] branding" when needed
   - Don't rely solely on context

4. **Verify Output**
   - Check colors match brand guidelines
   - Verify logo placement is correct
   - Ensure fonts are applied properly

### For Teams

1. **Standardize Installation**
   - Document installation process
   - Provide setup scripts
   - Include in onboarding

2. **Centralize Skill Management**
   - Designate a skill maintainer
   - Central repository for skills
   - Regular skill audits

3. **Training**
   - Train team on skill usage
   - Share best practices
   - Document common patterns

---

## Troubleshooting

### Skill Not Triggering

**Problem:** Claude doesn't seem to use the skill when requested.

**Solutions:**

1. **Verify installation:**
   ```bash
   ls -la ~/.claude/skills/pro-sites/SKILL.md
   ```

2. **Check YAML frontmatter:**
   ```bash
   head -n 10 ~/.claude/skills/pro-sites/SKILL.md
   ```
   Ensure no syntax errors in YAML.

3. **Use explicit trigger:**
   Instead of: "Create a presentation"
   Use: "Create a presentation using Pro Sites branding"

4. **Check skill name:**
   Use the exact name from YAML frontmatter.

5. **Restart Claude/session:**
   Skills may need session restart to load.

### Assets Not Found

**Problem:** Claude can't find logo or other assets.

**Solutions:**

1. **Verify asset paths:**
   ```bash
   ls -la ~/.claude/skills/pro-sites/assets/*.png
   ```

2. **Check SKILL.md references:**
   Ensure paths like `assets/logo.png` are correct.

3. **Re-package and reinstall:**
   ```bash
   # In generator repo
   cd brand-skills
   zip -r ../dist/pro-sites.skill pro-sites/

   # Reinstall
   rm -rf ~/.claude/skills/pro-sites
   unzip dist/pro-sites.skill -d ~/.claude/skills/
   ```

### Colors Don't Match

**Problem:** Output colors don't match brand guidelines.

**Solutions:**

1. **Verify hex codes in SKILL.md:**
   ```bash
   grep "#" ~/.claude/skills/pro-sites/SKILL.md
   ```

2. **Check color-system.md:**
   Ensure all colors are documented consistently.

3. **Use specific requests:**
   "Use Pro Sites primary color #0052CC for the header"

### Multiple Skills Conflict

**Problem:** Wrong brand applied when multiple skills installed.

**Solutions:**

1. **Use explicit brand names:**
   "Create with Pro Sites branding" (not just "create branded content")

2. **Check skill descriptions:**
   Ensure different brands have distinct keywords.

3. **Remove unused skills:**
   ```bash
   rm -rf ~/.claude/skills/unused-brand/
   ```

### Skill Updates Not Applying

**Problem:** Changes to skill don't appear in usage.

**Solutions:**

1. **Fully remove old version:**
   ```bash
   rm -rf ~/.claude/skills/pro-sites
   ```

2. **Install fresh copy:**
   ```bash
   unzip pro-sites.skill -d ~/.claude/skills/
   ```

3. **Clear any caches:**
   Restart Claude session or IDE.

4. **Verify update installed:**
   ```bash
   cat ~/.claude/skills/pro-sites/SKILL.md | grep "version"
   ```

---

## Quick Reference

### Installation Command

```bash
# User-level (personal use)
unzip pro-sites.skill -d ~/.claude/skills/

# Project-level (team use)
unzip pro-sites.skill -d .claude/skills/
```

### Trigger Phrases

```
"Use [Brand Name] branding"
"Apply [Brand Name] brand colors"
"Create [Brand Name] branded [artifact]"
"Follow [Brand Name] brand guidelines"
```

### Verification Commands

```bash
# Check installation
ls -la ~/.claude/skills/pro-sites/

# Verify YAML
head -n 10 ~/.claude/skills/pro-sites/SKILL.md

# List all skills
ls -la ~/.claude/skills/

# Check assets
ls -la ~/.claude/skills/pro-sites/assets/
```

---

## Summary

### The Two-Repository Model

**Generator Repository (this repo):**
- Create skills: `scripts/init_brand_skill.py`
- Validate skills: `scripts/validate_brand_assets.py`
- Package skills: Create .skill files
- Maintain and update skills

**Target Repositories (your projects):**
- Install skills: Extract .skill files
- Use skills: Request branded content
- Don't edit skills directly

### Key Takeaways

1. ✅ **Skills are packaged** - Create .skill files for distribution
2. ✅ **Skills are installed** - Extract to `~/.claude/skills/` or `.claude/skills/`
3. ✅ **Skills are triggered** - Use brand name in requests
4. ✅ **Skills are maintained** - Update in generator repo, re-distribute
5. ✅ **Skills are shared** - Distribute .skill files to team members

### Next Steps

1. Package your Pro Sites skill: `zip -r dist/pro-sites.skill brand-skills/pro-sites/`
2. Install in target project: `unzip pro-sites.skill -d ~/.claude/skills/`
3. Test with branded content request
4. Share with team members
5. Iterate based on feedback

---

**Need help?** Refer to the main README.md or create an issue in this repository.
