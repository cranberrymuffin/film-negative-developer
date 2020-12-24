# Film Negative Converter

A simple script which inverts and color corrects film negatives.

## How it works:

1. Takes the cropped negative
2. Inverts by subtracting the image from 255
3. Simple correction mapping pixels in each color channel to 0-255 range

## Instructions

To run: `python3 negative_developer.py file1.png file2.png....`

## Examples

Input: A *cropped* film negative:

![Input](https://github.com/cranberrymuffin/film-roll-developer/blob/main/data/negative_3.png)

Output:

![Output](https://github.com/cranberrymuffin/film-roll-developer/blob/main/results/processed_3.png)
