from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
import numpy as np

router = APIRouter(prefix="/polynomial", tags=["polynomial"])


class PolynomialRequest(BaseModel):
    coefficients: list[float]

    @field_validator("coefficients")
    @classmethod
    def validate_coefficients(cls, v: list[float]) -> list[float]:
        if len(v) < 2:
            raise ValueError(
                "At least 2 coefficients are required to define a polynomial "
                "(e.g. [a, b] for ax + b)."
            )
        if v[0] == 0:
            raise ValueError(
                "The leading coefficient (highest degree term) must be non-zero."
            )
        return v


class ComplexRoot(BaseModel):
    real: float
    imag: float


class PolynomialRootsResponse(BaseModel):
    degree: int
    roots: list[ComplexRoot]


@router.post("/roots", response_model=PolynomialRootsResponse)
def compute_roots(body: PolynomialRequest) -> PolynomialRootsResponse:
    """
    Compute the roots of a degree-n polynomial.

    The `coefficients` array is ordered by **descending** degree:
    `[a, b, c, d]` represents `a·x³ + b·x² + c·x + d`.

    Roots are returned as complex numbers (imaginary part is 0.0 for real roots).
    """
    coeffs = body.coefficients
    degree = len(coeffs) - 1

    try:
        raw_roots: np.ndarray = np.roots(coeffs)
    except np.linalg.LinAlgError as exc:
        raise HTTPException(status_code=422, detail=f"Root computation failed: {exc}") from exc

    roots = [
        ComplexRoot(real=float(r.real), imag=float(r.imag))
        for r in raw_roots
    ]

    return PolynomialRootsResponse(degree=degree, roots=roots)
