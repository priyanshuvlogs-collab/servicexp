# Service Express — ads landing rebuild

Customer-facing brand is **Service Express**. `servicexp.ca` is the domain only.

Live site today is Webware (Shopify-like URLs), not Shopify. This repo ships:

1. A Shopify 2.0 theme you can upload (`theme/`)
2. A static preview that matches the theme (`preview/`) — use this to QA and, if needed, paste into Webware while Shopify is set up
3. Copy and form field lists (`copy/`)

Ads slug stays live. **Do not 301** `/pages/contact-residential-commercial-hvac-company-gta` to Home.

## Owner decisions (do not ship both)

| Item | Default in this repo | Confirm |
| --- | --- | --- |
| Public address | **410 Hood Rd, Markham, ON L3R 3X2** | Other public listing: 226 Esna Park Dr #2, Markham, ON L3R 1H3. Theme setting `public_address` is `hood` or `esna`. Show **one**. |
| TSSA / gas ticket | Blank | Footer prints a licence line only if you paste a real number. Do not invent one. |
| Same-day / one-trip | Softened to “aim to diagnose in one visit” | Condo page used to claim SAME DAY and ONE TRIP. Restore that line only if you still run the policy. |
| Google rating | 4.8, large volume | Update `google_rating` and the Google URL if the live listing count changes. Schema `reviewCount` is a conservative 400 — replace with the live Google number. |
| Form destination | Shopify contact **or** preview thank-you | Connect email/SMS before ads spend. |

## Phone and NAP

- Call: [(416) 637-1678](tel:+14166371678) — `tel:+14166371678` everywhere
- Email: info@servicexpress.ca
- Hours claim: 24/7 emergency **dispatch** (we take the call; a truck is assigned when a tech is free). Not a 20-minute SLA.
- One address only (see table)

## Preview locally

```bash
python3 preview/build.py
python3 -m http.server 4173 --directory preview
```

Open http://127.0.0.1:4173/pages/contact-residential-commercial-hvac-company-gta.html

Campaign H1: add `?job=cooling|heat|condo|commercial|install`.

## Shopify install

1. Zip the `theme/` folder and upload (Online Store → Themes → Add theme → Upload).
2. Create or keep these **page handles** (do not rename the ads slug):

   | Handle | Template |
   | --- | --- |
   | `contact-residential-commercial-hvac-company-gta` | `page.ads-landing` |
   | `thank-you` | `page.thank-you` |
   | `condo-hvac-repair-maintenance` | `page.condo` |
   | `residential-hvac-contractor-gta` | `page.residential` |
   | `commercial-hvac-contractor-gta` | `page.commercial` |
   | `hvac-products` | `page.products` |
   | `service-areas` | `page.service-areas` |
   | `hvac-contractor-markham-on` | `page.markham` |
   | `hvac-contractor-richmond-hill-on` | `page.richmond-hill` |
   | `hvac-contractor-scarborough-on` | `page.scarborough` |
   | `hvac-contractor-toronto-on` | `page.toronto` |
   | `markham-hvac-company-work` | `page.our-work` |

3. Theme settings → Firm: pick Hood or Esna, paste TSSA only if real, optional Formspree URL.
4. Point the Shopify contact form notification to `info@servicexpress.ca` and a mobile SMS if you have one.

### Connect the form (required before ads)

Shopify’s contact form **cannot attach photos**. Options:

1. **Now:** Shopify contact email + “text the photo to (416) 637-1678”.
2. **Better:** Formspree / Basin / a serverless webhook in theme setting `form_endpoint`. Then SMS via Twilio or the form tool.
3. **Later:** ServiceTitan or Housecall Pro booking widget. Keep the same visible fields (job type, property, emergency flag, address). Do not replace this with a newsletter signup.

## What this kills on the old page

- H1 “CONTACT SERVICE EXPRESS”
- Four equal NAP cards as the page
- New Brunswick 506 phone placeholder and “✓ Valid”
- White box over the map pin (iframe is a clean `maps.google.com` embed, no overlay)
- “Get In Touch” with no emergency vs quote split
- Recycled “15,000… meet and beyond your expectation” on every city page

## Compliance

- No invented TSSA numbers, dealer badges, or rebate dollar amounts
- Heat-pump / Enbridge / Save on Energy: “we help check current eligibility”
- 24/7 = dispatch intent
- Reviews are paraphrases of testimonials already on servicexp.ca (Stephanie / Jamie / J. Hsu). Link Google. No fake widgets.

## Files

- `theme/` — Dawn-style OS 2.0 sections (custom, not a stock four-card contact)
- `preview/` — static HTML for QA
- `copy/ADS-LANDING.md` — LP + thank-you + home/condo headlines
- `copy/FORM-FIELDS.md` — visible + hidden UTM fields
