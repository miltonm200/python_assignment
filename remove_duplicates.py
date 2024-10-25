import re

def remove_duplicates(text):
    # Use regex to match duplicate words separated by space, comma, or period
    result = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    result = re.sub(r'\b(New York)(, \1\b)+', r'\1', result)
    return result

input_text = (
    "In the bustling bustling city city of New York, New York, the the bright bright lights lights and and the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting. "
    "The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting."
)

output_text = remove_duplicates(input_text)
print(f'"{output_text}"')
