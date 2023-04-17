from invoke import task

@task
def start(ctx):
    """
    Run tests, and then start the program
    """
    ctx.run("poetry run invoke test")
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    """
    Run tests, and then start the program
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
    ctx.run("coverage html", pty=True)
