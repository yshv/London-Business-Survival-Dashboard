import user

# testing initialization of the class


def test_pass():
    check = user.User("test@test.com", "testname")
    assert check.email == "test@test.com"
    assert check.username == "testname"

# Checking if email is correct
# This test will fail as we have typed the wrong email
# incorrect email: "fail@fail.com"


def test_email_fail():
    check = user.User("test@test.com", "testname")
    assert check.hash_pass == "testpass"
    assert check.email == "fail@fail.com"

# Checking if pass is correct
# This test will fail as we have typed the wrong pass
# incorrect pass: "failpass"


def test_pass_fail():
    check = user.User("test@test.com", "testname")
    assert check.hash_pass == "failpass"
    assert check.email == "test@test.com"

