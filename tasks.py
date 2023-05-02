from invoke import task

@task
def start(ctx):
    """
    Run tests, and then start the program
    """
    
    # The idea with running tests before the program is just for
    # development purposes; it's handy to always run tests when 
    # starting the application, since that way bugs that may be 
    # hidden behind actions are more likely to be found initially

    ctx.run("poetry run invoke test")
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    """
    Run tests
    """
    ctx.run("python3 src/test.py", pty=True)

@task
def coverage(ctx):
    """
    Run coverage. Can be expanded with "-report" to also generate an html doc
    """
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    """
    Generate an html report in addition
    """
    ctx.run("coverage report", pty=True)
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    """
    Do a pylint check.
    """
    ctx.run("pylint src", pty=True)

@task
def build(ctx):
    """
    Build with poetry.
    """
    ctx.run("poetry build", pty=True)

@task
def format(ctx):
    """
    Do an autopep8 formatting
    """
    ctx.run("autopep8 --in-place --recursive src", pty=True)
