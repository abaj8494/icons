#!/usr/bin/env bash
#
# generate-icons.sh
#
# Script to generate favicons and related icons from an SVG.
# Requires ImageMagick (magick command). 
# Customize as needed.

# The source SVG file (change if needed)
SVG="abs_hsv.svg"

if [[ ! -f "$SVG" ]]; then
  echo "Error: '$SVG' not found in current directory."
  exit 1
fi

echo "Generating icons from $SVG..."

#
# 1) PNG Favicons (common sizes)
#
for size in 16 32 48 64 128 256; do
  echo " - favicon-${size}x${size}.png"
  magick convert "$SVG" \
    -background none \
    -resize ${size}x${size} \
    favicon-${size}x${size}.png
done

#
# 2) Multi-resolution favicon.ico
#
echo " - favicon.ico (multi-size)"
magick convert \
  favicon-16x16.png \
  favicon-32x32.png \
  favicon-48x48.png \
  favicon-64x64.png \
  favicon-128x128.png \
  favicon-256x256.png \
  favicon.ico

#
# 3) Apple Touch Icon (180x180 is common for iOS)
#
echo " - apple-touch-icon.png (180x180)"
magick convert "$SVG" \
  -background none \
  -resize 180x180 \
  apple-touch-icon.png

#
# 4) Android Chrome Icons
#
echo " - android-chrome-192x192.png"
magick convert "$SVG" \
  -background none \
  -resize 192x192 \
  android-chrome-192x192.png

echo " - android-chrome-512x512.png"
magick convert "$SVG" \
  -background none \
  -resize 512x512 \
  android-chrome-512x512.png

#
# 5) Microsoft Tiles
#
# Common tile sizes: 70x70, 144x144, 150x150, 310x150, 310x310
#
echo " - mstile-70x70.png"
magick convert "$SVG" \
  -background none \
  -resize 70x70 \
  mstile-70x70.png

echo " - mstile-144x144.png"
magick convert "$SVG" \
  -background none \
  -resize 144x144 \
  mstile-144x144.png

echo " - mstile-150x150.png"
magick convert "$SVG" \
  -background none \
  -resize 150x150 \
  mstile-150x150.png

echo " - mstile-310x150.png"
magick convert "$SVG" \
  -background none \
  -resize 310x150 \
  mstile-310x150.png

echo " - mstile-310x310.png"
magick convert "$SVG" \
  -background none \
  -resize 310x310 \
  mstile-310x310.png

#
# 6) Safari Pinned Tab (monochrome SVG)
#
echo " - safari-pinned-tab.svg"
cp "$SVG" safari-pinned-tab.svg

echo "Done!"

