import numpy as np
from prettytable import PrettyTable

class GameWithNature:
    def __init__(self, matrix, ALPHA) -> None:
        self.matrix = matrix
        self.ALPHA = ALPHA

    def solve(self):
        self.print_matrix(self.matrix)
        self.bernully()
        self.pessimistic()
        self.optimistic()
        self.gurwic()
        self.savage()

    def print_matrix(self, matrix):
        table = PrettyTable()
        header = [f"b{i + 1}" for i in range(matrix.shape[1])]
        table.field_names = ['Стратегии', *header]

        for i in range(matrix.shape[0]):
            table.add_row([f"a{i + 1}", *matrix[i]])
        
        print(table)


    def print_column(self, column, criterion):
        table = PrettyTable()
        table.field_names = ["Стратегии", criterion]
        for i in range(len(column)):
            table.add_row([f"a{i+1}", column[i]])

        print(table)
        print(f'Оптимальная стратегия - a{column.index(max(column)) + 1}: {max(column)}')

    def bernully(self):
        print("\n\nКритерий Бернулли\n")
        result_vars = [round(sum(self.matrix[i])*(1/self.matrix.shape[1]), 2) for i in range(self.matrix.shape[0])]
        self.print_column(result_vars, "Б")


    def pessimistic(self):
        print("\n\Критерий Вальда\n")
        result_vars = [min(self.matrix[i]) for i in range(self.matrix.shape[0])]
        self.print_column(result_vars, "В")


    def optimistic(self):
        print("\n\nОптимистический критерий\n")
        result_vars = [max(self.matrix[i]) for i in range(self.matrix.shape[0])]
        self.print_column(result_vars, "опт")


    def gurwic(self):
        print("\n\nКритерий Гурвица\n")
        print(f'Вероятность везения: {self.ALPHA}')
        result_vars = [(round(self.ALPHA * min(self.matrix[i]) + (1 - self.ALPHA) * max(self.matrix[i]), 2)) for i in range(self.matrix.shape[0])]
        self.print_column(result_vars, "Г")


    def savage(self):
        print("\n\nКритерий Севиджа\n")
        matrix_of_risks = np.zeros(self.matrix.shape)
        for j in range(self.matrix.shape[1]):
            maximal = self.matrix[0, j]
            for i in range(1, self.matrix.shape[0]):
                if self.matrix[i, j] > maximal:
                    maximal = self.matrix[i, j]
            for i in range(0, self.matrix.shape[0]):
                matrix_of_risks[i, j] = maximal - self.matrix[i, j]
        
        print('Матрица рисков:')
        self.print_matrix(matrix_of_risks)
        result_vars = [max(matrix_of_risks[i]) for i in range(self.matrix.shape[0])]
        for i in range(len(result_vars)):
            print("{: >3}".format(f"a{i + 1}"), end="")
            print("{: >8}".format(result_vars[i]), end="")
            print()
        print(f'Оптимальная стратегия - a{result_vars.index(min(result_vars)) + 1}: {min(result_vars)}')



