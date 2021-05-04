import mysql.connector
#establishing the connection
conn = mysql.connector.connect(user='root', password='bhavana31',database='NEWHORIZON')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
print("*-----NEW HORIZON COVID HELP DESK-----*\n1.Student\n2.Faculty ")
choice=input("Enter your choice to login:")
if choice==1:
    usn=str(input("Please enter your usn:"))
    sql_select_query = """SELECT NAME FROM STUDENTS WHERE USN =%s"""
    cursor.execute(sql_select_query,(usn,))
    res1=cursor.fetchone()
    print("Welcome,",res1)
    print("HOPE YOU ARE DOING GOOD :) ")
    print("Remember our 3 protective layers...\n1.Wear mask\n2.Maintain Social distancing\n3.Sanitize often")
    print("****BEWARE OF COVID VIRUS!!****\n1.Covid Symptoms\n2.Covid Positive\n3.Post a message")
    choice_student=input("Please enter your choice further:")
    if choice_student==1:
        print("Kindly answer the below questions(Please give answers as yes/no)")
        ques1=str(input("\nQ1).Are you suffering from cold?"))
        ques2=str(input("\nQ2).Do you have fever?"))
        ques3=str(input("\nQ3).Do you have stomach ache?"))
        ques4=str(input("\nQ4).Do you have headache?"))
        ques5=str(input("\nQ5).Do you have body pains?"))
        ques6=str(input("\nQ6).Do you have thraot pain?"))
        print("---------Thank you for answering the above questions!!---------")
        sql_Query = "select * from DRAPPOINTMENT"
        cursor.execute(sql_Query)
        records = cursor.fetchall()
        print("\nDr.NHCE is available in the below dates and timings")
        for row in records:
            print("DATE AVAILABLE : ", row[0], )
            print("TIME AVAILABLE : ", row[1],":",row[2],row[3],"\n")
        date_select=str(input("\nPlease enter the date for appointment with Dr.NHCE:"))
        print("Please enter the timings:")
        hour_select=int(input("\nPlease enter the hour:"))
        min_select=int(input("\nPlaese enter the minute:"))
        apm_select=input("Please enter AM or PM:")
        print("\nYour appointment with Dr.NHCE is scheduled on:",date_select,"at",hour_select,":",min_select,apm_select)
        print("\nTake good care of yourselves until then!!Get well soon!!")
        sql="INSERT INTO DRAPPOINTMENTFIXED VALUES(%s,%s,%s,%s)"
        cursor.execute(sql,(date_select,hour_select,min_select,apm_select,))
        #commit changes to database
        conn.commit()
  

elif choice==2:
    faculty_id=int(input("Please enter faculty ID:"))
    sql_select="""SELECT FNAME FROM FACULTY WHERE FNO=%s"""
    cursor.execute(sql_select,(faculty_id,))
    res2=cursor.fetchone()
    print("Welcome",res2)
    print("HOPE YOU ARE DOING GOOD :) ")
    print("Remember our 3 protective layers...\n1.Wear mask\n2.Maintain Social distancing\n3.Sanitize often")
    print("****BEWARE OF COVID VIRUS!!****\n1.Covid Symptoms\n2.Covid Positive\n3.Post a message")
    choice_faculty=input("Please enter your choice further:")
    if choice_faculty==1:
        print("Kindly answer the below questions(Please give answers as yes/no)")
        ques1=str(input("\nQ1).Are you suffering from cold?"))
        ques2=str(input("\nQ2).Do you have fever?"))
        ques3=str(input("\nQ3).Do you have stomach ache?"))
        ques4=str(input("\nQ4).Do you have headache?"))
        ques5=str(input("\nQ5).Do you have body pains?"))
        ques6=str(input("\nQ6).Do you have thraot pain?"))
        print("---------Thank you for answering the above questions!!---------")
        sql_Query = "select * from DRAPPOINTMENT"
        cursor.execute(sql_Query)
        records = cursor.fetchall()
        print("\nDr.NHCE is available in the below dates and timings")
        for row in records:
            print("DATE AVAILABLE : ", row[0])
            print("TIME AVAILABLE : ", row[1],":",row[2],row[3],"\n")
        print("\nPlease note that appointments below are already fixed,kindly select date and timings other than that.\n")
        sqlfixed="select * from DRAPPOINTMENTFIXED"
        cursor.execute(sqlfixed)
        result=cursor.fetchall()
        for r in result:
            print("Date fixed :",r[0])
            print("Time fixed :",r[1],r[2],r[3],"\n")
        date_select=str(input("\nPlease enter the date for appointment with Dr.NHCE:"))
        print("Please enter the timings:")
        hour_select=int(input("Please enter the hour:"))
        min_select=int(input("Plaese enter the minute:"))
        apm_select=input("Please enter AM or PM:")
        print("\nYour appointment with Dr.NHCE is scheduled on:",date_select,"at",hour_select,":",min_select,apm_select)
        print("\nTake good care of yourselves until then!!Get well soon!!")
        sql="INSERT INTO DRAPPOINTMENTFIXED VALUES(%s,%s,%s,%s)"
        cursor.execute(sql,(date_select,hour_select,min_select,apm_select,))
        #commit changes to database
        conn.commit()

 




