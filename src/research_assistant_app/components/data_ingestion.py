from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import re


def clean_up_text(content: str) -> str:
    """
    Remove unwanted characters and patterns in text input.

    :param content: Text input.

    :return: Cleaned version of original text input.
    """

    # Fix hyphenated words broken by newline
    content = re.sub(r"(\w+)-\n(\w+)", r"\1\2", content)

    # Remove specific unwanted patterns and characters
    unwanted_patterns = [
        "\\n",
        "  —",
        "——————————",
        "—————————",
        "—————",
        r"\\u[\dA-Fa-f]{4}",
        r"\uf075",
        r"\uf0b7",
    ]
    for pattern in unwanted_patterns:
        content = re.sub(pattern, "", content)

    # Fix improperly spaced hyphenated words and normalize whitespace
    content = re.sub(r"(\w)\s*-\s*(\w)", r"\1-\2", content)
    content = re.sub(r"\s+", " ", content)

    return content


def get_cleaned_dir_docs(pdf_file_dir):
    print(pdf_file_dir)
    documents = SimpleDirectoryReader(pdf_file_dir).load_data()

    # Call function
    cleaned_docs = []
    for d in documents:
        cleaned_text = clean_up_text(d.text)
        d.text = cleaned_text
        cleaned_docs.append(d)

    return cleaned_docs


def get_cleaned_input_docs(pdf_file):

    documents = SimpleDirectoryReader(input_files=[pdf_file]).load_data()

    # Call function
    cleaned_docs = []
    for d in documents:
        cleaned_text = clean_up_text(d.text)
        d.text = cleaned_text
        cleaned_docs.append(d)

    return cleaned_docs


if __name__ == "__main__":
    # docs = get_cleaned_dir_docs("Data\10200221027_Rajarshi Roy_ (1).pdf")
    docs = get_cleaned_dir_docs("E:\projects\AI research assistant\Data")
    print(docs)
