# Image-Coloration
Using Python and scikit-learn to recolor an image using k-means clustering

Example usage:

If you have image 'rose.jpg' that you want to turn into 5 colors interpolated between black and white, call the following:

`k_means_coloration('rose.jpg', 5)`

To specify your own colors to interpolate between, pass in arguments `color_1` and `color_2` as RGB arrays.

For example, the following would be interpolated between `[255, 0, 0]` (red) and `[0, 0, 255]` (blue).

`k_means_coloration('rose.jpg', 5, color_1=[255, 0, 0], color_2=[0, 0, 255]`

[example input/outpt](https://imgur.com/a/G6SUSds)
