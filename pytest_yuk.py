"""
Display tests you are uneasy with, using 🤢/🤮 for pass/fail of tests marked with yuk.
Action only takes place if `--yuk` is passeed.
Test marked with @pytest.mark.yuk
  * will display 🤢 if passing.
  * will display 🤮 if failing.
"""
__version__ = '0.0.1.post2'

def pytest_report_teststatus(report, config):
    if not config.option.yuk:
        return
    if ('yuk' in report.keywords) and (report.when == 'call'):
        if report.passed:
            return report.outcome, "🤢", f"{report.outcome.upper()} 🤢"
        if report.failed:
            return report.outcome, "🤮", f"{report.outcome.upper()} 🤮"

def pytest_addoption(parser):
    group = parser.getgroup("yuk")
    group._addoption("--yuk",
                     action="store_true", dest="yuk", default=False,
                     help="Show 🤢/🤮 for pass/fail of tests marked 'yuk'")


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "yuk: Show 🤢/🤮 for pass/fail of tests marked 'yuk' when run with '--yuk'.")

