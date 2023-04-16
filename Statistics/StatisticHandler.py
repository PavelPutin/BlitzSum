import yaml
import os


class StatisticHandler:
    FILE = os.path.join(os.getcwd(), "resources", "statistics.yaml")

    @staticmethod
    def get_data():
        with open(StatisticHandler.FILE, "r") as stream:
            return yaml.safe_load(stream)

    @staticmethod
    def write_data(total_games, best_score):
        with open(StatisticHandler.FILE, "w") as stream:
            data = {
                "total_games": total_games,
                "best_score": best_score
            }
            yaml.safe_dump(data, stream)
