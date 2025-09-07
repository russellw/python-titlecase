#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script for titlecas.py - the vendorable titlecase function
"""

import titlecas

def test_basic_cases():
    """Test basic titlecasing functionality"""
    cases = [
        ('the quick brown fox', 'The Quick Brown Fox'),
        ('hello world', 'Hello World'),
        ('a tale of two cities', 'A Tale of Two Cities'),
        ('the great gatsby', 'The Great Gatsby'),
    ]
    
    print("Testing basic cases...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_small_words():
    """Test handling of small words"""
    cases = [
        ('and then there were none', 'And Then There Were None'),
        ('for whom the bell tolls', 'For Whom the Bell Tolls'),
        ('of mice and men', 'Of Mice and Men'),
        ('in the beginning', 'In the Beginning'),
        ('by the sea', 'By the Sea'),
    ]
    
    print("\nTesting small words...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_special_cases():
    """Test special cases like abbreviations, names, etc."""
    cases = [
        ('iPhone vs. android', 'iPhone vs. Android'),
        ('U.S.A. and U.K.', 'U.S.A. And U.K.'),
        ('dr. john smith', 'Dr. John Smith'),
        ('mrs. jane doe', 'Mrs. Jane Doe'),
        ('API endpoints', 'API Endpoints'),
        ('HTML and CSS', 'HTML And CSS'),
        ('NEW YORK TIMES', 'New York Times'),
        ('ALL CAPS TEXT', 'All Caps Text'),
    ]
    
    print("\nTesting special cases...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_mac_mc_names():
    """Test Mac/Mc name handling"""
    cases = [
        ('mcconnell vs. mcdonald', 'McConnell vs. McDonald'),
        ('macarthur and macdonald', 'MacArthur and MacDonald'),
        ('mckinley mountain', 'McKinley Mountain'),
    ]
    
    print("\nTesting Mac/Mc names...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_apostrophes():
    """Test apostrophe handling"""
    cases = [
        ("d'artagnan's story", "d'Artagnan's Story"),
        ("o'connor's restaurant", "O'Connor's Restaurant"),
        ("it's a wonderful life", "It's a Wonderful Life"),
    ]
    
    print("\nTesting apostrophes...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_hyphens_and_slashes():
    """Test hyphen and slash handling"""
    cases = [
        ('self-driving car', 'Self-Driving Car'),
        ('state-of-the-art technology', 'State-of-the-Art Technology'),
        ('API/REST endpoints', 'API/REST Endpoints'),
        ('html/css/javascript', 'HTML/CSS/JavaScript'),
    ]
    
    print("\nTesting hyphens and slashes...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_edge_cases():
    """Test edge cases"""
    cases = [
        ('', ''),
        ('a', 'A'),
        ('the', 'The'),
        ('   spaces   around   ', '   Spaces   Around   '),
        ('punctuation!', 'Punctuation!'),
        ('question?', 'Question?'),
    ]
    
    print("\nTesting edge cases...")
    for input_text, expected in cases:
        result = titlecas.titlecase(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_text}' -> '{result}'")
        if result != expected:
            print(f"  Expected: '{expected}'")

def test_small_first_last_parameter():
    """Test the small_first_last parameter"""
    test_text = "a tale of two cities"
    
    print("\nTesting small_first_last parameter...")
    
    # With small_first_last=True (default)
    result_true = titlecas.titlecase(test_text, small_first_last=True)
    expected_true = "A Tale of Two Cities"
    status = "✓" if result_true == expected_true else "✗"
    print(f"{status} small_first_last=True: '{result_true}'")
    if result_true != expected_true:
        print(f"  Expected: '{expected_true}'")
    
    # With small_first_last=False
    result_false = titlecas.titlecase(test_text, small_first_last=False)
    expected_false = "a Tale of Two cities"
    status = "✓" if result_false == expected_false else "✗"
    print(f"{status} small_first_last=False: '{result_false}'")
    if result_false != expected_false:
        print(f"  Expected: '{expected_false}'")

def test_normalise_space_characters():
    """Test the normalise_space_characters parameter"""
    test_text = "hello\tworld\u00A0test"  # tab and non-breaking space
    
    print("\nTesting normalise_space_characters parameter...")
    
    # With normalise_space_characters=False (default)
    result_false = titlecas.titlecase(test_text, normalise_space_characters=False)
    print(f"✓ normalise_space_characters=False: '{result_false}' (preserves original spaces)")
    
    # With normalise_space_characters=True
    result_true = titlecas.titlecase(test_text, normalise_space_characters=True)
    expected_true = "Hello World Test"
    status = "✓" if result_true == expected_true else "✗"
    print(f"{status} normalise_space_characters=True: '{result_true}'")
    if result_true != expected_true:
        print(f"  Expected: '{expected_true}'")

def run_all_tests():
    """Run all test suites"""
    print("=" * 60)
    print("TITLECAS.PY TEST SUITE")
    print("=" * 60)
    
    test_basic_cases()
    test_small_words()
    test_special_cases()
    test_mac_mc_names()
    test_apostrophes()
    test_hyphens_and_slashes()
    test_edge_cases()
    test_small_first_last_parameter()
    test_normalise_space_characters()
    
    print("\n" + "=" * 60)
    print("Test suite completed!")
    print("=" * 60)

if __name__ == "__main__":
    run_all_tests()