if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):

        # This line splits the input into a name and a list of scores.
        # Example input: "Krishna 67 68 69"
        # After split(): ['Krishna', '67', '68', '69']
        # name = 'Krishna', *line = ['67', '68', '69']

        name, *line = input().split()

#The * (star) operator allows "unpacking" multiple values into a list.
#Since the first value is always the name and the rest are scores, name, *line splits the first token into name and the remaining tokens into line as a list.

        # We now convert each string score in 'line' to float using map().
        # So scores becomes: [67.0, 68.0, 69.0]

        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    if query_name in student_marks:
        val_list = student_marks[query_name]
        avg = sum(val_list) / len(val_list)
        print(f"{avg:.2f}")
    else:
        print("Query name is not in dictionary")
