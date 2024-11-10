import click


# @click.command()

# # work with argument
# @click.argument('number1', type=int )
# @click.argument('number2', type=int)
# @click.argument('method', default='add')

# def main(number1, number2, method):
#     """ ADD number 1 and number2 """
#     if method == "add":
#         click.echo("{} + {} = {}".format(number1, number2,number1+number2))
    
#     elif method == "sub":
#         click.echo("{} - {} = {}".format(number1, number2,number1-number2))
#     elif method == "mul":
#         click.echo("{} * {} = {}".format(number1, number2,number1*number2))
#     elif method == "div":
#         click.echo("{} / {} = {}".format(number1, number2,number1/number2))
#     elif method == "mod":
#         click.echo("le reste de la division de {} par  {} est {}".format(number1, number2,number1%number2))

@click.command()
@click.argument("source", nargs=-1)
@click.argument("destination", nargs=1)
def  main(source, destination):
    click.echo(source)
    click.echo(destination)
    for f in source:
        click.echo(f)
        click.echo(destination)
       
        click.echo("Moving {} to Folder {}".format(f, destination))


if __name__ == "__main__":
    main()