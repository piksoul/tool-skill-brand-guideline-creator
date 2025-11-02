#!/usr/bin/env python3
"""
Brand Asset Validator

Validates brand skill assets including logos, colors, and file structure.

Usage:
    python scripts/validate_brand_assets.py acme-corp
    python scripts/validate_brand_assets.py acme-corp --path /custom/path
    python scripts/validate_brand_assets.py acme-corp --strict
"""

import argparse
import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []
        self.info: List[str] = []

    def add_error(self, message: str):
        self.errors.append(f"ERROR: {message}")

    def add_warning(self, message: str):
        self.warnings.append(f"WARNING: {message}")

    def add_suggestion(self, message: str):
        self.suggestions.append(f"SUGGESTION: {message}")

    def add_info(self, message: str):
        self.info.append(f"INFO: {message}")

    def is_valid(self, strict=False) -> bool:
        if self.errors:
            return False
        if strict and self.warnings:
            return False
        return True

    def print_results(self):
        """Print validation results"""
        print()
        print("=" * 70)
        print("BRAND ASSET VALIDATION REPORT")
        print("=" * 70)
        print()

        if self.errors:
            print("ERRORS:")
            for error in self.errors:
                print(f"  ✗ {error}")
            print()

        if self.warnings:
            print("WARNINGS:")
            for warning in self.warnings:
                print(f"  ⚠ {warning}")
            print()

        if self.suggestions:
            print("SUGGESTIONS:")
            for suggestion in self.suggestions:
                print(f"  💡 {suggestion}")
            print()

        if self.info:
            print("INFO:")
            for info in self.info:
                print(f"  ℹ {info}")
            print()

        # Summary
        print("=" * 70)
        if not self.errors and not self.warnings:
            print("✓ All validations passed!")
        elif not self.errors:
            print(f"✓ Validation passed with {len(self.warnings)} warning(s)")
        else:
            print(f"✗ Validation failed with {len(self.errors)} error(s)")
        print("=" * 70)
        print()


def check_file_exists(path: Path, result: ValidationResult, required: bool = True) -> bool:
    """Check if a file exists"""
    if path.exists():
        result.add_info(f"Found: {path.name}")
        return True
    else:
        if required:
            result.add_error(f"Required file missing: {path}")
        else:
            result.add_warning(f"Optional file missing: {path}")
        return False


def validate_image_file(path: Path, result: ValidationResult) -> Dict:
    """Validate image file and return metadata"""
    if not path.exists():
        return {}

    try:
        # Try to import PIL (Pillow) for image validation
        try:
            from PIL import Image
            has_pil = True
        except ImportError:
            has_pil = False
            result.add_warning(f"Pillow library not installed - cannot validate image dimensions")
            result.add_suggestion("Install Pillow: pip install Pillow")

        # Check file extension
        valid_extensions = ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp']
        if path.suffix.lower() not in valid_extensions:
            result.add_warning(f"{path.name}: Unsupported format '{path.suffix}'. Recommended: PNG or SVG")

        # Check file size
        file_size = path.stat().st_size
        if file_size < 1024:  # Less than 1KB
            result.add_warning(f"{path.name}: Very small file size ({file_size} bytes) - may be placeholder")
        elif file_size > 5 * 1024 * 1024:  # Larger than 5MB
            result.add_warning(f"{path.name}: Large file size ({file_size / 1024 / 1024:.1f}MB) - consider optimizing")

        # If PIL is available, check dimensions
        if has_pil and path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
            try:
                with Image.open(path) as img:
                    width, height = img.size
                    result.add_info(f"{path.name}: {width}x{height}px")

                    # Check minimum dimensions
                    if height < 50:
                        result.add_error(f"{path.name}: Height {height}px is below minimum 50px")
                    elif height < 100:
                        result.add_warning(f"{path.name}: Height {height}px is low. Recommended: 100px+")

                    # Check if image is too large
                    if width > 3000 or height > 3000:
                        result.add_suggestion(f"{path.name}: Very large dimensions ({width}x{height}). Consider creating optimized version")

                    # Check aspect ratio (warn if very unusual)
                    aspect_ratio = width / height
                    if aspect_ratio > 5 or aspect_ratio < 0.2:
                        result.add_warning(f"{path.name}: Unusual aspect ratio {aspect_ratio:.2f}:1")

                    return {
                        'width': width,
                        'height': height,
                        'format': img.format,
                        'mode': img.mode
                    }
            except Exception as e:
                result.add_error(f"{path.name}: Failed to read image - {str(e)}")

        return {'exists': True}

    except Exception as e:
        result.add_error(f"{path.name}: Validation error - {str(e)}")
        return {}


def validate_hex_color(color: str) -> bool:
    """Check if color is valid hex format"""
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))


def validate_rgb_color(color_str: str) -> bool:
    """Check if color is valid RGB format"""
    # Match patterns like: RGB: 0, 102, 204 or rgb(0, 102, 204)
    pattern1 = r'RGB:\s*(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})'
    pattern2 = r'rgb\(\s*(\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\s*\)'

    match = re.search(pattern1, color_str) or re.search(pattern2, color_str)
    if not match:
        return False

    # Check if values are in valid range (0-255)
    r, g, b = int(match.group(1)), int(match.group(2)), int(match.group(3))
    return all(0 <= val <= 255 for val in [r, g, b])


def extract_colors_from_skill_md(skill_md_path: Path, result: ValidationResult) -> List[str]:
    """Extract color codes from SKILL.md"""
    colors_found = []

    try:
        with open(skill_md_path, 'r') as f:
            content = f.read()

        # Find hex colors
        hex_pattern = r'`(#[0-9A-Fa-f]{6})`'
        hex_matches = re.findall(hex_pattern, content)

        for hex_color in hex_matches:
            if validate_hex_color(hex_color):
                colors_found.append(hex_color)
                result.add_info(f"Found color: {hex_color}")
            else:
                result.add_error(f"Invalid hex color format: {hex_color}")

        # Check for RGB format
        rgb_pattern = r'RGB:\s*\d{1,3},\s*\d{1,3},\s*\d{1,3}'
        rgb_matches = re.findall(rgb_pattern, content)

        for rgb in rgb_matches:
            if not validate_rgb_color(rgb):
                result.add_error(f"Invalid RGB color values: {rgb}")

    except Exception as e:
        result.add_error(f"Failed to read SKILL.md: {str(e)}")

    return colors_found


def validate_skill_md_structure(skill_md_path: Path, result: ValidationResult) -> bool:
    """Validate SKILL.md structure and content"""
    try:
        with open(skill_md_path, 'r') as f:
            content = f.read()

        # Check for YAML frontmatter
        if not content.startswith('---'):
            result.add_error("SKILL.md missing YAML frontmatter (should start with '---')")
            return False

        # Extract frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            result.add_error("SKILL.md has malformed YAML frontmatter")
            return False

        frontmatter = parts[1]
        body = parts[2]

        # Check required frontmatter fields
        required_fields = ['name:', 'description:']
        for field in required_fields:
            if field not in frontmatter:
                result.add_error(f"SKILL.md frontmatter missing required field: {field.rstrip(':')}")

        # Check for license field (recommended)
        if 'license:' not in frontmatter:
            result.add_warning("SKILL.md frontmatter missing 'license:' field (recommended)")

        # Check body sections
        recommended_sections = [
            '## Overview',
            '## Brand Assets',
            '### Logo',
            '### Colors',
            '## Implementation Guidelines'
        ]

        for section in recommended_sections:
            if section not in body:
                result.add_warning(f"SKILL.md missing recommended section: {section}")

        # Check for placeholder text that should be replaced
        placeholders = ['[PLACEHOLDER]', 'TODO:', 'FIXME:', 'XXX:']
        for placeholder in placeholders:
            if placeholder in content:
                result.add_warning(f"SKILL.md contains placeholder text: {placeholder}")

        return True

    except Exception as e:
        result.add_error(f"Failed to validate SKILL.md: {str(e)}")
        return False


def validate_directory_structure(skill_path: Path, result: ValidationResult) -> bool:
    """Validate the skill directory structure"""

    # Check required directories
    required_dirs = ['assets', 'references']
    for dir_name in required_dirs:
        dir_path = skill_path / dir_name
        if not dir_path.exists():
            result.add_error(f"Required directory missing: {dir_name}/")
        elif not dir_path.is_dir():
            result.add_error(f"{dir_name} exists but is not a directory")
        else:
            result.add_info(f"Found directory: {dir_name}/")

    # Check optional directories
    optional_dirs = ['scripts']
    for dir_name in optional_dirs:
        dir_path = skill_path / dir_name
        if dir_path.exists():
            result.add_info(f"Found optional directory: {dir_name}/")

    return True


def validate_brand_skill(skill_path: Path, strict: bool = False) -> ValidationResult:
    """Main validation function"""
    result = ValidationResult()

    print(f"Validating brand skill at: {skill_path}")
    print()

    # Check if skill directory exists
    if not skill_path.exists():
        result.add_error(f"Skill directory not found: {skill_path}")
        return result

    # Validate directory structure
    validate_directory_structure(skill_path, result)

    # Check for SKILL.md
    skill_md = skill_path / 'SKILL.md'
    if check_file_exists(skill_md, result, required=True):
        validate_skill_md_structure(skill_md, result)
        extract_colors_from_skill_md(skill_md, result)

    # Check for logo files
    print("Checking logo files...")
    assets_dir = skill_path / 'assets'

    logo_files = {
        'logo.png': {'required': True, 'description': 'Primary logo'},
        'logo.svg': {'required': False, 'description': 'Vector logo (recommended)'},
        'logo-white.png': {'required': False, 'description': 'Logo for dark backgrounds'},
        'logo-horizontal.png': {'required': False, 'description': 'Horizontal orientation'},
    }

    logos_found = 0
    for logo_file, meta in logo_files.items():
        logo_path = assets_dir / logo_file
        # Also check for .placeholder files
        placeholder_path = assets_dir / f"{logo_file}.placeholder"

        if logo_path.exists():
            validate_image_file(logo_path, result)
            logos_found += 1
        elif placeholder_path.exists():
            if meta['required']:
                result.add_error(f"Primary logo is still a placeholder: {logo_file}.placeholder - replace with actual image")
            else:
                result.add_warning(f"Logo placeholder found: {logo_file}.placeholder - replace with actual image")
        else:
            if meta['required']:
                result.add_error(f"Required logo missing: {logo_file}")
            else:
                result.add_info(f"Optional logo not provided: {logo_file}")

    if logos_found == 0:
        result.add_error("No logo files found in assets/")
    elif logos_found == 1:
        result.add_suggestion("Consider adding logo variants (SVG, white version, horizontal)")

    # Check for reference files
    print("Checking reference documentation...")
    references_dir = skill_path / 'references'

    reference_files = {
        'color-system.md': 'Color palette and usage guidelines',
        'typography.md': 'Font specifications and pairing rules',
        'logo-usage.md': 'Logo placement and clearspace guidelines'
    }

    for ref_file, description in reference_files.items():
        ref_path = references_dir / ref_file
        if check_file_exists(ref_path, result, required=False):
            # Check file is not empty
            if ref_path.stat().st_size < 100:
                result.add_warning(f"{ref_file} is very small - may need content")

    # Suggest optimal formats
    print("Checking for optimal formats...")

    if not (assets_dir / 'logo.svg').exists():
        result.add_suggestion("Add SVG logo format for better scaling (logo.svg)")

    # Check for templates
    templates_dir = assets_dir / 'templates'
    if templates_dir.exists():
        template_files = list(templates_dir.glob('*'))
        if template_files:
            result.add_info(f"Found {len(template_files)} template file(s)")
        else:
            result.add_warning("templates/ directory exists but is empty")
    else:
        result.add_suggestion("Consider adding pre-branded templates in assets/templates/")

    # Check for scripts
    scripts_dir = skill_path / 'scripts'
    if scripts_dir.exists():
        script_files = list(scripts_dir.glob('*.py'))
        if script_files:
            result.add_info(f"Found {len(script_files)} script file(s)")
            # Check if scripts are executable
            for script in script_files:
                if not os.access(script, os.X_OK):
                    result.add_warning(f"Script is not executable: {script.name}")
                    result.add_suggestion(f"Make executable: chmod +x {script}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Validate brand skill assets and structure',
        epilog='Example: python validate_brand_assets.py acme-corp'
    )

    parser.add_argument('skill_name', help='Skill directory name (e.g., "acme-corp")')
    parser.add_argument('--path', help='Base path to skills directory (default: ./brand-skills/)')
    parser.add_argument('--strict', action='store_true', help='Treat warnings as errors')

    args = parser.parse_args()

    # Determine skill path
    if args.path:
        base_path = Path(args.path)
    else:
        base_path = Path('brand-skills')

    skill_path = base_path / args.skill_name

    # Run validation
    result = validate_brand_skill(skill_path, args.strict)

    # Print results
    result.print_results()

    # Exit with appropriate code
    if result.is_valid(strict=args.strict):
        return 0
    else:
        return 1


if __name__ == '__main__':
    sys.exit(main())
