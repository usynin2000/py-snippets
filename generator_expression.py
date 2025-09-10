
# Base

nums = (x for x in range(5))

print(next(nums))  # 0
print(next(nums))  # 1
print(next(nums))  # 2


# Next with condition
nums = (x for x in range(5) if x % 2 == 0)  # только чётные: 0, 2, 4, 6, 8


# Find first element by condition
print(next(nums))  # 0
print(next(nums))  # 2
print(next(nums))  # 4

providers = [
    {"name": "email", "template": "EMAIL"},
    {"name": "sms", "template": "SMS"},
    {"name": "push", "template": "PUSH"},
]

sms_template = next((prov["template"] for prov in providers if prov["name"] == "sms"))

print(sms_template)  # SMS


# StopIteration

nums = (x for x in [1, 2, 3] if x > 10)
# print(next(nums))  # StopIteration


# Using Default
nums = (x for x in [1, 2, 3] if x > 10)

print(next(nums, None))
print(next(nums, "empty"))


# When we need only first concurrence

words = ["apple", "banana", "cherry"]

first_with_a = next((w for w in words if "a" in w))
print(first_with_a)


