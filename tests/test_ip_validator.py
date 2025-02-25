import pytest
from src.ip_validator import validate_ip_address

def test_valid_ip_addresses():
    """Test valid IP address formats"""
    assert validate_ip_address('1.2.3.4') == True
    assert validate_ip_address('0.0.0.0') == True
    assert validate_ip_address('9.9.9.9') == True

def test_invalid_ip_addresses():
    """Test invalid IP address formats"""
    # Test multi-digit numbers
    assert validate_ip_address('12.3.4.5') == False
    assert validate_ip_address('1.23.4.5') == False
    
    # Test non-numeric characters
    assert validate_ip_address('a.b.c.d') == False
    assert validate_ip_address('1.2.3.x') == False
    
    # Test incorrect number of parts
    assert validate_ip_address('1.2.3') == False
    assert validate_ip_address('1.2.3.4.5') == False
    
    # Test empty string
    assert validate_ip_address('') == False
    
    # Test non-string input
    assert validate_ip_address(12345) == False
    assert validate_ip_address(None) == False

def test_edge_cases():
    """Test edge cases of IP address validation"""
    # Test whitespace
    assert validate_ip_address(' 1.2.3.4 ') == False
    assert validate_ip_address('1. 2.3.4') == False
    
    # Test negative numbers (not allowed)
    assert validate_ip_address('-1.2.3.4') == False
    
    # Test special characters
    assert validate_ip_address('1.2.3.@') == False