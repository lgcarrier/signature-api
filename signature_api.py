from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware  # Add CORS middleware
from PIL import Image, ImageDraw, ImageFont
import os
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="Signature Generator API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://luxury-sunflower-6bd87f.netlify.app/"],  # Allows all origins (adjust for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Pydantic model for request validation
class SignatureRequest(BaseModel):
    name: str
    font_style: str = "GreatVibes"  # Default font

# Font mapping
FONTS = {
    "Sacramento": "fonts/Sacramento/Sacramento-Regular.ttf",
    "GreatVibes": "fonts/Great_Vibes/GreatVibes-Regular.ttf",
    "DancingScript-Regular": "fonts/Dancing_Script/static/DancingScript-Regular.ttf",
    "DancingScript-Medium": "fonts/Dancing_Script/static/DancingScript-Medium.ttf",
    "DancingScript-SemiBold": "fonts/Dancing_Script/static/DancingScript-SemiBold.ttf",
    "DancingScript-Bold": "fonts/Dancing_Script/static/DancingScript-Bold.ttf",
    "Parisienne": "fonts/Parisienne/Parisienne-Regular.ttf",
    "Allura": "fonts/Allura/Allura-Regular.ttf"
}

# Signature generation function
def generate_signature(name: str, font_style: str, output_file: str = "signature.png"):
    # Validate font style
    if font_style not in FONTS:
        raise ValueError(f"Invalid font style. Choose from: {', '.join(FONTS.keys())}")
    
    # Image settings
    width, height = 600, 100
    background_color = (255, 255, 255)  # White background
    ink_color = (0, 0, 255)  # Blue ink

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load the selected font
    try:
        font = ImageFont.truetype(FONTS[font_style], 40)
    except Exception as e:
        raise ValueError(f"Failed to load font '{font_style}': {str(e)}")

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), name, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Draw the signature in blue ink
    draw.text((x, y), name, font=font, fill=ink_color)

    # Save the image
    image.save(output_file)
    return output_file

# API endpoint to generate and return the signature
@app.post("/generate-signature/", response_class=FileResponse)
async def create_signature(request: SignatureRequest):
    name = request.name.strip()
    font_style = request.font_style

    if not name:
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    
    # Generate the signature file
    output_file = "signature.png"
    try:
        generate_signature(name, font_style, output_file)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Return the file as a response
    if os.path.exists(output_file):
        return FileResponse(output_file, media_type="image/png", filename=f"{name}_signature.png")
    else:
        raise HTTPException(status_code=500, detail="Failed to generate signature")

# Cleanup (optional)
@app.on_event("shutdown")
def cleanup():
    output_file = "signature.png"
    if os.path.exists(output_file):
        os.remove(output_file)

# Run the app (for testing locally)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)