
from scheduler.triage import validate, score

def test_validate_missing_fields():
    row = {"task":"read", "estimated_minutes":"", "required_tools":"book"}
    ok, errs = validate(row)
    assert ok is False and "estimated_minutes" in errs

def test_validate_good_row():
    row = {"task":"math HW", "estimated_minutes":"30", "required_tools":"notebook"}
    ok, errs = validate(row)
    assert ok is True and errs == {}

def test_score_basic_range():
    row = {"task":"math HW", "estimated_minutes":"30", "required_tools":"notebook"}
    s = score(row)
    assert isinstance(s, int) and 0 <= s <= 100
