from tabulate import tabulate

PLAN_PRICES = {
    "Basic Plan":    120_000,
    "Standard Plan": 160_000,
    "Premium Plan":  200_000,
}

PLAN_TABLE = [
    [True,  True,  True,  "Bisa Stream"],
    [True,  True,  True,  "Bisa Download"],
    [True,  True,  True,  "Kualitas SD"],
    [False, True,  True,  "Kualitas HD"],
    [False, False, True,  "Kualitas UHD"],
    [1,     2,     4,     "Jumlah Device"],
    [
        "3rd party Movie only",
        "Basic Plan Content + Sports",
        "Basic Plan + Standard Plan + PacFlix Original Series",
        "Jenis Konten",
    ],
    [120_000, 160_000, 200_000, "Harga (Rp)"],
]

PLAN_HEADERS = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

class User:
    def __init__ (self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    def check_benefit(self):
        print(" == PacFlix Plan List === ")
        print("")
        print(PLAN_HEADERS)
        print(PLAN_TABLE)
        print(tabulate(PLAN_TABLE, headers=PLAN_HEADERS))
    
    def check_plan(self):
        plan = self.current_plan
        print(f"=== Paket Aktif: {plan} ({self.duration_plan} bulan) ===" ) 

        plan_index = list(PLAN_PRICES.keys()).index(plan)
        header = list(PLAN_PRICES.keys())[plan_index]

        rows = []

        for row in PLAN_TABLE:
            fitur = []
            fitur.append(row[plan_index])
            fitur.append(row[-1])
            rows.append(fitur)

        print(tabulate(rows, headers=[header, 'service']))
