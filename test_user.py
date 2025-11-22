import pytest
from User import *
from unittest.mock import MagicMock

# free_user = Users.create_new_user(FreeUser)

# prem_user = Users.create_new_user(PremiumUser)
# def test_create_user():
#     user1 = create_new_user()

@pytest.fixture
def create_input_sequence(monkeypatch):
    """Generator that yields the inputs in the correct order."""
    input_seq = [
        "Jane",       # 1st call to input()
        "Doe",        # 2nd call to input()
        "jane@test.com", # 3rd call to input()
        "1234" # Last call for DL
    ]

    mock_input = MagicMock(side_effect=input_seq)

    monkeypatch.setattr('builtins.input', mock_input)

    return mock_input

@pytest.fixture
def mock_single_post_input(monkeypatch):
    """Mocks up single post input"""
    test_post_content = "My first test using pytest"
    monkeypatch.setattr('builtins.input', lambda _: test_post_content)
    return test_post_content

def test_create_new_user(monkeypatch):
    input_gen = create_input_sequence()

    monkeypatch.setattr('builtins.input', lambda _: next(input_gen)) # That lambda is a placeholder)
    
    new_user = Users.create_new_user(FreeUser)

    assert new_user.first_name == "Jane"
    assert new_user.last_name == "Doe"
    assert new_user.email_address == "jane@test.com"
    assert new_user.license_number == "1234"


def test_free_user_add_post(mock_single_post_input, capsys):
    """Tests the add_post method using monkeypatch to mock input and capsys to capture print output."""
    # 1. Arrange
    account = Users()
    account.add_post()

    assert mock_single_post_input in account.posts
    assert len(account.posts) == 1

    captured = capsys.readouterr()
    expected_output = f"Post has been posted: '{mock_single_post_input}'\n"
    assert captured.out == expected_output

    """.out: This attribute contains a string of everything that was written to standard output (stdout)—i.e., everything printed by the print() function in your code.

.err: This attribute contains a string of everything that was written to standard error (stderr).

.in_: This attribute contains a string of any content that was read from standard input (stdin)."""

    