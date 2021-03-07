DB={}
final={}

def insert_data(filename,owner):
    DB[filename]=owner

def main():
    insert_data('input.txt', 'stan')
    insert_data('gopal.txt', 'nanda')
    insert_data('papu.txt', 'nanda')
    insert_data('nanda.txt', 'nanda')
    insert_data('stan.txt', 'stan')
    insert_data('code.py','randy')
    insert_data('output.txt','randy')

main()
print(DB,end="\n")
print(final)
for key in DB:
    if DB[key] in final:
        final[DB[key]].append(key)
    else:
        final[DB[key]]=[key]

print(final)

