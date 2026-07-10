from models.streaming.user import User, PLAN_PRICES
from data.streaming.data import data_user
from models.commerce.membership import Membership
from models.streaming.new_user import NewUser
from data.commerce.membership_data import membership_data

def banner(menu="PacGroup"):
    print("=" * 50)
    print(f"Selamat Datang di {menu}!")
    print("=" * 50)

def menu_existing_user(user):
    while True:
        print(f"Halo, {user.username}! Pilih Menu:")
        print("1. Lihat semua plan Pacflix")
        print("2. Lihat detail plan aktif saya")
        print("3. Keluar")

        choice = input("Masukkan pilihan (1-3)\n").strip()

        if choice == "1":
            user.check_benefit()
        elif choice == "2":
            user.check_plan()
        elif choice == "3":
            print("Selamat tinggal!")
            break

def menu_utama_streaming():
    banner()
    while True:
        print("Menu Utama")
        print(" 1. Login sebagai pengguna terdaftar")
        print(" 2. Daftar sebagai pengguna baru")
        print(" 3. Keluar")
        
        choice = input("Masukkan pilihan 1-3\n").strip()

        if choice == '1':
            username = input("Masukan username:").strip()

            if username not in data_user:
                print(f"Username {username} tidak ditemukan!")
                continue

            plan, duration, ref_code = data_user[username]
            user = User(username, duration, plan)
            menu_existing_user(user)
        
        elif choice == '2':
            username = input("Masukan username baru: ").strip()

            print("Pilih plan:")
            plans = list(PLAN_PRICES.keys())
            for i, plan in enumerate(plans, 1):
                print(f"{i}. {plan} - Rp{PLAN_PRICES[plan]:,}")

            plan_choice = input(f"Masukkan pilihan (1-{len(plans)})\n").strip()
            if plan_choice not in [str(i) for i in range(1, len(plans)+1)]:
                print("Pilihan tidak valid!")
                continue

            chosen_plan = plans[int(plan_choice) - 1]
            ref_input = input("Punya kode referral? (kosongkan jika tidak ada): ").strip()

            new_user = NewUser(username)
            new_user.register(chosen_plan, ref_input if ref_input else None)
        elif choice == '3':
            print("Terimakasih telah menggunakan PacFlix!")
            break

def menu_utama_ecommerce():
    while True:
        banner("PacCommerce")
        print("Menu Utama PaCommerce")
        print(" 1. Show Benefit")
        print(" 2. Show Requirements")
        print(" 3. Predict Membership")
        print(" 4. Hitung Belanja")
        print(" 5. Keluar")

        choice = input ("Masukan pilihan 1-5\n").strip()

        if choice == '1':
            print("\n=== Benefit Membership ===")
            for tier, info in membership_data.items():
                print(f"\n{tier}:")
                for benefit in info["benefit"]:
                    print(f"  - {benefit}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == '2':
            print("\n=== Requirement Membership ===")
            for tier, info in membership_data.items():
                print(f"\n{tier}: {info['requirement']}")
            input("\nTekan Enter untuk kembali ke menu...")

        elif choice == '3':
            username = input("Masukan username anda!: ")
            expense = int(input("Masukan Monthly expense anda: "))
            income = int(input("Masukan Monthly income anda: "))
            user = Membership(username)
            member = user.predict_membership(expense, income)

            print(f"{user.username} anda diprediksi masuk ke tier {member}")

        elif choice == '4':
            username = input("Masukan username anda!: ")
            expense = int(input("Masukan Monthly expense anda: "))
            income = int(input("Masukan Monthly income anda: "))

            user = Membership(username)
            tier = user.predict_membership(expense, income)

            print(f"\n{username} anda diprediksi masuk ke tier {tier}")

            total_belanja = int(input("Masukan total belanja anda (Rp): "))
            discount = membership_data[tier]["discount_percent"]
            potongan = total_belanja * discount / 100
            total_bayar = total_belanja - potongan

            print(f"\n=== Rincian Belanja ===")
            print(f"Total belanja      : Rp{total_belanja:,}")
            print(f"Diskon ({tier})      : {discount}%")
            print(f"Potongan           : Rp{potongan:,.0f}")
            print(f"Total yang dibayar : Rp{total_bayar:,.0f}")

            
        else:
            print("Terimakasih telah mengunjungi PacCOmmerce")
            break

    

def menu_utama():
    while True:
        banner("PacGroup")
        print("Menu Utama PacGroup")
        print(" 1. Streaming Video")
        print(" 2. Belanja")
        print(" 3. Keluar")

        choice = input("Masukkan pilihan 1-3\n").strip()

        if choice == '1':
            menu_utama_streaming()
        elif choice == '2':
            menu_utama_ecommerce()
        else:
            print("Terimakasih telah menggunakan aplikasi PacGroup")
            break

menu_utama()


    
