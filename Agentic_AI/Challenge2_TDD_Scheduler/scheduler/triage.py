
from typing import Dict, Tuple, List

# TODO: Implement these using TDD.
def validate(row: Dict[str, str]) -> Tuple[bool, Dict[str, str]]:
    """Return (ok, errors). errors maps field->message."""
    raise NotImplementedError

def score(row: Dict[str, str]) -> int:
    """Return a priority score 0..100."""
    raise NotImplementedError

def plan_day(rows: List[Dict[str, str]], day_minutes: int = 180) -> List[Dict]:
    """Return ordered plan with start times (HH:MM), respecting day_minutes and short breaks."""
    raise NotImplementedError
