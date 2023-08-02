# image2audio

This project aims to encode image data into an audio file and subsequently decode it back into an image. The primary use case is transmitting image data over mediums designed for audio communication, such as radio signals. The project offers a simple Python-based solution to convert images to audio and back, with considerations for image resizing and grayscale conversion.

## Features

- Image Encoding: The encode.py script converts an image into a normalized list of grayscale values, which is then converted into an audio signal and saved as a .wav file.
- Image Decoding: The decode.py script takes the .wav audio file and extracts the normalized grayscale data. This data is then reconstructed back into the image, preserving the original dimensions.
## Usage

1. Run encode.py with an image file to create the corresponding audio file.
2. Run decode.py with the audio file to reconstruct the image.
   
**Note:** This project is a simple implementation and may not handle all edge cases. Further modifications may be needed based on specific requirements or constraints.

## Example [^1]
### Original image
![image](https://github.com/Flopflak/image2audio/assets/77279409/1c2562ff-d040-4504-aab3-e1aeb6e560d4)

### Reconstructed image
![image](https://github.com/Flopflak/image2audio/assets/77279409/5e49d128-5035-456e-bf94-e00ef0d057a7)


[^1]: The reconstructed file is for some reason 4 times bigger than the original one. I have no idea why.
