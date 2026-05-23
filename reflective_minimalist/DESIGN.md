---
name: Reflective Minimalist
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#7a5900'
  on-secondary: '#ffffff'
  secondary-container: '#ffc334'
  on-secondary-container: '#6f5100'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#121c2a'
  on-tertiary-container: '#7a8495'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ffdea1'
  secondary-fixed-dim: '#f9bd2e'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5c4300'
  tertiary-fixed: '#d9e3f6'
  tertiary-fixed-dim: '#bdc7d9'
  on-tertiary-fixed: '#121c2a'
  on-tertiary-fixed-variant: '#3d4756'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Manrope
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1120px
  section-gap: 8rem
  stack-gap: 1.5rem
  gutter: 24px
  margin-desktop: 40px
  margin-mobile: 20px
---

## Brand & Style
The design system is centered on the intersection of professional clarity and personal reflection. It targets an audience that values deep thought, quiet aesthetics, and premium editorial experiences. The atmosphere is intentional and calm, utilizing heavy whitespace and a "less but better" approach to UI elements.

The style is a refined **Minimalism** with a **Premium Editorial** lean. It avoids visual clutter, allowing the content to breathe. Subtle motion and high-quality typography create a sense of craftsmanship, while soft, ambient depth provides a tactile feel that keeps the digital experience grounded and approachable.

## Colors
The palette is built on a foundation of "Off-White" and "Soft Gray" to reduce eye strain and provide a sophisticated backdrop for text. 

- **Primary:** Black (#000000) is used for high-contrast typography and core branding elements, ensuring maximum readability.
- **Secondary/Accent:** A warm gold (#ECB221) is carried over from the legacy brand as a "Fidelity" accent color, used sparingly for specific highlights like link underlines or active states.
- **Tertiary:** Deep Charcoal/Navy (#1F2937) provides a softer alternative to black for secondary text or UI borders.
- **Neutral:** A range of grays (#F9FAFB, #F3F4F6) defines container backgrounds and structural divisions without creating hard lines.

## Typography
This design system employs a pairing of a high-performance geometric sans-serif for structure and a literary serif for long-form reading.

- **Headlines:** Use **Manrope** for a modern, bold, and architectural feel. It commands attention and provides a professional anchor for each page.
- **Body:** Use **Newsreader** for all article content and personal reflections. This serif font evokes a "bookish" and academic quality, making long-form reading comfortable and immersive.
- **UI Labels:** **Inter** is used for functional elements like navigation, buttons, and metadata tags due to its exceptional legibility at small sizes.

## Layout & Spacing
The design system utilizes a **Fixed Grid** layout for desktop to maintain editorial control over line lengths and content density. 

- **Desktop:** A centered 12-column grid with a maximum width of 1120px. 
- **Rhythm:** Spacing follows a strict 8px base unit. Section gaps are intentionally generous (128px+) to create a "gallery" feel where each piece of content is distinct.
- **Reading Experience:** For blog posts, the content column is constrained to a narrower 720px width to optimize the "characters per line" for readability.
- **Mobile:** Transition to a single-column fluid layout with 20px side margins and reduced vertical spacing.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and **Tonal Layering**. 

Elements do not "float" aggressively; instead, they lift subtly off the surface. Use a single, large-radius shadow (Blur: 32px, Y: 8px) with very low opacity (3-5% Black) to suggest elevation on cards and dropdowns. 

Backgrounds use #F9FAFB, while primary "interactive" surfaces (like cards or input fields) use pure #FFFFFF to draw the eye. No heavy borders are used; depth is defined by the transition from the soft gray page to the crisp white container.

## Shapes
The shape language is consistently **Rounded**, utilizing an 8px to 12px radius. 

- **Standard Elements:** Buttons, input fields, and tags use an 8px radius.
- **Containers:** Large cards and featured image wrappers use a 16px (rounded-lg) radius to feel approachable and modern.
- **Interactive States:** Hovering over elements should trigger a slight "expansion" feel through a 2px shadow increase rather than a change in shape.

## Components
- **Buttons:** Primary buttons are solid black (#000000) with white text, featuring an 8px corner radius. Secondary buttons use a ghost style with a subtle #F3F4F6 background on hover.
- **Cards:** Cards are pure white (#FFFFFF) against the soft gray background. They feature a subtle 1px border (#F1F5F9) and an ambient shadow on hover.
- **Input Fields:** Minimalist design with a bottom-only border that transitions to black when focused. Backgrounds are slightly tinted (#F3F4F6) to define the hit area.
- **Chips/Tags:** Small, uppercase labels using **Inter** with high letter spacing. Use a soft gray background or a very faint gold tint for categories.
- **Links:** Inline links in body text feature a thick 2px underline in the accent gold (#ECB221) at 30% opacity, which becomes 100% opaque on hover.
- **Signature Component:** A custom "Reflections" quote block that uses a large serif opening quote in the accent color, centered to evoke the tagline: "Have you ever felt like?".