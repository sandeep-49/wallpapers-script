# Wallpapers Script

A simple python automation script to fetch wallpaper from Unsplash and also update as desktop wallpaper.

To set the wallpaper in MacOS, remove SPI_SETDESKWALLPAPER parameter and replace:

```
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)
```

with

```
cmd = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

subprocess.Popen(cmd%wallpaper, shell=True)
subprocess.call(["killall Dock"], shell=True)
```
