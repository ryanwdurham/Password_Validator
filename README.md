# 🔒 Password Strength Validator

**Stop using weak passwords!** This app helps you create secure passwords that hackers hate.

## 🚀 What Does It Do?

This password validator checks if your password is strong enough to protect your accounts. It gives you:

- 💪 **Real-time strength meter** - Watch your password get stronger as you type!
- 🎯 **Instant feedback** - Know exactly what to fix
- 🏆 **Score out of 100** - Gamify your password security
- 🌐 **Beautiful web interface** - Because security should look good too

View the HTML page here: https://ryanwdurham.github.io/Password_Validator/password_checker_app.html 

## Watch a demo video of my Password Validator and Pytest in action:

Watch it here:  https://www.loom.com/share/73ae4807e4744ad3a55c5df557e4a807


## 🛠️ Quick Start

### Try the Web App (Easiest!)
1. Download this repo
2. Open `password_checker_app.html` in your browser
3. Start typing and watch the magic happen! ✨

### Use the Python Code
```python
from password_validator import PasswordValidator

validator = PasswordValidator()
result = validator.validate("MyP@ssw0rd123")

# Get detailed feedback
print(result)
```

## 🧪 Testing

I wrote **48 comprehensive tests** using Pytest to make sure this validator actually works!
```bash
pytest test_password_validator.py -v
```

All tests passing? ✅ You bet!

## 📊 What Makes a Strong Password?

The validator checks 8 different things:

1. ✅ At least 8 characters long
2. ✅ Has uppercase letters (ABC)
3. ✅ Has lowercase letters (abc)
4. ✅ Has numbers (123)
5. ✅ Has special characters (!@#)
6. ✅ No common words (like "password")
7. ✅ No sequential patterns (like "abc" or "123")
8. ✅ No repeating characters (like "aaa")

## 💡 Pro Tip

Try the demo passwords in the web app to see examples of weak vs. strong passwords!

**Built with Python, Pytest,  and HTML**
