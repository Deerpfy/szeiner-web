# SZEINER.COM - Detailni analyza designu, UI a UX

**Datum analyzy:** 6. prosince 2025  
**Analyzovany web:** https://szeiner.com/  
**Ucel dokumentu:** Podklad pro redesign webu s porovnanim konkurence

---

## 1. PREHLED WEBU A JEHO STRUKTURY

### 1.1 Zakladni informace
- **Platforma:** WordPress
- **Tema:** Custom/Premium tema s hernim zamerenim
- **Hlavni sekce:** Products, Services, Community, Company
- **Pocet hlavnich stranek:** 15+
- **Jazykova verze:** Pouze anglictina

### 1.2 Mapa webu (Site Structure)
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
│   └── Discord (/dc/) -> externi
├── COMPANY
│   ├── About Us (/about/)
│   ├── Career (/career/)
│   └── Live Status (status.szeiner.com) -> subdomena
├── Store (/store/)
├── Account (account.szeiner.com) -> subdomena
└── Legal
    ├── Privacy Policy (/privacy-policy/)
    ├── Terms of Use (/terms-of-use/)
    └── GDPR (/gdpr/)
```

---

## 2. DESIGN ANALYZA

### 2.1 Barevna paleta

#### Primarni barvy
| Nazev | Hex kod | Pouziti |
|-------|---------|---------|
| Tmave pozadi | #0a0a0a / #121212 | Hlavni pozadi webu |
| Akcent cervena/oranzova | #ff6b35 / #e85a2c | CTA tlacitka, zvyrazneni |
| Bila | #ffffff | Text, nadpisy |
| Seda | #888888 / #666666 | Sekundarni text |

#### Sekundarni barvy
| Nazev | Hex kod | Pouziti |
|-------|---------|---------|
| Tmave seda | #1a1a1a / #2a2a2a | Karty, sekce |
| Modra | #3498db | Odkazy (hover) |
| Zelena | #27ae60 | Uspech, pozitivni stavy |

### 2.2 Typografie

#### Fonty
| Typ | Font | Pouziti |
|-----|------|---------|
| Nadpisy | System/Sans-serif | H1, H2, H3 |
| Body text | System/Sans-serif | Odstavce, popisy |
| Akcent | - | Neidentifikovan specialni font |

#### Velikosti pisma (odhad)
| Element | Desktop | Mobile |
|---------|---------|--------|
| H1 | 48-56px | 32-36px |
| H2 | 32-40px | 24-28px |
| H3 | 24-28px | 20-22px |
| Body | 16px | 14-16px |
| Small | 12-14px | 12px |

### 2.3 Layout a Grid

#### Struktura
- **Max-width kontejneru:** ~1200px
- **Padding sekci:** 60-100px vertikalne
- **Grid:** 12-sloupcovy system (WordPress)
- **Guttery:** 20-30px

#### Responzivni breakpointy
| Breakpoint | Sirka | Popis |
|------------|-------|-------|
| Desktop | 1200px+ | Plny layout |
| Tablet | 768-1199px | Zuzeny layout |
| Mobile | <768px | Jednoslovcovy layout |

### 2.4 Vizualni prvky

#### Ikony
- SVG placeholder ikony (lazy loading)
- Minimalisticke cerne/bile ikony
- Chybi konzistentni icon set

#### Obrazky
- **Format:** JPG/PNG (bez WebP optimalizace)
- **Lazy loading:** Implementovan (SVG placeholdery)
- **Kvalita:** Vysoka (1920x1080 screenshoty her)
- **Problem:** Obrazky se nenacitaji spravne (viditelne SVG placeholdery)

#### Animace a efekty
- Hover efekty na kartach
- Smooth scrolling
- Parallax efekt na hero sekci (odhad)
- Lightbox galerie pro screenshoty

---

## 3. UI KOMPONENTY - DETAILNI ROZBOR

### 3.1 Navigace

#### Hlavni menu (Desktop)
```
Struktura:
[LOGO] [PRODUCTS v] [SERVICES v] [COMMUNITY v] [COMPANY v] [CART] [LOGIN]
```

| Vlastnost | Hodnota | Hodnoceni |
|-----------|---------|-----------|
| Pozice | Fixni (sticky) | OK |
| Pozadi | Transparentni -> tmave pri scrollu | OK |
| Dropdown | Ano, multi-level | Potrebuje zlepseni |
| Pocet polozek | 6 hlavnich | Na hrane (max 7) |
| Hamburger (mobile) | Ano | OK |

**Problemy:**
- Dropdown menu ma prilis mnoho urovni
- "X" jako login tlacitko je matouci
- Chybi vizualni indikator aktivni stranky
- Logo je SVG placeholder (nenacita se)

#### Breadcrumbs
```
[Home] » [GAMES] » [Azulgar: Star Commanders]
```
- Implementovano na podstrankach
- Chybi na homepage
- Styling: bile linky s "»" oddelovacem

### 3.2 Hero sekce (Homepage)

#### Aktualni struktura
```
+------------------------------------------+
|                                          |
|        # Life is a Game...               |
|                                          |
|        ### We are the gamemakers         |
|                                          |
|  "You do not become a player..."         |
|  "When your heart started beating..."    |
|                                          |
+------------------------------------------+
```

**Problemy:**
- ZADNE CTA tlacitko
- Pozadi se nenacita (SVG placeholder)
- Text je poeticky, ale neinformativni
- Chybi jasna value proposition

#### Doporucena struktura
```
+------------------------------------------+
|                                          |
|     # SZEINER Game Studio                |
|     Ceske nezavisle herni studio         |
|                                          |
|  [NASE HRY]  [PRIPOJ SE NA DISCORD]      |
|                                          |
+------------------------------------------+
```

### 3.3 Karty (Cards)

#### Game Card (stranka /game/azulgar/)
```
+------------------------------------------+
| [VIDEO THUMBNAIL]                        |
+------------------------------------------+
| Azulgar: Star Commanders                 |
| August, 2017                             |
| 16,79 EUR                     Rating: 4.0|
|                                          |
| Popis hry...                             |
|                                          |
| [STEAM BUTTON]                           |
| [FREE DEDICATION SERVER]                 |
+------------------------------------------+
```

**Pozitiva:**
- Jasna cena
- Rating viditelny
- Steam tlacitko pritomne

**Problemy:**
- "DEDICATION" misto "DEDICATED" - preklep
- Chybi dalsi platformy (GOG, Epic)
- Video thumbnail se nenacita

#### Partner Logos
- RegioJet, HexPlay, DoKadz, Boseka
- Vsechny obrazky jsou SVG placeholdery
- Chybi alternativni text (ALT)

### 3.4 Tlacitka (Buttons)

#### Typy tlacitek
| Typ | Styl | Pouziti |
|-----|------|---------|
| Primary | Oranzove/cervene pozadi, bile text | CTA akce |
| Secondary | Outline, bile ohraniceni | Sekundarni akce |
| Ghost | Pouze text, bez pozadi | Navigace |
| Steam | Steam branding | Odkaz na Steam |

#### Problemy s tlacitky
- "Contact US" na webhostingu je mailto link, ne formular
- Chybi hover stavy na nekterych tlacitcich
- Nekonzistentni velikosti
- Steam tlacitko je obrazek, ne styled button

### 3.5 Formularove prvky

#### Kontaktni formular
- **NEEXISTUJE** - pouze mailto linky
- info@szeiner.com, jobs@szeiner.com, investors@szeiner.com

#### Login
- Externi subdomena: account.szeiner.com
- Neni integrovany do hlavniho webu

### 3.6 Paticka (Footer)

#### Struktura
```
+------------------+------------------+------------------+
| INFORMATION      | TERMS & POLICY   | ACCOUNT          |
|                  |                  |                  |
| Since 2008       | Privacy Policy   | Login            |
| Email            | Terms of Use     |                  |
| Company name     | GDPR             |                  |
| ICO              |                  |                  |
| Location         |                  |                  |
|                  |                  |                  |
| REVIEWS          |                  |                  |
| Google 5.0       |                  |                  |
+------------------+------------------+------------------+
| Copyright 2017-25 SZEINER s.r.o. Create with [heart]  |
+-------------------------------------------------------+
```

**Pozitiva:**
- Identifikacni udaje (ICO, sidlo)
- Google Reviews widget
- Pravni odkazy

**Problemy:**
- "Create with" - gramaticka chyba ("Created with")
- Chybi socialni site (Twitter, Facebook, Instagram)
- Chybi newsletter signup
- Chybi sitemap odkaz

### 3.7 Timeline komponenta (About stranka)

#### Struktura
```
2024 ─●─ LEXTOSHOP
         |
2021 ─●─ NEO: Commanders [IMG]
         |
2020 ─●─ Cybershift on Steam! [IMG]
         |
2018 ─●─ We are SZEINER!
         |
2017 ─●─ Azulgar: Star Commanders [IMG]
         |
2017 ─●─ We are born!
```

**Pozitiva:**
- Vizualne atraktivni
- Chronologicky prehled
- Obrazky u milniku

**Problemy:**
- Obrazky se nenacitaji
- Chybi detaily u nekterych milniku
- Mohlo by byt interaktivnejsi

### 3.8 Galerie (Games Gallery)

#### Filtry
```
[All] [Azulgar] [Cybershift] [NEO]
```

**Funkcionalita:**
- JavaScript filtrovani
- Lightbox pro zvetseni
- Grid layout (3-4 sloupce)

**Problemy:**
- Vsechny obrazky jsou SVG placeholdery
- Chybi lazy loading indikator
- Neni jasne, ze se da kliknout

### 3.9 Cenik (Webhosting)

#### Struktura
```
+--------------------+--------------------+
|     STANDARD       |     PREMIUM        |
+--------------------+--------------------+
| 19.79 EUR/rok      | 47.49 EUR/rok      |
| 1 domena           | 3 domeny           |
| 5 GB prostoru      | 10 GB prostoru     |
| FREE SSL/TLS       | FREE SSL/TLS       |
| [Contact US]       | [Contact US]       |
+--------------------+--------------------+
```

**Problemy:**
- Pouze 2 plany (chybi variabilita)
- CTA je mailto, ne objednavkovy formular
- Chybi detailni specifikace
- Chybi srovnavaci tabulka features
- Ceny jsou v EUR bez CZK alternativy

---

## 4. UX ANALYZA - DETAILNI ROZBOR

### 4.1 User Flows

#### Flow 1: Navstevnik chce koupit hru
```
Homepage -> ??? (zadne CTA)
         -> Menu -> Products -> Games -> Azulgar
         -> Steam button -> Steam Store (externi)
```
**Pocet kroku:** 4-5
**Problem:** Chybi prima cesta z homepage

#### Flow 2: Navstevnik chce objednat webhosting
```
Homepage -> Menu -> Services -> Webhosting
         -> Contact US -> mailto link -> Email klient
         -> Napsat email -> Cekat na odpoved
```
**Pocet kroku:** 5+ (vcetne emailove komunikace)
**Problem:** Neni online objednavka

#### Flow 3: Navstevnik hleda praci
```
Homepage -> Menu -> Company -> Career -> ???
```
**Problem:** Career stranka nebyla analyzovana, ale pravdepodobne chybi formular

#### Flow 4: Navstevnik chce kontaktovat firmu
```
Homepage -> Scroll dolu -> Footer -> Email link
NEBO
Homepage -> Menu -> Company -> About Us -> Email linky
```
**Problem:** Zadny kontaktni formular

### 4.2 Pristupnost (Accessibility)

#### WCAG 2.1 Compliance
| Kriterium | Stav | Problem |
|-----------|------|---------|
| Alt texty obrazku | FAIL | SVG placeholdery bez alt |
| Kontrast textu | OK | Bile na tmavem |
| Klavesova navigace | NEURCENO | Nutno otestovat |
| Screen reader | FAIL | Chybi ARIA labels |
| Focus stavy | NEURCENO | Nutno otestovat |
| Skip links | CHYBI | Zadne skip navigace |

#### Kriticke problemy pristupnosti
1. Obrazky nemaji alternativni texty
2. SVG placeholdery jsou nesrozumitelne pro ctecky
3. Chybi semantic HTML na nekterych mistech
4. Logo nema textovou alternativu

### 4.3 Performance UX

#### Vnimana rychlost
| Problem | Dopad | Reseni |
|---------|-------|--------|
| SVG placeholdery misto obrazku | Vizualni "rozbity" web | Opravit lazy loading |
| Zadne skeleton loadery | Neviditelny obsah | Pridat loading states |
| Chybi progresivni nahravani | Pomale LCP | Optimalizovat critical path |

#### Frustracni body
1. Kliknuti na obrazek -> nic se nestane (placeholder)
2. Hledani CTA na homepage -> nenalezeno
3. Pokus o objednavku webhostingu -> pouze email

### 4.4 Informacni architektura

#### Silne stranky
- Logicka struktura menu
- Breadcrumbs navigace
- Jasna hierarchie stranek

#### Slabe stranky
- Prilis hluboky dropdown (3 urovne)
- Duplicitni polozky (Games v menu i v Products)
- Nejasny rozdil mezi Store a Products

### 4.5 Mikrointerakce

#### Existujici
- Hover efekty na kartach
- Dropdown animace
- Lightbox otevreni

#### Chybejici
- Loading indikatory
- Success/Error stavy
- Toast notifikace
- Progress bary
- Scroll-to-top tlacitko

### 4.6 Copywriting UX

#### Problemy s texty
| Lokace | Problem | Oprava |
|--------|---------|--------|
| Homepage H1 | "Life is a Game..." - nejasne | "SZEINER - Ceske herni studio" |
| Homepage popis | "develompent" | "development" |
| Game detail | "DEDICATION SERVER" | "DEDICATED SERVER" |
| Footer | "Create with" | "Created with" |
| About | Prilis dlouhe odstavce | Rozdelit na kratsi sekce |

#### Ton komunikace
- Aktualni: Poeticky, aspiracni
- Doporuceny: Profesionalni, ale pristupny

---

## 5. SROVNANI S KONKURENCI

### 5.1 Srovnavaci tabulka - Design

| Kriterium | SZEINER | Amanita Design | Warhorse | SCS Software | Supergiant |
|-----------|---------|----------------|----------|--------------|------------|
| Vizualni identita | 2/5 | 5/5 | 4/5 | 4/5 | 5/5 |
| Barevna konzistence | 3/5 | 5/5 | 4/5 | 4/5 | 5/5 |
| Typografie | 2/5 | 4/5 | 4/5 | 3/5 | 4/5 |
| Obrazky/Media | 1/5 | 5/5 | 4/5 | 4/5 | 5/5 |
| Animace | 2/5 | 4/5 | 3/5 | 2/5 | 4/5 |
| **Celkem Design** | **10/25** | **23/25** | **19/25** | **17/25** | **23/25** |

### 5.2 Srovnavaci tabulka - UI

| Kriterium | SZEINER | Amanita Design | Warhorse | SCS Software | Supergiant |
|-----------|---------|----------------|----------|--------------|------------|
| Navigace | 3/5 | 5/5 | 4/5 | 4/5 | 4/5 |
| CTA tlacitka | 1/5 | 3/5 | 4/5 | 3/5 | 5/5 |
| Formularove prvky | 0/5 | 2/5 | 3/5 | 3/5 | 3/5 |
| Karty/komponenty | 2/5 | 4/5 | 4/5 | 4/5 | 5/5 |
| Konzistence UI | 2/5 | 5/5 | 4/5 | 4/5 | 5/5 |
| **Celkem UI** | **8/25** | **19/25** | **19/25** | **18/25** | **22/25** |

### 5.3 Srovnavaci tabulka - UX

| Kriterium | SZEINER | Amanita Design | Warhorse | SCS Software | Supergiant |
|-----------|---------|----------------|----------|--------------|------------|
| User flow | 2/5 | 4/5 | 4/5 | 4/5 | 5/5 |
| Pristupnost | 1/5 | 3/5 | 3/5 | 3/5 | 3/5 |
| Performance UX | 1/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Informacni arch. | 3/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| Mikrointerakce | 2/5 | 4/5 | 3/5 | 2/5 | 4/5 |
| **Celkem UX** | **9/25** | **19/25** | **18/25** | **17/25** | **20/25** |

### 5.4 Celkove skore

| Studio | Design | UI | UX | **CELKEM** |
|--------|--------|----|----|------------|
| SZEINER | 10/25 | 8/25 | 9/25 | **27/75 (36%)** |
| Amanita Design | 23/25 | 19/25 | 19/25 | **61/75 (81%)** |
| Warhorse Studios | 19/25 | 19/25 | 18/25 | **56/75 (75%)** |
| SCS Software | 17/25 | 18/25 | 17/25 | **52/75 (69%)** |
| Supergiant Games | 23/25 | 22/25 | 20/25 | **65/75 (87%)** |

### 5.5 Co konkurence dela lepe

#### Amanita Design
- Vizualni konzistence s hrami (muchomurkova estetika)
- Minimalisticka navigace (5 polozek)
- Funkcni obrazky a lazy loading
- Transparentni GDPR

#### Warhorse Studios
- Dvojjazycnost (CZ/EN)
- Jasne zamereni na jeden ucel (nábor)
- Profesionalni press kit
- Kvalitni fotografie tymu

#### SCS Software
- Kompletni pravni compliance
- Aktivni forum komunita (159k clenu)
- Statistiky na homepage (1.6M FB fans)
- Detailni press materialy

#### Supergiant Games
- Nejlepsi vizualni identita
- Jasne CTA pro kazdou platformu
- Brand konzistence s hrami
- Dedicated GDPR sekce

### 5.6 Co SZEINER muze zlepsit (inspirace)

| Oblast | Inspirace od | Konkretni akce |
|--------|--------------|----------------|
| Hero sekce | Supergiant | Pridat video background + CTA |
| Galerie her | Amanita | Funkcni obrazky s hover efekty |
| Navigace | Amanita | Zjednodusit na 5 polozek |
| Press kit | Warhorse | Vytvorit press.szeiner.com |
| Komunita | SCS Software | Integrace Discord/Forum stats |
| CTA | Supergiant | Tlacitka pro vsechny platformy |
| Legal | SCS Software | Kompletni GDPR dokumentace |

---

## 6. DOPORUCENI PRO REDESIGN

### 6.1 Kriticke opravy (okamzite)

#### Vizualni problemy
1. **Opravit lazy loading obrazku** - aktualne se zobrazuji pouze SVG placeholdery
2. **Nahrat skutecne logo** - aktualne placeholder
3. **Opravit preklepy** - "develompent", "DEDICATION", "Create with"

#### Funkcni problemy
4. **Pridat CTA na homepage** - minimalne 2 tlacitka
5. **Vytvorit kontaktni formular** - nahradit mailto linky
6. **Opravit alt texty** - pristupnost

### 6.2 Krátkodobe zlepseni (1-4 tydny)

#### Design
7. Vytvorit konzistentni icon set
8. Implementovat WebP format pro obrazky
9. Pridat skeleton loadery
10. Zlepsit hover stavy tlacitek

#### UI
11. Zjednodusit navigaci (max 5 polozek)
12. Pridat aktivni stav v menu
13. Redesign hero sekce s video pozadim
14. Pridat Steam widget na homepage

#### UX
15. Zkratit user flows na max 3 kroky
16. Pridat vyhledavani
17. Implementovat scroll-to-top
18. Pridat cookie consent

### 6.3 Strednedoba vylepseni (1-3 mesice)

19. Vytvorit ceskou jazykovou verzi
20. Redesign webhosting sekce s online objednavkou
21. Pridat blog s pravidelnymi aktualizacemi
22. Integrace socialnich siti do paticku
23. Vytvorit press kit stranku
24. Implementovat newsletter signup
25. Pridat testimonials/reviews sekci

### 6.4 Dlouhodobe cile (3-6 mesicu)

26. Kompletni redesign s novou vizualni identitou
27. Vytvorit interaktivni prvky (demo, minihry)
28. Implementovat vice animaci a mikrointerakci
29. A/B testovani konverznich prvku
30. Integrace analytickeho dashboardu

---

## 7. WIREFRAMES - NAVRHY KLICOVYCH STRANEK

### 7.1 Homepage - novy navrh

```
+================================================================+
| [LOGO] [HRY] [SLUZBY] [KOMUNITA] [O NAS]      [CZ/EN] [LOGIN]  |
+================================================================+
|                                                                 |
|                    [VIDEO POZADI - GAMEPLAY]                    |
|                                                                 |
|              # SZEINER GAME STUDIO                              |
|              Ceske nezavisle herni studio od 2017               |
|                                                                 |
|        [NASE HRY]          [PRIPOJ SE NA DISCORD]               |
|                                                                 |
+================================================================+
|                                                                 |
|  ## NASE HRY                                                    |
|                                                                 |
|  +----------------+  +----------------+  +----------------+     |
|  | [AZULGAR IMG]  |  | [CYBERSHIFT]   |  | [NEO CMDR]     |     |
|  |                |  |                |  |                |     |
|  | Azulgar: SC    |  | Cybershift     |  | NEO: Commanders|     |
|  | Sci-Fi Sandbox |  | Arcade Action  |  | Strategy       |     |
|  |                |  |                |  |                |     |
|  | [STEAM] [GOG]  |  | [STEAM]        |  | [STEAM]        |     |
|  +----------------+  +----------------+  +----------------+     |
|                                                                 |
+================================================================+
|                                                                 |
|  ## PROC SZEINER?                                               |
|                                                                 |
|  [IKONA]           [IKONA]           [IKONA]                    |
|  Ceske studio      Aktivni vyvoj     Komunita                   |
|  Od 2017           Pravidelne        5000+ hracu                |
|                    updaty            na Discordu                |
|                                                                 |
+================================================================+
|                                                                 |
|  ## NEJNOVEJSI AKTUALITY                                        |
|                                                                 |
|  +---------------------------+  +---------------------------+   |
|  | [IMG] LEXTOSHOP Launch    |  | [IMG] Azulgar Update 2.0  |   |
|  | 24. dubna 2024            |  | 15. brezna 2024           |   |
|  +---------------------------+  +---------------------------+   |
|                                                                 |
+================================================================+
|                                                                 |
|  ## NAM VERUJI                                                  |
|                                                                 |
|  [REGIOJET]  [HEXPLAY]  [DOKADZ]  [BOSEKA]                      |
|                                                                 |
+================================================================+
|  SZEINER          PRODUKTY        KOMUNITA        PODPORA       |
|  O nas            Hry             Discord         FAQ           |
|  Kariera          LEXTOSHOP       Blog            Kontakt       |
|  Press kit        Webhosting      Twitter         Podpora       |
|                                                                 |
|  [FB] [TW] [DC] [YT] [LI]         Newsletter: [____] [ODEBRAT]  |
|                                                                 |
|  SZEINER s.r.o. | ICO: 05822882 | Zbysov 90, CZ                 |
|  Privacy Policy | Terms | GDPR | Cookies                        |
+================================================================+
```

### 7.2 Stranka hry - novy navrh

```
+================================================================+
| [NAVIGACE]                                                      |
+================================================================+
| Home > Hry > Azulgar: Star Commanders                           |
+================================================================+
|                                                                 |
|  +---------------------------+  +---------------------------+   |
|  |                           |  |                           |   |
|  |     [TRAILER VIDEO]       |  |  # Azulgar: Star          |   |
|  |                           |  |    Commanders             |   |
|  |     [PLAY BUTTON]         |  |                           |   |
|  |                           |  |  Sci-Fi open world        |   |
|  +---------------------------+  |  sandbox hra              |   |
|                                 |                           |   |
|  [SCR1] [SCR2] [SCR3] [SCR4]    |  Cena: 399 Kc / 16.79 EUR|   |
|                                 |                           |   |
|                                 |  [STEAM] [GOG] [EPIC]     |   |
|                                 |                           |   |
|                                 |  Hodnoceni: **** 4.0/5    |   |
|                                 |  Recenzi: 247             |   |
|                                 +---------------------------+   |
|                                                                 |
+================================================================+
|                                                                 |
|  ## O HRE                                                       |
|                                                                 |
|  Azulgar: Star Commanders je Sci-Fi open world sandbox hra...   |
|                                                                 |
|  ### Klicove features                                           |
|  [x] Proceduralne generovany vesmir                             |
|  [x] Stavba lodi a stanic                                       |
|  [x] Multiplayer                                                |
|  [x] Otevreny svet                                              |
|                                                                 |
+================================================================+
|                                                                 |
|  ## SYSTEMOVE POZADAVKY                                         |
|                                                                 |
|  MINIMALNI              DOPORUCENE                              |
|  Windows 7 64bit        Windows 10 64bit                        |
|  Intel i5               Intel i7                                |
|  8 GB RAM               16 GB RAM                               |
|  GTX 670                GTX 1060                                |
|                                                                 |
+================================================================+
|                                                                 |
|  ## GALERIE                                                     |
|                                                                 |
|  [IMG] [IMG] [IMG] [IMG] [IMG] [IMG]                            |
|                                                                 |
+================================================================+
|                                                                 |
|  ## MOHLO BY VAS ZAJIMAT                                        |
|                                                                 |
|  +----------------+  +----------------+                         |
|  | [CYBERSHIFT]   |  | [NEO CMDR]     |                         |
|  +----------------+  +----------------+                         |
|                                                                 |
+================================================================+
| [FOOTER]                                                        |
+================================================================+
```

---

## 8. TECHNICKA SPECIFIKACE PRO IMPLEMENTACI

### 8.1 Doporuceny tech stack

```
Frontend:
- Framework: Next.js 14+ (React)
- Styling: Tailwind CSS
- Animace: Framer Motion
- Ikony: Lucide Icons nebo Heroicons
- State: Zustand nebo React Query

CMS:
- Strapi nebo Contentful (headless)
- Alternativa: WordPress REST API

Hosting:
- Vercel (frontend)
- Vlastni server (backend/CMS)
- CloudFlare (CDN + DDoS)

Analytics:
- Google Analytics 4
- Hotjar (heatmapy)
- Plausible (alternativa)
```

### 8.2 Design tokeny

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

### 8.3 Komponenty k vytvoreni

| Komponenta | Priorita | Slozitost |
|------------|----------|-----------|
| Navbar | Kriticka | Stredni |
| Hero | Kriticka | Vysoka |
| GameCard | Kriticka | Nizka |
| Button | Kriticka | Nizka |
| Footer | Kriticka | Nizka |
| Timeline | Vysoka | Stredni |
| Gallery | Vysoka | Stredni |
| PricingCard | Vysoka | Nizka |
| ContactForm | Vysoka | Stredni |
| CookieConsent | Vysoka | Nizka |
| Newsletter | Stredni | Nizka |
| Testimonial | Stredni | Nizka |
| SearchModal | Stredni | Vysoka |
| LanguageSwitcher | Stredni | Nizka |

---

## 9. ZAVER

### Hlavni zjisteni

Web szeiner.com trpi **zasadnimi designovymi a UX problemy**, ktere negativne ovlivnuji uživatelskou zkusenost a konverzni potencial:

1. **Nefunkcni obrazky** - lazy loading nefunguje spravne
2. **Zadne CTA** - navstevnik nevi, co ma delat
3. **Chybejici formulare** - pouze mailto linky
4. **Preklepy a gramaticke chyby** - neprofesionalni dojem
5. **Slaba vizualni identita** - nekonzistentni s konkurenci

### Prioritni akce

1. **Okamzite:** Opravit obrazky a preklepy
2. **Tento tyden:** Pridat CTA tlacitka a kontaktni formular
3. **Tento mesic:** Redesign homepage a navigace
4. **Tento kvartal:** Kompletni redesign s novou vizualni identitou

### Ocekavany dopad redesignu

| Metrika | Aktualne | Po redesignu |
|---------|----------|--------------|
| Design skore | 10/25 (40%) | 20/25 (80%) |
| UI skore | 8/25 (32%) | 20/25 (80%) |
| UX skore | 9/25 (36%) | 18/25 (72%) |
| Celkove skore | 27/75 (36%) | 58/75 (77%) |
| Bounce rate (odhad) | 70%+ | 40-50% |
| Konverzni pomer | ~0% | 2-3% |

---

*Dokument vytvoren: 6. prosince 2025*
*Pro pouziti s Claude Code pri redesignu webu szeiner.com*
