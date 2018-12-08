## Tool for conversion of images into "dice-representation"

A command line based tool that will allow the user to convert any picture
to a representation of a six-faced die.

### How to use 

The simplest way to use this script is to clone this github repo and interact with the script via the command line interface. The actual conversion method could
nevertheless be imported and use in other applications or python as well. For cli usage, the following is a recommended procedure

#### 1. Clone

```bash
cd yourfavdir
git clone https://github.com/almaan/diceconverter.git
cd diceconverter
chmod +x dice_converter.py

```

#### 2. Run an example

```bash
./dice_converter --input_file res/test_case1.png --output_file res/test_case1_out.png --die_size 30 --resize_factor 0.2

```
This will use a 30x30 size for each die (representing a pixel in the previous picture) and rescale width and height by a factor of 0.2. If you want to keep the same dimensions of the image as before replace --resize\_factor with --keep\_size


### Example
Below is an example of a conversion from a given picture into a dice-representation, this is also found in the _res_ folder, then in higher resolution <br>
<div align="center">
<img src="https://github.com/almaan/diceconverter/blob/master/res/test_case2.png" alt="drawing" width="500" height="500"/>
</div>
<br>
Turned into
<br>
<div align="center">
<img src="https://github.com/almaan/diceconverter/blob/master/res/test_case2_out.png" alt="drawing" width="500" height="500"/>
</div>

