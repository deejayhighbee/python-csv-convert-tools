import chardet

def detect_encoding(file_path, num_bytes=10000):
    with open(file_path, 'rb') as f:
        rawdata = f.read(num_bytes)
    result = chardet.detect(rawdata)
    return result['encoding']

if __name__ == "__main__":
    file_path = 'file.csv'  # Ensure this path is correct
    encoding = detect_encoding(file_path)
    print(f"Detected encoding: {encoding}")
