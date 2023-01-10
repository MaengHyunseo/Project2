# Windmill
Draw a windmill and turn the wings

## Rotation Matrix
```python
def Rmat(deg):
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R
```
Get degree and rotate the surface as much as the degree
## Translate Matrix
```python
def Tmat(a, b):
    H = np.eye(3)
    H[0, 2] = a
    H[1, 2] = b
    return H
```
Get coordinate and move the surface at the coordinate
## Draw Wings
```python
wing_height = 300
wing = np.array([[0, -80, 1], [wing_height, 0, 1], [0, 80, 1]])

while True:
    degree += 1

    H1 = Tmat(380, 330) @ Rmat(degree) @ Tmat(-wing_height, 0)
    wing1 = remove3D(H1 @ wing.T)
    H2 = H1 @ Tmat(wing_height, 0) @ Rmat(90) @ Tmat(-wing_height, 0)
    wing2 = remove3D(H2 @ wing.copy().T)
    H3 = H2 @ Tmat(wing_height, 0) @ Rmat(90) @ Tmat(-wing_height, 0)
    wing3 = remove3D(H3 @ wing.copy().T)
    H4 = H3 @ Tmat(wing_height, 0) @ Rmat(90) @ Tmat(-wing_height, 0)
    wing4 = remove3D(H4 @ wing.copy().T)

    pygame.draw.polygon(screen, WOOD, wing1)
    pygame.draw.polygon(screen, BLACK, wing1, 5)
    pygame.draw.polygon(screen, WOOD, wing2)
    pygame.draw.polygon(screen, BLACK, wing2, 5)
    pygame.draw.polygon(screen, WOOD, wing3)
    pygame.draw.polygon(screen, BLACK, wing3, 5)
    pygame.draw.polygon(screen, WOOD, wing4)
    pygame.draw.polygon(screen, BLACK, wing4, 5)
```
First, draw a triangle(it will be a wing). Then, translate it to our center of rotation, (380, 330) and rotate it amount of degree value. Since it rotates based on the base of triangle, move it up to the height so that it can rotate based on the vertex.
Second wing should be the same as first wing but have angle difference as much as 90 degrees. To do that, translate the triangle back to the height and rotate 90 degrees, and translate it to the amount of its height.

# Clock
```python
def degrees_to_pos(R, theta):
    y = np.cos(2 * np.pi * theta / 360) * R
    x = np.sin(2 * np.pi * theta / 360) * R
    return x + 400 - 15 , -(y - 400) - 15
```
This is the function for converting degrees to position coordinate. It gets radius and theta value and calculate x, y position.
To make it locate based on the center of window, + 400(= window width / 2) to x coordinate and - 400(= window height / 2) to y coordinate. -15 is to correct the result that is slightly skewed from the center.
```python
current_time = datetime.datetime.now()
s = current_time.second
m = current_time.minute
h = current_time.hour

# second hand
R = 300
theta = s * (360 / 60)
pygame.draw.line(screen, RED, (400, 400), degrees_to_pos(R, theta), 8)

# minute hand
R = 350
theta = (m + s / 60) * (360 / 60)
pygame.draw.line(screen, BLACK, (400, 400), degrees_to_pos(R, theta), 8)

# hour hand
R = 210
theta = (h + m / 60) * (360 / 12)
pygame.draw.line(screen, BLACK, (400, 400), degrees_to_pos(R, theta), 8)
```
The hour hand is drawn to a length of 210, the minute hand to a length of 350, and the second hand to a length of 300. Calculating the degree of second hand is simple. It takes 60 seconds to turn 360 degrees, so divide 360 by 60 and multiply the current seconds. The minute hand is similar but it have to be influenced by seconds. So, add the amount of seconds devided by 60. The hour hand is the same as above.
