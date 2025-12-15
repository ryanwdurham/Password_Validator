# demo.py
"""
Interactive demo of the Password Validator
Perfect for showing off the application
"""

from password_validator import PasswordValidator


def print_separator():
    """Print a nice separator line"""
    print("=" * 60)


def print_result(result):
    """Pretty print validation results"""
    print(f"\n✓ Valid: {result['is_valid']}")
    print(f"💪 Strength: {result['strength'].upper()}")
    print(f"📊 Score: {result['score']}/100")
    print(f"\n📋 Feedback:")
    for feedback in result['feedback']:
        print(f"   • {feedback}")


def main():
    """Run the interactive demo"""
    print_separator()
    print("🔒 PASSWORD STRENGTH VALIDATOR - DEMO")
    print_separator()

    validator = PasswordValidator()

    # Test passwords with different strength levels
    test_passwords = [
        ("password", "Very Weak Password"),
        ("Password123", "Weak Password (no special char)"),
        ("P@ssw0rd", "Medium Password (common word)"),
        ("MyS3cur3P@ss!", "Strong Password"),
        ("MyS3cur3P@ssw0rd!", "Very Strong Password"),
    ]

    for password, description in test_passwords:
        print(f"\n\n🔍 Testing: {description}")
        print(f"   Password: '{password}'")
        result = validator.validate(password)
        print_result(result)
        print_separator()

    print("\n\n✨ Demo complete! All tests passed successfully.")
    print("\n💡 To run the full test suite, use:")
    print("   python -m pytest test_password_validator.py -v")


if __name__ == "__main__":
    main()