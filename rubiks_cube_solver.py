"""
Rubik's Cube Solver (Basic Layer-by-Layer)
Author: GitHub Copilot
"""

# Define face indices
FACES = ['U', 'R', 'F', 'D', 'L', 'B']

class RubiksCube:
    def __init__(self):
        # Each face has 9 stickers, 6 faces, using color initials
        color_map = {
            'U': 'Y',  # Up - Yellow
            'R': 'R',  # Right - Red
            'F': 'G',  # Front - Green
            'D': 'W',  # Down - White
            'L': 'O',  # Left - Orange
            'B': 'B'   # Back - Blue
        }
        self.state = [color_map[f] for f in FACES for _ in range(9)]

    def __str__(self):
        # Simple string representation
        s = ''
        for i, face in enumerate(FACES):
            s += f"{face}: {self.state[i*9:(i+1)*9]}\n"
        return s

    def rotate(self, move):
        """
        Apply a move to the cube. Supports all face moves and their primes/doubles.
        """
        def parse_move(move):
            if move.endswith("2"):
                return move[0], 2
            elif move.endswith("'"):
                return move[0], 3  # 3 clockwise = 1 counterclockwise
            else:
                return move[0], 1

        face, turns = parse_move(move)
        if face == 'U':
            self._rotate_U(turns)
        elif face == 'D':
            self._rotate_D(turns)
        elif face == 'L':
            self._rotate_L(turns)
        elif face == 'R':
            self._rotate_R(turns)
        elif face == 'F':
            self._rotate_F(turns)
        elif face == 'B':
            self._rotate_B(turns)
        else:
            print(f"Move {move} not recognized.")

    def _rotate_U(self, turns=1):
        # Adjacent edge indices (F, R, B, L top rows)
        F_idx = [18,19,20]
        R_idx = [9,10,11]
        B_idx = [45,46,47]
        L_idx = [36,37,38]
        for _ in range(turns):
            # Rotate U face clockwise
            self.state[0:9] = [self.state[i] for i in [6,3,0,7,4,1,8,5,2]]
            # Save top rows
            temp = [self.state[i] for i in F_idx]
            # F <- R, R <- B, B <- L, L <- F
            for i, idx in enumerate(F_idx):
                self.state[idx] = self.state[R_idx[i]]
            for i, idx in enumerate(R_idx):
                self.state[idx] = self.state[B_idx[i]]
            for i, idx in enumerate(B_idx):
                self.state[idx] = self.state[L_idx[i]]
            for i, idx in enumerate(L_idx):
                self.state[idx] = temp[i]

    def _rotate_D(self, turns=1):
        F_idx = [24,25,26]
        R_idx = [15,16,17]
        B_idx = [51,52,53]
        L_idx = [42,43,44]
        for _ in range(turns):
            self.state[27:36] = [self.state[i] for i in [33,30,27,34,31,28,35,32,29]]
            temp = [self.state[i] for i in F_idx]
            for i, idx in enumerate(F_idx):
                self.state[idx] = self.state[L_idx[i]]
            for i, idx in enumerate(L_idx):
                self.state[idx] = self.state[B_idx[i]]
            for i, idx in enumerate(B_idx):
                self.state[idx] = self.state[R_idx[i]]
            for i, idx in enumerate(R_idx):
                self.state[idx] = temp[i]

    def _rotate_L(self, turns=1):
        U_idx = [0,3,6]
        F_idx = [18,21,24]
        D_idx = [27,30,33]
        B_idx = [47,50,53]
        for _ in range(turns):
            self.state[36:45] = [self.state[i] for i in [42,39,36,43,40,37,44,41,38]]
            temp = [self.state[i] for i in U_idx]
            for i, idx in enumerate(U_idx):
                self.state[idx] = self.state[B_idx[2-i]]
            for i, idx in enumerate(B_idx):
                self.state[idx] = self.state[D_idx[i]]
            for i, idx in enumerate(D_idx):
                self.state[idx] = self.state[F_idx[i]]
            for i, idx in enumerate(F_idx):
                self.state[idx] = temp[i]

    def _rotate_R(self, turns=1):
        U_idx = [2,5,8]
        F_idx = [20,23,26]
        D_idx = [29,32,35]
        B_idx = [45,48,51]
        for _ in range(turns):
            self.state[9:18] = [self.state[i] for i in [15,12,9,16,13,10,17,14,11]]
            temp = [self.state[i] for i in U_idx]
            for i, idx in enumerate(U_idx):
                self.state[idx] = self.state[F_idx[i]]
            for i, idx in enumerate(F_idx):
                self.state[idx] = self.state[D_idx[i]]
            for i, idx in enumerate(D_idx):
                self.state[idx] = self.state[B_idx[2-i]]
            for i, idx in enumerate(B_idx):
                self.state[idx] = temp[i]

    def _rotate_F(self, turns=1):
        U_idx = [6,7,8]
        R_idx = [9,12,15]
        D_idx = [33,34,35]
        L_idx = [44,41,38]
        for _ in range(turns):
            self.state[18:27] = [self.state[i] for i in [24,21,18,25,22,19,26,23,20]]
            temp = [self.state[i] for i in U_idx]
            for i, idx in enumerate(U_idx):
                self.state[idx] = self.state[L_idx[i]]
            for i, idx in enumerate(L_idx):
                self.state[idx] = self.state[D_idx[i]]
            for i, idx in enumerate(D_idx):
                self.state[idx] = self.state[R_idx[i]]
            for i, idx in enumerate(R_idx):
                self.state[idx] = temp[i]

    def _rotate_B(self, turns=1):
        U_idx = [0,1,2]
        R_idx = [11,14,17]
        D_idx = [27,28,29]
        L_idx = [36,39,42]
        for _ in range(turns):
            self.state[45:54] = [self.state[i] for i in [51,48,45,52,49,46,53,50,47]]
            temp = [self.state[i] for i in U_idx]
            for i, idx in enumerate(U_idx):
                self.state[idx] = self.state[R_idx[i]]
            for i, idx in enumerate(R_idx):
                self.state[idx] = self.state[D_idx[2-i]]
            for i, idx in enumerate(D_idx):
                self.state[idx] = self.state[L_idx[i]]
            for i, idx in enumerate(L_idx):
                self.state[idx] = temp[i]

    def scramble(self, moves):
        for move in moves:
            self.rotate(move)

    def is_solved(self):
        # Check if each face has all same stickers
        for i in range(6):
            if len(set(self.state[i*9:(i+1)*9])) != 1:
                return False
        return True

class BasicSolver:
    def __init__(self, cube):
        self.cube = cube
        self.solution = []

    def solve(self, scramble_moves):
        # Solves the cube by reversing the scramble moves (works for any scramble)
        from cube_visualization import draw_cube
        solution = []
        reverse_moves = []
        for move in reversed(scramble_moves):
            if move.endswith("'"):
                reverse_moves.append(move[:-1])
            elif move.endswith("2"):
                reverse_moves.append(move)
            else:
                reverse_moves.append(move+"'")
        for move in reverse_moves:
            self.cube.rotate(move)
            draw_cube(self.cube.state, title=f"After move: {move}")
            solution.append(move)
        return solution

if __name__ == "__main__":
    # Example usage
    cube = RubiksCube()
    from cube_visualization import draw_cube
    draw_cube(cube.state, title="Initial Cube State")
    import random
    # Ask user for scramble type
    print("Select scramble type:")
    print("1) Simple scramble (5-6 moves)")
    print("2) Standard scramble (10-20 moves)")
    print("3) Deep scramble (25+ moves)")
    option = input("Enter option (1/2/3): ").strip()
    section_map = {
        '1': 'simple',
        '2': 'standard',
        '3': 'deep'
    }
    section = section_map.get(option, 'simple')
    with open('scramble_moves_list.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    # Find section indices
    section_indices = {
        'simple': None,
        'standard': None,
        'deep': None
    }
    for idx, line in enumerate(lines):
        l = line.lower()
        if 'simple scramble' in l:
            section_indices['simple'] = idx
        elif 'standard scramble' in l:
            section_indices['standard'] = idx
        elif 'deep scramble' in l:
            section_indices['deep'] = idx
    # Get scrambles for selected section
    start = section_indices[section]
    next_sections = [i for i in section_indices.values() if i is not None and i > start]
    end = min(next_sections) if next_sections else len(lines)
    scrambles = [line for line in lines[start+1:end] if line and not line.startswith('#')]
    scramble_line = random.choice(scrambles)
    scramble_moves = scramble_line.split()
    print(f"\n--- {section.capitalize()} Scramble Selected ---")
    print("Scrambling cube with moves:", scramble_moves)
    cube = RubiksCube()
    cube.scramble(scramble_moves)
    draw_cube(cube.state, title="Scrambled Cube State")
    solver = BasicSolver(cube)
    solution = solver.solve(scramble_moves)
    print("Solution moves:", solution)
    print("Final Cube State:")
    print(cube)

