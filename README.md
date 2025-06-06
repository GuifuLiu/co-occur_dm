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
For `discovery`, we filter data instances so that both `DM1` and `DM2` (at sentence initial of Arg2) occur more than once in PDTB3. 

## Model

```
.
└── model/
    ├── prompt
    └── mask-fill
```
