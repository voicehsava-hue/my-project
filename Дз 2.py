print("Загадайте число от -1 000 000 000 до 1 000 000 000.")
print("Отвечайте: '>' (больше), '<' (меньше) или '=' (угадал).\n")

attempt = 1

def ask_user(guess_val):
    global attempt
    print(f"Попытка №{attempt}: Это число {guess_val}?")
    answer = input("Введите >, < или = : ").strip()

    if answer == "=":
        print(f"\nПобеда! Число {guess_val} угадано за {attempt} попыток!")
        exit()

    attempt += 1
    return answer

first_ans = ask_user(0)
low = -10 ** 9
high = 10 ** 9

if first_ans == ">":
    low = 1
    step = 10
    while step <= 10 ** 9:
        ans = ask_user(step)
        if ans == "<":
            high = step
            low = step // 10
            break
        step *= 10

elif first_ans == "<":
    high = -1
    step = 10
    while step <= 10 ** 9:
        ans = ask_user(-step)
        if ans == ">":
            low = -step
            high = -(step // 10)
            break
        step *= 10


while low <= high:
    mid = (low + high) // 2
    ans = ask_user(mid)

    if ans == ">":
        low = mid + 1
    elif ans == "<":
        high = mid - 1
