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
|  | Discovery: `DM1 not in PDTB` | 5194 |
|  | PDTB |  |
| Explicit - Implicit | PDTB | 1706 |


## Model

```
.
└── model/
    ├── prompt
    └── mask-fill
```
