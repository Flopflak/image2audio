# image2audio

This project aims to encode image data into an audio file and subsequently decode it back into an image. The primary use case is transmitting image data over mediums designed for audio communication, such as radio signals. The project offers a simple Python-based solution to convert images to audio and back, with considerations for image resizing and grayscale conversion.

## Features

- Image Encoding: The encode.py script converts an image into a normalized list of grayscale values, which is then converted into an audio signal and saved as a .wav file.
- Image Decoding: The decode.py script takes the .wav audio file and extracts the normalized grayscale data. This data is then reconstructed back into the image, preserving the original dimensions.
## Usage

1. Run encode.py with an image file to create the corresponding audio file.
2. Run decode.py with the audio file to reconstruct the image.
   
**Note:** This project is a simple implementation and may not handle all edge cases. Further modifications may be needed based on specific requirements or constraints.

## Example
### Original image
<img src=https://github.com/Flopflak/image2audio/assets/77279409/1d2ddc86-f6ac-4875-a5b0-ab153968150a style="width: 500px;">

### Reconstructed image
<img src=https://github.com/Flopflak/image2audio/assets/77279409/aedeb085-9e28-4ff9-b675-1eb71237be01 style="width: 500px;">
