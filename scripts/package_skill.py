#!/usr/bin/env python3
"""
Brand Skill Packager

Packages brand skills into distributable .skill files.

Usage:
    python scripts/package_skill.py pro-sites
    python scripts/package_skill.py pro-sites --output custom-output-dir
    python scripts/package_skill.py --all
"""

import argparse
import os
import sys
import zipfile
from pathlib import Path
from datetime import datetime


def validate_skill_structure(skill_path: Path) -> tuple[bool, list[str]]:
    """Validate skill has required structure"""
    errors = []

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        errors.append(f"Missing required file: SKILL.md")
        return False, errors

    # Check SKILL.md has YAML frontmatter
    try:
        with open(skill_md, 'r') as f:
            content = f.read()
            if not content.startswith('---'):
                errors.append("SKILL.md missing YAML frontmatter (must start with '---')")

            # Check for required fields
            if 'name:' not in content[:500]:
                errors.append("SKILL.md frontmatter missing 'name:' field")
            if 'description:' not in content[:500]:
                errors.append("SKILL.md frontmatter missing 'description:' field")
    except Exception as e:
        errors.append(f"Error reading SKILL.md: {str(e)}")
        return False, errors

    # Check required directories
    assets_dir = skill_path / 'assets'
    if not assets_dir.exists():
        errors.append("Missing required directory: assets/")

    references_dir = skill_path / 'references'
    if not references_dir.exists():
        errors.append("Missing required directory: references/")

    if errors:
        return False, errors

    return True, []


def should_exclude(file_path: str, exclude_patterns: list[str]) -> bool:
    """Check if file should be excluded from package"""
    file_path = file_path.lower()

    for pattern in exclude_patterns:
        if pattern in file_path:
            return True

    return False


def package_skill(skill_path: Path, output_dir: Path, exclude_patterns: list[str]) -> tuple[bool, str]:
    """Package a skill into a .skill file"""

    skill_name = skill_path.name
    output_file = output_dir / f"{skill_name}.skill"

    print(f"Packaging: {skill_name}")
    print(f"Source: {skill_path}")
    print(f"Output: {output_file}")
    print()

    # Validate structure
    print("Validating skill structure...")
    valid, errors = validate_skill_structure(skill_path)

    if not valid:
        print("❌ Validation failed:")
        for error in errors:
            print(f"   - {error}")
        return False, str(output_file)

    print("✅ Validation passed")
    print()

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create zip file
    print("Creating package...")
    file_count = 0

    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through skill directory
            for root, dirs, files in os.walk(skill_path):
                # Filter out excluded directories
                dirs[:] = [d for d in dirs if not should_exclude(d, exclude_patterns)]

                for file in files:
                    file_path = Path(root) / file

                    # Check if file should be excluded
                    rel_path = file_path.relative_to(skill_path.parent)
                    if should_exclude(str(rel_path), exclude_patterns):
                        print(f"   Skipping: {rel_path}")
                        continue

                    # Add to zip
                    arcname = rel_path
                    zipf.write(file_path, arcname)
                    file_count += 1

        print()
        print(f"✅ Package created: {output_file}")
        print(f"   Files included: {file_count}")
        print(f"   Size: {output_file.stat().st_size / 1024:.1f} KB")
        return True, str(output_file)

    except Exception as e:
        print(f"❌ Error creating package: {str(e)}")
        return False, str(output_file)


def list_skills(base_path: Path) -> list[Path]:
    """List all skill directories"""
    skills = []

    if not base_path.exists():
        return skills

    for item in base_path.iterdir():
        if item.is_dir() and (item / 'SKILL.md').exists():
            skills.append(item)

    return sorted(skills)


def main():
    parser = argparse.ArgumentParser(
        description='Package brand skills into distributable .skill files',
        epilog='Example: python package_skill.py pro-sites'
    )

    parser.add_argument(
        'skill_name',
        nargs='?',
        help='Skill directory name (e.g., "pro-sites")'
    )

    parser.add_argument(
        '--path',
        default='brand-skills',
        help='Base path to skills directory (default: ./brand-skills/)'
    )

    parser.add_argument(
        '--output',
        default='dist',
        help='Output directory for .skill files (default: ./dist/)'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='Package all skills in the skills directory'
    )

    parser.add_argument(
        '--exclude',
        nargs='*',
        default=[
            '.placeholder',
            '__pycache__',
            '.pyc',
            '.DS_Store',
            '.git',
            'node_modules',
            '.vscode',
            '.idea'
        ],
        help='Patterns to exclude from package'
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.skill_name and not args.all:
        parser.print_help()
        print("\nError: Must specify skill_name or --all")
        return 1

    base_path = Path(args.path)
    output_dir = Path(args.output)

    if not base_path.exists():
        print(f"Error: Skills directory not found: {base_path}")
        return 1

    # Get skills to package
    if args.all:
        skills = list_skills(base_path)
        if not skills:
            print(f"No skills found in {base_path}")
            return 1
        print(f"Found {len(skills)} skill(s) to package")
        print()
    else:
        skill_path = base_path / args.skill_name
        if not skill_path.exists():
            print(f"Error: Skill not found: {skill_path}")
            return 1
        skills = [skill_path]

    # Package skills
    print("=" * 70)
    print("BRAND SKILL PACKAGER")
    print("=" * 70)
    print()

    successful = []
    failed = []

    for skill_path in skills:
        success, output_file = package_skill(skill_path, output_dir, args.exclude)

        if success:
            successful.append(output_file)
        else:
            failed.append(skill_path.name)

        print()
        print("-" * 70)
        print()

    # Summary
    print("=" * 70)
    print("PACKAGING SUMMARY")
    print("=" * 70)
    print()

    if successful:
        print(f"✅ Successfully packaged {len(successful)} skill(s):")
        for output_file in successful:
            print(f"   • {output_file}")
        print()

    if failed:
        print(f"❌ Failed to package {len(failed)} skill(s):")
        for skill_name in failed:
            print(f"   • {skill_name}")
        print()

    print("Next steps:")
    print("1. Test the packaged skill by extracting it:")
    if successful:
        print(f"   unzip {successful[0]} -d /tmp/test/")
    print("2. Install the skill:")
    if successful:
        print(f"   unzip {successful[0]} -d ~/.claude/skills/")
    print("3. Use the skill in your projects")
    print()

    return 0 if not failed else 1


if __name__ == '__main__':
    sys.exit(main())
