import click


@click.command()

# work with argument
@click.argument('name', default="patrick")

def main(name):
    click.echo("Hello {}".format(name))
    


if __name__ == "__main__":
    main()