# Webová prezentace herních studií: komplexní analýza a best practices

**Analýza webů pěti indie/středních herních studií odhaluje významné rozdíly v přístupu k digitální prezentaci.** Nejlépe si vedou SCS Software a Supergiant Games s profesionálním designem a solidní GDPR compliance, zatímco Team Cherry a částečně Warhorse Studios mají mezery v právních náležitostech. Všechna studia spoléhají na sílu svých her namísto agresivního SEO, což je pro herní průmysl typické, ale ne optimální.

---

## 1. Amanita Design — minimalistický přístup s českou duší

**URL:** https://amanita-design.net/  
**Založení:** 2003 | **Sídlo:** Brno, ČR | **Velikost:** ~10-15 lidí (několik menších týmů)  
**Známé hry:** Machinarium, Samorost série, Botanicula, Creaks, Chuchel

### Technický stav

Studio využívá **Cloudflare CDN** s aktivním Rocket Loaderem pro optimalizaci JavaScriptu, což zajišťuje solidní rychlost načítání globálně. Web běží na **HTTPS** s platným certifikátem. Struktura URL je čistá a sémantická (`/games/machinarium.html`), byť použití přípony `.html` je mírně zastaralé. Navigace zahrnuje pouze **5 položek** (Home, About, Games, Merch, Contact), což je ideální pro přehlednost.

### SEO hodnocení

Title tag hlavní stránky je problematicky krátký — obsahuje pouze „Amanita Design" bez jakýchkoli klíčových slov typu „indie games" nebo „adventure games". Meta description existuje, ale není dostatečně optimalizovaná. Struktura nadpisů je logická (H1 pro logo, H2 pro sekce, H3 pro podsekce). **Backlink profil je silný** díky organickým zmínkám z Wikipedie, Steam, GOG, herních médií a prestižních ocenění z IGF (Independent Games Festival).

### UX a design

Vizuální identita webu je **výjimečně konzistentní** s uměleckým stylem her studia. Logo využívá stylizovanou muchomůrku (Amanita muscaria), což odkazuje na psychedelickou estetiku her. CTA prvky jsou však slabé — chybí výrazná tlačítka „Buy Now" nebo přímé odkazy na nákupní platformy v hlavní navigaci. Merch store běží na samostatné subdoméně přes Shopify.

### Právní náležitosti

Privacy Policy je **kompletní a transparentní**. Klíčový bod: „We do not collect, process or store any personal data from any of our games on any platform." Web obsahuje odkaz na cookie preferences v patičce. GDPR compliance je splněno včetně uvedení Data Privacy Officera (Tomáš Dvořák) a kontaktního emailu privacy@amanita-design.net.

### Co se od nich naučit
- Minimalistická navigace s jasnou hierarchií
- Vizuální konzistence mezi webem a produkty
- Transparentní přístup k ochraně dat v herách

---

## 2. Warhorse Studios — korporátní přístup s bezpečnostní mezerou

**URL:** https://warhorsestudios.cz/  
**Založení:** 2011 | **Sídlo:** Praha, ČR | **Velikost:** 250+ zaměstnanců  
**Známé hry:** Kingdom Come: Deliverance (6+ mil. kopií), Kingdom Come: Deliverance II (2025)

### Technický stav

Hlavní doména používá **HTTPS**, ale kritický problém představuje **nevalidní SSL certifikát** na subdoméně forum.warhorsestudios.cz (certificate mismatch). Toto je bezpečnostní riziko, které může odradit uživatele a negativně ovlivnit důvěryhodnost. Technologický stack zahrnuje Google Tag Manager, Google Universal Analytics a Embedly. Struktura URL je čistá (`/about/`, `/career/`, `/our-games/`).

### SEO hodnocení

Title tagy jsou generické — „Warhorse Studios - Warhorse" postrádá klíčová slova jako „Kingdom Come" nebo „Czech game developer". Obsah je minimalistický, zaměřený primárně na recruitment. Silnou stránkou je **dvojjazyčná verze** (CZ/EN) a profesionální prezentace klíčových osobností (Daniel Vávra, Martin Klíma). Backlink profil je robustní díky mediální pozornosti kolem Kingdom Come.

### UX a design

Navigace obsahuje 5 položek s jasným zaměřením na nábor zaměstnanců. Hlavní CTA je „Přidejte se" směřující na kariérní sekci. Design je profesionální s tmavým pozadím a kontrastními prvky. Press materiály jsou dostupné na dedikované subdoméně press.warhorsestudios.cz.

### Právní náležitosti

**Problematická oblast.** Privacy Policy není viditelně odkazována v patičce hlavního webu. Cookie consent mechanismus nebylo možné ověřit. Fórum má vlastní Privacy Policy, která je však nedostupná kvůli SSL chybě. Pro studio vlastněné PLAION (Koch Media) je toto překvapivá nedostatečnost.

### Co se od nich naučit
- Jasné zaměření webu na primární účel (recruitment)
- Profesionální press kit na dedikované subdoméně
- Dvojjazyčná prezentace pro mezinárodní publikum

---

## 3. SCS Software — nejkompletnější právní compliance

**URL:** https://www.scssoft.com/  
**Založení:** 1997 | **Sídlo:** Praha, ČR | **Velikost:** 51-200 zaměstnanců  
**Známé hry:** Euro Truck Simulator 2 (22+ mil. kopií), American Truck Simulator (6+ mil. kopií)

### Technický stav

Web běží na **Nginx serveru** s PHP backendem, využívá jQuery a Modernizr. HTTPS je aktivní s platným certifikátem. Struktura URL je exemplární — krátká, sémantická, bez parametrů (`/about`, `/projects`, `/technology`). Blog běží externě na Blogger platformě (blog.scssoft.com), což není ideální pro SEO konsolidaci.

### SEO hodnocení

Title tag hlavní stránky je dobře optimalizovaný: „SCS Software - Simulation games development since 1997" — obsahuje klíčové slovo, brand i historii. Chybí však viditelný H1 nadpis v textu (pouze v logu). Obsah je kvalitní s osobními příběhy zaměstnanců a testimonials od hráčů. Web uvádí statistiky sociálních sítí: **1.6M Facebook fans, 261k Twitter followers, 445k YouTube subscribers**.

### UX a design

Navigace je přehledná se 6 položkami v hlavním menu a 4 položkami v patičce. CTA prvky jsou přítomny („View all projects", „Join the team"), ale mohly by být vizuálně výraznější. Design je profesionální s kvalitními obrázky kamionů a herních scén. Patička obsahuje detailní **licenční informace** k truck značkám (Mercedes-Benz, Volvo, MAN, Freightliner).

### Právní náležitosti

**Nejlepší v této analýze.** Privacy Policy je kompletní a strukturovaná podle GDPR:
- Identifikace správce dat s IČO
- Odkaz na Nařízení EU 2016/679
- Kategorie zpracovávaných dat a účely
- Práva subjektů údajů (přístup, oprava, výmaz, přenositelnost)
- Detailní informace o cookies včetně návodu na správu v prohlížečích
- **Whistleblowing stránka** pro interní oznamování

### Co se od nich naučit
- Kompletní GDPR compliance jako vzor pro ostatní
- Detailní press kit s fakty a čísly pro média
- Aktivní komunitní fórum (159k členů) jako engagement nástroj

---

## 4. Supergiant Games — vzorový design a brand identity

**URL:** https://www.supergiantgames.com/  
**Založení:** 2009 | **Sídlo:** San Francisco, USA | **Velikost:** 18-20 zaměstnanců  
**Známé hry:** Bastion, Transistor, Hades (Game of the Year), Hades II

### Technický stav

Web je postaven jako **JavaScript Single Page Application** s CMS Contentful. Obrázky jsou servírovány přes CDN (images.ctfassets.net) s lazy loadingem a kvalitativní optimalizací (?w=285&q=50). HTTPS je aktivní. Upozornění „This app works best with JavaScript enabled" indikuje závislost na JS, což může ovlivnit SEO crawlování a přístupnost.

### SEO hodnocení

Title tag je kreativní: „Supergiant Games is a small developer with big ambitions" — komunikuje hodnoty studia, ale postrádá explicitní klíčová slova. Struktura nadpisů je správná s jedním H1 na stránku. URL jsou čisté (`/games/hades-ii`, `/blog/`, `/team/`). Store subdoména má přes **52,800 Google backlinků**, což svědčí o silné autoritě domény.

### UX a design

Vizuální identita je **bezkonkurenčně nejsilnější** v této analýze. Barevné schéma vychází z her (tmavé pozadí s červenými/oranžovými akcenty Hades). Logo je stylizované „SG" v červené. Navigace má 11 položek, což je na hranici přehlednosti, ale logické uspořádání (hry chronologicky od nejnovější) to kompenzuje. CTA prvky jsou jasné — každá hra má tlačítka pro všechny platformy (Steam, Nintendo, PlayStation, Xbox, Epic, Mac).

### Právní náležitosti

Privacy Policy je komplexní s dedikovanou sekcí „Your European Privacy Rights" pro GDPR. Obsahuje certifikaci EU-US Privacy Shield Framework. Poslední aktualizace je však z **prosince 2018**, což je zastaralé. Cookie banner nebyl jednoznačně identifikován, což je riziko pro EU návštěvníky.

### Co se od nich naučit
- Výjimečná vizuální konzistence s brand identity her
- Jasné CTA pro každou platformu u každé hry
- Dedikovaná GDPR sekce pro evropské uživatele

---

## 5. Team Cherry — úspěšný minimalismu s právními mezerami

**URL:** https://www.teamcherry.com.au/  
**Založení:** 2014 | **Sídlo:** Adelaide, Austrálie | **Velikost:** ~3 hlavní členové  
**Známé hry:** Hollow Knight ($195+ mil. tržeb), Hollow Knight: Silksong (2025)

### Technický stav

Web běží na **Squarespace** s Cloudflare CDN, což zajišťuje rychlost a stabilitu bez nutnosti vlastní infrastruktury. HTTPS je aktivní. Struktura URL je čistá díky Squarespace defaults (`/about`, `/games`, `/faq`, `/blog/[slug]`). Obrázky jsou servírovány přes Squarespace CDN.

### SEO hodnocení

Title tagy jsou **velmi slabé** — pouze „Team Cherry" nebo „Games — Team Cherry" bez jakýchkoli klíčových slov. Meta descriptions pravděpodobně chybí. Struktura nadpisů je nekonzistentní (H4 místo H3 pro jména členů). Blog slouží primárně pro patch notes a oznámení, ne pro SEO obsah. Přesto má web silný organický traffic díky kultovní popularitě Hollow Knight.

### UX a design

Navigace je minimalistická (Blog, Games, Merchandise, About + patička s FAQ a Contact). Design je konzistentní s tmavou estetikou Hollow Knight. CTA prvky existují, ale nejsou vizuálně výrazné. Merchandise je integrován přímo na webu (Squarespace Online Stores). Chybí vyhledávání na blogu.

### Právní náležitosti

**Nejslabší v této analýze.** Cookie consent banner nebyl nalezen — významné riziko pro GDPR compliance. Privacy Policy je umístěna v FAQ (ne na samostatné stránce) a je velmi stručná:

> „Team Cherry does not collect or store any player data through any of its software."

Chybí informace o právech uživatelů dle GDPR, kontakt na DPO, a řešení cookies Squarespace platformy.

### Co se od nich naučit
- Efektivní využití platformy jako Squarespace pro malé týmy
- Jasná pravidla pro fanouškovský obsah (community guidelines)
- Blog jako primární komunikační kanál s komunitou

---

## Srovnávací tabulka všech analyzovaných studií

| Kritérium | Amanita Design | Warhorse Studios | SCS Software | Supergiant Games | Team Cherry |
|-----------|----------------|------------------|--------------|------------------|-------------|
| **Velikost týmu** | ~15 | 250+ | 100-200 | ~20 | ~3 |
| **HTTPS** | ✅ | ⚠️ (forum SSL chyba) | ✅ | ✅ | ✅ |
| **Čisté URL** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Title tag optimalizace** | ❌ | ❌ | ✅ | ⚠️ | ❌ |
| **Meta descriptions** | ⚠️ | ❌ | ⚠️ | ⚠️ | ❌ |
| **Struktura nadpisů** | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| **Cookie consent** | ✅ | ⚠️ | ✅ | ⚠️ | ❌ |
| **Privacy Policy** | ✅ Kompletní | ⚠️ Nejasná | ✅ Kompletní | ✅ (zastaralá) | ❌ Základní |
| **GDPR compliance** | ✅ | ⚠️ | ✅ | ✅ | ❌ |
| **Dvojjazyčnost** | ❌ | ✅ CZ/EN | ❌ | ❌ | ❌ |
| **Design kvalita** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **CTA efektivita** | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| **Blog/novinky** | ❌ | ❌ | ✅ (externí) | ✅ | ✅ |
| **Press kit** | ⚠️ | ✅ Dedikovaná subdoména | ✅ | ⚠️ | ✅ |
| **Celkové skóre** | 7.5/10 | 6.5/10 | 8.5/10 | 8/10 | 6/10 |

---

## Identifikované best practices pro web herního studia

### Technické minimum
- **HTTPS je povinnost** — všechna analyzovaná studia ho mají, ale pozor na subdomény (příklad Warhorse)
- **Čisté URL bez parametrů** — `/games/nazev-hry` namísto `/games.php?id=123`
- **CDN pro globální rychlost** — Cloudflare používají 3 z 5 studií
- **Responzivní design** — všechna studia mají mobilní verzi

### SEO essentials
- **Title tag s klíčovými slovy** — SCS Software ukazuje správný přístup: „[Brand] - [Klíčové slovo] since [Rok]"
- **Meta descriptions pro každou stránku** — většina studií toto podceňuje
- **Jeden H1 na stránku** — Supergiant Games to dělá správně
- **Blog pro čerstvý obsah** — Team Cherry a SCS Software udržují aktivní blogy

### UX a design
- **Maximálně 5-7 položek v hlavní navigaci** — Amanita Design (5), SCS Software (6)
- **Jasné CTA pro nákup her** — Supergiant Games má tlačítka pro všechny platformy
- **Vizuální konzistence s brand identity her** — Supergiant Games je vzorem
- **Press kit na dedikované stránce/subdoméně** — Warhorse Studios best practice

### Právní compliance
- **Cookie consent banner je povinný pro EU** — SCS Software a Amanita Design to mají
- **Kompletní Privacy Policy** — SCS Software jako vzor s IČO, účely, právy uživatelů
- **GDPR sekce pro evropské návštěvníky** — Supergiant Games
- **Kontakt na DPO** — Amanita Design uvádí konkrétní osobu a email

---

## Hlavní mezery na trhu a příležitosti

Analýza odhalila několik oblastí, kde lze překonat konkurenci:

1. **SEO optimalizace je všeobecně podceňovaná** — studia spoléhají na brand awareness namísto organického vyhledávání. Kvalitní SEO může přinést významnou konkurenční výhodu.

2. **Strukturovaná data (Schema.org) nikdo nepoužívá** — implementace VideoGame schema může zlepšit zobrazení ve vyhledávačích.

3. **Interaktivní prvky chybí** — žádné studio nemá interaktivní demo, trailer player nebo behind-the-scenes obsah přímo na webu.

4. **Newsletter integrace je slabá** — pouze Supergiant Games má prominentní „Join" sekci.

5. **Lokalizace webů** — pouze Warhorse má CZ/EN verzi, přestože všechna česká studia prodávají globálně.

Tyto zjištění poskytují jasný roadmap pro vytvoření konkurenceschopného webu herního studia, který překoná analyzovanou konkurenci v klíčových oblastech.