import json
import os
import random

class JSONSplitter:
    def __init__(self, train_ratio, test_ratio, validation_ratio):
        self.train_ratio = train_ratio
        self.test_ratio = test_ratio
        self.validation_ratio = validation_ratio

    def split_json_data(self, input_json_file):
        if self.train_ratio + self.test_ratio + self.validation_ratio != 1.0:
            raise ValueError("Ratios should sum up to 1")

        with open(input_json_file, 'r') as file:
            data = json.load(file)

        data_list = list(data.items())
        random.shuffle(data_list)

        total_count = len(data_list)
        train_count = int(total_count * self.train_ratio)
        test_count = int(total_count * self.test_ratio)
        validation_count = total_count - train_count - test_count

        train_data = dict(data_list[:train_count])
        test_data = dict(data_list[train_count:train_count + test_count])
        validation_data = dict(data_list[train_count + test_count:])

        # Get the directory and filename
        directory = os.path.dirname(input_json_file)
        filename = os.path.splitext(os.path.basename(input_json_file))[0]

        # Writing to new JSON files
        with open(os.path.join(directory, f"{filename}_train.json"), 'w') as train_file:
            json.dump(train_data, train_file, indent=4)

        with open(os.path.join(directory, f"{filename}_test.json"), 'w') as test_file:
            json.dump(test_data, test_file, indent=4)

        with open(os.path.join(directory, f"{filename}_validation.json"), 'w') as validation_file:
            json.dump(validation_data, validation_file, indent=4)

        print("Data split and saved successfully!")

# Example usage:
# splitter = JSONSplitter(0.7, 0.2, 0.1)
# splitter.split_json_data('path/to/your/original.json')
