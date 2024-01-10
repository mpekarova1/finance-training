# Import your extractor and transformer modules
from src.extractors import extractor1
from src.transformers import transformer1

def main():
    # Call the function from the extractor module
    data = extractor1.extract_data()

    # Call the function from the transformer module
    transformed_data = transformer1.transform_data(data)

    # Continue with the rest of your program...

if __name__ == "__main__":
    main()