import os

SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASSWORD = os.environ['SENDER_PASSWORD']
RECEIVER_EMAILS = os.environ['RECEIVER_EMAILS']

print("Starting program...")
print("Env vars:", SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAILS)