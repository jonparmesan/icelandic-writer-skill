# Icelandic Writer Skill for Claude Code

A Claude Code skill that enables advanced Icelandic writing with correct grammar, natural style, and automated spell/grammar checking via GreynirCorrect.

## What it does

- Writes, translates, and reviews Icelandic text with proper grammar
- Covers the full case system, noun declension, verb conjugation, word order (V2), and more
- Automatically verifies output with GreynirCorrect before presenting to the user
- Avoids common errors: dative sickness, indicative encroachment, anglicisms
- Includes an idiom and expression reference for natural-sounding prose

## Installation

Copy `SKILL.md` into your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/icelandic-writer
cp SKILL.md ~/.claude/skills/icelandic-writer/
```

## Requirements

For the automated grammar checking, install GreynirCorrect:

```bash
pip3 install reynir-correct
```

## License

MIT
