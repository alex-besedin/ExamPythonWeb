from django.core.exceptions import ValidationError


def mb_to_bytes(mb):
    return mb * 1024 * 1024


def validate_image_less_than_5mb(image_obj):
    filesize = image_obj.file.size
    megabyte_limit = 5.0
    if filesize > mb_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is {megabyte_limit}MB")


def name_alphabetic_validator(value):
    for char in value:
        if not char.isalpha() and char != '-':
            raise ValidationError('If you are not a child of Elon Musk, your name should contain only alphabetical letters... and "-"!')
