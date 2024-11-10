import click


@click.command()

# work with argument
@click.argument('number1', type=int )
@click.argument('number2', type=int)
@click.argument('method', default='add')

def main(number1, number2, method):
    if method == "add":
        click.echo("{} + {} = {}".format(number1, number2,number1+number2))
    elif method == "sub":
        click.echo("{} - {} = {}".format(number1, number2,number1-number2))
    elif method == "mul":
        click.echo("{} * {} = {}".format(number1, number2,number1*number2))
    elif method == "div":
        click.echo("{} / {} = {}".format(number1, number2,number1/number2))
    elif method == "mod":
        click.echo("le reste de la division de {} par  {} est {}".format(number1, number2,number1%number2))


if __name__ == "__main__":
    main()