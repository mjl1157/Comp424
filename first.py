"""docstring
Matthew Levasseur
3/31/2022"""
def main():
    input1 = 'math'
    input2 = ['math', 'comp', 'eng', 'math']
    result = count_course(input1, input2)
    print(result)
    input1 = 'eng'
    result = count_course(input1, input2)
    print(result)

"""The count_course function will take the given_name of a course and iterate
over the course list input of variable courses counting and accumulating each
time that course appears in the list to variable course_count"""

def count_course(given_name, courses):#function header
    course_count = 0 #local accumulating variable
    for course in courses:  #for loop iterating over list courses.
        if course == given_name: #conditional set to run code if course matches
                                 #given_name
            course_count += 1 #accumulating code that runs if course matches
    return course_count #returns the total number of matches

"""The course_frequency function will iterate through the list courses using
for loop, conditional statement and a dictionary accumulator to track course as
the key and number of times that course appears as the value"""

courses = ['math', 'comp', 'eng', 'math'] #List input for course_frequency test

def course_frequency(list): #function header
    cf = {} #dictionary accumulator variable initialized
    for course in list: #for loop iterating over variable list
        if course not in cf: #conditional to run if course not in dictionary
            cf[course] = 1 #adds the course at intial key value 1
    cf[course] = cf[course] + 1 #adds 1 to the key value/count in dictionary
    return(cf)#returns the accumulated dictionary with frequecy values



















main()
print(course_frequency(courses))
