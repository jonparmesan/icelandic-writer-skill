---
name: icelandic-writer
description: |
  Write in Icelandic at an advanced level with correct grammar, natural style,
  and proper conventions. Covers case system, verb conjugation, noun/adjective
  declension, word order (V2), pronouns, spelling, idioms, and common pitfalls.
  Use when writing, translating to, or reviewing Icelandic text.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Icelandic Writer: Advanced Grammar & Style Reference

You are an expert Icelandic writer. When asked to write, translate, or review Icelandic text, use this reference to produce grammatically correct, natural-sounding prose.

## Your Task

When given text to write, translate, edit, or review in Icelandic:

1. **Get the grammar right** — Cases, agreement, verb forms, word order
2. **Sound natural** — Use proper register, avoid anglicisms, use indigenous vocabulary
3. **Avoid common errors** — Dative sickness, indicative encroachment, new passive
4. **Match the register** — Formal/academic vs. informal/conversational
5. **Use idioms where appropriate** — Natural Icelandic expression, not word-for-word translation

### MANDATORY: GreynirCorrect Verification Loop

**You MUST run GreynirCorrect BEFORE presenting any Icelandic text to the user.** This is not optional. Follow this loop:

```
1. Write/edit the Icelandic text → save to /tmp/icelandic_check.txt
2. Run GreynirCorrect on the file (see SPELL & GRAMMAR VERIFICATION section)
3. If real errors found → fix them in the text → go back to step 1
4. Repeat until GreynirCorrect returns no real errors (only ignorable false positives)
5. ONLY THEN present the text to the user
```

**Never skip this loop.** Even for small edits, single sentences, or reviews — always verify with GreynirCorrect first. If you rewrite anything to fix an error, you must re-run GreynirCorrect on the updated text to confirm you didn't introduce new errors.

---

## THE CASE SYSTEM (Fallkerfi)

Icelandic has four cases that govern nouns, pronouns, adjectives, and numerals. Case is determined by syntactic role, governing verbs, or prepositions.

### Case Functions

| Case | Icelandic Name | Primary Function | Example |
|------|---------------|-----------------|---------|
| Nominative | Nefnifall | Subject, dictionary form | Það er **hestur** (That is a horse) |
| Accusative | Þolfall | Direct object | Ég borða **fisk** (I eat fish) |
| Dative | Þágufall | Indirect object, verbs of helping/communication | Þú hjálpar **hesti** (You help a horse) |
| Genitive | Eignarfall | Possession, formal registers, certain verbs | Þeir sakna **dags** (They miss a day) |

### Preposition + Case Government

| Case | Prepositions |
|------|-------------|
| Accusative | um (about), gegnum (through), kringum (around) |
| Dative | frá (from), af (of/off), með (with), úr (out of) |
| Genitive | til (to), vegna (because of), án (without), milli (between) |

### Quirky (Non-Nominative) Subjects

Icelandic uniquely allows oblique-case subjects:

- **Accusative subjects**: Mig langar (I want) — NOT *Mér langar (dative sickness error)
- **Dative subjects**: Mér finnst (I think/feel), Mér líkar (I like)
- **Genitive subjects**: Rare, mostly archaic

---

## NOUN DECLENSION (Nafnorð)

### Finding the Stem

Remove the nominative singular ending (-ur, -r, -i, -a, -Ø) to find the stem. Double consonants: remove the second (e.g., steinn → stein-).

### Strong Noun Paradigms

| Case | Masc. (hattur) | Fem. (borg) | Neut. (glas) |
|------|---------------|-------------|-------------|
| Nom. Sg. | hattur | borg | glas |
| Acc. Sg. | hatt | borg | glas |
| Dat. Sg. | hatti | borg | glasi |
| Gen. Sg. | hatts | borgar | glass |
| Nom. Pl. | hattar | borgir | glös |
| Acc. Pl. | hatta | borgir | glös |
| Dat. Pl. | höttum | borgum | glösum |
| Gen. Pl. | hatta | borga | glasa |

### Weak Noun Paradigms

| Case | Masc. (banki) | Fem. (gata) | Neut. (auga) |
|------|--------------|-------------|-------------|
| Nom. Sg. | banki | gata | auga |
| Acc. Sg. | banka | götu | auga |
| Dat. Sg. | banka | götu | auga |
| Gen. Sg. | banka | götu | auga |
| Nom. Pl. | bankar | götur | augu |
| Acc. Pl. | banka | götur | augu |
| Dat. Pl. | bönkum | götum | augum |
| Gen. Pl. | banka | gatna | augna |

### A-Mutation (u-umlaut)

Stem 'a' → 'ö' when 'u' appears in the following syllable. Most visible in dative plural:
- hattur → höttum
- banki → bönkum
- glas → glösum

The diphthong 'au' does NOT undergo a-mutation.

---

## THE DEFINITE ARTICLE (Ákveðinn greinir)

Icelandic has NO separate word for "the" — definiteness is expressed by a suffix on the noun.

### Suffixed Article (Nominative Singular)

| Gender | Suffix | Example |
|--------|--------|---------|
| Masculine | -inn | hestur → hesturinn |
| Feminine | -in / -an | borg → borgin, peysa → peysan |
| Neuter | -ið / -að | ár → árið, auga → augað |

### Adjective Interaction

The definite article triggers **weak adjective declension**:

- **Indefinite (strong adj.)**: íslenskur hestur (an Icelandic horse)
- **Definite (weak adj.)**: íslenski hesturinn (the Icelandic horse)

Weak adjectives are more regular and typically end in -a or -i. Strong adjectives undergo full case declension.

---

## VERB SYSTEM (Sagnorð)

### Verb Classes

| Class | Formation | Present | Past | Example |
|-------|-----------|---------|------|---------|
| -a verbs (Weak 1) | Most productive, used for loanwords | ég tala | ég talaði | tala (speak) |
| -i verbs (Weak 2) | Dental suffix in past (-ði/-di/-ti) | ég geri | ég gerði | gera (do) |
| Strong verbs | Ablaut (vowel shift), no ending | ég fer | ég fór | fara (go) |
| -ur verbs (Mixed) | Stem e/y, dental + vowel shift | ég tel | ég taldi | telja (count) |
| Hybrid verbs | Mixed strong/weak traits | — | — | hafa, segja |
| Preterite-present | Old past forms = present | ég á | ég átti | eiga (own/must) |

### Indicative Conjugation — Weak Class 1 (spila)

| Person | Present | Past |
|--------|---------|------|
| ég | spila | spilaði |
| þú | spilar | spilaðir |
| hann/hún/það | spilar | spilaði |
| við | spilum | spiluðum |
| þið | spilið | spiluðuð |
| þeir/þær/þau | spila | spiluðu |

### Vera (to be) — Indicative Present

| Person | Form |
|--------|------|
| ég | er |
| þú | ert |
| hann/hún/það | er |
| við | erum |
| þið | eruð |
| þeir/þær/þau | eru |

### Subjunctive Mood (Viðtengingarháttur)

Used for wishes, hopes, uncertainty, politeness, counterfactuals.

- **Present subjunctive**: Hún vonar að þið komið (She hopes you come)
- **Past subjunctive**: Uncertainty, counterfactuals, formal politeness
  - sé (pres. subj. of vera) vs. væri (past subj.)

### Middle Voice (-st verbs)

Formed by adding -st (from reflexive pronoun sik). Three main uses:

| Type | Meaning | Example |
|------|---------|---------|
| Anticausative | Transitive → intransitive | splundra → splundrast (shatter itself) |
| Reciprocal | Mutual action | Við hittumst (We meet each other) |
| Deponent | Only exists in middle voice | óttast (to fear) |

### Auxiliary Verb Order (CIAO)

Modal > Perfect hafa > Progressive vera > Passive vera

- **hafa**: Perfect tense (hefur barið — has hit)
- **vera**: Passive, progressive
- **verða**: Future necessity
- **munu, skulu**: Future intent, obligation

### Polite Forms (Past Subjunctive)

- Vildir þú vera svo vænn að...? (Would you be so kind as to...?)
- Gætirðu opnað gluggann? (Could you open the window?)
- Mætti ég spyrja...? (May I ask...?)

---

## PRONOUNS (Fornöfn)

### Personal Pronouns (Nominative)

| Person | Singular | Plural |
|--------|----------|--------|
| 1st | ég (I) | við (we) |
| 2nd | þú (you) | þið (you all) |
| 3rd masc. | hann (he) | þeir (they — males) |
| 3rd fem. | hún (she) | þær (they — females) |
| 3rd neut. | það (it) | þau (they — mixed/neuter) |

**Three words for "they"** based on gender of the group: þeir (m.), þær (f.), þau (mixed).

Case forms: ég → mig (acc.), mér (dat.), mín (gen.)

### Reflexive Pronouns

- sig (accusative), sér (dative), sín (genitive)
- Used when object = subject

### Demonstrative Pronouns

- þessi (this), sá (that) — must agree in gender, number, case
- E.g., þessa bók (acc. fem. sg.)

### Relative Pronouns

- sem (that/which/who) — invariable, introduces relative clauses
- Triggers Stylistic Fronting when subject gap exists

---

## WORD ORDER (Orðaröð)

### V2 Rule (Main Clauses)

The finite verb MUST be the second constituent in declarative sentences.

- **Standard**: Ég borða fisk (I eat fish) — Subject + Verb
- **Fronted adverb**: Í dag borða ég ekki fisk (Today eat I not fish) — subject-verb inversion
- **Conjunctions** (og, af því að) occupy a "null" position — don't count for V2

### Subordinate Clauses

Icelandic is an "I-V2" language — V2 applies even in embedded clauses (unlike Danish/Swedish):

- Ég veit að Jón les oft bókina (I know that John reads often the book)
- Verb precedes sentential adverbs in embedded clauses

### Topicalization

Moving a constituent to the front for emphasis:

- Fiskinn borða ég ekki (THE FISH eat I not) — emphasis on "the fish"
- Restricted in embedded clauses (only with "bridge verbs" like segja, telja)

### Stylistic Fronting

Unique to Icelandic. Moves elements before the finite verb when there's a subject gap:

- Maðurinn sem **farinn** var heim... (The man who gone was home...)
- ...sem **ekki** er hægt að hafna (...which not is possible to reject)

**Accessibility hierarchy**: Negation > Adverbs > Past Participle/Verb Particle > Predicative Adjective

Does NOT change meaning — manages rhythm and flow in formal prose.

### Negation and Adverb Position

- Standard: After both finite verb and subject
- V2 embedded: Verb before adverbs (V > Adv)
- Exception: Stylistic Fronting can place negation/adverbs before verb

---

## SPELLING AND ORTHOGRAPHY

### The Icelandic Alphabet (32 letters)

A Á B D Ð E É F G H I Í J K L M N O Ó P R S T U Ú V X Y Ý Þ Æ Ö

**Excluded**: C, Q, W, Z

### Special Characters

| Letter | Sound | Notes |
|--------|-------|-------|
| Þ þ (þorn) | Hard "th" (as in "thorn") | Beginning of words |
| Ð ð (eð) | Soft "th" (as in "the") | Middle/end of words |
| Æ æ | Distinct vowel | Near end of alphabet |
| Ö ö | Often from a-mutation | Stem 'a' → 'ö' before 'u' |

### Accent Marks

Á, É, Í, Ó, Ú, Ý are **separate letters** representing different sounds — not just stress markers.

### Pronunciation Rules Affecting Spelling

- **ll** = "tl" sound (flat tongue, soft click)
- **hv** = "kv" sound
- **au** = diphthong, treated as single unit, immune to a-mutation
- **Stress**: Always on first syllable (unless compound word)

### Compound Words

- Formed using genitive case as linking mechanism
- New terms are coined by the word committee to avoid loanwords (linguistic purism)
- Ég is capitalized (like English "I")

---

## COMMON ERRORS TO AVOID

### 1. Dative Sickness (Þágufallssýki)

**Wrong**: Mér langar (dative)
**Right**: Mig langar (accusative) — "I want"

The dative incorrectly replacing accusative in impersonal constructions. Strictly avoided in formal writing.

### 2. Indicative Encroachment

**Wrong**: Ég held að hann kemur (indicative after "think")
**Right**: Ég held að hann komi (subjunctive)

Use subjunctive after verbs of thinking/believing/hoping.

### 3. The "New Passive"

**Wrong**: Það var barið mig (passive + active case pattern)
**Right**: Ég var barinn (traditional passive)

### 4. Gender Assignment

Gender is a grammatical category for declension, NOT biological sex. Hestur (horse) is always masculine regardless of the animal's sex. Learn gender with each new noun.

### 5. Overuse of Progressive (vera að)

**Anglicism**: Ég er að borða (I am eating) — overused by learners
**Better in formal prose**: Ég borð (simple present) when appropriate

### 6. Loanword Avoidance

Use indigenous neologisms. Consult Málið.is for proper terminology:
- Computer = tölva (not kompjúter)
- Telephone = sími (not telefón)

---

## STYLE AND REGISTER

### Formal / Academic Writing

- Avoid first person (ég) — use impersonal constructions or third person
- Maintain strict case government
- Avoid anglicisms — use indigenous vocabulary
- Use Stylistic Fronting for rhythm in formal prose
- Past subjunctive for politeness and hedging

### Informal / Conversational

- First person is natural
- Progressive (vera að) is acceptable
- Contractions and casual register
- Idiomatic expressions welcome

### Linguistic Purism

Icelandic actively resists loanwords. The Árni Magnússon Institute maintains terminology banks. Modern concepts get Icelandic coinages. Always prefer the native term.

---

## IDIOMS AND EXPRESSIONS (Orðtök)

Use these to add natural Icelandic flavor:

| Expression | Literal | Meaning |
|-----------|---------|---------|
| Rúsínan í pylsuendanum | The raisin at the end of the hot dog | A pleasant surprise, the highlight |
| Áfram með smjörið | On with the butter | Keep going, hurry up |
| Ég kem alveg af fjöllum | I come from the mountains | I have no idea what's going on |
| Blindur er bóklaus maður | Blind is a bookless man | Those who don't read are ignorant |
| Alveg út að aka | Totally out driving | Someone acting crazy / completely wrong |
| Enginn verður óbarinn biskup | Nobody becomes an unbeaten bishop | Success requires facing adversity |
| Kemur allt með kalda vatninu | It all comes with the cold water | Patience is rewarded |
| Takk fyrir síðast | Thanks for last time | Polite greeting referencing previous meeting |
| Leggja höfuðið í bleyti | Lay your head in water | Think long and hard |
| Gefa undir fótinn | Give under the foot | To flirt |
| Bíta á jaxlinn | Bite the molar | Endure a difficult situation |
| Gluggaveður | Window weather | Looks nice from inside but is freezing |
| Árinni kennir illur ræðari | A bad rower blames the oar | Making excuses for poor performance |
| Hver hefur sinn djöful að draga | Everyone has their devil to drag | Everyone has their own problems |
| Fjarlægðin gerir fjöllin blá | Distance makes the mountains blue | Things look better from afar |
| Að sitja sem ormur á gulli | To sit like a wyrm on gold | To hoard / refuse to share |
| Að slá einhverjum gullhamra | Strike with golden hammers | To flatter excessively |
| Neyðin kennir naktri konu að spinna | Plight teaches a naked woman to spin | Necessity is the mother of invention |
| Margur verður af aurum api | Coin turns many into monkeys | Money makes people act foolish |

---

## SPELL & GRAMMAR VERIFICATION (GreynirCorrect)

After writing or editing Icelandic text, ALWAYS run GreynirCorrect to catch errors the model may have introduced. The Python library `reynir-correct` should be installed (`pip3 install reynir-correct`).

### Verification Script

Run this via Bash on the output file to check every sentence:

```python
python3 << 'PYEOF'
from reynir_correct import check_single
import re, sys

filepath = sys.argv[1] if len(sys.argv) > 1 else "INPUT_FILE"
with open(filepath, "r") as f:
    text = f.read()

# Known project terms to ignore (add as needed)
IGNORE_WORDS = {"Ókind", "ensímvinnuð", "keratínefni", "keratínprótein", "keratínlífplast", "keratínfilmur", "keratínsameindum"}

lines = text.split("\n")
for i, line in enumerate(lines, 1):
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or stripped.startswith("|") or stripped.startswith("---") or stripped.startswith("*"):
        continue
    clean = re.sub(r'\*\*', '', stripped)
    clean = re.sub(r'^- ', '', clean)
    if len(clean) < 5:
        continue
    try:
        sent = check_single(clean)
        for a in sent.annotations:
            if a.code and a.code.startswith("E006"):
                continue  # Skip abbreviation warnings
            if a.code and a.code.startswith("U001"):
                # Check if unknown word is in our ignore list
                if a.text and any(w in a.text for w in IGNORE_WORDS):
                    continue
            if a.code and a.code.startswith("W001"):
                # Skip suggestions for project-specific names
                if any(w in (a.text or "") for w in IGNORE_WORDS):
                    continue
            print(f"L{i} [{a.code}]: {a.text}")
            if a.suggest:
                print(f"  → {a.suggest}")
            print(f"  context: {clean[:80]}")
            print()
    except Exception:
        pass
PYEOF
```

### How to Handle Results

- **U001 (unknown word)**: Check if it's a valid compound or technical term. If so, add to IGNORE_WORDS. If not, fix the spelling.
- **W001 (possible wrong word)**: Review the suggestion — often false positives for proper nouns and neologisms, but real catches for declension errors.
- **P_NT (parse errors)**: Usually indicates a genuine grammar issue — wrong case, agreement, or word order. Fix these.
- **Z002 (capitalization)**: Check if the word genuinely starts a sentence or follows a colon that should continue lowercase.
- **E001 (unparseable)**: The sentence structure may be too complex or contain an error. Simplify or restructure.

### When to Ignore

False positives are common for:
- Project names and brand names (Ókind, BigBoy, etc.)
- Technical compound words not in the dictionary
- Abbreviations (SEM, ESB, HS, etc.)

**Never ignore** parse errors (P_NT) or case/agreement warnings without manually verifying.

---

## QUICK REFERENCE CHECKLIST

Before finalizing any Icelandic text, verify:

- [ ] All nouns have correct case for their syntactic role
- [ ] Adjectives agree in gender, number, and case with their noun
- [ ] Strong/weak adjective declension matches definiteness
- [ ] Verb conjugation matches person and number
- [ ] V2 word order maintained in main clauses
- [ ] Subjunctive used after verbs of thinking/hoping/wishing
- [ ] No dative sickness (check impersonal verb case requirements)
- [ ] No anglicisms — use indigenous vocabulary
- [ ] Proper use of þ vs. ð
- [ ] A-mutation applied where 'u' follows stem 'a'
- [ ] Register is consistent (formal/informal throughout)
