import ctypes

SPI_SETDESKWALLPAPER = 20

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if __name__ == "__main__":
    image_path = input("Enter the path of the image you want to set as wallpaper: ")
    change_wallpaper(image_path)
    print("Wallpaper changed successfully!")