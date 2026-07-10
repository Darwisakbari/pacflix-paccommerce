from math import sqrt

class Membership:
    def __init__(self, username):
        self.username = username
    
    def predict_membership(self, monthly_expense, monthly_income):
        res = []

        membership_parameter = [[8, 15], [6, 10], [5, 7]]
        
        # perhitungan jarak/eucledean distance
        for index, _ in enumerate(membership_parameter):

            tmp = round(sqrt((monthly_expense - membership_parameter[index][0]) ** 2 + (monthly_income -
            membership_parameter[index][1]) ** 2), 2)

            res. append(tmp)

        res_dict = { "Platinum": res[0],
                     "Gold": res[1],
                     "Silver": res[2]
                     }

       # print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {res_dict}")

        for member, distance in res_dict. items():
            if distance == min(res):
                return member

