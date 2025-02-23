import pytest
from src.text_word_splitter import split_text_to_words

def test_basic_capital_letter_splitting():
    text = "HelloWorld"
    assert split_text_to_words(text) == ["Hello", "World"]

def test_punctuation_splitting():
    text = "Hello,World!Test."
    assert split_text_to_words(text) == ["Hello", ",World", "!Test", "."]

def test_mixed_capital_and_punctuation():
    text = "HelloWorld!TestCase."
    assert split_text_to_words(text) == ["Hello", "World", "!Test", "Case", "."]

def test_uppercase_sequence():
    text = "HelloUSAWorld"
    assert split_text_to_words(text) == ["Hello", "U", "S", "A", "World"]

def test_quotation_preservation():
    text = "Hello\"World\"Test"
    assert split_text_to_words(text) == ["Hello", "\"World\"", "Test"]

def test_complex_mixed_case_and_punctuation():
    text = "Hello,WorldTest!ABC.Example"
    assert split_text_to_words(text) == ["Hello", ",World", "Test", "!A", "B", "C", ".Example"]

def test_empty_string():
    text = ""
    assert split_text_to_words(text) == []

def test_single_word():
    text = "SingleWord"
    assert split_text_to_words(text) == ["Single", "Word"]

def test_error_handling():
    with pytest.raises(TypeError):
        split_text_to_words(None)
    with pytest.raises(TypeError):
        split_text_to_words(123)

def test_special_characters():
    text = "Hello#World%Test"
    assert split_text_to_words(text) == ["Hello", "#World", "%Test"]