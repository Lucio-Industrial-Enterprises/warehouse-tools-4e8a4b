"""Shipping rate calculations."""

_SERVICES = {"standard", "express"}

_BASE = {
    "standard": {"local": 5.0, "regional": 8.0},
    "express":  {"local": 10.0, "regional": 15.0},
}

_RATE_PER_KG = {
    "standard": 1.5,
    "express":  3.0,
}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Return a shipping quote in dollars.

    Parameters
    ----------
    weight_kg:
        Parcel weight; must be positive.
    zone:
        Delivery zone – ``"local"`` or ``"regional"``.
    service:
        Shipping service level – ``"standard"`` (default) or ``"express"``.

    Returns
    -------
    float
        Quoted price rounded to two decimal places.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _SERVICES:
        raise ValueError(f"unknown service: {service!r}; choose from {sorted(_SERVICES)}")
    base = _BASE[service][zone]
    return round(base + _RATE_PER_KG[service] * weight_kg, 2)
