import math
from noise import pnoise2

# Constants
NUM_VERTS_X = 30
NUM_VERTS_Y = 30
totalVerts = NUM_VERTS_X * NUM_VERTS_Y
totalTriangles = 2 * (NUM_VERTS_X - 1) * (NUM_VERTS_Y - 1)
offset = -50.0
TRIANGLE_SIZE = 1.0
waveheight = 0.3

# Initialize vertex and index arrays
gGroundVertices = [0.0] * totalVerts * 3
gGroundIndices = [0] * totalTriangles * 3

# Generate vertices
for i in range(NUM_VERTS_X):
    for j in range(NUM_VERTS_Y):
        idx = (i + j * NUM_VERTS_X) * 3
        gGroundVertices[idx] = (i - NUM_VERTS_X * 0.5) * TRIANGLE_SIZE
        gGroundVertices[idx + 1] = (j - NUM_VERTS_Y * 0.5) * TRIANGLE_SIZE
        # gGroundVertices[idx + 2] = waveheight * math.sin(float(i)) * math.cos(float(j) + offset)
        gGroundVertices[idx + 2] = pnoise2(i * 0.1, j * 0.1, octaves = 4) * waveheight;

# Generate indices
index = 0
for i in range(NUM_VERTS_X - 1):
    for j in range(NUM_VERTS_Y - 1):
        gGroundIndices[index] = 1 + j * NUM_VERTS_X + i
        gGroundIndices[index + 1] = 1 + j * NUM_VERTS_X + i + 1
        gGroundIndices[index + 2] = 1 + (j + 1) * NUM_VERTS_X + i + 1
        gGroundIndices[index + 3] = 1 + j * NUM_VERTS_X + i
        gGroundIndices[index + 4] = 1 + (j + 1) * NUM_VERTS_X + i + 1
        gGroundIndices[index + 5] = 1 + (j + 1) * NUM_VERTS_X + i
        index += 6

# Write to an OBJ file
with open("mod_terrain.obj", "w") as obj_file:
    # Write the object name
    obj_file.write("o Terrain\n")

    # Write vertices
    for i in range(totalVerts):
        obj_file.write(f"v {gGroundVertices[i * 3]} {gGroundVertices[i * 3 + 1]} {gGroundVertices[i * 3 + 2]}\n")

    # Write faces
    for i in range(totalTriangles):
        obj_file.write(f"f {gGroundIndices[i * 3]} {gGroundIndices[i * 3 + 1]} {gGroundIndices[i * 3 + 2]}\n")

print("OBJ file 'mod_terrain.obj' has been created successfully.")
