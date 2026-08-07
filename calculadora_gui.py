import math
import tkinter as tk
from tkinter import messagebox


class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("420x470")
        self.root.resizable(False, False)
        self.ultimo_resultado = 0.0

        tk.Label(root, text="Número 1 / Ángulo:", font=("Arial", 12)).grid(
            row=0, column=0, padx=10, pady=8, sticky="w"
        )
        self.num1_entry = tk.Entry(root, width=18, font=("Arial", 12))
        self.num1_entry.grid(row=0, column=1, padx=10, pady=8)

        tk.Label(root, text="Número 2 (opcional):", font=("Arial", 12)).grid(
            row=1, column=0, padx=10, pady=8, sticky="w"
        )
        self.num2_entry = tk.Entry(root, width=18, font=("Arial", 12))
        self.num2_entry.grid(row=1, column=1, padx=10, pady=8)

        self.result_var = tk.StringVar(value="Resultado: 0")
        tk.Label(root, textvariable=self.result_var, font=("Arial", 13, "bold"), fg="darkblue").grid(
            row=2, column=0, columnspan=2, padx=10, pady=12
        )

        tk.Label(root, text="Usar último resultado: ", font=("Arial", 10)).grid(
            row=3, column=0, columnspan=2, pady=(0, 8)
        )

        self.usar_ultimo_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            root,
            text="Operar con el resultado anterior",
            variable=self.usar_ultimo_var,
            font=("Arial", 10),
        ).grid(row=4, column=0, columnspan=2, pady=(0, 10))

        buttons = [
            ("Suma", self.sumar),
            ("Resta", self.restar),
            ("Multiplicar", self.multiplicar),
            ("Dividir", self.dividir),
            ("Seno", self.seno),
            ("Coseno", self.coseno),
            ("Tangente", self.tangente),
            ("Limpiar", self.limpiar),
        ]

        for index, (text, command) in enumerate(buttons):
            row = 5 + (index // 2)
            col = index % 2
            tk.Button(
                root,
                text=text,
                command=command,
                width=14,
                height=2,
                font=("Arial", 11, "bold"),
                bg="#eaf2ff",
            ).grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

        for col in range(2):
            root.grid_columnconfigure(col, weight=1)

    def _leer_numero_1(self):
        valor = self.num1_entry.get().strip()
        if self.usar_ultimo_var.get():
            return float(self.ultimo_resultado)
        if valor == "":
            raise ValueError("Debe ingresar el número 1 / ángulo.")
        return float(valor)

    def _leer_numero_2(self):
        if self.usar_ultimo_var.get():
            return float(self.ultimo_resultado)
        valor = self.num2_entry.get().strip()
        if valor == "":
            return 0.0
        return float(valor)

    def _mostrar_resultado(self, valor):
        if isinstance(valor, float) and valor.is_integer():
            valor = int(valor)
        self.ultimo_resultado = float(valor)
        self.result_var.set(f"Resultado: {valor}")

    def sumar(self):
        try:
            a = self._leer_numero_1()
            b = self._leer_numero_2()
            self._mostrar_resultado(a + b)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def restar(self):
        try:
            a = self._leer_numero_1()
            b = self._leer_numero_2()
            self._mostrar_resultado(a - b)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def multiplicar(self):
        try:
            a = self._leer_numero_1()
            b = self._leer_numero_2()
            self._mostrar_resultado(a * b)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def dividir(self):
        try:
            a = self._leer_numero_1()
            b = self._leer_numero_2()
            if b == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            self._mostrar_resultado(a / b)
        except (ValueError, ZeroDivisionError) as exc:
            messagebox.showerror("Error", str(exc))

    def seno(self):
        try:
            angulo = self._leer_numero_1()
            self._mostrar_resultado(math.sin(angulo))
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def coseno(self):
        try:
            angulo = self._leer_numero_1()
            self._mostrar_resultado(math.cos(angulo))
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def tangente(self):
        try:
            angulo = self._leer_numero_1()
            self._mostrar_resultado(math.tan(angulo))
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def limpiar(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.ultimo_resultado = 0.0
        self.usar_ultimo_var.set(False)
        self.result_var.set("Resultado: 0")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()
