def search_keyword(document_path, keyword):

    with open(document_path, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if keyword.lower() in line.lower():
                return f"Keyword '{keyword}' found on line {line_number}"

    return f"Keyword '{keyword}' not found."

# Example usage
document_path = r"C:\Users\andre\source\repos\Custom SIT tester for Python\Inspect.txt" 
keyword = "Machine Learning"
result = search_keyword(document_path, keyword)
print(result)



