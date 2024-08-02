"""
Day 7 - HTML Website Generator
"""

import click


def create(title, heading, body_text, output):
    content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>{title}</title>
    </head>
    <body>
      <h1>{heading}</h1>
      <p>{body_text}</h1>
    </body>
    </html>
    """

    with open(output, "w") as file:
        file.write(content)
    click.echo(f"HTML file '{output}' is created!")


@click.command()
@click.option("--title", prompt="Title of the website", help="Website title.")
@click.option(
    "--heading", prompt="Main heading of the website", help="Website main heading."
)
@click.option(
    "--body-text",
    prompt="Main body text of the website",
    help="Website main body text.",
)
@click.option("--output", default="index.html", help="Output website to HTML.")
def generate(title, heading, body_text, output):
    """Generate website by user defined content."""
    create(title, heading, body_text, output)


if __name__ == "__main__":
    generate()
