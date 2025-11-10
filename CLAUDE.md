# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python-based HTML funnel template system that generates static landing pages from JSON configuration files. The system uses a simple variable replacement approach (`{{variable}}`) to create customized client funnels without requiring a complex templating engine.

## Essential Commands

### Build System
```bash
npm run build              # Build using config/client-config.json
npm run build:custom path  # Build using custom config file
npm run serve              # Preview at localhost:8000
npm run dev                # Build and serve in one command
```

The build process is Python 3-based despite using npm scripts. The actual build engine is `build-template.py`.

## Core Architecture

### Three-Part System

1. **Configuration** (`config/client-config.json`)
   - Single JSON file defines all customizable aspects
   - Nested structure: `client`, `branding`, `content`, `media`, `forms`, `pages`, `seo`

2. **Templates** (`templates/*.html`)
   - HTML files with `{{variable}}` placeholders
   - Three templates: `index.html` (main page), `education-page.html`, `confirmation-page.html`
   - CSS is embedded in templates using template variables for colors

3. **Build Script** (`build-template.py`)
   - Python script that performs string replacement
   - Processes all templates in one pass
   - Generates dynamic HTML sections for arrays (pillars, testimonials, forms)

### Variable Replacement System

The system uses **simple string replacement**, not a templating engine. This has important implications:

- Variables must match exactly: `{{content.heroTitle}}` (case-sensitive)
- No conditionals or loops in templates
- Array-based content (pillars, testimonials, forms) is generated as HTML strings in Python
- Adding new variables requires updating both `client-config.json` AND `build-template.py`

**To add a new template variable:**

1. Add the field to `config/client-config.json` in the appropriate section
2. Add a replacement line in `build-template.py` in the `replace_variables()` method
3. Use `{{section.fieldName}}` in templates
4. For optional fields, use `.get('fieldName', '')` in Python to avoid KeyErrors

Example from recent work:
```python
# In build-template.py
processed_content = processed_content.replace('{{content.heroPresents}}', content_config.get('heroPresents', ''))
```

### Output Structure

Running `npm run build` generates the `output/` directory:
```
output/
├── index.html
├── education-page.html
├── confirmation-page.html
└── assets/
    ├── (all files from assets/)
    └── (subdirectories copied recursively)
```

The output directory is served directly for deployment and preview.

## Configuration Schema Patterns

### Content Splitting Pattern
Headlines can be split into multiple parts for separate styling:
```json
"content": {
  "heroPresents": "SIMO PRESENTS...",  // Styled smaller and green
  "heroTitle": "HOW TO BUILD...",       // Main large headline
}
```

Then in template:
```html
<div class="hero-presents">{{content.heroPresents}}</div>
<h1 class="hero-title">{{content.heroTitle}}</h1>
```

### Dynamic HTML Generation
Arrays in config are converted to HTML in Python:

**Testimonials**: Loops through `media.testimonials[]` array to generate cards
**Pillars**: Loops through `content.pillars[]` array to generate feature sections
**Forms**: Generates complete form HTML from `forms.applicationForm.fields[]` array

These are inserted as complete HTML blocks, not individual variables.

## Video Integration

The system supports Vidalytics video embeds:
- Embed ID goes in `media.heroVideo.embedId`
- Template uses special div: `<div id="vidalytics_embed_{{media.heroVideo.embedId}}"></div>`
- Custom CSS in templates handles aspect ratio and responsive sizing
- External script loads the actual video player

## Styling Architecture

**All CSS is embedded in the HTML templates.** There are no separate CSS files.

Colors use template variables:
```css
.hero-title {
    color: {{branding.textColor}};
}
```

This means color changes only require updating `client-config.json`, then rebuilding.

## Important Patterns

### File Path Handling
- All paths in config are relative to the output directory
- Assets reference: `"image": "assets/testimonial.jpg"`
- After build, this resolves to `output/assets/testimonial.jpg`

### Responsive Typography
Templates use `clamp()` for fluid typography:
```css
font-size: clamp(2rem, 6vw, 3.5rem);
```

### Color System Convention
The current project (Simo) uses:
- `primaryColor`: Black background (#000000)
- `accentColor`: Shopify green (#00B34D)
- `textColor`: Light beige (#EDE8E1)
- `secondaryColor`: Off-white (#F2EEE6)

## Working with Multiple Clients

To create a new client funnel:
1. Duplicate `config/client-config.json` to `config/new-client-config.json`
2. Update all fields for the new client
3. Add new client assets to `assets/` (or use subdirectories)
4. Build with: `npm run build:custom config/new-client-config.json`

## Deployment

The system generates static HTML suitable for:
- Vercel (set output dir to `output`)
- Netlify (set publish dir to `output`)
- Any static file host

No server-side processing required after build.
