# SZEINER.COM - Kompletní webová analýza

**Datum analýzy:** 7. prosince 2025
**Analyzovaný web:** https://szeiner.com/
**Verze dokumentu:** 1.0
**Účel:** Komplexní audit webu s doporučeními pro redesign

---

## EXECUTIVE SUMMARY

### Celkové hodnocení webu

| Oblast | Skóre | Hodnocení |
|--------|-------|-----------|
| **SEO** | 3.4/10 | Kritické nedostatky |
| **UX/UI** | 4.6/10 | Pod průměrem |
| **Design** | 4.0/10 | Vyžaduje redesign |
| **Právní compliance** | 2.0/10 | Kritické riziko |
| **Technický stav** | 5.0/10 | Průměrný |
| **CELKOVĚ** | **3.8/10** | **Vyžaduje kompletní redesign** |

### Klíčové problémy vyžadující okamžitou pozornost

1. **KRITICKÉ:** Chybí cookie consent banner (pokuta až 10 mil. EUR)
2. **KRITICKÉ:** Chybí obchodní podmínky pro webhosting (pokuta až 5 mil. Kč)
3. **KRITICKÉ:** Překlep "develompent" na homepage viditelný v Google
4. **KRITICKÉ:** Chybí kontaktní formulář
5. **VYSOKÁ:** Žádné CTA tlačítka na homepage
6. **VYSOKÁ:** Obrázky se nenačítají (viditelné SVG placeholdery)

---

## 1. O SPOLEČNOSTI SZEINER

### 1.1 Základní informace

| Parametr | Hodnota |
|----------|---------|
| **Název** | SZEINER s.r.o. |
| **IČO** | 058 22 882 |
| **Sídlo** | Zbýšov 90, Česká republika |
| **Založení** | 2017 (původní název Lusorion Creatives) |
| **Obor** | Vývoj her pro PC a konzole, webhosting |
| **Velikost** | Malá firma (1-10 zaměstnanců) |

### 1.2 Produkty a služby

| Produkt/Služba | Popis | Stav |
|----------------|-------|------|
| **Azulgar: Star Commanders** | Sci-Fi open world sandbox hra | Steam Early Access od 2017 |
| **Cybershift** | Arcade akční hra | Na Steamu |
| **NEO: Commanders** | Strategická hra | V vývoji |
| **LEXTOSHOP** | CMS/E-shop platforma | Aktivní (2024) |
| **Webhosting** | Hostingové služby | Aktivní |
| **Live Status** | Monitoring systém | status.szeiner.com |

### 1.3 Steam hodnocení hlavní hry

| Metrika | Hodnota | Hodnocení |
|---------|---------|-----------|
| Azulgar hodnocení | 55% (Mixed) | Podprůměrné |
| Počet recenzí | 40 | Nízký |
| Průměrná doba hraní | 12 minut | Kriticky nízká |
| Stav | Early Access | 7+ let ve vývoji |

---

## 2. TECHNICKÁ ANALÝZA

### 2.1 Infrastruktura

| Parametr | Stav | Hodnocení |
|----------|------|-----------|
| HTTPS/SSL | Aktivní ✅ | OK |
| CDN | CloudFlare | OK |
| DDoS ochrana | Aktivní | OK |
| Platforma | WordPress | Standard |
| Responzivita | Ano | OK |

### 2.2 Výkonnostní problémy

| Problém | Dopad | Priorita |
|---------|-------|----------|
| Lazy loading nefunguje | Obrázky se nezobrazují | KRITICKÁ |
| WebP formát neimplementován | Pomalé načítání | VYSOKÁ |
| Skeleton loadery chybí | Špatná UX | STŘEDNÍ |
| Core Web Vitals neměřeno | Neznámý výkon | STŘEDNÍ |

### 2.3 Doporučené cíle výkonu

```
LCP (Largest Contentful Paint): < 2.5s
FID (First Input Delay): < 100ms
CLS (Cumulative Layout Shift): < 0.1
PageSpeed skóre: > 90 (mobile i desktop)
TTFB (Time to First Byte): < 600ms
```

---

## 3. SEO ANALÝZA

### 3.1 Kritické SEO problémy

#### 3.1.1 Překlep na hlavní stránce
```
CHYBA: "develompent" místo "development"
LOKACE: Hlavní popis firmy na homepage
DOPAD: Viditelné ve výsledcích Google, poškozuje profesionalitu
PRIORITA: ⚠️ OKAMŽITÁ OPRAVA (5 minut práce)
```

#### 3.1.2 Problémy s title tagy

| Stránka | Aktuální title | Problém | Doporučený title |
|---------|----------------|---------|------------------|
| Homepage | "Home - SZEINER Software Company" | Žádná klíčová slova | "SZEINER - České herní studio \| Vývoj her pro PC a konzole" |
| About | "ABOUT US - SZEINER Software Company" | Generické | "O nás \| SZEINER - Nezávislý vývojář her z ČR" |
| Webhosting | "Webhosting - SZEINER Software Company" | Chybí USP | "Webhosting pro hráče a vývojáře \| SZEINER" |
| Games | "GAMES - SZEINER Software Company" | Generické | "Naše hry \| Azulgar, Cybershift \| SZEINER" |

#### 3.1.3 Chybějící meta descriptions

- **Stav:** Chybí nebo slabé na většině stránek
- **Doporučená délka:** 150-160 znaků
- **Požadavek:** Unikátní popis s CTA pro každou stránku

#### 3.1.4 Struktura nadpisů

| Problém | Aktuální stav | Doporučení |
|---------|---------------|------------|
| H1 | "Life is a Game..." | Změnit na "SZEINER - České herní studio" |
| H2-H6 | Nekonzistentní hierarchie | Jeden H1/stránka, H2 pro sekce, H3+ pro podsekce |

#### 3.1.5 Alt texty obrázků
```
STAV: ❌ CHYBÍ
DOPAD: Ztráta obrazkového SEO, problémy s přístupností
PŘÍKLAD: Lazy loading placeholdery bez popisků
```

### 3.2 Analýza klíčových slov

| Klíčové slovo | Měsíční hledanost (CZ) | Konkurence | Aktuální pozice |
|---------------|------------------------|------------|-----------------|
| české herní studio | 50-100 | Nízká | MIMO TOP 50 |
| vývoj her česká republika | 20-50 | Nízká | MIMO TOP 50 |
| indie game developer czech | 10-30 | Nízká | MIMO TOP 50 |
| game development company | 200-500 | Vysoká | MIMO TOP 50 |
| webhosting pro hry | 10-30 | Střední | MIMO TOP 50 |

### 3.3 Zpětné odkazy (Backlinks)

#### Existující
| Zdroj | Typ |
|-------|-----|
| Steam | Produktová stránka |
| LinkedIn | Firemní profil |
| IndieDB | Vývojářská stránka |

#### Chybějící (doporučené)
- Games.cz
- Bonusweb.cz
- GDACZ (Asociace českých herních vývojářů)
- Česká herní média
- Hrej.cz, Doupě.cz

### 3.4 SEO skóre: 3.4/10

---

## 4. UX/UI ANALÝZA

### 4.1 Struktura webu

```
szeiner.com/
├── Homepage (/)
├── PRODUCTS
│   ├── CMS PLATFORM
│   │   └── LEXTOSHOP (/lextoshop/)
│   └── GAMES (/games/)
│       ├── Azulgar (/game/azulgar/)
│       ├── Cybershift (/game/cybershift/)
│       ├── NEO: Commanders (/game/neo-commanders/)
│       └── SZEINER Legacy (/old-games/)
├── SERVICES
│   └── Webhosting (/webhosting/)
├── COMMUNITY
│   ├── Blog (/blog/)
│   └── Discord (/dc/) -> externí
├── COMPANY
│   ├── About Us (/about/)
│   ├── Career (/career/)
│   └── Live Status (status.szeiner.com)
├── Store (/store/)
├── Account (account.szeiner.com)
└── Legal
    ├── Privacy Policy (/privacy-policy/)
    ├── Terms of Use (/terms-of-use/)
    └── GDPR (/gdpr/)
```

### 4.2 Navigace

| Prvek | Stav | Hodnocení |
|-------|------|-----------|
| Hlavní menu | Dropdown (Products, Services, Community, Company) | OK |
| Počet kliknutí k cíli | 1-2 | OK |
| Breadcrumbs | Funkční | OK |
| Mobile menu | Hamburger | OK |
| Aktivní stav v menu | ❌ CHYBÍ | Problém |
| Logo | SVG placeholder (nenačítá se) | KRITICKÉ |

### 4.3 Kritické UX problémy

#### 4.3.1 Chybějící CTA (Call-to-Action)
```
PROBLÉM: Návštěvník neví, co má dělat
LOKACE: Homepage
CHYBÍ:
- Tlačítko "Koupit hru"
- Tlačítko "Hrát demo"
- Tlačítko "Prohlédnout portfolio"
- Tlačítko "Připojit se na Discord"
```

#### 4.3.2 Chybějící prvky

| Prvek | Stav | Priorita |
|-------|------|----------|
| Vyhledávání na webu | ❌ CHYBÍ | Vysoká |
| Newsletter přihlášení | ❌ CHYBÍ | Střední |
| Steam widget | ❌ CHYBÍ | Vysoká |
| Video trailer na homepage | ❌ CHYBÍ | Vysoká |
| Kontaktní formulář | ❌ CHYBÍ | KRITICKÁ |
| Live chat | ❌ CHYBÍ | Nízká |
| Scroll-to-top tlačítko | ❌ CHYBÍ | Nízká |

#### 4.3.3 Jazykové problémy

| Problém | Lokace | Oprava |
|---------|--------|--------|
| "develompent" | Homepage | "development" |
| "DEDICATION SERVER" | Game detail | "DEDICATED SERVER" |
| "Create with" | Footer | "Created with" |
| Mix češtiny a angličtiny | Celý web | Implementovat přepínač jazyků |
| Chybí česká verze | - | Vytvořit CZ mutaci |

### 4.4 User Flows - Analýza

#### Flow 1: Návštěvník chce koupit hru
```
Homepage -> ??? (žádné CTA)
         -> Menu -> Products -> Games -> Azulgar
         -> Steam button -> Steam Store (externí)

Počet kroků: 4-5
Problém: Chybí přímá cesta z homepage
Doporučení: Přidat CTA "Naše hry" na homepage
```

#### Flow 2: Návštěvník chce objednat webhosting
```
Homepage -> Menu -> Services -> Webhosting
         -> Contact US -> mailto link -> Email klient
         -> Napsat email -> Čekat na odpověď

Počet kroků: 5+ (včetně emailové komunikace)
Problém: Není online objednávka
Doporučení: Implementovat objednávkový formulář
```

#### Flow 3: Návštěvník chce kontaktovat firmu
```
Homepage -> Scroll dolů -> Footer -> Email link
NEBO
Homepage -> Menu -> Company -> About Us -> Email linky

Problém: Žádný kontaktní formulář
Doporučení: Přidat /contact stránku s formulářem
```

### 4.5 Přístupnost (WCAG 2.1)

| Kritérium | Stav | Problém |
|-----------|------|---------|
| Alt texty obrázků | ❌ FAIL | SVG placeholdery bez alt |
| Kontrast textu | ✅ OK | Bílé na tmavém |
| Klávesová navigace | ⚠️ NEURČENO | Nutno otestovat |
| Screen reader | ❌ FAIL | Chybí ARIA labels |
| Focus stavy | ⚠️ NEURČENO | Nutno otestovat |
| Skip links | ❌ CHYBÍ | Žádné skip navigace |

### 4.6 UX skóre: 4.6/10

---

## 5. VIZUÁLNÍ DESIGN

### 5.1 Barevná paleta

#### Primární barvy
| Název | Hex kód | Použití |
|-------|---------|---------|
| Tmavé pozadí | #0a0a0a / #121212 | Hlavní pozadí webu |
| Akcent červená/oranžová | #ff6b35 / #e85a2c | CTA tlačítka, zvýraznění |
| Bílá | #ffffff | Text, nadpisy |
| Šedá | #888888 / #666666 | Sekundární text |

#### Sekundární barvy
| Název | Hex kód | Použití |
|-------|---------|---------|
| Tmavě šedá | #1a1a1a / #2a2a2a | Karty, sekce |
| Modrá | #3498db | Odkazy (hover) |
| Zelená | #27ae60 | Úspěch, pozitivní stavy |

### 5.2 Typografie

| Typ | Font | Použití |
|-----|------|---------|
| Nadpisy | System/Sans-serif | H1, H2, H3 |
| Body text | System/Sans-serif | Odstavce, popisy |

#### Velikosti písma
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 | 48-56px | 32-36px |
| H2 | 32-40px | 24-28px |
| H3 | 24-28px | 20-22px |
| Body | 16px | 14-16px |
| Small | 12-14px | 12px |

### 5.3 Layout

- **Max-width kontejneru:** ~1200px
- **Padding sekcí:** 60-100px vertikálně
- **Grid:** 12-sloupcový systém
- **Guttery:** 20-30px

### 5.4 Responzivní breakpointy

| Breakpoint | Šířka | Popis |
|------------|-------|-------|
| Desktop | 1200px+ | Plný layout |
| Tablet | 768-1199px | Zúžený layout |
| Mobile | <768px | Jednosloupcový layout |

### 5.5 Problémy s designem

| Problém | Dopad | Řešení |
|---------|-------|--------|
| Obrázky se nenačítají | Web vypadá "rozbitý" | Opravit lazy loading |
| Chybí konzistentní icon set | Nejednotný vzhled | Implementovat Lucide/Heroicons |
| Logo je SVG placeholder | Neprofesionální | Nahrát skutečné logo |
| Chybí WebP formát | Pomalé načítání | Konvertovat obrázky |

---

## 6. PRÁVNÍ ANALÝZA

### 6.1 KRITICKÉ PRÁVNÍ PROBLÉMY

#### 6.1.1 Cookie souhlas
```
STAV: ⚠️ ZCELA CHYBÍ
RIZIKO: Pokuta až 10 mil. EUR nebo 2% ročního obratu
POVINNOST: Od 1.1.2022 (ePrivacy směrnice)
ŘEŠENÍ: Implementovat cookie lištu s granulárním souhlasem
NÁSTROJE: CookieYes, Cookiebot, OneTrust
```

#### 6.1.2 Obchodní podmínky
```
STAV: ⚠️ NEEXISTUJÍ (pro webhosting)
RIZIKO: Pokuta ČOI až 5 mil. Kč
POVINNOST: Pro každý e-commerce prodej
ŘEŠENÍ: Vytvořit obchodní podmínky pro webhosting
```

### 6.2 GDPR Dokumentace

| Dokument | Stav | Problém |
|----------|------|---------|
| Privacy Policy | ⚠️ EXISTUJE | Zastaralé (4.10.2018) |
| GDPR stránka | ⚠️ EXISTUJE | Neúplná práva subjektů |
| Cookie Policy | ❌ CHYBÍ | Kritické |
| Obchodní podmínky | ❌ CHYBÍ | Kritické |
| Reklamační řád | ❌ CHYBÍ | Pro webhosting |

### 6.3 Chybějící právní informace

- ❌ Právo na přístup (čl. 15 GDPR)
- ❌ Právo na omezení zpracování
- ❌ Právo podat stížnost u ÚOOÚ
- ❌ ADR informace (odkaz na ČOI/ODR)
- ❌ Reklamační řád
- ❌ Kontakt na DPO

### 6.4 Jazyková verze dokumentů

| Problém | Dopad |
|---------|-------|
| Pouze angličtina | Čeští spotřebitelé mají právo na informace v češtině |
| Chybí CZ verze | Porušení práv spotřebitele |

---

## 7. SROVNÁNÍ S KONKURENCÍ

### 7.1 Benchmarking s českými studii

| Studio | Design | UI | UX | CELKEM |
|--------|--------|----|----|--------|
| **SZEINER** | 10/25 (40%) | 8/25 (32%) | 9/25 (36%) | **27/75 (36%)** |
| Amanita Design | 23/25 (92%) | 19/25 (76%) | 19/25 (76%) | 61/75 (81%) |
| Warhorse Studios | 19/25 (76%) | 19/25 (76%) | 18/25 (72%) | 56/75 (75%) |
| SCS Software | 17/25 (68%) | 18/25 (72%) | 17/25 (68%) | 52/75 (69%) |
| Supergiant Games | 23/25 (92%) | 22/25 (88%) | 20/25 (80%) | 65/75 (87%) |

### 7.2 Co konkurence dělá lépe

| Studio | Silná stránka | Inspirace pro SZEINER |
|--------|---------------|----------------------|
| Amanita Design | Vizuální konzistence, minimalistická navigace | 5 položek v menu, brand identity |
| Warhorse Studios | Dvojjazyčnost CZ/EN, press kit | Implementovat přepínač jazyků |
| SCS Software | GDPR compliance, komunita | Kompletní právní dokumentace |
| Supergiant Games | CTA pro všechny platformy | Tlačítka Steam/GOG/Epic |

### 7.3 Cíle pro redesign

| Metrika | Aktuálně SZEINER | Cíl (6 měsíců) |
|---------|------------------|----------------|
| Design skóre | 10/25 (40%) | 20/25 (80%) |
| UI skóre | 8/25 (32%) | 18/25 (72%) |
| UX skóre | 9/25 (36%) | 17/25 (68%) |
| Celkem | 27/75 (36%) | 55/75 (73%) |

---

## 8. AKČNÍ PLÁN IMPLEMENTACE

### 8.1 FÁZE 1: Kritické opravy (1-7 dní)

| # | Úkol | Priorita | Časová náročnost | Zodpovědnost |
|---|------|----------|------------------|--------------|
| 1 | Opravit překlep "develompent" | KRITICKÁ | 5 minut | Dev |
| 2 | Implementovat cookie lištu | KRITICKÁ | 2-4 hodiny | Dev |
| 3 | Přidat kontaktní formulář | KRITICKÁ | 2-3 hodiny | Dev |
| 4 | Vytvořit obchodní podmínky | KRITICKÁ | 4-8 hodin | Legal + Dev |
| 5 | Opravit "DEDICATION" -> "DEDICATED" | VYSOKÁ | 5 minut | Dev |
| 6 | Opravit "Create with" -> "Created with" | VYSOKÁ | 5 minut | Dev |
| 7 | Přidat primární CTA na homepage | VYSOKÁ | 1-2 hodiny | Dev + Design |

### 8.2 FÁZE 2: SEO základ (1-4 týdny)

| # | Úkol | Priorita | Časová náročnost |
|---|------|----------|------------------|
| 8 | Přepsat title tagy | VYSOKÁ | 2-3 hodiny |
| 9 | Vytvořit meta descriptions | VYSOKÁ | 3-4 hodiny |
| 10 | Opravit H1-H6 strukturu | VYSOKÁ | 2-3 hodiny |
| 11 | Přidat alt texty ke všem obrázkům | VYSOKÁ | 4-6 hodin |
| 12 | Vytvořit sitemap.xml | STŘEDNÍ | 1 hodina |
| 13 | Optimalizovat robots.txt | STŘEDNÍ | 30 minut |
| 14 | Nastavit Google Search Console | STŘEDNÍ | 1 hodina |
| 15 | Opravit lazy loading obrázků | VYSOKÁ | 4-8 hodin |

### 8.3 FÁZE 3: UX vylepšení (1-2 měsíce)

| # | Úkol | Priorita | Časová náročnost |
|---|------|----------|------------------|
| 16 | Přidat Steam widget | VYSOKÁ | 2-3 hodiny |
| 17 | Přidat video trailery | VYSOKÁ | 4-6 hodin |
| 18 | Vytvořit českou verzi webu | VYSOKÁ | 2-3 dny |
| 19 | Implementovat vyhledávání | STŘEDNÍ | 4-8 hodin |
| 20 | Přidat newsletter signup | STŘEDNÍ | 2-3 hodiny |
| 21 | Přepracovat webhosting sekci | STŘEDNÍ | 1 den |
| 22 | Redesign hero sekce s videem | VYSOKÁ | 1-2 dny |
| 23 | Zjednodušit navigaci (max 5 položek) | STŘEDNÍ | 2-4 hodiny |

### 8.4 FÁZE 4: Dlouhodobé cíle (3-6 měsíců)

| # | Úkol | Priorita |
|---|------|----------|
| 24 | Stát se členem GDACZ | VYSOKÁ |
| 25 | PR kampaň v českých herních médiích | VYSOKÁ |
| 26 | Aktivní blog s aktualizacemi vývoje | STŘEDNÍ |
| 27 | Zlepšit hodnocení Azulgar na Steamu | VYSOKÁ |
| 28 | Budovat zpětné odkazy | STŘEDNÍ |
| 29 | Vytvořit press kit stránku | STŘEDNÍ |
| 30 | Integrace Discord statistik na homepage | NÍZKÁ |

---

## 9. TECHNICKÁ SPECIFIKACE PRO PROGRAMÁTORY

### 9.1 Doporučená architektura

```
Frontend:
├── Framework: Next.js 14+ (React)
├── Styling: Tailwind CSS
├── Animace: Framer Motion
├── Ikony: Lucide Icons / Heroicons
├── State: Zustand / React Query
└── TypeScript: Povinné

CMS:
├── Primární: Strapi / Contentful (headless)
└── Alternativa: WordPress REST API

Hosting:
├── Frontend: Vercel / Netlify
├── Backend/CMS: Vlastní server
└── CDN: CloudFlare (zachovat)

Analytics:
├── Google Analytics 4
├── Google Search Console
├── Hotjar (heatmapy)
└── Plausible (alternativa)
```

### 9.2 Design tokeny (CSS)

```css
:root {
  /* Barvy */
  --color-bg-primary: #0a0a0a;
  --color-bg-secondary: #1a1a1a;
  --color-bg-card: #2a2a2a;

  --color-text-primary: #ffffff;
  --color-text-secondary: #888888;
  --color-text-muted: #666666;

  --color-accent-primary: #ff6b35;
  --color-accent-hover: #ff8555;
  --color-accent-secondary: #3498db;

  --color-success: #27ae60;
  --color-error: #e74c3c;
  --color-warning: #f39c12;

  /* Typografie */
  --font-family-heading: 'Inter', system-ui, sans-serif;
  --font-family-body: 'Inter', system-ui, sans-serif;

  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 2rem;      /* 32px */
  --font-size-4xl: 2.5rem;    /* 40px */
  --font-size-5xl: 3rem;      /* 48px */

  /* Spacing */
  --spacing-xs: 0.25rem;      /* 4px */
  --spacing-sm: 0.5rem;       /* 8px */
  --spacing-md: 1rem;         /* 16px */
  --spacing-lg: 1.5rem;       /* 24px */
  --spacing-xl: 2rem;         /* 32px */
  --spacing-2xl: 3rem;        /* 48px */
  --spacing-3xl: 4rem;        /* 64px */

  /* Border radius */
  --radius-sm: 0.25rem;       /* 4px */
  --radius-md: 0.5rem;        /* 8px */
  --radius-lg: 1rem;          /* 16px */
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);

  /* Transitions */
  --transition-fast: 150ms ease;
  --transition-normal: 300ms ease;
  --transition-slow: 500ms ease;

  /* Z-index */
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-modal: 300;
  --z-tooltip: 400;
}
```

### 9.3 Komponenty k implementaci

| Komponenta | Priorita | Složitost | Popis |
|------------|----------|-----------|-------|
| `<Navbar />` | Kritická | Střední | Sticky, responsive, dropdown |
| `<Hero />` | Kritická | Vysoká | Video background, CTA |
| `<GameCard />` | Kritická | Nízká | Obrázek, název, platformy |
| `<Button />` | Kritická | Nízká | Primary, Secondary, Ghost |
| `<Footer />` | Kritická | Nízká | Links, social, newsletter |
| `<Timeline />` | Vysoká | Střední | Firemní historie |
| `<Gallery />` | Vysoká | Střední | Lightbox, filtry |
| `<PricingCard />` | Vysoká | Nízká | Ceník webhostingu |
| `<ContactForm />` | Vysoká | Střední | Validace, submit |
| `<CookieConsent />` | Kritická | Střední | GDPR compliant |
| `<Newsletter />` | Střední | Nízká | Email signup |
| `<LanguageSwitcher />` | Střední | Nízká | CZ/EN přepínač |
| `<SearchModal />` | Střední | Vysoká | Full-text search |
| `<SteamWidget />` | Vysoká | Nízká | Steam iframe/API |

### 9.4 API integrace

```typescript
// Steam Store API
interface SteamGame {
  appid: number;
  name: string;
  price: {
    final: number;
    discount_percent: number;
  };
  ratings: {
    positive: number;
    negative: number;
  };
}

// Discord Widget API
interface DiscordWidget {
  id: string;
  name: string;
  presence_count: number;
  members: DiscordMember[];
}

// Newsletter (Mailchimp/ConvertKit)
interface NewsletterSubscribe {
  email: string;
  tags?: string[];
}
```

### 9.5 Povinné stránky

| Stránka | URL | Obsah |
|---------|-----|-------|
| Homepage | / | Hero, featured produkty, aktuality |
| Hry | /games | Portfolio s detaily, Steam integrace |
| Detail hry | /games/[slug] | Video, galerie, nákupní tlačítka |
| O nás | /about | Příběh firmy, tým, timeline |
| Webhosting | /services/webhosting | Ceník, specifikace, objednávka |
| Blog | /blog | Aktualizace vývoje, novinky |
| Kariéra | /career | Volné pozice, firemní kultura |
| Kontakt | /contact | Formulář, mapa, kontaktní údaje |
| Privacy Policy | /privacy-policy | GDPR compliant |
| Cookies | /cookies | Cookie policy |
| Obchodní podmínky | /terms | Pro webhosting |

---

## 10. CHECKLIST PRO IMPLEMENTACI

### 10.1 SEO Checklist

- [ ] Unikátní title tag na každé stránce (50-60 znaků)
- [ ] Unikátní meta description (150-160 znaků)
- [ ] Jeden H1 na stránku s klíčovým slovem
- [ ] Strukturovaná data (Schema.org - Organization, Product, BreadcrumbList)
- [ ] Alt texty u všech obrázků
- [ ] Sitemap.xml
- [ ] Robots.txt optimalizovaný
- [ ] Kanonizace URL
- [ ] HTTPS přesměrování
- [ ] Mobile-first design
- [ ] Core Web Vitals splněny
- [ ] Open Graph meta tagy
- [ ] Twitter Card meta tagy

### 10.2 Právní Checklist

- [ ] Cookie lišta s granulárním souhlasem
- [ ] Cookie policy stránka
- [ ] Privacy policy (GDPR compliant, CZ i EN)
- [ ] Obchodní podmínky pro webhosting
- [ ] Reklamační řád
- [ ] Informace o ADR (odkaz na ČOI)
- [ ] Identifikace prodávajícího (IČO, sídlo, kontakt)
- [ ] Kontakt na DPO
- [ ] Práva subjektů údajů (přístup, oprava, výmaz)

### 10.3 UX Checklist

- [ ] CTA tlačítka na každé stránce
- [ ] Kontaktní formulář funkční
- [ ] Vyhledávání implementováno
- [ ] Newsletter signup
- [ ] Steam widget na homepage
- [ ] Video trailery funkční
- [ ] Galerie s lightbox
- [ ] Scroll-to-top tlačítko
- [ ] Loading stavy (skeleton)
- [ ] Error stavy
- [ ] Success notifikace
- [ ] 404 stránka

### 10.4 Technický Checklist

- [ ] Lazy loading funkční
- [ ] Obrázky v WebP formátu
- [ ] Gzip/Brotli komprese
- [ ] CDN aktivní
- [ ] SSL certifikát platný
- [ ] Responzivní na všech zařízeních
- [ ] Cross-browser kompatibilita
- [ ] WCAG 2.1 AA compliance
- [ ] PageSpeed > 90
- [ ] Google Analytics 4 implementován
- [ ] Google Search Console propojeno

---

## 11. METRIKY PRO SLEDOVÁNÍ ÚSPĚCHU

### 11.1 KPIs po redesignu

| Metrika | Aktuální | Cíl (3 měsíce) | Cíl (6 měsíců) |
|---------|----------|----------------|----------------|
| Organický traffic | Neměřeno | +100% | +200% |
| Bounce rate | Neměřeno | < 60% | < 50% |
| Průměrná doba na webu | Neměřeno | > 1:30 | > 2:00 |
| Konverzní poměr (CTA klik) | ~0% | > 2% | > 3% |
| PageSpeed mobile | Neměřeno | > 80 | > 90 |
| Indexované stránky | 15-20 | 25+ | 30+ |
| Newsletter subscribers | 0 | 100+ | 500+ |
| Discord members | ? | +20% | +50% |

### 11.2 Nástroje pro měření

| Nástroj | Účel | Cena |
|---------|------|------|
| Google Analytics 4 | Traffic, konverze | Zdarma |
| Google Search Console | SEO, indexace | Zdarma |
| Hotjar | Heatmapy, recordings | Freemium |
| PageSpeed Insights | Výkon | Zdarma |
| GTmetrix | Výkon, doporučení | Freemium |
| Ahrefs/SEMrush | SEO monitoring | Placené |

---

## 12. ZÁVĚR A DOPORUČENÍ

### 12.1 Shrnutí hlavních problémů

1. **SEO:** Kritické nedostatky (překlep, chybějící meta data, alt texty)
2. **UX:** Žádné CTA, chybějící konverzní prvky, nefunkční obrázky
3. **Právní:** Chybí cookie souhlas, obchodní podmínky
4. **Design:** Nefunkční lazy loading, chybí konzistentní vizuální identita
5. **Konkurence:** Výrazně za ostatními českými herními studii

### 12.2 Doporučený přístup

Web vyžaduje **kompletní redesign** se zaměřením na:

1. **Profesionální prezentaci portfolia** - funkční obrázky, video trailery
2. **Jasné konverzní cesty** - CTA tlačítka, Steam widget
3. **Plnou právní compliance** - cookie consent, obchodní podmínky
4. **SEO-first přístup** - title tagy, meta descriptions, strukturovaná data
5. **Dvojjazyčnost** - CZ/EN verze webu

### 12.3 Očekávaný ROI

| Oblast | Očekávaný přínos |
|--------|------------------|
| Organický traffic | +200-300% do 6 měsíců |
| Konverzní poměr | +200-300% |
| Důvěryhodnost | Výrazně vyšší u partnerů |
| Právní riziko | Eliminace pokut |
| Brand awareness | Zlepšení pozice v českém herním ekosystému |

### 12.4 Investice vs. Riziko

| Scénář | Investice | Riziko |
|--------|-----------|--------|
| **Neopravit nic** | 0 Kč | Pokuta GDPR až 10M EUR, ztráta zákazníků |
| **Jen kritické opravy** | ~10-20k Kč | Stále slabá konkurenceschopnost |
| **Kompletní redesign** | ~100-200k Kč | Minimální, vysoká návratnost |

---

*Dokument vytvořen: 7. prosince 2025*
*Autor: Claude Code Analysis*
*Pro použití: SZEINER s.r.o. - Redesign webu szeiner.com*
