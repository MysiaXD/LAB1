class MatrixProcessor:
    """
    Клас для виконання математичних операцій з матрицями.
    Відповідає лише за обчислення
    """

    def __init__(self, matrix_a: list[list[float]], matrix_b: list[list[float]]):
        """
        Конструктор класу. Приймає матриці ззовні, а не створює їх всередині.
        """
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self._validate_matrices()

    def _validate_matrices(self):
        """
        Прихований метод для перевірки коректності вхідних даних.
        """
        if not self.matrix_a or not self.matrix_b or not self.matrix_a[0] or not self.matrix_b[0]:
            raise ValueError("Матриці не можуть бути порожніми.")

        rows_a, cols_a = len(self.matrix_a), len(self.matrix_a[0])
        rows_b, cols_b = len(self.matrix_b), len(self.matrix_b[0])

        if any(len(row) != cols_a for row in self.matrix_a) or any(len(row) != cols_b for row in self.matrix_b):
            raise ValueError("Некоректна форма матриці (різна кількість елементів у рядках).")

        if rows_a != rows_b or cols_a != cols_b:
            raise ValueError("Розмірності матриць A та B не співпадають. Додавання неможливе.")

    def add_matrices(self) -> list[list[float]]:
        """
        Метод для додавання двох матриць.
        Повертає нову матрицю, нічого не виводячи на екран.
        """
        rows = len(self.matrix_a)
        cols = len(self.matrix_a[0])

        matrix_c = []
        for i in range(rows):
            row_c = []
            for j in range(cols):
                row_c.append(self.matrix_a[i][j] + self.matrix_b[i][j])
            matrix_c.append(row_c)

        return matrix_c

    def calculate_column_averages(self, matrix: list[list[float]]) -> list[float]:
        """
        Метод для обчислення середнього значення кожного стовпчика переданої матриці.
        Повертає список із середніми значеннями.
        """
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        averages = []

        for j in range(cols):
            column_sum = 0.0
            for i in range(rows):
                column_sum += matrix[i][j]
            averages.append(column_sum / rows)

        return averages

if __name__ == "__main__":
    #Створ дані
    A = [
        [1.5, 2.5, 3.0],
        [4.1, 5.2, 6.3],
        [7.0, 8.8, 9.1]
    ]

    B = [
        [0.5, 1.5, 2.0],
        [1.9, 2.8, 3.7],
        [4.0, 5.2, 6.9]
    ]

    try:
        #Ініціалізуємо об'єкт нашого класу
        processor = MatrixProcessor(A, B)

        #Викон додавання
        C = processor.add_matrices()

        print("--- Матриця C (Результат додавання A + B) ---")
        for row in C:
            formatted_row = [f"{elem:.2f}" for elem in row]
            print("\t".join(formatted_row))

        #Викон другу дію
        averages = processor.calculate_column_averages(C)

        print("\n--- Середнє значення кожного стовпчика матриці C ---")
        for idx, avg in enumerate(averages):
            print(f"Стовпчик {idx + 1}: {avg:.2f}")

    except ValueError as ve:
        print(f"Помилка даних: {ve}")
    except TypeError:
        print("Помилка типу: Елементи матриць повинні бути числами.")
    except Exception as e:
        print(f"Непередбачувана помилка під час виконання: {e}")