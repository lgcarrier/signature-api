import requests
import os

# Base URL of the running API
BASE_URL = "http://localhost:8000"
ENDPOINT = f"{BASE_URL}/generate-signature/"

# Test cases with different fonts
test_cases = [
    {
        "name": "John Smith",
        "font_style": "GreatVibes",
        "description": "Valid name with GreatVibes",
        "expected_status": 200,
        "output_file": "john_smith_greatvibes.png"
    },
    {
        "name": "",
        "font_style": "Sacramento",
        "description": "Empty name (should fail)",
        "expected_status": 400,
        "output_file": None
    },
    {
        "name": "Alexandra Marie",
        "font_style": "DancingScript-Bold",
        "description": "Long name with DancingScript-Bold",
        "expected_status": 200,
        "output_file": "alexandra_marie_dancingscriptbold.png"
    },
    {
        "name": "Emma Jones",
        "font_style": "Parisienne",
        "description": "Name with Parisienne",
        "expected_status": 200,
        "output_file": "emma_jones_parisienne.png"
    },
    {
        "name": "Liam Carter",
        "font_style": "Allura",
        "description": "Name with Allura",
        "expected_status": 200,
        "output_file": "liam_carter_allura.png"
    }
]

def test_signature_api():
    print("Starting API tests...\n")
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['description']}")
        payload = {"name": test['name'], "font_style": test['font_style']}
        
        # Send POST request
        try:
            response = requests.post(ENDPOINT, json=payload, timeout=5)
            status_code = response.status_code
            
            # Check status code
            if status_code == test['expected_status']:
                if status_code == 200:
                    # Save the image with a unique filename
                    output_file = test['output_file']
                    with open(output_file, "wb") as f:
                        f.write(response.content)
                    print(f"  Success: Status {status_code}, Saved as '{output_file}'")
                    
                    # Verify file exists
                    if os.path.exists(output_file):
                        print(f"  File '{output_file}' created successfully")
                    else:
                        print(f"  Error: File '{output_file}' not found after saving")
                else:
                    print(f"  Success: Status {status_code} (expected error), Response: {response.text}")
            else:
                print(f"  Failed: Expected status {test['expected_status']}, got {status_code}")
                print(f"  Response: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"  Error: Failed to connect to API - {e}")
        
        print("-" * 50)

def cleanup():
    print("\nCleaning up test files...")
    for test in test_cases:
        if test['output_file'] and os.path.exists(test['output_file']):
            os.remove(test['output_file'])
            print(f"Removed '{test['output_file']}'")

if __name__ == "__main__":
    test_signature_api()
    cleanup()
    print("Tests completed.")