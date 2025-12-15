# test_password_validator.py
"""
Comprehensive test suite for Password Validator
"""

import pytest
from password_validator import PasswordValidator


# Test initialization and configuration

def test_validator_default_initialization():
    """Test validator initializes with default settings"""
    validator = PasswordValidator()
    assert validator.min_length == 8
    assert validator.max_length == 128


def test_validator_custom_length_requirements():
    """Test validator with custom length requirements"""
    validator = PasswordValidator(min_length=12, max_length=64)
    assert validator.min_length == 12
    assert validator.max_length == 64


# Test length validation

def test_check_length_valid():
    """Test password with valid length"""
    validator = PasswordValidator()
    assert validator.check_length("Password123!") == True


def test_check_length_too_short():
    """Test password that is too short"""
    validator = PasswordValidator()
    assert validator.check_length("Pass1!") == False


def test_check_length_too_long():
    """Test password that exceeds maximum length"""
    validator = PasswordValidator(min_length=8, max_length=20)
    long_password = "A" * 25
    assert validator.check_length(long_password) == False


def test_check_length_empty_password():
    """Test empty password"""
    validator = PasswordValidator()
    assert validator.check_length("") == False


def test_check_length_none_password():
    """Test None as password"""
    validator = PasswordValidator()
    assert validator.check_length(None) == False


# Test character type checks

def test_has_uppercase_present():
    """Test password with uppercase letters"""
    validator = PasswordValidator()
    assert validator.has_uppercase("Password") == True


def test_has_uppercase_absent():
    """Test password without uppercase letters"""
    validator = PasswordValidator()
    assert validator.has_uppercase("password123!") == False


def test_has_lowercase_present():
    """Test password with lowercase letters"""
    validator = PasswordValidator()
    assert validator.has_lowercase("Password") == True


def test_has_lowercase_absent():
    """Test password without lowercase letters"""
    validator = PasswordValidator()
    assert validator.has_lowercase("PASSWORD123!") == False


def test_has_digit_present():
    """Test password with digits"""
    validator = PasswordValidator()
    assert validator.has_digit("Password123") == True


def test_has_digit_absent():
    """Test password without digits"""
    validator = PasswordValidator()
    assert validator.has_digit("Password!") == False


def test_has_special_char_present():
    """Test password with special characters"""
    validator = PasswordValidator()
    assert validator.has_special_char("Password123!") == True


def test_has_special_char_various():
    """Test various special characters"""
    validator = PasswordValidator()
    special_chars = "!@#$%^&*()_+-="
    for char in special_chars:
        assert validator.has_special_char(f"Pass{char}123") == True


def test_has_special_char_absent():
    """Test password without special characters"""
    validator = PasswordValidator()
    assert validator.has_special_char("Password123") == False


# Test common pattern detection

def test_no_common_patterns_secure():
    """Test password without common patterns"""
    validator = PasswordValidator()
    assert validator.has_no_common_patterns("MyS3cur3P@ss!") == True


def test_no_common_patterns_contains_password():
    """Test password containing 'password'"""
    validator = PasswordValidator()
    assert validator.has_no_common_patterns("MyPassword123!") == False


def test_no_common_patterns_contains_12345():
    """Test password containing '12345'"""
    validator = PasswordValidator()
    assert validator.has_no_common_patterns("Hello12345!") == False


def test_no_common_patterns_case_insensitive():
    """Test that pattern detection is case-insensitive"""
    validator = PasswordValidator()
    assert validator.has_no_common_patterns("QWERTY123!") == False


# Test sequential character detection

def test_no_sequential_chars_secure():
    """Test password without sequential characters"""
    validator = PasswordValidator()
    assert validator.has_no_sequential_chars("P@ssw0rd!") == True


def test_no_sequential_chars_has_abc():
    """Test password with sequential letters (abc)"""
    validator = PasswordValidator()
    assert validator.has_no_sequential_chars("Pabc123!") == False


def test_no_sequential_chars_has_123():
    """Test password with sequential numbers (123)"""
    validator = PasswordValidator()
    assert validator.has_no_sequential_chars("Pass123!") == False


def test_no_sequential_chars_has_xyz():
    """Test password with sequential letters (xyz)"""
    validator = PasswordValidator()
    assert validator.has_no_sequential_chars("Pxyz!987") == False


# Test repeating character detection

def test_no_repeating_chars_secure():
    """Test password without excessive repetition"""
    validator = PasswordValidator()
    assert validator.has_no_repeating_chars("P@ssw0rd!") == True


def test_no_repeating_chars_has_aaa():
    """Test password with repeating letters"""
    validator = PasswordValidator()
    assert validator.has_no_repeating_chars("Paaassword1!") == False


def test_no_repeating_chars_has_111():
    """Test password with repeating numbers"""
    validator = PasswordValidator()
    assert validator.has_no_repeating_chars("Pass1110!") == False


def test_no_repeating_chars_two_same_allowed():
    """Test that two identical characters are allowed"""
    validator = PasswordValidator()
    assert validator.has_no_repeating_chars("Paassword1!") == True


# Test full validation

def test_validate_empty_password():
    """Test validation of empty password"""
    validator = PasswordValidator()
    result = validator.validate("")

    assert result['is_valid'] == False
    assert result['strength'] == 'invalid'
    assert result['score'] == 0
    assert 'Password cannot be empty' in result['feedback']


def test_validate_very_strong_password():
    """Test validation of very strong password"""
    validator = PasswordValidator()
    result = validator.validate("MyS3cur3P@ssw0rd!")

    assert result['is_valid'] == True
    assert result['strength'] == 'very strong'
    assert result['score'] >= 90


def test_validate_strong_password():
    """Test validation of strong password"""
    validator = PasswordValidator()
    result = validator.validate("S3cur3P@ss")

    assert result['is_valid'] == True
    assert result['strength'] in ['strong', 'very strong']
    assert result['score'] >= 70


def test_validate_weak_password():
    """Test validation of weak password"""
    validator = PasswordValidator()
    result = validator.validate("password")

    assert result['is_valid'] == False
    assert result['strength'] in ['very weak', 'weak']
    assert result['score'] < 60


def test_validate_password_too_short():
    """Test validation of password that's too short"""
    validator = PasswordValidator()
    result = validator.validate("P@s1")

    assert result['is_valid'] == False
    assert any('between' in fb for fb in result['feedback'])


def test_validate_password_missing_uppercase():
    """Test validation feedback for missing uppercase"""
    validator = PasswordValidator()
    result = validator.validate("mypassword123!")

    assert any('uppercase' in fb.lower() for fb in result['feedback'])


def test_validate_password_missing_lowercase():
    """Test validation feedback for missing lowercase"""
    validator = PasswordValidator()
    result = validator.validate("MYPASSWORD123!")

    assert any('lowercase' in fb.lower() for fb in result['feedback'])


def test_validate_password_missing_digit():
    """Test validation feedback for missing digit"""
    validator = PasswordValidator()
    result = validator.validate("MyPassword!")

    assert any('number' in fb.lower() for fb in result['feedback'])


def test_validate_password_missing_special():
    """Test validation feedback for missing special character"""
    validator = PasswordValidator()
    result = validator.validate("MyPassword123")

    assert any('special' in fb.lower() for fb in result['feedback'])


def test_validate_password_with_common_pattern():
    """Test validation feedback for common patterns"""
    validator = PasswordValidator()
    result = validator.validate("MyPassword123!")

    assert any('common' in fb.lower() for fb in result['feedback'])


def test_validate_password_with_sequential():
    """Test validation feedback for sequential characters"""
    validator = PasswordValidator()
    result = validator.validate("MyPass123!")

    assert any('sequential' in fb.lower() for fb in result['feedback'])


def test_validate_password_with_repeating():
    """Test validation feedback for repeating characters"""
    validator = PasswordValidator()
    result = validator.validate("MyPasssss1!")

    assert any('repeating' in fb.lower() for fb in result['feedback'])


def test_validate_perfect_password_feedback():
    """Test that perfect password gets positive feedback"""
    validator = PasswordValidator()
    result = validator.validate("MyS3cur3P@ssw0rd!")

    assert 'Password meets all requirements!' in result['feedback']


# Test convenience methods

def test_get_strength_label_very_strong():
    """Test strength label for very strong password"""
    validator = PasswordValidator()
    strength = validator.get_strength_label("MyS3cur3P@ssw0rd!")
    assert strength == 'very strong'


def test_get_strength_label_weak():
    """Test strength label for weak password"""
    validator = PasswordValidator()
    strength = validator.get_strength_label("password")
    assert strength in ['very weak', 'weak']


def test_is_valid_password_true():
    """Test is_valid method returns True for good password"""
    validator = PasswordValidator()
    assert validator.is_valid_password("MyS3cur3P@ss!") == True


def test_is_valid_password_false():
    """Test is_valid method returns False for bad password"""
    validator = PasswordValidator()
    assert validator.is_valid_password("password") == False


# Test edge cases

def test_validate_password_with_spaces():
    """Test password containing spaces"""
    validator = PasswordValidator()
    result = validator.validate("My P@ssw0rd 123")
    # Spaces are valid characters
    assert result['is_valid'] == True


def test_validate_unicode_characters():
    """Test password with unicode characters"""
    validator = PasswordValidator()
    result = validator.validate("MyP@ss™ø®∂123")
    # Should handle unicode gracefully
    assert result is not None
    assert 'score' in result


def test_validator_scoring_consistency():
    """Test that validation scoring is consistent"""
    validator = PasswordValidator()

    # Same password should always get same score
    result1 = validator.validate("MyS3cur3P@ss!")
    result2 = validator.validate("MyS3cur3P@ss!")

    assert result1['score'] == result2['score']
    assert result1['strength'] == result2['strength']