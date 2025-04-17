# Blockchain Seed Phrase Generator

A Python utility for generating random blockchain seed phrases from custom word lists.(Word list has been included😉)

## Overview

This tool allows you to generate random seed phrases for cryptocurrency wallets using your own word list. While most wallets use standardized BIP39 word lists, this tool offers flexibility for educational purposes or specialized use cases where custom word lists are needed.

## Features

- Generate multiple seed phrases of customizable length (default: 12 words)
- Process word lists from various input sources:
  - Interactive command-line input
  - Text files
  - Standard input (stdin)
- Automatically removes duplicate words from input
- Provides statistics about the combination space of your word list
- Simple command-line interface with multiple options

## Installation

No external dependencies are required! Simply clone this repository:

```bash
git clone https://github.com/ROHITCRAFTSYT/Seed-phrase-generator
cd Seed-phrase-generator
```

## Usage

### Basic Usage

```bash
python seed_phrase_generator.py
```

This will prompt you to enter your word list and then generate 10 seed phrases of 12 words each.

### Command-line Options

```
usage: seed_phrase_generator.py [-h] [-l LENGTH] [-n NUMBER] [-i] [-f FILE]

Generate blockchain seed phrases from a list of words

options:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Length of each seed phrase (default: 12)
  -n NUMBER, --number NUMBER
                        Number of phrases to generate (default: 10)
  -i, --interactive     Run in interactive mode
  -f FILE, --file FILE  File containing word list (one word per line or comma-separated)
```

### Examples

#### Interactive Mode

```bash
python seed_phrase_generator.py --interactive
```

Follow the prompts to enter your words. Type 'END' on a new line when you're finished.

#### From a File

```bash
python seed_phrase_generator.py --file my_wordlist.txt
```

Where `my_wordlist.txt` contains your words, either one per line or comma-separated.

#### Custom Length and Count

```bash
python seed_phrase_generator.py --length 24 --number 5
```

Generates 5 seed phrases of 24 words each.

## Input Format

The word list can be provided in various formats:
- Space-separated words
- Comma-separated words
- Newline-separated words
- Any combination of the above

The script will clean the input and create a list of unique words.

## Security Notice

⚠️ **Important Warning**: This tool is for educational and experimental purposes only.

For actual cryptocurrency wallets, please use:
- Hardware wallets (like Ledger, Trezor)
- Well-established wallet software with BIP39 standard implementation
- The standard BIP39 wordlist which ensures compatibility across wallets

Never share your actual seed phrase with anyone or store it digitally.

## Limitations

- Does not implement BIP39 checksum validation
- Cannot generate all possible combinations (impossible due to combinatorial explosion)
- Not intended for production use with real cryptocurrency assets

## License

MIT
