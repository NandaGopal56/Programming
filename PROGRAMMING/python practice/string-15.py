"""
Write a Python function to create the HTML string with tags around the word(s). Go to the editor
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""
def add_tags(tag,str):
    first='<'+tag+'>'
    second='</'+tag+'>'
    str="'"+first+ str +second+"'"

    print(str)

def alternate_method(tag,str):
    
    print("<%s>%s</%s>" %(tag,str,tag))

add_tags('i', 'Python')
add_tags('b', 'Python Tutorial')

alternate_method('i', 'Python')
alternate_method('i', 'Python tutorial')