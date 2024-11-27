import psycopg2
from config import load_config

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query(year):
    return ("""
        SELECT c.name AS genre, COUNT(DISTINCT f.film_id) AS movie_count FROM rental r
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE EXTRACT(YEAR FROM r.rental_date) = """ + year + """ GROUP BY c.name;
    """)

def get_rentals(year):
    config = load_config()
    result = []

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query(year))

                for row in iter_row(cur, 10):
                    result.append(row)
                return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
