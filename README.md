# Deep Hedging 5.2

This repository contains code for reproducing the results of section 5.2 of the deep hedging paper.

## Installation

Create a virtual environment using Python 3.12 or later and install the required packages:

```bash
pip install -r requirements.txt
```

TensorFlow 2.19+ is required for Python 3.12. The requirements file includes `tf-keras` and `ipython` which are necessary for TensorFlow Probability and plotting utilities.

## Usage

After installing the dependencies, you can import and run the training utilities:

```python
from deephedging.trainer import train
from deephedging.gym import VanillaDeepHedgingGym
from deephedging.world import SimpleWorld_Spot_ATM
```

Make sure to keep the repository root on your `PYTHONPATH` when running scripts or Jupyter notebooks.
