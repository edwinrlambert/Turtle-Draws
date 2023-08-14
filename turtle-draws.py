import turtle
import colorsys
import random
from PIL import Image
import io
import os
import time


# * Function to setup turtle.
def setup_turtle():
    try:
        # Initialize turtle variables.
        t = turtle.Turtle()
        screen = turtle.Screen()

        # Initialize screen options.
        screen.screensize(canvwidth=screen.window_width(),
                          canvheight=screen.window_height())
        screen.bgcolor("black")
        screen.setup(width=1.0, height=1.0)

        # Set turtle boundaries to match canvas size.
        left_bound = -screen.window_width() / 2
        right_bound = screen.window_width() / 2
        bottom_bound = -screen.window_height() / 2
        top_bound = screen.window_height() / 2
        turtle.setworldcoordinates(
            left_bound, bottom_bound, right_bound, top_bound)

        # Set other turtle properties.
        t.color("white")
        t.speed(0)
        t.pensize(3)

        return t, screen
    except turtle.TurtleGraphicsError as te:
        print(f"An error occurred while setting up the turtle: {te}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to draw random circles.
def random_circle(t):
    radius = random.randint(1, 100)
    t.circle(radius)


# Function to draw random dots.
def random_dot(t):
    size = random.randint(1, 20)
    t.dot(size)


# Function to move in a random speed.
def random_speed(t):
    speed = random.randint(0, 10)
    t.speed(speed)


# * Function to draw random patterns.
def draw_random_patterns(t, iterations=1000):
    commands = [t.fd, t.bk, t.rt, t.lt,
                random_circle, random_dot, random_speed]

    # Disable automatic updating of canvas.
    turtle.tracer(0)
    turtle.penup()
    turtle.hideturtle()

    n = 70
    h = 0
    for _ in range(0, random.randint(0, iterations)):
        c = colorsys.hsv_to_rgb(h, 1, 0.8)
        h += 1/n

        for i in range(5):
            try:
                t.color(c)
                t.width(i)
                random_command = random.choice(commands)
                execute_random_command(t, random_command)
                turtle.update()
            except turtle.TurtleGraphicsError as te:
                print(f"Turtle Graphics Error: {te}")
            except ValueError as ve:
                print(f"Value Error: {ve}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


# * Function to execute random turtle commands.
def execute_random_command(t, command):
    try:
        if command in [t.fd, t.bk, t.rt, t.lt]:
            distance = random.randint(1, 200)
            command(distance)
        else:
            command(t)
    except Exception as e:
        print(
            f"An error occurred while executing the command {command.__name__}: {e}")


# * Function to Save the Image.
def save_image(screen):
    timestamp = int(time.time())
    image_folder = "./turtle-draws-img"
    image_name = f"{image_folder}/turtle_art_{timestamp}.png"

    # Ensure the image directory exists
    if not os.path.exists(image_folder):
        try:
            os.makedirs(image_folder)
        except OSError as e:
            print(
                f"Error occurred while creating the directory {image_folder}: {e}")
            return

    try:
        canvas_ps = screen.getcanvas().postscript(colormode="color")
        image = Image.open(io.BytesIO(canvas_ps.encode("UTF-8")))
        image_rgb = image.convert("RGBA")
        pixels = image_rgb.load()
        width, height = image_rgb.size

        for y in range(height):
            for x in range(width):
                if pixels[x, y] == (255, 255, 255, 255):
                    pixels[x, y] = (0, 0, 0, 255)

        # Save the image.
        image_rgb.save(image_name)

    except IOError as e:
        print(f"IOError occurred while saving the file: {e}")
    except Exception as e:
        print(f"Unexpected error occurred while saving the file: {e}")


# * Function to Close Turtle.
def close_turtle(screen):
    # Close turtle screen
    try:
        screen.bye()
        turtle.done()
    except turtle.Terminator:
        print("Turtle has already been terminated.")
    except Exception as e:
        print(f"Unexpected error encountered: {e}")
    finally:
        turtle.bye()


# * Main Function.
def main():
    t, screen = setup_turtle()
    draw_random_patterns(t)
    save_image(screen)
    close_turtle(screen)


# * Run Main Function.
if __name__ == "__main__":
    main()
