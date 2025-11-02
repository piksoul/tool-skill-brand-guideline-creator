# Brand Skill Architecture: Multi-Repository Pattern

## Overview

The brand skill system follows a **multi-repository architecture** where skills are created centrally but deployed and used independently per client. This pattern provides optimal flexibility, security, and maintainability.

## Architecture Pattern

```
┌─────────────────────────────────────────────────────────────┐
│  GENERATOR REPOSITORY (Central Factory)                      │
│  tool-skill-brand-guideline-creator/                         │
│                                                               │
│  Purpose: CREATE, VALIDATE, PACKAGE brand skills             │
│  Owner: Brand/Development team                               │
│  Access: Internal team only                                  │
│                                                               │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   CREATE    │ -> │  VALIDATE   │ -> │   PACKAGE   │     │
│  │ init_brand  │    │  validate_  │    │  package_   │     │
│  │  _skill.py  │    │  brand.py   │    │  skill.py   │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                                       │             │
│         v                                       v             │
│  brand-skills/                            dist/               │
│  ├── pro-sites/                          ├── pro-sites.skill │
│  ├── acme-corp/                          ├── acme-corp.skill │
│  └── startup-xyz/                        └── startup-xyz.skill│
│                                                               │
└───────────────────────────────┬───────────────────────────────┘
                                │
                    DISTRIBUTE .skill files
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        v                       v                       v
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│ CLIENT REPO A │      │ CLIENT REPO B │      │ CLIENT REPO C │
│ pro-sites/    │      │ acme-corp/    │      │ startup-xyz/  │
│               │      │               │      │               │
│ .claude/      │      │ .claude/      │      │ .claude/      │
│   skills/     │      │   skills/     │      │   skills/     │
│   └─pro-sites│      │   └─acme-corp │      │   └─startup   │
│               │      │               │      │               │
│ projects/     │      │ projects/     │      │ projects/     │
│ content/      │      │ content/      │      │ content/      │
│               │      │               │      │               │
│ Independent   │      │ Independent   │      │ Independent   │
│ cadence       │      │ cadence       │      │ cadence       │
│ & evolution   │      │ & evolution   │      │ & evolution   │
└───────────────┘      └───────────────┘      └───────────────┘
```

## Repository Types

### 1. Generator Repository (Factory)

**Name:** `tool-skill-brand-guideline-creator`

**Purpose:** Central factory for creating and managing brand skills

**Contents:**
```
tool-skill-brand-guideline-creator/
├── scripts/
│   ├── init_brand_skill.py       # Create new skills
│   ├── validate_brand_assets.py  # Validate skills
│   └── package_skill.py          # Package for distribution
├── brand-skills/                 # Source skills (editable)
│   ├── pro-sites/
│   ├── acme-corp/
│   └── startup-xyz/
├── templates/                    # Reusable templates
├── dist/                         # Packaged .skill files
│   ├── pro-sites.skill
│   ├── acme-corp.skill
│   └── startup-xyz.skill
└── docs/
    ├── README.md
    ├── SKILL_USAGE_PLAYBOOK.md
    └── ARCHITECTURE.md (this file)
```

**Activities:**
- ✅ Create new brand skills
- ✅ Edit and maintain skills
- ✅ Validate skill structure
- ✅ Package skills for distribution
- ✅ Version control skills
- ❌ NOT for using skills in actual work
- ❌ NOT for generating branded content

**Team:** Brand/Development team, skill maintainers

**Updates:** When brand guidelines change, update here first

---

### 2. Client Brand Repositories (Usage)

**Name Pattern:** `{client-name}-brand`

**Purpose:** Dedicated repository for each client's branded work

**Example: Pro Sites**
```
pro-sites-brand/
├── README.md
├── .claude/skills/
│   └── pro-sites/               # Installed skill
│       ├── SKILL.md
│       ├── assets/
│       ├── references/
│       └── scripts/
├── brand-assets/
│   ├── logos/
│   │   ├── original/            # Master files from client
│   │   └── variations/
│   ├── fonts/
│   ├── guidelines/
│   │   └── brand-manual.pdf
│   └── style-guide/
├── projects/
│   ├── website-redesign-2024/
│   ├── marketing-campaign-q4/
│   ├── sales-materials/
│   └── client-portal/
├── generated-content/
│   ├── presentations/
│   ├── marketing/
│   ├── web-components/
│   ├── documents/
│   └── graphics/
└── templates/
    ├── presentation-master.pptx
    ├── document-template.docx
    └── email-template.html
```

**Activities:**
- ✅ Install packaged skills
- ✅ Generate branded content
- ✅ Create client deliverables
- ✅ Manage client projects
- ✅ Store brand assets
- ❌ NOT for editing skills (edit in generator repo)
- ❌ NOT for creating new skills

**Team:** Client-specific team, designers, developers

**Updates:** When receiving updated .skill files, reinstall

---

## Why Separate Repositories Per Client?

### 1. **Independent Development Cadence**

Each client has unique needs and timelines:

```
Pro Sites (Fast-moving startup)
├── Weekly brand updates
├── Rapid iteration
├── Frequent experiments
└── Agile workflow

Acme Corp (Enterprise client)
├── Quarterly updates
├── Formal approval process
├── Stable, long-term projects
└── Waterfall workflow

Startup XYZ (New client)
├── Daily changes
├── Brand still evolving
├── Experimental phase
└── Rapid prototyping
```

**Benefit:** Each repo evolves at its own pace without affecting others.

---

### 2. **Isolated Brand Evolution**

Brand changes stay contained:

```
Scenario: Pro Sites rebrands with new logo and colors

pro-sites-brand/
├── Receive updated pro-sites.skill v2.0.0
├── Uninstall old skill
├── Install new skill
└── All Pro Sites projects now use new brand

acme-corp-brand/
└── Unchanged! Still uses acme-corp.skill v1.5.0

startup-xyz-brand/
└── Unchanged! Still uses startup-xyz.skill v0.8.0
```

**Benefit:** No risk of accidentally applying wrong brand to wrong client.

---

### 3. **Access Control & Security**

Sensitive client work stays isolated:

```
Team Structure:
├── Pro Sites team → Access to pro-sites-brand/ only
├── Acme Corp team → Access to acme-corp-brand/ only
└── Startup XYZ team → Access to startup-xyz-brand/ only

Confidential clients:
└── nda-client-brand/ → Restricted repository access
```

**Benefit:** Each team sees only their client's work and assets.

---

### 4. **Version Independence**

Different clients can use different skill versions:

```
pro-sites-brand/
└── Uses pro-sites.skill v2.0.0 (latest, stable)

acme-corp-brand/
└── Uses acme-corp.skill v1.5.0 (locked, approved)

startup-xyz-brand/
└── Uses startup-xyz.skill v0.9.0-beta (experimental)
```

**Benefit:** Version updates are opt-in per client, not forced globally.

---

### 5. **Clear Ownership & Responsibility**

Each repository has a clear owner:

```
Repository              Owner               Responsibility
─────────────────────────────────────────────────────────────
tool-skill-brand-*      Brand Team          Skill creation
pro-sites-brand         Pro Sites PM        Pro Sites work
acme-corp-brand         Acme Account Mgr    Acme projects
startup-xyz-brand       Startup Lead        Startup deliverables
```

**Benefit:** Clear accountability, easier to manage, simpler auditing.

---

### 6. **Project Organization**

Each client's work is logically grouped:

```
pro-sites-brand/projects/
├── website-redesign/
│   ├── Components use Pro Sites branding automatically
│   └── All assets in one place
├── marketing-q4/
│   ├── Campaign materials
│   └── Consistent brand application
└── sales-materials/
    └── Branded documents
```

**Benefit:** Everything for one client is together, easy to find and manage.

---

## Workflow Example

### Creating and Deploying a New Client Skill

**Step 1: Create in Generator Repo**
```bash
# In tool-skill-brand-guideline-creator/
cd tool-skill-brand-guideline-creator

# Create new skill
python scripts/init_brand_skill.py "New Client Co" \
  --primary-color "#FF6600" \
  --font-heading "Roboto"

# Add logos
cp /path/to/logo.png brand-skills/new-client-co/assets/

# Validate
python scripts/validate_brand_assets.py new-client-co

# Package
python scripts/package_skill.py new-client-co

# Result: dist/new-client-co.skill
```

**Step 2: Create Client Repository**
```bash
# Create dedicated client repo
mkdir ../new-client-co-brand
cd ../new-client-co-brand
git init

# Set up structure
mkdir -p .claude/skills
mkdir -p brand-assets/{logos,fonts,guidelines}
mkdir -p projects
mkdir -p generated-content
mkdir -p templates

echo "# New Client Co Brand Repository" > README.md
```

**Step 3: Install Skill in Client Repo**
```bash
# Still in new-client-co-brand/
unzip ../tool-skill-brand-guideline-creator/dist/new-client-co.skill \
  -d .claude/skills/

# Commit
git add .
git commit -m "Initialize New Client Co brand repository with skill"
```

**Step 4: Start Creating**
```bash
# Create first project
mkdir projects/website-launch
cd projects/website-launch

# Ask Claude to create branded content
# Claude automatically uses .claude/skills/new-client-co/
```

---

## Multi-Client Agency Scenario

For agencies handling many clients, you can choose between:

### Option A: Separate Repos Per Client (Recommended)

```
my-agency/
├── tool-skill-brand-guideline-creator/   # Skill factory
├── client-a-brand/                       # Client A work
├── client-b-brand/                       # Client B work
├── client-c-brand/                       # Client C work
└── client-d-brand/                       # Client D work
```

**Pros:**
- ✅ Maximum isolation
- ✅ Clear boundaries
- ✅ Independent access control
- ✅ Separate git histories

**Cons:**
- ⚠️ More repositories to manage
- ⚠️ Switching requires changing directories

---

### Option B: Multi-Client Single Repo (Alternative)

```
agency-brand-work/
├── .claude/skills/
│   ├── client-a/          # All skills in one repo
│   ├── client-b/
│   ├── client-c/
│   └── client-d/
└── clients/
    ├── client-a/          # All work in one repo
    ├── client-b/
    ├── client-c/
    └── client-d/
```

**Pros:**
- ✅ Single repository
- ✅ Easy to switch between clients
- ✅ Shared tools and templates

**Cons:**
- ⚠️ Less isolation
- ⚠️ Harder access control
- ⚠️ Mixed git history
- ⚠️ All teams see all clients

**Recommendation:** Use Option A (separate repos) for most scenarios. Use Option B only for very small teams where everyone works on all clients.

---

## Skill Update Workflow

### When a Client's Brand Changes

**Step 1: Update in Generator Repo**
```bash
# In tool-skill-brand-guideline-creator/
cd brand-skills/pro-sites

# Edit SKILL.md, update colors, add new logos, etc.
# Validate
cd ../..
python scripts/validate_brand_assets.py pro-sites

# Re-package with new version
python scripts/package_skill.py pro-sites
# Creates dist/pro-sites.skill (updated)
```

**Step 2: Distribute to Client Repo**
```bash
# Option A: Copy file
cp dist/pro-sites.skill /path/to/pro-sites-brand/

# Option B: Push to shared location
git add dist/pro-sites.skill
git commit -m "Update Pro Sites skill v2.0.0"
git push
```

**Step 3: Update Client Repo**
```bash
# In pro-sites-brand/
cd pro-sites-brand

# Remove old skill
rm -rf .claude/skills/pro-sites

# Install updated skill
unzip /path/to/pro-sites.skill -d .claude/skills/

# Commit update
git add .claude/skills/pro-sites
git commit -m "Update Pro Sites brand skill to v2.0.0"

# All future work uses updated brand!
```

---

## Best Practices

### For Generator Repository

1. **Version Skills**: Tag skill versions in git
   ```bash
   git tag -a pro-sites-v1.0.0 -m "Pro Sites skill v1.0.0"
   ```

2. **Document Changes**: Maintain CHANGELOG for each skill
   ```
   brand-skills/pro-sites/CHANGELOG.md
   ```

3. **Test Before Packaging**: Always validate before distributing
   ```bash
   python scripts/validate_brand_assets.py pro-sites
   ```

4. **Archive Old Versions**: Keep old .skill files
   ```
   dist/
   ├── archive/
   │   ├── pro-sites-v1.0.0.skill
   │   └── pro-sites-v1.5.0.skill
   └── pro-sites.skill  (latest)
   ```

### For Client Repositories

1. **Track Skill Version**: Document which skill version is installed
   ```bash
   echo "pro-sites.skill v2.0.0" > .claude/skills/VERSION
   ```

2. **Don't Edit Skills Directly**: Always update through generator repo

3. **Commit Skill Updates**: Track skill changes in git history
   ```bash
   git commit -m "Update skill: Pro Sites v2.0.0 (new logo, updated colors)"
   ```

4. **Test After Updates**: Verify branding works after skill updates
   ```bash
   # Create test content to verify brand application
   ```

---

## Scaling

### Small Team (1-3 clients)
```
tool-skill-brand-guideline-creator/  # Skill factory
client-a-brand/                       # Client repos
client-b-brand/
client-c-brand/
```

### Medium Team (4-10 clients)
```
brand-skills/                        # Skill factory
clients/
├── client-a-brand/
├── client-b-brand/
├── client-c-brand/
├── client-d-brand/
└── ...
```

### Large Team (10+ clients)
```
skills-factory/                      # Central skill creation
clients/
├── enterprise/
│   ├── client-a-brand/
│   ├── client-b-brand/
│   └── ...
├── startups/
│   ├── client-x-brand/
│   ├── client-y-brand/
│   └── ...
└── agencies/
    └── ...
```

---

## Summary

**Key Principles:**

1. **One Factory, Many Users**
   - Create skills centrally
   - Deploy skills independently

2. **Separation of Concerns**
   - Generator repo: CREATE skills
   - Client repos: USE skills

3. **Independence**
   - Each client repo evolves independently
   - No cross-contamination

4. **Flexibility**
   - Different cadences per client
   - Different versions per client
   - Different teams per client

5. **Maintainability**
   - Clear ownership
   - Easy updates
   - Simple rollback

**The Pattern:**
```
CREATE → PACKAGE → DISTRIBUTE → INSTALL → USE
   ↓         ↓          ↓           ↓        ↓
Generator  .skill    Share      Client   Branded
  Repo      File     File        Repo    Content
```

This architecture provides the optimal balance of centralized skill management and distributed, flexible usage.
