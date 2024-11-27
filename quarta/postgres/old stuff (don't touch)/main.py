import matplotlib.pyplot as p
from query import get_part_vendors

def percentage(pct, values):
    abs = int(pct / 100. * sum(values))
    return "{:.1f}%\n({:d})".format(pct, abs)

def main():
    vendors = {}

    for product, vendor in get_part_vendors():
        vendors[vendor] = vendors.get(vendor, 0) + 1

    labels = list(vendors.keys())
    values = list(vendors.values())

    p.figure(figsize=(10, 7))
    p.pie(values, labels=labels, autopct=lambda pct: percentage(pct, values), startangle=140)
    p.axis('equal')
    p.show()


if __name__ == '__main__':
    main()
