from functools import partial


def send_email(to, subject, body, from_addr="noreply@example.com", priority="normal"):
    """Imitation of sending email"""
    return f"""
    From: {from_addr}
    To: {to}
    Subject: {subject}
    Priority: {priority}

    {body}
    """


# State positional arguments
send_to_user = partial(send_email, "user@exmaple.com")
send_welcome = partial(send_to_user, "Welcome to our serivce!")
send_notification = partial(send_to_user, "Important notification!")

print("Sending greeting letter")
result1 = send_welcome("Dear user, thank you for registration")
print(result1)


print("\n Sending notification:")
result2 = send_notification("Your accoutn will expire soon")
print(result2)


## State named argumets
send_urgent = partial(send_email, priority="urgent", from_addr="admin@example.com")

print("\nSending urgent letter:")
result3 = send_urgent("boss@example.com", "Critical issue", "System is down!")
print(result3)