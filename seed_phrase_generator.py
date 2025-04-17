#!/usr/bin/env python3
import random
import re
import argparse


def clean_word_list(text):
    """Clean and parse input text into a list of words."""
    # Replace newlines with spaces and split by commas or whitespace
    words = re.split(r'[,\s]+', text.replace('\n', ' '))
    # Filter out empty strings and normalize words
    return [word.strip().lower() for word in words if word.strip()]


def generate_seed_phrase(word_list, length=12):
    """Generate a single seed phrase of specified length."""
    if len(word_list) < length:
        raise ValueError(f"Not enough words provided. Need at least {length} words.")
    
    # Randomly select words for the seed phrase
    selected_words = random.sample(word_list, length)
    return " ".join(selected_words)


def generate_multiple_phrases(word_list, phrase_length=12, num_phrases=10):
    """Generate multiple seed phrases."""
    return [generate_seed_phrase(word_list, phrase_length) for _ in range(num_phrases)]


def main():
    parser = argparse.ArgumentParser(description='Generate blockchain seed phrases from a list of words')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of each seed phrase (default: 12)')
    parser.add_argument('-n', '--number', type=int, default=10, help='Number of phrases to generate (default: 10)')
    parser.add_argument('-i', '--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('-f', '--file', type=str, help='File containing word list (one word per line or comma-separated)')
    
    args = parser.parse_args()
    
    # Get the word list
    if args.interactive:
        print("Enter your list of words (separated by spaces, commas, or newlines).")
        print("Type 'END' on a line by itself when finished:")
        
        lines = []
        while True:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        
        word_list_text = ' '.join(lines)
    elif args.file:
        try:
            with open(args.file, 'r') as f:
                word_list_text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            return
    else:
        # If neither interactive nor file is specified, use stdin
        print("Enter your list of words (separated by spaces, commas, or newlines).")
        print("Press Ctrl+D (Unix) or Ctrl+Z (Windows) when finished:")
        word_list_text = ' '.join(line for line in iter(input, ''))
    
    # Process the word list
    word_list = clean_word_list(word_list_text)
    
    # Remove duplicates while preserving order
    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    
    word_list = unique_words
    
    # Check if we have enough words
    if len(word_list) < args.length:
        print(f"Error: Not enough unique words. Found {len(word_list)}, need at least {args.length}")
        return
    
    print(f"\nFound {len(word_list)} unique words. Generating {args.number} seed phrases of length {args.length}...\n")
    
    # Generate the phrases
    phrases = generate_multiple_phrases(word_list, args.length, args.number)
    
    # Print the results
    for i, phrase in enumerate(phrases, 1):
        print(f"Phrase {i}: {phrase}")
    
    print(f"\nCombination space: {len(word_list)}^{args.length} possible combinations")
    
    # Calculate rough estimate of total possible combinations
    from math import comb
    total_combinations = comb(len(word_list), args.length)
    print(f"Total unique combinations: {total_combinations:,}")


if __name__ == "__main__":
    main()