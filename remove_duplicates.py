def remove_duplicates(text):
    words = text.split()  
    result = [words[0]]  

    for word in words[1:]:
        if word != result[-1]: 
            result.append(word)

    return ' '.join(result)

# Input text
input_text = """In the bustling bustling city city of New York, New York, the the bright bright lights lights and and 
the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that 
is is both both exhilarating exhilarating and and exhausting exhausting. The bustling city lights and the constant hum 
of activity create an atmosphere that is both exhilarating and exhausting."""

# Remove duplicate words
output_text = remove_duplicates(input_text)

print(output_text)
