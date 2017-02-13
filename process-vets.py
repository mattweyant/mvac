import csv
from titlecase import titlecase

count = 0
vets = []
with open('vetslist.txt') as lines:
    for line in lines:
        count += 1
        line = line.strip()

        if line:
            print line
            last_suff, first_mi = line.split(',', 1)

            last_suff = last_suff.split()
            first_mi = first_mi.split()

            first = first_mi[0].strip()
            mi = None
            last = last_suff[0].strip()
            suff = None

            if len(first_mi) > 1:
                mi = first_mi[1].strip()

            if len(last_suff) > 1:
                suff = last_suff[1].strip()

            vets.append(
                {
                    'first': titlecase(first),
                    'middle': mi,
                    'last': titlecase(last),
                    'suffix': suff
                }
            )

print "Found %d vets" % count

with open('wwii-vets.csv', 'w') as out:
    writer = csv.DictWriter(out, fieldnames=['first', 'middle', 'last', 'suffix'])
    writer.writeheader()
    writer.writerows(vets)