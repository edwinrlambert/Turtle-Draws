# Turtle Draws

A Python script that uses the turtle module to create mesmerizing random drawings and save them as PNG images.

## Features

* Initializes a full-screen turtle canvas with predefined settings.
* Draws random patterns consisting of random circles, dots, and movements.
* Saves the created artwork as a .png image in the turtle-draws-img directory.
* Closes the turtle window after saving the image.

## Dependencies

* `turtle`: Built-in Python module for drawing.
* `colorsys`: Built-in Python module for color system conversions.
* `random`: Built-in Python module for generating random numbers.
* `PIL (Pillow)`: Python Imaging Library, used for saving the turtle drawings as images.

## Installation

1. **Clone the code from this repository:**

   ```
   https://github.com/edwinrlambert/Turtle-Draws.git
   ```

2. **Create a virtual environment using the `virtualenv` command.**

   Virtual environments are created so that the libraries that are installed and used for this project won't impact any other libraries installed for other projects. This creates an encapsulation for the project so that anything installed for this project can only be used for this project.

   Do the following in the terminal.

   **Installing virtualenv (this can be done globally)**

   ```py
   pip install virtualenv
   ```

   **Creating a virtual environment**

   ```py
   virtualenv project-name-env
   ```

   where `project-name-env` can be any name that you want to give. Example: `virtualenv turtle-draws-env`

   <small>Having **-env** at the end is not mandatory, it gives an indication that helps us understand that this is a virtual environment directory.</small>

   **Activate the virtual environment to start using it.**

   ```
   project-name-env/Scripts/activate
   ```

3. **Install the necessary libraries for the project.**

   Use the **requirements.txt** file to install all the dependencies/libraries used in this project.

   Since we're installing this in a virtual environment, all the libraries will be installed within this environment.

   To install packages from a **requirements.txt** file, you would use:

   ```py
   pip install -r requirements.txt
   ```

   This will install all of the packages listed in the requirements.txt file.


## How to Run
1. Ensure you have all the dependencies installed.
2. Run the script:
    ```
    python turtle-draws.py
    ```
3. Check the turtle-draws-img directory for the saved artwork.

## Functions
* `setup_turtle()`: Sets up the turtle with predefined settings.
* `random_circle(t)`: Draws a random circle.
* `random_dot(t)`: Draws a random dot.
* `random_speed(t)`: Sets a random speed for the turtle.
* `draw_random_patterns(t, iterations=1000)`: Draws random patterns on the screen.
* `save_image(screen)`: Saves the drawing as a .png image.
* `close_turtle(screen)`: Closes the turtle window.

## License
This project is open-sourced under the MIT License.