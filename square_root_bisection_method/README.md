# 🧮 Square Root Calculator using Bisection Method

This is a simple Python program that calculates the square root of a non-negative number using the **Bisection Method**, a classic numerical technique.

---

## 🚀 Features

- Implements the bisection method to approximate square roots
- Accepts user input through the console
- Handles edge cases: 0, 1, and negative numbers
- Includes iteration limit and precision control
- Returns result up to 10 decimal places

---

## 📌 How It Works

The Bisection Method is a root-finding technique that repeatedly divides an interval in half and selects the subinterval in which a root exists. It stops when the square of the midpoint is close enough to the target value.

---

## 🧠 Logic

1. Input a non-negative number
2. If the number is 0 or 1, return immediately
3. Otherwise, apply the bisection search in the range [0, max(1, N)]
4. Repeat until the square of the midpoint is within a specified tolerance


