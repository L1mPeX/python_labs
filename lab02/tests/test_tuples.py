import pytest
from lab02.src.tuples import format_record


def test_format_record():
    assert format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)) == \
           "Иванов И.И., гр. BIVT-25, GPA 4.60"
    assert format_record(("Петров Пётр", "IKBO-12", 5.0)) == \
           "Петров П., гр. IKBO-12, GPA 5.00"
    assert format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)) == \
           "Петров П.П., гр. IKBO-12, GPA 5.00"
    assert format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)) == \
           "Сидорова А.С., гр. ABB-01, GPA 4.00"

    with pytest.raises(ValueError):
        format_record(("", "IKBO-12", 4.5))

    with pytest.raises(ValueError):
        format_record(("Иванов Иван", "", 4.5))

    with pytest.raises(TypeError):
        format_record(("Иванов Иван", "IKBO-12", "отлично"))
