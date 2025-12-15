# password_validator.py
"""
Password Strength Validator
A professional tool for validating password security
"""

import re


class PasswordValidator:
    """Validates password strength based on security best practices"""

    def __init__(self, min_length=8, max_length=128):
        """
        Initialize the validator with configurable length requirements

        Args:
            min_length: Minimum password length (default: 8)
            max_length: Maximum password length (default: 128)
        """
        self.min_length = min_length
        self.max_length = max_length

    def check_length(self, password):
        """Check if password meets length requirements"""
        if not password:
            return False
        return self.min_length <= len(password) <= self.max_length

    def has_uppercase(self, password):
        """Check if password contains at least one uppercase letter"""
        return bool(re.search(r'[A-Z]', password))

    def has_lowercase(self, password):
        """Check if password contains at least one lowercase letter"""
        return bool(re.search(r'[a-z]', password))

    def has_digit(self, password):
        """Check if password contains at least one digit"""
        return bool(re.search(r'\d', password))

    def has_special_char(self, password):
        """Check if password contains at least one special character"""
        special_chars = r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]'
        return bool(re.search(special_chars, password))

    def has_no_common_patterns(self, password):
        """Check for common weak patterns"""
        common_patterns = [
            'password', '12345', 'qwerty', 'abc123',
            'letmein', 'welcome', 'monkey', '111111'
        ]
        password_lower = password.lower()
        return not any(pattern in password_lower for pattern in common_patterns)

    def has_no_sequential_chars(self, password):
        """Check for sequential characters (abc, 123, etc.)"""
        password_lower = password.lower()

        # Check for sequential letters (abc, xyz, etc.)
        for i in range(len(password_lower) - 2):
            if password_lower[i:i + 3].isalpha():
                chars = password_lower[i:i + 3]
                if (ord(chars[1]) == ord(chars[0]) + 1 and
                        ord(chars[2]) == ord(chars[1]) + 1):
                    return False

        # Check for sequential numbers (123, 456, etc.)
        for i in range(len(password) - 2):
            if password[i:i + 3].isdigit():
                nums = password[i:i + 3]
                if (int(nums[1]) == int(nums[0]) + 1 and
                        int(nums[2]) == int(nums[1]) + 1):
                    return False

        return True

    def has_no_repeating_chars(self, password):
        """Check for excessive character repetition (aaa, 111, etc.)"""
        for i in range(len(password) - 2):
            if password[i] == password[i + 1] == password[i + 2]:
                return False
        return True

    def validate(self, password):
        """
        Validate password and return detailed results

        Returns:
            dict: Contains 'is_valid', 'strength', 'score', and 'feedback'
        """
        if not password:
            return {
                'is_valid': False,
                'strength': 'invalid',
                'score': 0,
                'feedback': ['Password cannot be empty']
            }

        # Run all checks
        checks = {
            'length': self.check_length(password),
            'uppercase': self.has_uppercase(password),
            'lowercase': self.has_lowercase(password),
            'digit': self.has_digit(password),
            'special_char': self.has_special_char(password),
            'no_common_patterns': self.has_no_common_patterns(password),
            'no_sequential': self.has_no_sequential_chars(password),
            'no_repeating': self.has_no_repeating_chars(password)
        }

        # LENGTH IS A HARD REQUIREMENT - If length fails, password is invalid
        if not checks['length']:
            return {
                'is_valid': False,
                'strength': 'invalid',
                'score': 0,
                'feedback': [f'Password must be between {self.min_length} and {self.max_length} characters']
            }

        # Calculate score (out of 100)
        score = 0
        feedback = []

        # Length check passed (20 points)
        score += 20

        # Character diversity (15 points each) - INCREASED FROM 10
        if checks['uppercase']:
            score += 15
        else:
            feedback.append('Add at least one uppercase letter (A-Z)')

        if checks['lowercase']:
            score += 15
        else:
            feedback.append('Add at least one lowercase letter (a-z)')

        if checks['digit']:
            score += 15
        else:
            feedback.append('Add at least one number (0-9)')

        if checks['special_char']:
            score += 15
        else:
            feedback.append('Add at least one special character (!@#$%^&*)')

        # Security checks (adjusted points)
        if checks['no_common_patterns']:
            score += 10
        else:
            feedback.append('Avoid common words and patterns')

        if checks['no_sequential']:
            score += 5
        else:
            feedback.append('Avoid sequential characters (abc, 123)')

        if checks['no_repeating']:
            score += 5
        else:
            feedback.append('Avoid repeating characters (aaa, 111)')

        # Determine strength
        if score >= 90:
            strength = 'very strong'
        elif score >= 75:
            strength = 'strong'
        elif score >= 60:
            strength = 'medium'
        elif score >= 40:
            strength = 'weak'
        else:
            strength = 'very weak'

        # Password is valid if score is at least 75 (INCREASED FROM 60)
        is_valid = score >= 75

        return {
            'is_valid': is_valid,
            'strength': strength,
            'score': score,
            'feedback': feedback if feedback else ['Password meets all requirements!']
        }

    def get_strength_label(self, password):
        """Get a simple strength label for the password"""
        result = self.validate(password)
        return result['strength']

    def is_valid_password(self, password):
        """Simple boolean check if password is valid"""
        result = self.validate(password)
        return result['is_valid']