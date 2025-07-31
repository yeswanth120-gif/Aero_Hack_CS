"""
Rubik's Cube Visualization using matplotlib
Author: GitHub Copilot
"""
def draw_cube(state, title=None):
    """
    Prints a 3x3 Rubik's Cube net from the state array in ASCII.
    state: list of 54 stickers
    """
    face_order = ['U', 'L', 'F', 'R', 'B', 'D']
    faces = {f: state[i*9:(i+1)*9] for i, f in enumerate(face_order)}
    # Use color initials for each sticker, not face letters
    color_map = {
        'Y': 'Y', 'O': 'O', 'G': 'G', 'W': 'W', 'R': 'R', 'B': 'B'
    }
    def face_to_str(face):
        return [' '.join([color_map.get(c, c) for c in face[i*3:(i+1)*3]]) for i in range(3)]
    U = face_to_str(faces['U'])
    L = face_to_str(faces['L'])
    F = face_to_str(faces['F'])
    R = face_to_str(faces['R'])
    B = face_to_str(faces['B'])
    D = face_to_str(faces['D'])
    if title:
        print(f"\n{title}")
    # Print U face
    for row in U:
        print("      " + row)
    # Print L F R B faces
    for i in range(3):
        print(f"{L[i]}   {F[i]}   {R[i]}   {B[i]}")
    # Print D face
    for row in D:
        print("      " + row)
