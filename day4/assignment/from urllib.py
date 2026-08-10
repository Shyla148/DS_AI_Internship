from urllib.parse import urlparse, parse_qs

def extract_url_parameters(url):
    """Parses a URL and extracts its query string parameters."""
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    return params

# Program execution
test_url = "https://example.com/search?q=python&page=2&lang=en"
query_params = extract_url_parameters(test_url)
print("URL Query Parameters:", query_params)