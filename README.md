# Signature Generator API

This project is a simple Signature Generator API built with FastAPI. It creates custom signature images using various font styles extracted from a local fonts directory.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Font Licenses](#font-licenses)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Signature Generator API generates a signature image by rendering a given name using a specified font. The API validates the inputs and returns the generated image. This is particularly useful for applications that require customizable digital signatures.

## Features

- **Dynamic Signature Generation:** Generate signatures using different font styles.
- **FastAPI Backend:** Lightweight and performant.
- **PIL for Image Processing:** High-quality image rendering of signatures.
- **Automatic Testing:** Sample tests to validate API functionality.

## Prerequisites

- **Python 3.7+**
- **macOS** (the project was developed and tested on macOS)
- **Pip**

Ensure you have a working Python environment on your machine. You may consider using a virtual environment to manage dependencies.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd signature_api
   ```

2. **Install Dependencies:**

   Install required packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Fonts Directory:**

   The project includes a `fonts` directory with various font styles. Ensure that this directory is present at the root of the project.

## Usage

### Running the API

Start the API using Uvicorn:

```bash
uvicorn signature_api:app --reload
```

This will run the API on `http://localhost:8000`.

### API Endpoints

#### POST /generate-signature/

- **Description:** Generates a signature image based on the provided name and selected font.
- **Request Body:**
  - `name` (string): The name to be rendered as a signature. Must not be empty.
  - `font_style` (string): The font to use. Valid options are:
    - `Sacramento`
    - `GreatVibes`
    - `DancingScript-Regular`
    - `DancingScript-Medium`
    - `DancingScript-SemiBold`
    - `DancingScript-Bold`
    - `Parisienne`
    - `Allura`

- **Response:**
  - **200 OK:** Returns the generated signature image in PNG format with a filename formatted as `<name>_signature.png`.
  - **400 Bad Request:** If input validation fails (e.g., empty name or invalid font style).
  - **500 Internal Server Error:** If the signature generation fails for any reason.

#### Example Request using curl:

```bash
curl -X POST \
  http://localhost:8000/generate-signature/ \
  -H 'Content-Type: application/json' \
  -d '{"name": "John Doe", "font_style": "GreatVibes"}' --output john_doe_signature.png
```

## Testing

A set of tests is provided to validate the API functionality. To run the tests, execute the following command in the project directory:

```bash
python test_signature_api.py
```

The tests cover various scenarios including valid and invalid inputs, and verify that the corresponding image files are created as expected.

## Project Structure

```
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
├── signature_api.py   # FastAPI application
├── test_signature_api.py  # Test cases for the API
└── fonts/             # Directory containing fonts and their respective licenses
    ├── Allura/
    │   ├── Allura-Regular.ttf
    │   └── OFL.txt
    ├── Dancing_Script/
    │   ├── DancingScript-VariableFont_wght.ttf
    │   ├── OFL.txt
    │   ├── README.txt
    │   └── static/
    │       ├── DancingScript-Bold.ttf
    │       ├── DancingScript-Medium.ttf
    │       ├── DancingScript-Regular.ttf
    │       └── DancingScript-SemiBold.ttf
    ├── Great_Vibes/
    │   ├── GreatVibes-Regular.ttf
    │   └── OFL.txt
    ├── Parisienne/
    │   ├── Parisienne-Regular.ttf
    │   └── OFL.txt
    └── Sacramento/
        ├── Sacramento-Regular.ttf
        └── OFL.txt
```

## Font Licenses

Most fonts are distributed under the SIL Open Font License (OFL). Please refer to the respective `OFL.txt` files in each font directory for license details.

## Troubleshooting

- **API Connection Issues:**
  - Ensure that the API is running on `http://localhost:8000`.
  - Check if the port is already in use or firewall restrictions on macOS.

- **Font Loading Errors:**
  - Verify that the fonts in the `fonts` directory are correctly referenced in `signature_api.py`.

- **Test Failures:**
  - Check the output in your terminal for any error messages.
  - Ensure that the generated image files are not locked or in use by another process.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is open source and available under the MIT License. For font licenses, refer to the `OFL.txt` files within each font directory.
