import os
import zipfile
from PIL import Image

def extract_epub(epub_path, extract_to):
    """Extracts the EPUB file to a specified directory."""
    with zipfile.ZipFile(epub_path, 'r') as epub_zip:
        epub_zip.extractall(extract_to)

def repackage_epub(clean_dir, output_path):
    """Creates a new EPUB file from the cleaned directory."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
        for root, _, files in os.walk(clean_dir):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, clean_dir)
                epub_zip.write(full_path, relative_path)

def mirror_images(image_dir):
    """Mirrors all images vertically."""
    for image_file in os.listdir(image_dir):
        if image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_path = os.path.join(image_dir, image_file)
            image = Image.open(image_path)

            # Mirror the image vertically
            mirrored_image = image.transpose(Image.FLIP_TOP_BOTTOM)

            # Save the mirrored image back to the same path
            mirrored_image.save(image_path)
            print(f"Mirrored: {image_file}")

def main():
    import sys

    if len(sys.argv) != 2:
        print("Usage: python clean_epub.py <epub_file>")
        sys.exit(1)

    epub_path = sys.argv[1]
    if not epub_path.endswith('.epub') or not os.path.exists(epub_path):
        print("Error: Provide a valid EPUB file.")
        sys.exit(1)

    base_name = os.path.splitext(epub_path)[0]
    output_path = f"{base_name}-clean.epub"
    temp_dir = f"{base_name}_temp"

    # Extract EPUB
    print("Extracting EPUB...")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    extract_epub(epub_path, temp_dir)
    print("Extraction complete.\n")

    # Mirror images
    image_dir = os.path.join(temp_dir, 'images')
    if os.path.exists(image_dir):
        print("Mirroring images vertically...\n")
        mirror_images(image_dir)
    else:
        print("No images directory found.\n")

    # Repackage cleaned EPUB
    print("Repackaging EPUB...")
    repackage_epub(temp_dir, output_path)
    print(f"Cleaned EPUB saved as {output_path}")

    # Clean up temporary files
    print("Cleaning up temporary files...")
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(temp_dir)
    print("Done!")

if __name__ == "__main__":
    main()
