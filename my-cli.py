import click


@click.command()
#basic options
@click.option("--name","-n", default="Musterman", help="Firstname description")

#multiple Values : !!! for this option 2 Arguments are required
@click.option("--favorites","-f", nargs=2, default=["Dance", "programing"], help="Your Favorites Activities")

#Multiples values
@click.option("--salary", "-s", type = int ,nargs=2, help="Your Monthly Salary")
def main(name, favorites, salary):
    click.echo("Hello World, My name is {} and my monthly salary is {}. These are my fovorites activities: {}".format(name,favorites, sum(salary)))



if __name__== "__main__":
    main()