import os
from invoke import task
from src.config import DATABASE_FILE_PATH


@task
def start(ctx):
    if not os.path.isfile(DATABASE_FILE_PATH):
        ctx.run("python3 src/build.py", pty=True)
    ctx.run("python3 src/main.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def lint(ctx):
    ctx.run("pylint src", pty=True)


@task
def format(ctx):  # pylint: disable=redefined-builtin
    ctx.run("autopep8 --in-place --recursive src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)