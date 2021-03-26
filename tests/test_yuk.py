import pytest
from textwrap import dedent

@pytest.fixture()
def file_structure(pytester):
    content = dedent("""
    import pytest

    @pytest.mark.yuk
    def test_pass():
        assert 1 == 1

    @pytest.mark.yuk
    def test_fail():
        assert 1 == 2

    def test_pass_unmarked():
        assert 1 == 1

    def test_fail_unmarked():
        assert 1 == 2
    """
    )
    pytester.makepyfile(test_foo=content)


def test_verbose(file_structure, pytester):
    result = pytester.runpytest("-v", "test_foo.py")
    result.assert_outcomes(passed=2, failed=2)
    result.stdout.fnmatch_lines(['*test_pass PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail FAILED*'])
    result.stdout.fnmatch_lines(['*test_pass_unmarked PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail_unmarked FAILED*'])


def test_verbose_yuk(file_structure, pytester):
    result = pytester.runpytest("-v", "--yuk", "test_foo.py")
    result.assert_outcomes(passed=2, failed=2)
    result.stdout.fnmatch_lines(['*test_pass PASSED 🤢*'])
    result.stdout.fnmatch_lines(['*test_fail FAILED 🤮*'])
    result.stdout.fnmatch_lines(['*test_pass_unmarked PASSED*'])
    result.stdout.fnmatch_lines(['*test_fail_unmarked FAILED*'])


def test_nonverbose(file_structure, pytester):
    result = pytester.runpytest("test_foo.py")
    result.assert_outcomes(passed=2, failed=2)
    result.stdout.fnmatch_lines(['*.F.F*'])


def test_nonverbose_yuk(file_structure, pytester):
    result = pytester.runpytest("--strict-markers", "--yuk", "test_foo.py")
    result.assert_outcomes(passed=2, failed=2)
    result.stdout.fnmatch_lines(['*🤢🤮.F*'])
    outcome_line = result.stdout.lines[0]
