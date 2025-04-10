from PIL import Image



def rgb_to_cmyk(image_path, output_path):
    img = Image.open(image_path).convert("RGB")
    cmyk_img = img.convert("CMYK")
    cmyk_img.save(output_path)
    print(f"Saved CMYK image to : {output_path}")



if __name__ == "__main__":
    input_image = "DSC_1547.jpg"
    output_image = "output_cmyk.jpg"
    rgb_to_cmyk(input_image, output_image)