# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a shipping quote
in dollars. Zones are `local` and `regional`; weights must be positive.

### Service levels

| Service    | Base (local) | Base (regional) | Per-kg rate |
|------------|-------------|-----------------|-------------|
| `standard` | $5.00       | $8.00           | $1.50       |
| `express`  | $10.00      | $15.00          | $3.00       |

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 3 kg, local zone
python -m warehouse.cli 3 local

# Express quote – 3 kg, regional zone
python -m warehouse.cli 3 regional --service express
```
