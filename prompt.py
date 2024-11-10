import click



@click.command()
@click.option("--name", default="patrick", help="Your Name Description")

def main(name):
    fname= click.prompt("Enter your Name")
    click.echo(f" Your name is {fname}")
    
if __name__=="__main__":
    main()