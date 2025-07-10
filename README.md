# Predicting Co-occurring Discourse Markers

## Dataset
```
.
└── dataset/
    ├── explicit-explicit/
    │   ├── discovery
    │   └── pdtb3
    └── explicit-implicit/
        └── pdtb3
```
For `discovery`, we filter data instances so that either both `DM1` and `DM2` (at sentence initial of Arg2) occur more than once in PDTB3 (`both PDTB connective`), or just `DM2` (`DM2 PDTB connective`). 

| Type  | Split | n   |
| ---   | ---   | --- |
| Explicit - Explicit | Discovery: `DM1 in PDTB` | 1288 |
|  | Discovery: `DM1 not in PDTB` | 4658 |
|  | PDTB |  |
| Explicit - Implicit | PDTB | 1706 |


## Model

```
.
└── model/
    ├── prompt
    └── mask-fill
```

## Model Prediction

Model predicted markers and probabilities are saved as `top_5_conn` and `top_5_score`. You can access prediction file this way:
```
from datasets import load_dataset
reloaded_dataset = load_dataset("model/mask-fill/predictions/<train_data>_<train_data>", streaming=True)
```
