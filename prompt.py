import click



@click.command()
@click.option("--name", prompt=True, default="patrick")

def main(name):
    click.echo(f" Your name is {name}")
    
if __name__=="__main__":
    main()