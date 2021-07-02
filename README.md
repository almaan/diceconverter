# Tool for conversion of images into "dice-representation"

A command line based tool that will allow the user to convert any picture
to a representation of a six-faced die.

## How to use 

The simplest way to use this script is to clone this github repo and interact with the script via the command line interface. The actual conversion method could
nevertheless be imported and use in other applications or python as well. For cli usage, the following is a recommended procedure

### 1. Clone

```bash
cd yourfavdir
git clone https://github.com/almaan/diceconverter.git
cd diceconverter
chmod +x dice_converter.py

```

## 2. Example Runs
There are two different _modes_ in which you can run this tool: _default_ and
_custom_ mode. In the  default mode you'll be using the standard die face
templates provided in the `faces` folder, where each face has one specific image
associated with it. In the custom mode you can specify your very own face
templates, with several alternative templates associated with each image (e.g.,
different rotations). Below are two examples, one on how to run each mode.

### Alternative 1 : Default mode

```bash
./dice_converter --image_file res/test_case1.png --output_file res/test_case1_out.png --die_size 30 --resize_factor 0.2

```
This will use a 30x30 size for each die (representing a pixel in the previous
picture) and rescale width and height by a factor of 0.2. If you want to keep
the same dimensions of the image as before replace --resize\_factor with
--keep\_size

### Alternative 2 : Custom mode

To run in custom mode, you will have to create a YAML _design file_, where you
specify the path to each image and which face it is associated with. Below,
you'll see an example of such a design file:


```yaml
1:
    - faces_2/001.png
2:
    - faces_2/alt1_002.png
    - faces_2/alt2_002.png
3:
    - faces_2/alt1_003.png
    - faces_2/alt2_003.png
4:
    - faces_2/004.png
5:
    - faces_2/005.png
6:
    - faces_2/alt1_006.png
    - faces_2/alt2_006.png
```

I've used relative paths here, but it might be safer to use full paths depending
on your OS and where you keep your images.  In order to be able to read YAML
files in python, you need to install `PyYAML`, which you can get from `pip` by
running your equivalent to:

```bash
pip install pyyaml
```

Once you've assembled a design file and installed `pyyaml`, we can run a very
similar command to the one used in default mode:

```bash
./dice_converter --image_file res/test_case1.png --output_file
res/test_case1_out.png --die_size 30 --resize_factor 0.2 --design_file design.yaml

```

There is only one difference here to the previous command, we've added
`--design_file design.yaml` which tells the tool to not use the default face
images, but rather the ones specified in the design file. In the end this will
render the same type of output as default mode, but with the custom images, if
you list several images for one face (as done in the example for 2,3 and 6) any
time one of these faces are supposed to be inserted, one of these images will
randomly be selected.


### Output Example
Below is an example of a conversion from a given picture into a
dice-representation (using default mode), this is also found in the _res_
folder, then in higher resolution <br>
<div align="center">
<img src="https://github.com/almaan/diceconverter/blob/master/res/test_case2.png" alt="drawing" width="500" height="500"/>
</div>
<br>
Turned into
<br>
<div align="center">
<img src="https://github.com/almaan/diceconverter/blob/master/res/test_case2_out.png" alt="drawing" width="500" height="500"/>
</div>

### Credits
- Thanks to <a href="https://github.com/holysanctity">holysanctity</a> for
  making the suggestion to add the ability to choose between several different
  images for each face.
