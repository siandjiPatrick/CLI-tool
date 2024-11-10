import click


@click.command()
#basic options
@click.option("--name","-n", default="Musterman", help="Firstname description")
def main(name):
    print(f"Hello World, My name is {name}")



if __name__== "__main__":
    main()