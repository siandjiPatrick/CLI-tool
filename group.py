import click


@click.group
@click.version_option("1.0.0")
def main():
    pass


@main.group()
def config():
    click.echo("bienvenu dans la configuration")
    

@config.command()
def editor():
    """ configure Editor"""
    click.echo("configure editor")
    
    
@main.command()   

@click.argument("object_name") 
@click.option("--all", "-a",help="delete all object",)
def create(object_name,all):
    """ Create new Object"""
    click.echo("Create Object")
    

@main.command(help="delete object")
def delete():
    click.echo("Delete Object")


#main.add_command(cmd="delete")
#main.add_command(name="create")

if __name__ == "__main__":
    main()