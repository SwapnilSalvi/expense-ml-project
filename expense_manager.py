import pandas as pd
import random
from datetime import datetime, timedelta
import os


class ExpenseManager:
    def __init__(self, file_path="data/expenses_full.csv"):
        self.file_path = file_path

        self.categories = {
            "Food": ["Breakfast", "Lunch", "Dinner", "Snacks"],
            "Travel": ["Auto", "Bus", "Taxi"],
            "Shopping": ["Clothes", "Groceries", "Shoes", "Electronics"],
            "Bills": ["Rent", "Electricity", "Internet", "Credit Card"],
            "Entertainment": ["Movie", "Restaurant", "Outing"]
        }

    # -------------------------------
    # Generate Synthetic Data
    # -------------------------------
    def generate_data(self, start_date, end_date):
        data = []
        current_date = start_date

        while current_date <= end_date:
            day = current_date.weekday()

            data.extend(self._generate_food(current_date))
            data.extend(self._generate_travel(current_date))
            data.extend(self._generate_weekend(current_date, day))
            data.extend(self._generate_shopping(current_date))
            data.extend(self._generate_bills(current_date))

            current_date += timedelta(days=1)

        df = pd.DataFrame(data, columns=["date", "amount", "category", "note"])
        self._save(df)

        print("✅ Dataset generated successfully!")

    # -------------------------------
    # Add Expense
    # -------------------------------
    def add_expense(self, amount, category, note=""):
        self._validate_input(amount, category)

        new_data = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": category,
            "note": note
        }

        df_new = pd.DataFrame([new_data])
        df_old = self._load()

        df = pd.concat([df_old, df_new], ignore_index=True)
        self._save(df)

        print("✅ Expense added!")

    # -------------------------------
    # Internal Helper Methods
    # -------------------------------
    def _generate_food(self, date):
        entries = []
        for _ in range(random.randint(1, 3)):
            entries.append([
                date.date(),
                random.randint(50, 350),
                "Food",
                random.choice(self.categories["Food"])
            ])
        return entries

    def _generate_travel(self, date):
        if random.random() > 0.4:
            return [[
                date.date(),
                random.randint(30, 150),
                "Travel",
                random.choice(self.categories["Travel"])
            ]]
        return []

    def _generate_weekend(self, date, day):
        if day >= 5:
            return [[
                date.date(),
                random.randint(300, 1200),
                "Entertainment",
                random.choice(self.categories["Entertainment"])
            ]]
        return []

    def _generate_shopping(self, date):
        if random.random() > 0.8:
            return [[
                date.date(),
                random.randint(500, 3000),
                "Shopping",
                random.choice(self.categories["Shopping"])
            ]]
        return []

    def _generate_bills(self, date):
        if date.day in [2, 5, 10]:
            return [[
                date.date(),
                random.randint(1000, 6000),
                "Bills",
                random.choice(self.categories["Bills"])
            ]]
        return []

    def _validate_input(self, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if category not in self.categories:
            raise ValueError(f"Invalid category. Choose from {list(self.categories.keys())}")

    def _load(self):
        if os.path.exists(self.file_path):
            return pd.read_csv(self.file_path)
        return pd.DataFrame(columns=["date", "amount", "category", "note"])

    def _save(self, df):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        df.to_csv(self.file_path, index=False)
        
        
        
        
        
        
        
        
        
# manager = ExpenseManager()

# manager.generate_data(
#     start_date=datetime(2025, 1, 1),
#     end_date=datetime(2026, 3, 1)
# )


# manager.add_expense(250, "Food", "Lunch")