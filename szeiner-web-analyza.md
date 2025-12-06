# Komplexni audit webu szeiner.com

**Datum analyzy:** 6. prosince 2025  
**Analyzovany web:** https://szeiner.com/  
**Ucel dokumentu:** Podklad pro vytvoreni noveho zadani webu

---

## 1. O spolecnosti SZEINER

### Zakladni informace
- **Nazev:** SZEINER s.r.o.
- **ICO:** 058 22 882
- **Sidlo:** Zbysov 90, Ceska republika
- **Zalozeni:** 2017 (puvodni nazev Lusorion Creatives)
- **Obor:** Vyvoj her pro PC a konzole, webhosting, e-commerce platforma
- **Velikost:** Mala firma (1-10 zamestnancu)

### Produkty a sluzby
- **Hlavni produkt:** Azulgar: Star Commanders (Steam Early Access od 2017)
- **Sluzby:** Webhosting, LIVE Status monitoring system
- **Dalsi projekty:** E-shop platforma (gamevise.com)

---

## 2. Technicky stav webu

### Zabezpeceni
| Parametr | Stav | Poznamka |
|----------|------|----------|
| HTTPS/SSL | Aktivni | Platny certifikat |
| CDN | CloudFlare | DDoS ochrana |
| Security headers | Neovereno | Doporuceno otestovat |

### Vykon a rychlost
| Parametr | Stav | Doporuceni |
|----------|------|------------|
| Lazy loading | Implementovan | SVG placeholdery - castecne problemy |
| Core Web Vitals | Nemereno | Spustit PageSpeed Insights |
| LCP cil | < 2.5s | Overit |
| CLS cil | < 0.1 | Overit |

### Responzivita
- Responzivni design: ANO
- Mobilni zobrazeni: Funkcni
- Tablet zobrazeni: Funkcni

### Indexace
- Pocet indexovanych stranek: 15-20
- Robots.txt: Neovereno
- Sitemap.xml: Neovereno
- Google Search Console: Doporuceno nastavit

### Monitoring
- Status stranka: status.szeiner.com
- Sledovani dostupnosti: Aktivni

---

## 3. SEO Analyza

### KRITICKE PROBLEMY

#### 3.1 Preklep na hlavni strance
```
CHYBA: "develompent" misto "development"
LOKACE: Hlavni popis firmy na homepage
DOPAD: Viditelne ve vysledcich Google, poskozuje profesionalitu
PRIORITA: OKAMZITA OPRAVA
```

#### 3.2 Title tagy
| Stranka | Aktualni title | Problem |
|---------|----------------|---------|
| Homepage | "Home - SZEINER Software Company" | Zadna klicova slova |
| About | "ABOUT US - SZEINER Software Company" | Genericke |
| Webhosting | "Webhosting - SZEINER Software Company" | Chybi USP |

**Doporuceni pro nove title tagy:**
- Homepage: "SZEINER - Ceske herni studio | Vyvoj her pro PC a konzole"
- About: "O nas | SZEINER - Nezavisly vyvojar her z Ceske republiky"
- Webhosting: "Webhosting pro hrace a vyvojare | SZEINER"

#### 3.3 Meta descriptions
- Stav: Chybi nebo slabe na vetsite stranek
- Doporucena delka: 150-160 znaku
- Obsah: Unikatni popis s CTA pro kazdou stranku

#### 3.4 Struktura nadpisu
| Problem | Popis |
|---------|-------|
| H1 | "Life is a Game..." - zadna SEO hodnota |
| H2-H6 | Nekonzistentni hierarchie |

**Doporuceni:**
- H1: Jeden na stranku, obsahuje hlavni klicove slovo
- H2: Sekce stranky
- H3+: Podsekce

#### 3.5 Alt texty obrazku
- Stav: CHYBI
- Lazy loading placeholdery bez popisku
- Dopad: Ztrata obrazkoveho SEO, pristupnost

### Klicova slova - analyza

#### Cilena klicova slova (doporucena)
| Klicove slovo | Mesicni hledanost (CZ) | Konkurence |
|---------------|------------------------|------------|
| ceske herni studio | 50-100 | Nizka |
| vyvoj her ceska republika | 20-50 | Nizka |
| indie game developer czech | 10-30 | Nizka |
| game development company | 200-500 | Vysoka |
| webhosting pro hry | 10-30 | Stredni |

#### Aktualni pozice
- Pro vsechna relevantni klicova slova: MIMO TOP 50

### Zpetne odkazy (Backlinks)
| Zdroj | Typ |
|-------|-----|
| Steam | Produktova stranka |
| LinkedIn | Firemni profil |
| IndieDB | Vyvojarska stranka |
| Business directories | Katalogy firem |

**CHYBI:**
- Games.cz
- Bonusweb.cz
- GDACZ (Asociace ceskych hernich vyvojaru)
- Ceska herni media

### SEO Skore: 3.4/10

---

## 4. Uzivatelska zkusenost (UX)

### Navigace
| Prvek | Stav | Hodnoceni |
|-------|------|-----------|
| Hlavni menu | Dropdown (Products, Services, Community, Company) | OK |
| Pocet kliknuti k cili | 1-2 | OK |
| Breadcrumbs | Funkcni | OK |
| Mobile menu | Hamburger | OK |

### KRITICKE UX PROBLEMY

#### 4.1 Chybejici CTA (Call-to-Action)
```
PROBLEM: Navstevnik nevi, co ma delat
LOKACE: Homepage
CHYBI:
- Tlacitko "Koupit hru"
- Tlacitko "Hrat demo"
- Tlacitko "Prohlednout portfolio"
```

#### 4.2 Chybejici prvky
| Prvek | Stav | Priorita |
|-------|------|----------|
| Vyhledavani na webu | CHYBI | Vysoka |
| Newsletter prihlaseni | CHYBI | Stredni |
| Steam widget | CHYBI | Vysoka |
| Video trailer na homepage | CHYBI | Vysoka |
| Kontaktni formular | CHYBI | Kriticka |
| Live chat | CHYBI | Nizka |

#### 4.3 Jazykove problemy
- Gramaticke chyby v anglickem textu
- Mix cestiny a anglictiny bez prepinace jazyku
- Chybi ceska verze webu

#### 4.4 Komunita
- Blog: "0 Comments" u vsech clanku
- Zadna komunitni aktivita
- Chybi socialni proof

### Webhosting sekce
- Objednavka: Pouze email (info@szeiner.com)
- CHYBI: Online objednavkovy formular
- CHYBI: Cenik
- CHYBI: Specifikace balicku

### Design
- Styl: Tmavy, herni tematika
- Hodnoceni: Odpovida oboru
- Problem: Vizualni obsah se nenacita spravne

### UX Skore: 4.6/10

---

## 5. Konkurencni analyza

### Cesky herni trh - hlavni hraci

| Studio | Zamestnanci | Hlavni tituly | Rocni obrat |
|--------|-------------|---------------|-------------|
| Bohemia Interactive | 400+ | Arma, DayZ | 50M+ EUR |
| Warhorse Studios | 250+ | Kingdom Come: Deliverance | 30M+ EUR |
| SCS Software | 100+ | Euro Truck Simulator 2 | 20M+ EUR |
| Amanita Design | 25+ | Machinarium, Samorost | 5M+ EUR |

### Azulgar: Star Commanders - Steam analyza
| Metrika | Hodnota |
|---------|---------|
| Hodnoceni | 55% (Mixed) |
| Pocet recenzi | 40 |
| Prumerna doba hrani | 12 minut |
| Stav | Early Access (od 2017) |

**Kritika hracu:**
- Problematicke ovladani
- Nedokoncene mechaniky
- Prilis dlouha Early Access faze

### Trzni prilezitosti
| Prilezitost | CAGR | Poznamka |
|-------------|------|----------|
| Indie herni trh | 14.5% | $4.85B (2025) -> $9.55B (2030) |
| Simulace a sandbox | 17.2% | Nejrychleji rostouci zanr |
| Mobilni platformy | - | 52% prijmu indie her |
| Ceske statni dotace | - | Dostupne od 2014 |

### Konkurencni vyhody SZEINER
1. Mala, flexibilni struktura
2. Zkusenosti s vyvoje (od 2017)
3. Vlastni infrastruktura (webhosting)
4. Nizke provozni naklady

### Konkurencni nevyhody
1. Maly tym
2. Omezeny marketingovy rozpocet
3. Slaba online prezentace
4. Nedokonceny hlavni produkt

---

## 6. Pravni nalezitosti

### KRITICKE PRAVNI PROBLEMY

#### 6.1 Cookie souhlas
```
STAV: ZCELA CHYBI
RIZIKO: Pokuta az 10 mil. EUR nebo 2% rocniho obratu
POVINNOST: Od 1.1.2022 (ePrivacy smernice)
RESENI: Implementovat cookie listu s granularnim souhlasem
```

#### 6.2 Obchodni podminky
```
STAV: NEEXISTUJI (pro webhosting)
RIZIKO: Pokuta COI az 5 mil. Kc
POVINNOST: Pro kazdy e-commerce prodej
```

### GDPR Dokumentace
| Dokument | Stav | Problem |
|----------|------|---------|
| Privacy Policy | EXISTUJE | Zastarale (4.10.2018) |
| GDPR stranka | EXISTUJE | Neuplna prava subjektu |
| Cookie Policy | CHYBI | Kriticke |

### Chybejici pravni informace
- Pravo na pristup (cl. 15 GDPR)
- Pravo na omezeni zpracovani
- Pravo podat stiznost u UOOU
- ADR informace (odkaz na COI/ODR)
- Reklamacni rad

### Jazykova verze dokumentu
- Aktualni: Pouze anglictina
- Problem: Cesti spotrebitele maji pravo na informace v cestine

---

## 7. Akcni plan implementace

### FAZE 1: Kriticke opravy (1-7 dni)

| Ukol | Priorita | Casova narocnost |
|------|----------|------------------|
| Opravit preklep "develompent" | KRITICKA | 5 minut |
| Implementovat cookie listu | KRITICKA | 2-4 hodiny |
| Pridat kontaktni formular | KRITICKA | 2-3 hodiny |
| Vytvorit obchodni podminky | KRITICKA | 4-8 hodin |
| Pridat primarni CTA na homepage | VYSOKA | 1-2 hodiny |

### FAZE 2: SEO zaklad (1-4 tydny)

| Ukol | Priorita | Casova narocnost |
|------|----------|------------------|
| Prepsat title tagy | VYSOKA | 2-3 hodiny |
| Vytvorit meta descriptions | VYSOKA | 3-4 hodiny |
| Opravit H1-H6 strukturu | VYSOKA | 2-3 hodiny |
| Pridat alt texty ke vsem obrazkum | VYSOKA | 4-6 hodin |
| Vytvorit sitemap.xml | STREDNI | 1 hodina |
| Optimalizovat robots.txt | STREDNI | 30 minut |
| Nastavit Google Search Console | STREDNI | 1 hodina |

### FAZE 3: UX vylepseni (1-2 mesice)

| Ukol | Priorita | Casova narocnost |
|------|----------|------------------|
| Pridat Steam widget | VYSOKA | 2-3 hodiny |
| Pridat video trailery | VYSOKA | 4-6 hodin |
| Vytvorit ceskou verzi | VYSOKA | 2-3 dny |
| Implementovat vyhledavani | STREDNI | 4-8 hodin |
| Pridat newsletter signup | STREDNI | 2-3 hodiny |
| Prepracovat webhosting sekci | STREDNI | 1 den |

### FAZE 4: Dlouhodobe cile (3-6 mesicu)

| Ukol | Priorita |
|------|----------|
| Stat se clenem GDACZ | VYSOKA |
| PR kampan v ceskych hernich mediich | VYSOKA |
| Aktivni blog s aktualizacemi vyvoje | STREDNI |
| Zlepsit hodnoceni Azulgar na Steamu | VYSOKA |
| Budovat zpetne odkazy | STREDNI |

---

## 8. Technicke specifikace pro novy web

### Doporucena architektura
```
Frontend: React/Next.js nebo Vue/Nuxt
Styling: Tailwind CSS
CMS: Headless (Strapi, Contentful)
Hosting: Vercel/Netlify + vlastni backend
CDN: CloudFlare (zachovat)
Analytics: Google Analytics 4 + Hotjar
```

### Povinne stranky
1. **Homepage** - hero sekce s CTA, featured produkty, aktuality
2. **Hry/Produkty** - portfolio s detaily, Steam integrace
3. **O nas** - pribeh firmy, tym, hodnoty
4. **Sluzby** - webhosting s cenikem a objednavkou
5. **Blog/Novinky** - aktualizace vyvoje, herni novinky
6. **Kariera** - volne pozice, firemni kultura
7. **Kontakt** - formular, mapa, kontaktni udaje
8. **Pravni** - GDPR, Privacy Policy, Obchodni podminky, Cookies

### Jazykove verze
- Cestina (primarni pro CZ trh)
- Anglictina (pro mezinarodni publikum)
- Prepinac jazyku v hlavicce

### SEO checklist pro novy web
- [ ] Unikatni title tag na kazde strance (50-60 znaku)
- [ ] Unikatni meta description (150-160 znaku)
- [ ] Jeden H1 na stranku s klicovym slovem
- [ ] Strukturovana data (Schema.org - Organization, Product, BreadcrumbList)
- [ ] Alt texty u vsech obrazku
- [ ] Sitemap.xml
- [ ] Robots.txt
- [ ] Kanonizace URL
- [ ] HTTPS presmerovani
- [ ] Mobile-first design

### Pravni checklist
- [ ] Cookie lista s granularnim souhlasem
- [ ] Cookie policy
- [ ] Privacy policy (GDPR compliant, CZ i EN)
- [ ] Obchodni podminky
- [ ] Reklamacni rad
- [ ] Informace o ADR (odkaz na COI)
- [ ] Identifikace prodavajiciho (ICO, sidlo, kontakt)

### Performance cile
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1
- PageSpeed skore: > 90 (mobile i desktop)
- TTFB: < 600ms

---

## 9. Metriky pro sledovani uspechu

### KPIs po redesignu
| Metrika | Aktualni | Cil (6 mesicu) |
|---------|----------|----------------|
| Organicky traffic | Nemereno | +200% |
| Bounce rate | Nemereno | < 50% |
| Prumerna doba na webu | Nemereno | > 2 minuty |
| Konverzni pomer (CTA klik) | 0% | > 3% |
| PageSpeed mobile | Nemereno | > 90 |
| Indexovane stranky | 15-20 | 30+ |

### Nastroje pro mereni
- Google Analytics 4
- Google Search Console
- Hotjar (heatmapy, recordings)
- Ahrefs/SEMrush (SEO monitoring)
- PageSpeed Insights
- GTmetrix

---

## 10. Zaver a doporuceni

### Shrnuti hlavnich problemu
1. **SEO:** Kriticke nedostatky (preklep, chybejici meta data)
2. **UX:** Zadne CTA, chybejici konverzni prvky
3. **Pravni:** Chybi cookie souhlas, obchodni podminky
4. **Konkurence:** Mala firma proti velkym studiim

### Doporuceny pristup
Web vyzaduje kompletni redesign se zamerenim na:
1. Profesionalni prezentaci portfolia
2. Jasne konverzni cesty
3. Plnou pravni compliance
4. SEO-first pristup
5. Dvojjazycnost (CZ/EN)

### Ocekavany ROI
Pri spravne implementaci lze ocekavat:
- 3x narust organickeho trafficu do 6 mesicu
- Zlepseni konverzniho pomeru o 200-300%
- Vyssi duveryhodnost u potencialnich partneru
- Compliance s pravnimi predpisy (eliminace rizika pokut)

---

*Dokument vytvoren: 6. prosince 2025*  
*Pro pouziti s Claude Code pri tvorbe noveho zadani webu*
