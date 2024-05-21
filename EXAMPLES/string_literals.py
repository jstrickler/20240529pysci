s1 = "spam\n"   # all 4 are the same
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print()
print('Guido is the ex-"BDFL" of Python')
print()
print("""Guido's the ex-"BDFL" of Python""")
print(""" wheeeee "" hooray '' """)

query = """
select *
from customers
where state = "NV" 
   and current_balance > 10000
order by zip_code desc
"""

