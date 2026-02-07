import re

def extract_endpoints(code_text: str):
    """
    Extract FastAPI-style endpoints from code.
    Example: @app.get("/users")
    Returns list of dicts.
    """

    pattern = r'@app\.(get|post|put|delete|patch)\("([^"]+)"\)'
    matches = re.findall(pattern, code_text)

    endpoints = []
    for method, path in matches:
        endpoints.append({
            "method": method.upper(),
            "path": path
        })

    return endpoints
