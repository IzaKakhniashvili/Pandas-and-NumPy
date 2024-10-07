import pandas as pd
import matplotlib.pyplot as plt

students_data = pd.read_csv('student_scores_random_names.csv')

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']

def getFailedStudents(students_data):
    failed_students = students_data[students_data[subjects].lt(50).any(axis=1)]
    students = failed_students['Student'].unique()
    print("Students who could not pass at least one subject: ")
    for s in students:
        print(s)
        
        
def getAvgGrades(students_data):
    avg_grades = students_data[subjects].mean().reset_index()
    avg_grades.columns = ['Subject', "Average Grade"]
    print(avg_grades)
    
def getHighestAvgGrade(students_data):
    students_data['Average Grade'] = students_data[subjects].mean(axis=1)
    student_avg = students_data.groupby('Student')['Average Grade'].mean().reset_index()
    max_avg_grade = student_avg['Average Grade'].max()
    top_students = student_avg[student_avg['Average Grade'] == max_avg_grade]
    print(top_students)
    
def getHardestSubject(students_data):
    average_grades = students_data[subjects].mean()
    hardest_subject = average_grades.idxmin()
    print(f"Hardest subject: {hardest_subject}")

def createNewDataframe(students_data):
    average_grades_by_semester = students_data.groupby('Semester')[subjects].mean().reset_index()
    output_file_path = 'average_grades_by_semester.xlsx'
    average_grades_by_semester.to_excel(output_file_path, index=False)
    print(f"The average grades for each subject by semester have been saved to {output_file_path}.")
    
    return average_grades_by_semester


def plotAverageGradesBySubject(average_grades_by_semester):
    overall_avg = average_grades_by_semester[subjects].mean().reset_index()
    overall_avg.columns = ['Subject', 'Overall Average Grade']
    
    plt.figure(figsize=(10, 6))
    plt.bar(overall_avg['Subject'], overall_avg['Overall Average Grade'], color='skyblue')
    plt.title('Average Grade by Subject Across All Semesters')
    plt.xlabel('Subjects')
    plt.ylabel('Average Grade')
    plt.xticks(rotation=45)  
    plt.grid(axis='y')  
    plt.tight_layout()  
    plt.show()

def plotAverageGradesBySemester(average_grades_by_semester):
    
    plt.figure(figsize=(12, 8))
    for subject in subjects:
        plt.plot(average_grades_by_semester['Semester'], average_grades_by_semester[subject], marker='o', label=subject)
    
    plt.title('Average Grade for Each Subject by Semester')
    plt.xlabel('Semester')
    plt.ylabel('Average Grade')
    plt.xticks(rotation=45)  
    plt.grid()  
    plt.legend(title='Subjects')  
    plt.tight_layout() 
    plt.show()

def main():
    getFailedStudents(students_data)
    print("\nAverage Grades for Each Subject:")
    getAvgGrades(students_data)
    
    print("\nStudents with the Highest Average Grade:")
    getHighestAvgGrade(students_data)
    
    print("\nFinding the Hardest Subject:")
    getHardestSubject(students_data)
    
    print("\nCreating a new DataFrame with Average Grades by Semester:")
    average_grades_by_semester = createNewDataframe(students_data)
    
    plotAverageGradesBySubject(average_grades_by_semester)
    plotAverageGradesBySemester(average_grades_by_semester)
    
    
    
if __name__ == "__main__":
    main()