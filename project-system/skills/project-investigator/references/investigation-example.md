# Illustrative investigation: order total

This is a hypothetical teaching fixture, not an observation from a BuildSolid project and not executed evidence. The line numbers refer only to these excerpts.

`orders.py`:

```python
1  def total(items):
2      return sum(item["price"] * item["quantity"] for item in items)
3
4  def receipt(order):
5      return {"order_id": order["id"], "total": total(order["items"])}
```

`api.py`:

```python
1  from orders import receipt
2
3  def get_receipt(order):
4      return receipt(order)
```

**Question and snapshot:** Does the illustrated receipt path apply discounts? Hypothetical excerpts only; no repository revision or runtime result exists.

**Observed in the fixture:** `api.py:3-4` calls `receipt`; `orders.py:4-5` calls `total`; `orders.py:1-2` sums price times quantity. Neither excerpt includes a discount transformation.

**Inferred:** The path shown would return a pre-discount total for ordinary numeric inputs. This is a source-level inference, not an executed result.

**Unknown:** Other callers, middleware, accepted discount rules, and runtime data are absent. Inspect the real project's accepted contract, all `receipt` consumers, and a representative test before asserting actual behavior or blast radius. A Git commit message about a former discount would be historical context, not proof of current intent.

**Impact and next step:** The shown API consumer depends on `receipt.total`. A real investigation would cite the actual revision and callers, then route any desired change through an accepted implementation contract and executor.
