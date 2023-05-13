from Utils import SCORES_FILE_NAME

points_of_winning = 0


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, "r+") as f:
            content = f.read()
            f.seek(0)
            f.truncate()
            if len(content) < 1:
                f.write(str(points_of_winning))
            else:
                f.write(str(int(content) + points_of_winning))
    except FileNotFoundError:
        with open(SCORES_FILE_NAME, "w") as f:
            f.write(str(points_of_winning))
