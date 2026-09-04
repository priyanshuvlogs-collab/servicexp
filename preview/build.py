#!/usr/bin/env python3
"""Build static preview pages that mirror the Shopify dispatch theme."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT

PHONE = "(416) 637-1678"
TEL = "tel:+14166371678"
EMAIL = "info@servicexpress.ca"
ADDRESS = "410 Hood Rd, Markham, ON L3R 3X2"
MAP = "https://maps.google.com/maps?q=410+Hood+Rd,+Markham,+ON+L3R+3X2&hl=en&z=16&output=embed"
GOOGLE = "https://www.google.com/maps/search/?api=1&query=Service+Express+410+Hood+Rd+Markham"
ADS = "/pages/contact-residential-commercial-hvac-company-gta.html"

CHROME_HEAD = """<!doctype html>
<html lang="en-CA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{meta}">
  <link rel="canonical" href="https://www.servicexp.ca{canonical}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@700&family=Source+Sans+3:wght@450;600;650;700;750&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset}theme.css">
  {schema}
</head>
<body>
  <a class="skip-link" href="#job-request">Skip to job request</a>
  <div class="sx-sticky">
    <div class="wrap">
      <div class="sx-sticky__meta">
        <span>24/7 emergency</span>
        <span class="sx-sticky__dot hide-sm" aria-hidden="true">·</span>
        <span class="hide-sm">Markham-based · GTA</span>
      </div>
      <div class="sx-sticky__meta">
        <a class="btn-ghost hide-sm" href="{ads}#job-request">Book a visit</a>
        <a class="btn-call" href="{tel}">Call {phone}</a>
      </div>
    </div>
  </div>
  <header class="sx-header">
    <div class="wrap">
      <a class="logo" href="{home}"><img src="{asset}logo.png" width="118" height="60" alt="Service Express"></a>
      <nav aria-label="Primary">
        <ul class="nav-doors">
          <li><a href="{condo}"{condo_cur}>Condo</a></li>
          <li><a href="{home_svc}"{home_cur}>Home</a></li>
          <li><a href="{comm}"{comm_cur}>Commercial</a></li>
        </ul>
      </nav>
      <a class="nav-contact" href="{ads}">Contact</a>
      <button class="menu-toggle" type="button" data-menu-toggle aria-expanded="false" aria-controls="mobile-nav">Menu</button>
    </div>
    <div id="mobile-nav" class="nav-panel" data-nav-panel hidden>
      <a href="{condo}">Condo</a>
      <a href="{home_svc}">Home</a>
      <a href="{comm}">Commercial</a>
      <a href="{ads}">Contact</a>
      <a href="{tel}">Call {phone}</a>
    </div>
  </header>
  <main id="main">
"""

CHROME_FOOT = """
  </main>
  <footer class="sx-footer">
    <div class="wrap">
      <div>
        <h2>Service Express</h2>
        <p>Markham HVAC for houses, condos, and rooftops. 24/7 emergency dispatch — we take the call; a truck is assigned when a technician is free.</p>
        <p><a href="{tel}">{phone}</a><br><a href="mailto:{email}">{email}</a><br>{address}</p>
      </div>
      <div>
        <h3>Book a job</h3>
        <ul>
          <li><a href="{ads}">Request a tech</a></li>
          <li><a href="{condo}">Condo fan coil / heat pump</a></li>
          <li><a href="{home_svc}">Home furnace &amp; AC</a></li>
          <li><a href="{comm}">Commercial rooftop</a></li>
        </ul>
      </div>
      <div>
        <h3>Areas</h3>
        <ul>
          <li><a href="{p}service-areas/hvac-contractor-markham-on.html">Markham</a></li>
          <li><a href="{p}service-areas/hvac-contractor-richmond-hill-on.html">Richmond Hill</a></li>
          <li><a href="{p}service-areas/hvac-contractor-scarborough-on.html">Scarborough</a></li>
          <li><a href="{p}service-areas/hvac-contractor-toronto-on.html">Toronto</a></li>
        </ul>
      </div>
    </div>
    <div class="wrap legal">
      <p>© 2026 Service Express. Domain: servicexp.ca. Customer-facing name: Service Express.</p>
    </div>
  </footer>
  <div class="dock" role="navigation" aria-label="Call or book">
    <a class="btn-call" href="{tel}">Call {phone}</a>
    <a class="btn-primary" href="{ads}#job-request">Request a tech</a>
  </div>
  <script src="{asset}theme.js"></script>
</body>
</html>
"""

SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": ["HVACBusiness", "LocalBusiness"],
  "name": "Service Express",
  "url": "https://www.servicexp.ca",
  "telephone": "+1-416-637-1678",
  "email": "{EMAIL}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "410 Hood Rd",
    "addressLocality": "Markham",
    "addressRegion": "ON",
    "postalCode": "L3R 3X2",
    "addressCountry": "CA"
  }},
  "geo": {{ "@type": "GeoCoordinates", "latitude": 43.824766, "longitude": -79.336890 }},
  "areaServed": ["Markham", "Richmond Hill", "Scarborough", "Toronto", "Greater Toronto Area"],
  "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.8", "bestRating": "5", "reviewCount": "400" }}
}}
</script>"""


def paths(depth: int) -> dict:
    prefix = "../" * depth
    pages = prefix + "pages/"
    return {
        "asset": prefix + "assets/",
        "home": prefix + "index.html",
        "ads": pages + "contact-residential-commercial-hvac-company-gta.html",
        "condo": pages + "condo-hvac-repair-maintenance.html",
        "home_svc": pages + "residential-hvac-contractor-gta.html",
        "comm": pages + "commercial-hvac-contractor-gta.html",
        "p": pages,
        "tel": TEL,
        "phone": PHONE,
        "email": EMAIL,
        "address": ADDRESS,
        "schema": SCHEMA if depth <= 1 else "",
    }


def wrap(title, meta, canonical, depth, body, current=""):
    ctx = paths(depth)
    ctx.update(
        title=title,
        meta=meta,
        canonical=canonical,
        condo_cur=' aria-current="page"' if current == "condo" else "",
        home_cur=' aria-current="page"' if current == "home" else "",
        comm_cur=' aria-current="page"' if current == "comm" else "",
    )
    return CHROME_HEAD.format(**ctx) + body + CHROME_FOOT.format(**ctx)


PROOF = f"""
<section class="proof">
  <div class="wrap">
    <h2>What customers actually wrote</h2>
    <p class="section-sub">Paraphrased from reviews published on this site. <a href="{GOOGLE}">Read Google reviews</a>.</p>
    <div class="reviews">
      <article class="review">
        <div class="stars" aria-hidden="true">★★★★★</div>
        <blockquote>Matthew was on time and diagnosed the fan coil quickly. Easy fix, completed promptly. He explained everything. Rates were reasonable.</blockquote>
        <footer>Stephanie — condo / fan coil</footer>
      </article>
      <article class="review">
        <div class="stars" aria-hidden="true">★★★★★</div>
        <blockquote>Paul checked the system Thursday night at 8pm. The heating circuit board needed replacing under warranty. He came back the next morning with a new thermostat. The furnace felt like new.</blockquote>
        <footer>Jamie — house / furnace board</footer>
      </article>
      <article class="review">
        <div class="stars" aria-hidden="true">★★★★★</div>
        <blockquote>Thanks for showing up and rescuing us when the AC died on the hottest day that summer. The new unit is quiet and actually cools the house.</blockquote>
        <footer>J. Hsu — house / AC on a heat wave</footer>
      </article>
    </div>
  </div>
</section>
"""

SYSTEMS = """
<section class="systems">
  <div class="wrap">
    <h2>What we actually fix</h2>
    <p class="section-sub">Icons, not essays. If your building uses something else, still call — bring the model off the indoor label.</p>
    <div class="sys-grid">
      <article class="sys"><h3>Condo</h3><ul><li>Vertical fan coil (VFC)</li><li>Water-source heat pump</li><li>Magic Pak</li><li>PTAC / Sky Mark</li></ul></article>
      <article class="sys"><h3>Home</h3><ul><li>Furnace</li><li>AC</li><li>Ductless / mini-split</li><li>Boiler / in-floor</li></ul></article>
      <article class="sys"><h3>Commercial</h3><ul><li>Rooftop unit (RTU)</li><li>Makeup air (MAU)</li><li>Ventilation</li></ul></article>
    </div>
  </div>
</section>
"""

ADS_BODY = f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="kicker">Markham dispatch · houses, condos, rooftops</p>
      <h1 data-hero-h1>GTA HVAC repair and install — houses, condos, and rooftops.</h1>
      <p class="lede">Markham-based. Condo fan coils and heat pumps, residential furnace/AC, commercial rooftop. Call now or send the address.</p>
      <div class="hero__actions">
        <a class="btn-call btn-call--xl" href="{TEL}" style="width:auto;min-width:16rem;">Call {PHONE}</a>
        <a class="btn-outline" href="#job-request">Request a tech</a>
      </div>
      <ul class="chips">
        <li>4.8 Google</li>
        <li>15,000+ jobs claimed</li>
        <li>24/7 dispatch</li>
        <li>Condo + residential + commercial</li>
      </ul>
    </div>
  </div>
</section>
<section class="picker" id="job-picker">
  <div class="wrap">
    <h2>What failed?</h2>
    <p class="section-sub">Pick the job so the form is a dispatch ticket, not a newsletter signup.</p>
    <fieldset class="picker-block">
      <legend>I need</legend>
      <div class="options options--jobs">
        <label><input type="radio" name="job_type" value="No cooling"> No cooling</label>
        <label><input type="radio" name="job_type" value="No heat"> No heat</label>
        <label><input type="radio" name="job_type" value="Condo fan coil / heat pump"> Condo fan coil / heat pump</label>
        <label><input type="radio" name="job_type" value="New install / quote"> New install / quote</label>
        <label><input type="radio" name="job_type" value="Commercial rooftop"> Commercial rooftop</label>
        <label><input type="radio" name="job_type" value="Maintenance"> Maintenance</label>
      </div>
    </fieldset>
    <fieldset class="picker-block">
      <legend>Property</legend>
      <div class="options options--prop">
        <label><input type="radio" name="property_type" value="House"> House</label>
        <label><input type="radio" name="property_type" value="Condo / high-rise"> Condo / high-rise</label>
        <label><input type="radio" name="property_type" value="Commercial"> Commercial</label>
      </div>
    </fieldset>
    <div class="field picker-block">
      <label class="field-label" for="city-postal">City or postal</label>
      <input id="city-postal" data-city-input type="text" name="city_or_postal_picker" autocomplete="postal-code">
    </div>
  </div>
</section>
<section class="dispatch" id="job-request">
  <div class="wrap">
    <h2 class="section-title">Send the address. We’ll call back.</h2>
    <p class="section-sub">Name, mobile, and the job. Photo optional.</p>
    <div class="dispatch__grid">
      <form class="card" data-job-form data-platform="preview" data-thanks="thank-you.html" action="thank-you.html" method="get" novalidate>
        <p class="form-status" data-form-status hidden></p>
        <div class="field">
          <label class="field-label" for="job-name">Name</label>
          <input id="job-name" type="text" name="name" autocomplete="name">
        </div>
        <div class="field">
          <label class="field-label" for="job-mobile">Mobile</label>
          <input id="job-mobile" type="tel" name="mobile" autocomplete="tel" inputmode="tel">
          <span class="hint">Canadian number. We call this to confirm a window.</span>
        </div>
        <div class="field">
          <label class="field-label" for="job-address">Address or intersection</label>
          <input id="job-address" type="text" name="address" autocomplete="street-address">
        </div>
        <div class="field">
          <label class="field-label" for="job-notes">Anything the tech should know (optional)</label>
          <textarea id="job-notes" name="notes"></textarea>
        </div>
        <div class="field">
          <label class="field-label" for="job-photo">Photo of the unit label (optional)</label>
          <input id="job-photo" type="file" accept="image/*" capture="environment">
          <span class="hint">Or text the photo to {PHONE} after you send.</span>
        </div>
        <label class="check">
          <input type="checkbox" name="emergency_today" value="Yes">
          <span>Emergency — need someone today</span>
        </label>
        <input type="hidden" name="utm_source" value="">
        <input type="hidden" name="utm_medium" value="">
        <input type="hidden" name="utm_campaign" value="">
        <input type="hidden" name="utm_content" value="">
        <input type="hidden" name="utm_term" value="">
        <input type="hidden" name="gclid" value="">
        <input type="hidden" name="wbraid" value="">
        <input type="hidden" name="gbraid" value="">
        <input type="hidden" name="msclkid" value="">
        <input type="hidden" name="landing_page" value="">
        <input type="hidden" name="product" value="">
        <input type="hidden" name="h1_variant" value="">
        <input type="hidden" name="job_type" data-job-field value="">
        <input type="hidden" name="property_type" data-property-field value="">
        <input type="hidden" name="city_or_postal" data-city-field value="">
        <input type="hidden" name="email" value="">
        <textarea name="body" hidden></textarea>
        <p style="margin:0.85rem 0 0.6rem;color:var(--ink-soft);font-size:0.92rem;">We’ll call to confirm a window. This creates a job, not a mailing list.</p>
        <button class="btn-submit" type="submit">Send — we’ll call to confirm a window</button>
      </form>
      <aside class="card call-card">
        <h3>Faster: tap to call</h3>
        <p>No heat at 11pm, condo blowing warm air, or an RTU down on a plaza — call dispatch.</p>
        <a class="btn-call btn-call--xl" href="{TEL}">Call {PHONE}</a>
        <p class="hint" style="color:#cfe0d4;margin-top:0.85rem;">24/7 means we take emergency calls and aim to dispatch. It is not a promise a technician is 20 minutes away.</p>
      </aside>
    </div>
  </div>
</section>
{PROOF}
{SYSTEMS}
<section class="nap" id="map">
  <div class="wrap">
    <h2>Markham shop · GTA trucks</h2>
    <div class="nap-grid">
      <div class="map-frame">
        <iframe title="Map to Service Express in Markham" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP}"></iframe>
      </div>
      <div class="card">
        <ul class="nap-list">
          <li><span>Company</span> Service Express</li>
          <li><span>Phone</span> <a href="{TEL}">{PHONE}</a></li>
          <li><span>Email</span> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><span>Address</span> {ADDRESS}</li>
          <li><span>Hours</span> 24/7 emergency dispatch. After-hours rate may apply.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="faq">
  <div class="wrap">
    <h2>Before you book from an ad</h2>
    <details open>
      <summary>Do you service my condo brand?</summary>
      <p>We work on vertical fan coils, water-source heat pumps, Magic Pak, PTAC, and Sky Mark — plus most building-standard indoor units. Read the make off the closet or balcony unit and tell us when you call.</p>
    </details>
    <details>
      <summary>Is there an after-hours fee?</summary>
      <p>Evening, overnight, and holiday dispatch may include an after-hours rate. We tell you before a truck rolls. 24/7 means we take the emergency call and aim to dispatch — not that a technician is always twenty minutes away.</p>
    </details>
    <details>
      <summary>Do you offer financing?</summary>
      <p>Ask about current payment options on a replacement. We do not advertise a specific lender or rate on this page.</p>
    </details>
    <details>
      <summary>How fast for no heat?</summary>
      <p>Call {PHONE} now. We take no-heat calls around the clock and assign the next free technician. If you can stay warm with a space heater on a safe circuit, do that until we arrive.</p>
    </details>
    <details>
      <summary>Can you promise a heat-pump rebate dollar amount?</summary>
      <p>No. We help check current Enbridge, Save on Energy, and federal eligibility. Rebate rules change. We will not put a dollar figure on an ads page.</p>
    </details>
  </div>
</section>
""".replace("{PROOF}", PROOF).replace("{SYSTEMS}", SYSTEMS)


def prose_page(kicker, h1, lede, body_html, cta_href, cta_label):
    return f"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="hero__actions">
      <a class="btn-call" href="{TEL}">Call {PHONE}</a>
      <a class="btn-outline" href="{cta_href}">{cta_label}</a>
    </div>
  </div>
</section>
<section>
  <div class="wrap prose">{body_html}</div>
</section>
"""


def write(rel, html):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", path.relative_to(OUT))


def main():
    # copy assets
    theme_assets = ROOT.parent / "theme" / "assets"
    (OUT / "assets").mkdir(exist_ok=True)
    for name in ("theme.css", "theme.js", "logo.png"):
        src = theme_assets / name
        if src.exists():
            (OUT / "assets" / name).write_bytes(src.read_bytes())

    write(
        "pages/contact-residential-commercial-hvac-company-gta.html",
        wrap(
            "Book GTA HVAC Repair | Condo, Home, Commercial | Service Express",
            "Markham team for fan coils, furnaces, AC, rooftops. 24/7 emergency. Call (416) 637-1678.",
            "/pages/contact-residential-commercial-hvac-company-gta",
            1,
            ADS_BODY,
        ),
    )
    write(
        "pages/thank-you.html",
        wrap(
            "We’re calling you | Service Express",
            "If heat or AC is out, call (416) 637-1678 now.",
            "/pages/thank-you",
            1,
            f"""
<section class="thanks">
  <div class="wrap">
    <p class="kicker">Job request sent</p>
    <h1>We’re calling this number.</h1>
    <p class="lede">If you left a mobile, we use it to confirm a window. Number we have: <strong data-thanks-number>the mobile on your form</strong>.</p>
    <p class="lede"><strong>If heat or AC is out, do not wait on the callback.</strong></p>
    <a class="btn-call btn-call--xl" href="{TEL}" style="width:auto;min-width:18rem;">Call {PHONE} now</a>
    <p class="hint" style="margin-top:1rem;">24/7 is emergency dispatch — we take the call and assign the next free truck. After-hours rate may apply.</p>
  </div>
</section>
""",
        ),
    )

    home = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Markham team · GTA trucks</p>
    <h1>No heat, no cooling, or a condo unit down — call dispatch.</h1>
    <p class="lede">Service Express is a Markham HVAC shop for houses, high-rise fan coils and heat pumps, and commercial rooftops. Not a slogan mill. Call {PHONE} or send the address.</p>
    <div class="hero__actions">
      <a class="btn-call btn-call--xl" href="{TEL}" style="width:auto;min-width:16rem;">Call {PHONE}</a>
      <a class="btn-outline" href="pages/contact-residential-commercial-hvac-company-gta.html#job-request">Request a tech</a>
    </div>
    <ul class="chips">
      <li>4.8 Google</li>
      <li>15,000+ customers claimed on this site</li>
      <li>24/7 emergency dispatch</li>
    </ul>
  </div>
</section>
<section class="systems">
  <div class="wrap">
    <h2>Three doors. Pick the building.</h2>
    <div class="door-grid">
      <a class="door" href="pages/condo-hvac-repair-maintenance.html"><h3>Condo</h3><p>Fan coil, water-source heat pump, Magic Pak, PTAC. Warm air from the closet unit, leak in the pan, no heat on the 20th floor.</p></a>
      <a class="door" href="pages/residential-hvac-contractor-gta.html"><h3>Home</h3><p>Furnace, AC, ductless, boiler / in-floor. No heat at 11pm or an AC that died on a heat wave.</p></a>
      <a class="door" href="pages/commercial-hvac-contractor-gta.html"><h3>Commercial</h3><p>Rooftop units, makeup air, ventilation. RTU down on a plaza — call, don’t wait on a contact card.</p></a>
    </div>
  </div>
</section>
{SYSTEMS}
{PROOF}
"""
    write(
        "index.html",
        wrap(
            "GTA HVAC Repair | Houses, Condos, Rooftops | Service Express",
            "Markham HVAC for fan coils, furnaces, AC, and rooftops. 24/7 emergency dispatch. Call (416) 637-1678.",
            "/",
            0,
            home,
        ),
    )

    pages = {
        "pages/condo-hvac-repair-maintenance.html": (
            "Condo Fan Coil & Heat Pump Repair | Service Express",
            "High-rise VFC, WSHP, Magic Pak, PTAC. Call (416) 637-1678.",
            "/pages/condo-hvac-repair-maintenance",
            "condo",
            prose_page(
                "High-rise HVAC · GTA",
                "Condo fan coils and water-source heat pumps — not generic “quality.”",
                "If the closet unit is blowing warm air or the pan is leaking into the suite below, you need a high-rise tech, not a furnace flyer. We work VFC, WSHP, Magic Pak, PTAC, and Sky Mark.",
                """<p>Most GTA towers do not use a basement furnace. Heat and cooling live in a vertical fan coil, a water-source heat pump, a Magic Pak through the wall, a PTAC, or a Sky Mark package. Those systems share building water or a condenser loop. A house tech who only carries furnace boards will stare at the closet and guess.</p>
<p>Tell us the make on the indoor label. We aim to diagnose in one visit. Same-day and one-trip language stays only if the owner still runs that policy — confirm before advertising it on ads.</p>
<p>After-hours condo calls are dispatch intent. We take the call; a truck is assigned when a technician is free. Management offices and unit owners can both book.</p>"""
                + SYSTEMS,
                "contact-residential-commercial-hvac-company-gta.html?job=condo&amp;property=condo#job-request",
                "Request a condo tech",
            ),
        ),
        "pages/residential-hvac-contractor-gta.html": (
            "House Furnace & AC Repair GTA | Service Express",
            "Furnace, AC, ductless, boiler. Call (416) 637-1678.",
            "/pages/residential-hvac-contractor-gta",
            "home",
            prose_page(
                "Houses · GTA",
                "Furnace, AC, ductless, boiler — when the house goes quiet.",
                "No heat at 11pm or an AC that died on a heat wave. Markham dispatch for single-family homes across the GTA.",
                "<p>A house job is usually a furnace that will not ignite, an outdoor AC that will not start, a ductless head that ices, or a boiler that leaves the floors cold. We repair and replace those systems.</p><p>We do not promise a technician in twenty minutes. We take the call around the clock and assign the next free truck. After-hours rate may apply.</p><p>Ontario heat-pump and Enbridge offers change. We help check current rebate eligibility. We will not print a dollar amount on this page.</p>",
                "contact-residential-commercial-hvac-company-gta.html?job=heat&amp;property=house#job-request",
                "Request a house tech",
            ),
        ),
        "pages/commercial-hvac-contractor-gta.html": (
            "Commercial Rooftop HVAC GTA | Service Express",
            "RTU, makeup air, ventilation. Call (416) 637-1678.",
            "/pages/commercial-hvac-contractor-gta",
            "comm",
            prose_page(
                "Plazas · shops · light commercial",
                "Rooftop down? Ventilation off? Call, don’t email a card.",
                "RTU, makeup air, and ventilation for GTA plazas and shops. Markham-based.",
                "<p>When a rooftop unit fails on a strip plaza, the suite overheats or freezes and the tenant calls the landlord. That is a dispatch job. Send the address, unit letter, and rooftop make if you have it.</p><p>We work rooftop units, makeup air, and ventilation. We do not invent dealer badges.</p>",
                "contact-residential-commercial-hvac-company-gta.html?job=commercial&amp;property=commercial#job-request",
                "Request a rooftop tech",
            ),
        ),
    }

    # city copy pulled from theme JSON conceptually
    cities = {
        "pages/service-areas/hvac-contractor-markham-on.html": (
            "Markham HVAC Repair | Service Express",
            "Hood Road shop. Houses, condos, plaza rooftops. Call (416) 637-1678.",
            "/pages/service-areas/hvac-contractor-markham-on",
            "Markham HVAC from the shop on Hood Road.",
            "This is home base. Unionville and Cornell houses, Hwy 7 condos, and plaza rooftops along Woodbine and 14th.",
            """<p>Service Express is a Markham shop. The address we show on the ads landing page is 410 Hood Road — confirm with the owner if public listings should use Esna Park instead. Trucks leave this side of town for no-heat calls in older two-storey homes, fan-coil suites along Highway 7, and rooftop units on industrial plazas that bake in July and freeze in January.</p>
<p>Markham housing is mixed on purpose. Unionville and the streets west of Main still run mid-efficiency furnaces and aging outdoor AC. Cornell and Wismer have newer forced-air systems and more heat pumps. Along Highway 7 and Warden, high-rises use vertical fan coils or water-source heat pumps. A tech who only carries residential boards will waste a trip in those closets. Tell us the building and the label on the indoor unit.</p>
<p>Commercial work here is often a single RTU over a unit in a plaza, not a downtown office tower. Makeup air and washroom exhaust fail after a long weekend. We want the unit letter, the rooftop make if you can read the plate, and whether staff can stay open without cooling.</p>
<p>Reviews published on this site name technicians — Paul, Matthew, Ken, Alan — for evening furnace boards, heat-wave AC, and condo fan coils. We do not run a fake review widget. The on-site claim is more than 15,000 customers over the past decade. Google sits near 4.8 with a large review volume.</p>
<p>If you are in Markham with no heat tonight, call. 24/7 is dispatch intent: we answer and assign the next free truck. After-hours rate may apply. We aim to diagnose in one visit. We will not print rebate dollar amounts; we help check current Enbridge and Save on Energy eligibility when you replace a system.</p>
<p>Postal codes we see most from this shop: L3R, L3P, L6C, L6E. If you are in Unionville, Buttonville industrial, or a Hwy 7 suite, say which — the truck stock changes. Do not browse Products from an ad; use the dispatch form on the contact slug and keep that URL live.</p>""",
        ),
        "pages/service-areas/hvac-contractor-richmond-hill-on.html": (
            "Richmond Hill HVAC Repair | Service Express",
            "Yonge condos and house furnaces. Call (416) 637-1678.",
            "/pages/service-areas/hvac-contractor-richmond-hill-on",
            "Richmond Hill: Yonge condos and houses that still use a basement furnace.",
            "North of Major Mackenzie the houses get older. Along Yonge the buildings get taller.",
            """<p>Richmond Hill is not a find-replace of Markham. The Yonge corridor from 16th to Elgin Mills is condo and rental high-rise: closet fan coils, water-source heat pumps, and the occasional Magic Pak. Further north and east — Oak Ridges, Jefferson, the streets off Bathurst — you still get 90s furnaces, outdoor AC on a pad, and homeowners who call at 11pm when the house hits 12°C.</p>
<p>We drive from Markham. That matters on a no-heat night because the truck is already on the 404/407 side of York Region, not coming from Mississauga. It does not mean a 20-minute promise. 24/7 means we take the emergency call and aim to dispatch.</p>
<p>Condo property managers here often share a riser with several suites. If your pan is overflowing, the suite below is already involved. Send the building name, suite, and the make on the unit. Stephanie’s published review on this site is the pattern we want: a tech who can diagnose a fan coil without guessing.</p>
<p>House work is still the majority of winter calls: ignition failure, cracked heat exchanger suspicion, a thermostat that was “already replaced.” Paul showing up in the evening to read a furnace board — that review is on the site — is the house version of the same job. Summer is outdoor AC that will not start after a heat wave, same as J. Hsu wrote.</p>
<p>Plaza rooftops sit along Yonge and Major Mackenzie. If the RTU is down, give us the unit number and whether the kitchen hood or makeup air is also off. We service common rooftop brands; we do not invent dealer badges.</p>
<p>Richmond Hill replacements sometimes qualify for current heat-pump offers. We help check eligibility. We will not quote a rebate dollar on this page. Financing, if any, is discussed on the call — not advertised as a rate.</p>
<p>Common postals: L4B, L4C, L4E, L4S. Oak Ridges no-heat and a Yonge-and-16th fan coil are different tickets. Put the property type on the form so we do not send a rooftop kit to a basement furnace.</p>""",
        ),
        "pages/service-areas/hvac-contractor-scarborough-on.html": (
            "Scarborough HVAC Repair | Service Express",
            "Bungalows, Kennedy high-rises, plaza rooftops. Call (416) 637-1678.",
            "/pages/service-areas/hvac-contractor-scarborough-on",
            "Scarborough HVAC: older bungalows, Kennedy high-rises, plaza rooftops.",
            "A Markham shop that already runs east for fan coils and 20-year furnaces.",
            """<p>Scarborough jobs split three ways, and they are not the same truck kit. West Hill and the bungalow streets off Kingston Road still run aging furnaces and outdoor AC that have survived too many humid summers. The towers around Scarborough Town Centre, Kennedy, and the lake-facing buildings use fan coils and heat pumps in closets that rust from condensate. The plazas on Eglinton, Lawrence, and Sheppard lose rooftop units in July and call when the pharmacy is 30°C.</p>
<p>We are based in Markham, so the 401/404 run is a normal east dispatch, not a special trip. That is geography, not a guarantee of arrival time. Emergency service means we answer and assign the next free technician. After-hours rate may apply; we say so before we roll.</p>
<p>Condo calls here often start as “the AC is leaking.” That is usually a clogged condensate, a failed pump, or a coil that iced because the filter has not been changed since the last owner. Ken’s public write-up of a leaking suite — other companies stalled, then a patient walk-around — is the job we want described on the form: brand, leak vs no cooling vs no heat.</p>
<p>House no-heat in Scarborough in January is still a furnace. Bring the age if you know it. A 20-year unit that we get running for the night, then quote a replacement the next day, is the Jim Mulroney pattern already published on the testimonials page. We aim to diagnose in one visit. Same-day / one-trip marketing stays off this page unless the owner confirms the policy is current.</p>
<p>Commercial: tell us the plaza, the unit letter, and whether kitchen makeup air failed with the RTU. We work rooftops and ventilation. We do not pretend every job is a condo fan coil.</p>
<p>Rebates: we help check current Enbridge and Save on Energy rules for heat pumps. No invented dollar amounts. One public address only — Hood Road unless the owner switches the theme setting to Esna Park.</p>
<p>Postals we dispatch into: M1B, M1E, M1G, M1H, M1P, M1T. If you are in a Kingston Road bungalow, say furnace. If you are near STC, say fan coil or heat pump. That one word changes what is on the truck.</p>""",
        ),
        "pages/service-areas/hvac-contractor-toronto-on.html": (
            "Toronto HVAC Repair | Condo & Home | Service Express",
            "Closet fan coils downtown, house furnaces in East York. Call (416) 637-1678.",
            "/pages/service-areas/hvac-contractor-toronto-on",
            "Toronto HVAC for closet fan coils and houses that still have a furnace.",
            "Downtown the system is in the closet. East York and the Annex still have basements.",
            """<p>Toronto is where the condo wedge is loudest. New towers and many 80s–2000s buildings heat and cool from a vertical fan coil or a water-source heat pump in a hall closet. The complaint is almost always the same: warm air in July, no heat in January, or water on the laminate. PTAC and Magic Pak show up in older rentals and some mid-rises. Sky Mark packages appear on a shorter list of buildings. Read the label. Do not tell us you have “HVAC.”</p>
<p>Houses are a different job. East York, the Danforth side streets, parts of North York that people still call Toronto, and the Annex mixes: mid-efficiency furnaces, boilers, and more ductless every year because there is no room for ducts. Rick’s published 9pm furnace call and Jamie’s Thursday-night board replacement are house stories. Stephanie’s fan-coil diagnosis is the tower story. We keep them separate on the form so the truck is stocked.</p>
<p>Commercial rooftops in Toronto are often a single RTU over a restaurant or shop on St. Clair, Danforth, or a small industrial bay. Access, parking, and after-hours dock keys matter more than a pretty contact card. Send the intersection and the unit letter.</p>
<p>We drive in from Markham. Downtown parking and elevator waits add time. 24/7 is still dispatch intent, not a 20-minute SLA. If heat is out, call (416) 637-1678; do not wait on the form callback.</p>
<p>We help check current heat-pump rebate eligibility. We will not publish “you get $X.” We do not invent TSSA ticket numbers. The licence line in the footer stays blank until the owner supplies a real one.</p>
<p>Google sits near 4.8 with a large review volume. The 15,000+ customers line is an on-site claim, not a third-party audit. Technicians named in public reviews include Paul, Ken, Alan, and Matthew. No fake widgets on this page.</p>
<p>Downtown parking and suite access beat any slogan. Put the buzzer code and the intersection on the form. If the building uses a lockbox or a superintendent, say so. We still want the indoor-unit make before we guess at a board.</p>""",
        ),
    }

    for rel, (title, meta, canon, current, body) in pages.items():
        write(rel, wrap(title, meta, canon, 1, body, current))

    for rel, (title, meta, canon, h1, lede, body) in cities.items():
        html = prose_page(
            "Service area",
            h1,
            lede,
            body,
            "../contact-residential-commercial-hvac-company-gta.html#job-request",
            "Request a tech",
        )
        write(rel, wrap(title, meta, canon, 2, html))

    products = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="kicker">Equipment · not a catalogue browse</p>
    <h1>Price the system. Don’t wander the shop.</h1>
    <p class="lede">Ads visitors should not shop Products. If you landed here anyway, pick the system and send a job.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="product-grid">
      <article class="door"><h3>Furnace and AC</h3><p>Residential heating and cooling.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=furnace&amp;job=install#job-request">Price this system</a></p></article>
      <article class="door"><h3>Condo fan coil</h3><p>Vertical fan coil replace and retrofit.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=fan-coil&amp;job=condo#job-request">Price this system</a></p></article>
      <article class="door"><h3>Condo heat pump</h3><p>Water-source heat pumps in newer towers.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=wshp&amp;job=condo#job-request">Price this system</a></p></article>
      <article class="door"><h3>Boiler and in-floor</h3><p>Hydronic boilers, in-floor, snow melt.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=boiler&amp;job=install#job-request">Price this system</a></p></article>
      <article class="door"><h3>Commercial rooftop and MAU</h3><p>Rooftop, ventilation, makeup air.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=rtu&amp;job=commercial#job-request">Price this system</a></p></article>
      <article class="door"><h3>Ductless split</h3><p>Mini-splits where there is no ductwork.</p><p><a class="btn-primary" href="contact-residential-commercial-hvac-company-gta.html?product=ductless&amp;job=install#job-request">Price this system</a></p></article>
    </div>
  </div>
</section>
"""
    write(
        "pages/hvac-products.html",
        wrap(
            "Price This HVAC System | Service Express",
            "Furnace, fan coil, heat pump, rooftop. Call (416) 637-1678.",
            "/pages/hvac-products",
            1,
            products,
        ),
    )
    write(
        "pages/service-areas.html",
        wrap(
            "GTA HVAC Service Areas | Service Express",
            "Markham, Richmond Hill, Scarborough, Toronto.",
            "/pages/service-areas",
            1,
            prose_page(
                "GTA service areas",
                "Markham shop. Trucks into York and Toronto.",
                "Four city pages with local jobs — not the same paragraph with the city name swapped.",
                """<p><a href="service-areas/hvac-contractor-markham-on.html">Markham</a> · <a href="service-areas/hvac-contractor-richmond-hill-on.html">Richmond Hill</a> · <a href="service-areas/hvac-contractor-scarborough-on.html">Scarborough</a> · <a href="service-areas/hvac-contractor-toronto-on.html">Toronto</a></p>
<p>Surrounding GTA communities: call (416) 637-1678 and give the postal code.</p>""",
                "contact-residential-commercial-hvac-company-gta.html#job-request",
                "Request a tech",
            ),
        ),
    )
    write(
        "pages/markham-hvac-company-work.html",
        wrap(
            "Our Work | Service Express",
            "Job photos belong here — not stock HVAC.",
            "/pages/markham-hvac-company-work",
            1,
            prose_page(
                "Our work",
                "Job photos belong here — not stock HVAC.",
                "Add real install and repair photos. We will not invent a gallery.",
                "<p>Until the owner uploads job photos, use the ads landing reviews and call (416) 637-1678.</p>",
                "contact-residential-commercial-hvac-company-gta.html#job-request",
                "Request a tech",
            ),
        ),
    )


if __name__ == "__main__":
    main()
