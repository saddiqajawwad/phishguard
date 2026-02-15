# questions.py
# This file contains all phishing simulation scenarios.
# We keep it separate so the main app.py stays clean and readable.

QUESTIONS = [
    {
        "id": 1,
        "type": "Email",
        "scenario": "Your Google account will be suspended in 24 hours. Verify now.",
        "extra": "Link: http://google-security-check.xyz",
        "correct_answer": "phishing",
        "explanation": "This message creates urgency and uses a fake domain.",
        "red_flags": [
            "Urgency / threat (\"suspended in 24 hours\")",
            "Suspicious domain name",
            "Asks you to verify immediately"
        ]
    },
    {
        "id": 2,
        "type": "SMS",
        "scenario": "Congratulations! You won a cash prize. Claim now.",
        "extra": "Link: bit.ly/win-prize",
        "correct_answer": "phishing",
        "explanation": "Prize scams often use shortened links to hide the real website.",
        "red_flags": [
            "Too good to be true",
            "Shortened link",
            "Pushes you to click quickly"
        ]
    },
    {
        "id": 3,
        "type": "Email",
        "scenario": "Invoice attached. Please open it urgently.",
        "extra": "Attachment: invoice.exe",
        "correct_answer": "phishing",
        "explanation": "A real invoice is usually PDF. EXE files are dangerous.",
        "red_flags": [
            "Executable attachment (.exe)",
            "Urgent tone",
            "No proper company details"
        ]
    },
    {
        "id": 4,
        "type": "Email",
        "scenario": "Your Netflix payment failed. Update your card details.",
        "extra": "Sender: netflix.support@payhelp-mail.com",
        "correct_answer": "phishing",
        "explanation": "The sender domain is not Netflix, so it is likely fake.",
        "red_flags": [
            "Sender domain does not match Netflix",
            "Asks for payment/card details",
            "Common scam technique"
        ]
    },
    {
        "id": 5,
        "type": "WhatsApp",
        "scenario": "Mom’s phone is broken. Save my new number. Send me Rs. 20,000 urgently.",
        "extra": "Message received from an unknown number",
        "correct_answer": "phishing",
        "explanation": "This is a classic impersonation scam to steal money quickly.",
        "red_flags": [
            "Asks for money urgently",
            "Emotional pressure",
            "New/unknown number"
        ]
    },
    {
        "id": 6,
        "type": "Email",
        "scenario": "Suspicious activity detected in your bank account. Login to secure it.",
        "extra": "Link: http://hbl-secure-login.com",
        "correct_answer": "phishing",
        "explanation": "Banks usually use secure official domains and HTTPS.",
        "red_flags": [
            "Uses HTTP instead of HTTPS",
            "Fake bank domain",
            "Tries to scare you into logging in"
        ]
    },
    {
        "id": 7,
        "type": "Email",
        "scenario": "Your parcel is on hold. Pay Rs. 50 delivery fee to release it.",
        "extra": "No tracking number included",
        "correct_answer": "phishing",
        "explanation": "Delivery scams often ask for small fees to steal card details.",
        "red_flags": [
            "No tracking number",
            "Unexpected fee request",
            "Generic delivery message"
        ]
    },
    {
        "id": 8,
        "type": "Email",
        "scenario": "Your password was changed successfully. If this wasn’t you, contact support.",
        "extra": "No suspicious link included",
        "correct_answer": "legit",
        "explanation": "This looks like a normal security notification with no forced action link.",
        "red_flags": [
            "No urgent threat",
            "No suspicious link",
            "Informational message"
        ]
    }
]
