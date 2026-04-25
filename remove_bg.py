from PIL import Image

def remove_white_bg(img_path):
    # Open the image and convert it to RGBA
    img = Image.open(img_path)
    img = img.convert("RGBA")
    
    # Get image data
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Check if the pixel roughly matches a whitish background square
        # Threshold: RGB values > 240 (adjustable based on true bg color)
        if item[0] > 230 and item[1] > 230 and item[2] > 230:
            # Change white/off-white to transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(img_path, "PNG")

remove_white_bg(r"C:\Users\yughr\OneDrive\Desktop\Django Training\shopdjango\ecommerce\store\static\images\logo.png")
print("Successfully removed white background!")
