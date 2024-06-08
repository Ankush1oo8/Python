#search on pypi.org
import prettytable
table=prettytable.PrettyTable()
table.add_column("Pokemon",["Pikachu","Modi","Rahul"])
table.add_column("Type",["Electric","Politics","Madness"])

table.align="l"

print(table)