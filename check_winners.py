"""Проверка попадания участника в тройку лучших."""


def check_winners(scores: list[int], student_score: int) -> None:
    """Напечатать, входит ли student_score в три наибольших результата."""
    if student_score in sorted(scores, reverse=True)[:3]:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")


if __name__ == "__main__":
    scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
    check_winners(scores, 48)
