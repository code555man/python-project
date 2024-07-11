# marshal encode file
import marshal

def encode(code):
    
    return marshal.dumps(compile(code, '<string>', 'exec'))

# Example usage:

code = """

python("Hello World!")

"""

encoded_code = encode(code)

print(encoded_code)


# enc = marshal.loads(encoded_code)
# exec(enc)