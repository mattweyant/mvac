import csv
from string import Template

# TEMPLATE = Template("""
#     <tr>
#         <td>$name</td>
#         <td>$location</td>
#         <td>$neighborhood</td>
#         <td>$latitude</td>
#         <td>$longitude</td>
#     </tr>""")
#
# with open('final-memorials.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print TEMPLATE.substitute(row)

TEMPLATE = Template("""
    <tr>
        <td>$first</td>
        <td>$middle</td>
        <td>$last</td>
        <td>$suffix</td>
    </tr>""")

out = open('wwii.html', 'w')
with open('wwii-vets.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        out.write(TEMPLATE.substitute(row))
out.flush()
out.close()