import random


def get_total_dice(player_dice, comp_dice, nominal):
    return player_dice.count(nominal) + comp_dice.count(nominal)


print("=== ДОБРО ПОЖАЛОВАТЬ В ИГРУ ПЕРУДО! ===")

player_dice = [random.randint(1, 6) for _ in range(6)]
comp_dice = [random.randint(1, 6) for _ in range(6)]

print(f"Вы бросили кости! Ваши 6 значений: {player_dice}")
print("Компьютер тоже бросил свои 6 костей (они скрыты).\n")

current_count = 0
nominal = 0
current_turn = "player"

while True:
    if current_turn == "player":
        print("\n--- ВАШ ХОД ---")

        if current_count > 0:
            action = input(
                "Что делаете? (Введите '1' - поставить/повысить, '0' или 'НЕ ВЕРЮ' - проверить): ").strip().lower()
        else:
            action = "1"

        if action == "0" or "не верю" in action:
            print(f"\nВы выкрикнули: 'НЕ ВЕРЮ!'")
            print(f"Кости компьютера: {comp_dice}")
            print(f"Ваши кости: {player_dice}")

            total = get_total_dice(player_dice, comp_dice, nominal)
            print(f"Всего костей с номиналом {nominal} на столе: {total}")

            if total >= current_count:
                print(f"Ставка компьютера ({current_count} шт. по {nominal}) была ПРАВИЛЬНОЙ!")
                print("🏆 ВЫ ПРОИГРАЛИ! Компьютер победил!")
            else:
                print(f"Ставка компьютера ({current_count} шт. по {nominal}) была ЛОЖНОЙ!")
                print("🏆 ВЫ ПОБЕДИЛИ! Компьютер проиграл!")
            break
        else:
            while True:
                try:
                    new_count = int(input("Введите количество костей: "))
                    new_nominal = int(input("Введите номинал костей (от 1 до 6): "))

                    if new_nominal < 1 or new_nominal > 6:
                        print("Номинал должен быть строго от 1 до 6!")
                        continue

                    if new_count > current_count or (new_count == current_count and new_nominal > nominal):
                        current_count = new_count
                        nominal = new_nominal
                        break
                    else:
                        print(f"Ставка должна быть ВЫШЕ текущей! (Сейчас заявлено: {current_count} шт. по {nominal})")
                except ValueError:
                    print("Ошибка! Вводите только целые числа.")

            print(f"Вы сделали ставку: {current_count} шт. номинала {nominal}")
            current_turn = "comp"
    else:
        print("\n--- ХОД КОМПЬЮТЕРА ---")
        comp_has = comp_dice.count(nominal)

        if current_count > 4 and comp_has < 2 or current_count > 7:
            comp_action = "bluff"
        else:
            comp_action = "raise"

        if comp_action == "bluff":
            print(f"Компьютер говорит: 'НЕ ВЕРЮ!' твоей ставке ({current_count} шт. по {nominal})")
            print(f"Кости компьютера: {comp_dice}")
            print(f"Ваши кости: {player_dice}")

            total = get_total_dice(player_dice, comp_dice, nominal)
            print(f"Всего костей с номиналом {nominal} на столе: {total}")

            if total >= current_count:
                print(f"Ваша ставка была ПРАВИЛЬНОЙ!")
                print("🏆 ВЫ ПОБЕДИЛИ! Компьютер проиграл!")
            else:
                print(f"Ваша ставка была ЛОЖНОЙ!")
                print("🏆 ВЫ ПРОИГРАЛИ! Компьютер победил!")
            break
        else:
            if random.choice([True, False]) or nominal == 6:
                current_count += 1
                if nominal == 0:
                    nominal = random.randint(1, 6)
            else:
                if nominal < 6:
                    nominal += 1
                else:
                    current_count += 1

            print(f"Компьютер повышает ставку до: {current_count} шт. номинала {nominal}")
            current_turn = "player"

print("\n=== Игра завершена ===")
