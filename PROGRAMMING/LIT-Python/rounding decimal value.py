if __name__ == '__main__':
    from decimal import Decimal
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    avg = sum(marks) / len(marks)

    print("{0:.2f}".format(avg))   #this is used to round a integer upto some decimal point if it is less than the target decimal point also

                                 #or round() can be also used----->round(num,point)
    """
    input->
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

     output->
avg mark of malika

    """