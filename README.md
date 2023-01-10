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
