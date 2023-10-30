from moftransformer.examples import example_path
from moftransformer.utils import prepare_data
from moftransformer import __root_dir__

import os

# Get example path
root_cifs = example_path['root_cif']
# root_dataset = example_path['root_dataset']
root_dataset = os.path.join(__root_dir__, "database/qmof")

# downstream = example_path['downstream']
downstream = "bandgap"

train_fraction = 0.8  # default value
test_fraction = 0.1   # default value

# Run prepare data
prepare_data(root_cifs, root_dataset, downstream=downstream,
             train_fraction=train_fraction, test_fraction=test_fraction)