# Dispatch form fields

Visible

| Field | Required | Notes |
| --- | --- | --- |
| name | yes | Label, not placeholder-only |
| mobile | yes | 10-digit Canadian. `tel:+1` display is (416) 637-1678. No 506. No “✓ Valid”. |
| job_type | yes | From picker: No cooling / No heat / Condo fan coil / heat pump / New install / quote / Commercial rooftop / Maintenance |
| property_type | recommended | House / Condo / high-rise / Commercial |
| city_or_postal | recommended | City or postal |
| address | recommended | Address or intersection |
| notes | no | Free text |
| photo | no | File input. Shopify contact cannot attach files — text (416) 637-1678 or connect Formspree / webhook. |
| emergency_today | no | Checkbox: Emergency — need someone today |

Hidden (UTM-safe)

- utm_source, utm_medium, utm_campaign, utm_content, utm_term
- gclid, wbraid, gbraid, msclkid
- landing_page (full URL)
- product (from `?product=` on Price this system)
- h1_variant (which hero ran)

CTA: Send — we’ll call to confirm a window.

Shopify: posts as contact form; empty email is filled with `mobile-lead@servicexpress.ca` so the platform accepts the ticket. Real reach is the mobile.

Preview: stores payload in sessionStorage and goes to `/pages/thank-you`.
