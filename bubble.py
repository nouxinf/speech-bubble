from PIL import Image, UnidentifiedImageError

def main():
    img1 = None
    while img1 is None:
        try:
            print("What is the path to your file?")
            path = input(">")
            img1 = Image.open(path)
        except FileNotFoundError:
            print("File not found. Check the path.")
        except UnidentifiedImageError:
            print("File is not a valid image.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    img2 = None
    bubble_dir = None
    while img2 == None:
        print("Do you want the speech bubble on the left or right?")
        print("1) left")
        print("2) right")
        bubble_dir = input(">")
        if bubble_dir == "1" or bubble_dir.lower() == "left":
            img2 = Image.open("speechbubbleleft.png")
        else:
            img2 = Image.open("speechbubbleright.png")

    # Resize img2 to match the width of img1 and 20% of img1's height
    img1_width, img1_height = img1.size
    new_height = int(img1_height * 0.2)
    img2_resized = img2.resize((img1_width, new_height), Image.LANCZOS)

    # Paste resized img2 on top of img1 at (0, 0)
    img1.paste(img2_resized, (0, 0), mask=img2_resized)
    img1.show()

if __name__ == "__main__":
    main()
