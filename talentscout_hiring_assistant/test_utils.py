from utils import is_valid_email, is_valid_phone, should_end_conversation

# Test email validation
print("📧 Email Test")
print("Valid:", is_valid_email("hello@example.com"))     # ✅ True
print("Invalid:", is_valid_email("hello@com"))           # ❌ False

# Test phone validation
print("\n📞 Phone Test")
print("Valid:", is_valid_phone("+91 9876543210"))        # ✅ True
print("Invalid:", is_valid_phone("12345"))               # ❌ False

# Test exit keyword detection
print("\n🚪 Exit Detection Test")
print("Should Exit (bye):", should_end_conversation("bye"))        # ✅ True
print("Should Not Exit (hello):", should_end_conversation("hello"))  # ❌ False
