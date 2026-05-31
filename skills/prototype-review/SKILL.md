---
name: prototype-review
description: Use when a UI, landing page, design prototype, or frontend change needs product-quality review before delivery.
---

# Prototype Review

Use this skill to review a frontend or visual prototype with the eye of a product engineer. It is inspired by popular design-skill ecosystems, but this version focuses on practical Codex checks for real repositories.

## Workflow

1. Identify the product surface:
   - app screen
   - landing page
   - dashboard
   - component library
   - generated prototype
2. Find the render path:
   - package manager
   - dev server command
   - build command
   - preview URL
3. Inspect the UI across at least two viewport sizes when possible.
4. Check for:
   - layout overflow
   - clipped or overlapping text
   - missing loading and empty states
   - inaccessible controls
   - unclear hierarchy
   - inconsistent spacing, radius, and color use
   - broken image or asset references
5. Suggest or implement focused fixes.
6. Verify the result with a screenshot or build output when the environment supports it.

## Review Checklist

- Primary workflow is visible without reading explanatory copy.
- Buttons and controls use familiar affordances.
- Text fits containers on mobile and desktop.
- States exist for loading, empty, error, and success paths.
- Colors are not dominated by one narrow hue family unless the brand requires it.
- Repeated items use consistent dimensions.
- The design matches the domain: operational tools stay dense and calm; creative surfaces can be more expressive.

## Output

Return:

- what was reviewed
- what changed or should change
- verification performed
- remaining risks

## Safety Notes

- Do not invent a marketing page when the user asked for a usable app.
- Do not add decorative complexity that hides the actual product state.
- Do not claim visual verification unless a build, screenshot, or browser check actually ran.
