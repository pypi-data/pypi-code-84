import logging
from pathlib import Path

import click

from pynfogen.helpers import open_file


@click.group()
def artwork():
    """Manages artwork files."""
    pass


@artwork.command()
@click.argument("name", type=str)
@click.pass_obj
def edit(obj, name: str):
    """Edit an artwork file. If one does not exist, one will be created."""
    log = logging.getLogger("artwork")
    location = Path(obj["artwork"] / f"{name}.nfo")
    if not location.exists():
        log.info(f"Creating new artwork named {name}")
        location.parent.mkdir(exist_ok=True, parents=True)
        location.open("a").close()
    else:
        log.info(f"Opening existing artwork {name} for editing")
    open_file(str(location))


@artwork.command()
@click.argument("name", type=str)
@click.confirmation_option(prompt="Are you sure you want to delete the artwork?")
@click.pass_obj
def delete(obj, name: str):
    """Delete an artwork file."""
    log = logging.getLogger("artwork")
    location = Path(obj["artwork"] / f"{name}.nfo")
    if not location.exists():
        raise click.ClickException(f"Artwork {name} does not exist.")
    location.unlink()
    log.info(f"Artwork {name} has been deleted.")


@artwork.command(name="list")
@click.pass_obj
def list_(obj):
    """List all available artworks."""
    location = Path(obj["artwork"])
    if not location.is_dir():
        raise click.ClickException("No artworks exist.")
    for file in location.iterdir():
        print(file.stem)
