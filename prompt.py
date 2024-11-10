import click



@click.command()
@click.option("--name", prompt=True, default="Siandji", help="Your Name Description")

def main(name):
    fname= click.prompt("Enter your firstname")
    click.echo(f" Your name is {name} and your firtname is {fname}")
    
if __name__=="__main__":
    main()