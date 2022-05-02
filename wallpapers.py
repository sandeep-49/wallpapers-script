import os
import requests
import wget
import time
import ctypes

# Step1: Get the wallpaper from the internet.

# Step2: Save the wallpaper to a local directory.

SPI_SETDESKWALLPAPER = 20

def get_wallpaper():
    access_key = os.environ.get("UNSPLASH_ACCESS_KEY")
    url = "https://api.unsplash.com/photos/random?client_id=" + access_key
    params = {
        'query': 'minimal wallpapers',
        'orientation': 'landscape'
    }

    response = requests.get(url, params=params).json()
    image_source = response['urls']['raw']

    # Path to save the wallpapers
    download_path = os.getcwd() + '\Downloads\wallpaper.jpg'
    
    image = wget.download(image_source, download_path)
    return image

# Step3: Set the wallpaper.

def change_wallpaper():
    wallpaper = get_wallpaper()
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)

# Step4: Automate the calls to the script.

def main():
    try:
        # Number of times you want to call the script
        for i in range(3):
            change_wallpaper()
            time.sleep(5)
    except KeyboardInterrupt:
        print('\nHope you liked it?')
    except Exception as e:
        pass

if __name__ == '__main__':
    main()