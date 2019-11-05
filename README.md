# Mixer

A tool for calculating bakery formulas, based upon final desired yield.

## Usage

python Mixer *formula* *desired_yield* *depth*

- Formula, the class definde in formula.py
- Desired yield, the final weight to be produced.
- Depth, Level of subformulas to print

## Example output

```
python Mixer SourdoughWholemeal 1200 1

Formula Sourdough Wholemeal: 1200.00 [221.53%]
Bread Flour: 541.69 [100%]
Formula Sourdough Preferment: 216.67 [40%]
		Rye Starter: 75.37 [80%]
		Rye Flour: 94.21 [100%]
		Water: 47.10 [50%]
Water: 417.10 [77%]
Salt: 13.70 [2.53%]
Instant Yeast: 10.83 [2%]
```

```
python Mixer SourdoughWhite 1200 1

Formula Sourdough White: 1200.00 [214.83%]
Bread Flour: 558.58 [100%]
Formula Sourdough Preferment: 223.43 [40%]
		Rye Starter: 77.72 [80%]
		Rye Flour: 97.14 [100%]
		Water: 48.57 [50%]
Water: 403.85 [72.3%]
Salt: 14.13 [2.53%]
```
