def test_check_entry():
    from GUI_functions import check_entry
    answer = check_entry("Yes")
    assert answer == True
