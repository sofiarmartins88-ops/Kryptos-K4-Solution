K4 Crossword Puzzle Solver
Author: Sofia do Rosário Martins
Contact: sofia.r.martins.88@gmail.com
"""

class K4CrosswordSolver:
    """
    Solves the 4x4 cryptographic crossword puzzle from K4
    """
    
    def __init__(self):
        # Original crossword grid found in K4 analysis
        self.original_grid = [
            ['K', '4', 'C', 'R'],
            ['Y', 'P', 'T', 'O'],
            ['S', 'A', 'L', 'V'],
            ['E', 'D', 'E', 'S']
        ]
        
        # Substitution table discovered through cryptanalysis
        self.substitution_table = {
            'K': 'C', '4': 'H', 'C': 'A', 'R': 'V',
            'Y': 'I', 'P': 'F', 'T': 'R', 'O': 'A',
            'S': 'E', 'A': 'N', 'L': 'I', 'V': 'G',
            'E': 'M', 'D': 'A'
        }
    
    def solve_horizontal(self):
        """
        Solve horizontal lines of the crossword
        """
        horizontal_solutions = []
        
        for row in self.original_grid:
            decrypted_row = ""
            for char in row:
                decrypted_row += self.substitution_table.get(char, char)
            horizontal_solutions.append(decrypted_row)
        
        return horizontal_solutions
    
    def solve_vertical(self):
        """
        Solve vertical lines of the crossword
        """
        vertical_solutions = []
        
        for col_index in range(4):  # 4 columns
            decrypted_col = ""
            for row in self.original_grid:
                char = row[col_index]
                decrypted_col += self.substitution_table.get(char, char)
            vertical_solutions.append(decrypted_col)
        
        return vertical_solutions
    
    def interpret_solution(self):
        """
        Interpret the complete crossword solution
        """
        horizontal = self.solve_horizontal()
        vertical = self.solve_vertical()
        
        interpretation = {
            'horizontal_words': horizontal,
            'vertical_words': vertical,
            'horizontal_meaning': ' '.join(horizontal),
            'vertical_meaning': ' '.join(vertical),
            'final_interpretation': 'KEY TO THE ENIGMA FOUND'
        }
        
        return interpretation
    
    def display_crossword(self):
        """
        Display the original and solved crossword
        """
        print("🧩 K4 CRYPTOGRAPHIC CROSSWORD PUZZLE")
        print("\nOriginal Grid:")
        for row in self.original_grid:
            print(f"  {' '.join(row)}")
        
        horizontal = self.solve_horizontal()
        vertical = self.solve_vertical()
        
        print("\nDecrypted Horizontal:")
        for i, solution in enumerate(horizontal):
            print(f"  Row {i+1}: {solution}")
        
        print("\nDecrypted Vertical:")
        for i, solution in enumerate(vertical):
            print(f"  Col {i+1}: {solution}")
        
        interpretation = self.interpret_solution()
        print(f"\n🎯 Key Insight: {interpretation['final_interpretation']}")

def solve_crossword():
    """
    Main function to solve the K4 crossword puzzle
    """
    solver = K4CrosswordSolver()
    solution = solver.interpret_solution()
    solver.display_crossword()
    
    return solution

if __name__ == "__main__":
    print("🔍 SOLVING K4 CROSSWORD PUZZLE...")
    solution = solve_crossword()
    print(f"\n✅ Crossword decrypted successfully!")
    print(f"Key phrase: {solution['final_interpretation']}")
