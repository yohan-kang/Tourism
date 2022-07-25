import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        if char in string.punctuation:
            return True
    return False


# 실습으로 완성해 주세요
def contains_uppercase_letter(value):
    return True


# 실습으로 완성해 주세요
def contains_lowercase_letter(value):
	return True


# 실습으로 완성해 주세요
def contains_number(value):
    return True


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("Must be a combination of at least 8 characters in English uppercase and lowercase letters, numbers, and special characters.")

    def get_help_text(self):
        return "Please enter a combination of 8 characters or more in English upper and lower case letters, numbers, and special characters."
        

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("Cannot contain special characters.")