# Simple Text Encoder-Decoder

def encode(text, shift=3):
    """Encodes a string by shifting ASCII values."""
    print(f"Encoding text: {text} with shift: {shift}")
    encoded_text = [str(ord(char) + shift) for char in text]
    print(f"Encoded numeric values: {encoded_text}")
    result = "-".join(encoded_text)
    print(f"Final encoded string: {result}")
    return result

def decode(encoded_text, shift=3):
    """Decodes the encoded string back to original."""
    print(f"Decoding text: {encoded_text} with shift: {shift}")
    decoded_chars = [chr(int(num) - shift) for num in encoded_text.split("-")]
    print(f"Decoded characters: {decoded_chars}")
    result = "".join(decoded_chars)
    print(f"Final decoded string: {result}")
    return result

if __name__ == "__main__":
    # Test the encoder-decoder
    original_text = "Hello, GitHub!"
    print("Starting encoding process...")
    encoded = encode(original_text)
    print("Encoding complete. Starting decoding process...")
    decoded = decode(encoded)
    print("Decoding complete.")
    
    print(f"Original: {original_text}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    
    # Save output to a file for GitHub upload
    print("Saving results to output.txt...")
    with open("output.txt", "w") as f:
        f.write(f"Original: {original_text}\n")
        f.write(f"Encoded: {encoded}\n")
        f.write(f"Decoded: {decoded}\n")
    print("Results saved successfully.")
