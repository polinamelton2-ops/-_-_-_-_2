import random

# Таблица соответствия символов и кодов Морзе
MORSE_TABLE = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
    "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
    " ": "/"
}

VOCABULARY = ["code", "bit", "list", "soul", "next", "little", "snake", "mouse"]


def text_to_morse(message):
    """
    Кодирует английское сообщение в азбуку Морзе.

    Args:
        message (str): Английский текст для кодирования.

    Returns:
        str: Коды Морзе, разделённые пробелами.
    """
    encoded_parts = [MORSE_TABLE[ch] for ch in message.lower() if ch in MORSE_TABLE]
    return " ".join(encoded_parts)


def morse_to_text(morse_code):
    """
    Декодирует азбуку Морзе обратно в английский текст.

    Args:
        morse_code (str): Строка с кодами Морзе.

    Returns:
        str: Расшифрованный английский текст.
    """
    decoder = {v: k for k, v in MORSE_TABLE.items()}
    decoded_chars = [decoder[token] for token in morse_code.split() if token in decoder]
    return "".join(decoded_chars)


def select_word():
    """
    Возвращает случайное слово из словаря VOCABULARY.

    Returns:
        str: Случайно выбранное слово.
    """
    return random.choice(VOCABULARY)


def report_statistics(answers):
    """
    Формирует и печатает статистику ответов.

    Args:
        answers (list): Список булевых значений.

    Returns:
        None
    """
    total_questions = len(answers)
    correct_answers = sum(answers)
    incorrect_answers = total_questions - correct_answers
    print(f"\nВсего вопросов: {total_questions}")
    print(f"Верных ответов: {correct_answers}")
    print(f"Неверных ответов: {incorrect_answers}")


def play_guessing_game():
    """
    Проводит игру «Угадай слово» из 5 раундов.

    Returns:
        None
    """
    outcomes = []
    for round_number in range(1, 6):
        target_word = select_word()
        morse_hint = text_to_morse(target_word)
        print(f"Слово {round_number}: {morse_hint}")
        player_answer = input().strip().lower()
        if player_answer == target_word:
            print(f"Верно, это слово: {target_word}")
            outcomes.append(True)
        else:
            print(f"Неверно! Зашифрованное слово было: {target_word}")
            outcomes.append(False)
    report_statistics(outcomes)


def show_menu():
    """
    Отображает меню режимов работы.

    Returns:
        None
    """
    print("1 - шифрование (английский -> Морзе)")
    print("2 - дешифрование (Морзе -> английский)")
    print("3 - Игра «Угадай слово» (5 вопросов)")
    print("4 - Выход")


def main():
    """
    Главная функция программы.

    Returns:
        None
    """
    print("Добрый день! Введите ваше имя:")
    user_name = input().strip()
    print(f"Отлично, {user_name}! Выберите режим работы:")
    show_menu()

    while True:
        user_choice = input("Ваш выбор: ").strip()
        if user_choice == "1":
            source_text = input("Введите текст на английском: ")
            print(text_to_morse(source_text))
        elif user_choice == "2":
            source_morse = input("Введите код Морзе: ")
            print(morse_to_text(source_morse))
        elif user_choice == "3":
            play_guessing_game()
        elif user_choice == "4":
            print(f"До свидания, {user_name}!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()