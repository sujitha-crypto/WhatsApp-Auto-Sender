import pywhatkit as kit

print("✅ Script started!")

# Step 1: Get user input
phone_number = input("📱 Enter phone number (with +91...): ")
message = input("💬 Enter your message: ")

# Step 2: Send instantly (no schedule)
print(f"⚡ Opening WhatsApp and sending your message instantly to {phone_number}...\n")

kit.sendwhatmsg_instantly(
    phone_no=phone_number,
    message=message,
    wait_time=10,      # seconds to wait before typing
    tab_close=True,    # auto-close tab
    close_time=3       # seconds to wait before closing
)

print("✅ Message sent instantly!")
