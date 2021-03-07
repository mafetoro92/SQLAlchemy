from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, asc
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///task.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Tabla(Base):
    __tablename__ = 'homewords'
    id = Column(Integer, primary_key=True)
    assignment = Column(String, default='default task')
    limit_Date = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.assignment


Base.metadata.create_all(engine)

today = datetime.today().date()


class project_task:
    def __init__(self):
        self.rows = session.query(Tabla).all()
        self.today_row = session.query(Tabla).filter(Tabla.limit_Date == today).all()
        self.user_options = input(
'''1)today tasks
2) weeks tasks
3) all tasks
4) forgotten tasks
5)add tasks
6)delete tasks
0)quit
''')

    def option_1(self):
        if self.user_options == '1':
            print(f'\n{today}')
            if len(self.today_row) > 0:
                for count, item in enumerate(self.today_row):
                    print(f'{count + 1}. {item}\n')
            else:
                print('no tasks for today')

    def option_2(self):
        if self.user_options == '2':
            print(f'\n{today}')
            if len(self.today_row) > 0:
                for count, item in enumerate(self.rows):
                    print(f'{count + 1}. {item}\n')
            else:
                print('nothing for today')

            def days(n):
                d=today + timedelta(n)
                print(d)
                tasks=[]
                for j in self.rows:
                    if j.limit_Date == d:
                        tasks.append(j)
                if len(tasks) > 0:
                    for c, i in enumerate (tasks):
                        print(f'{c+1}.{i}\n')
                else:
                    print('nothing for today')
            days(1)
            days(2)
            days(3)
            days(4)
            days(5)
            days(6)

    def option_3(self):
        if self.user_options == '3':
            print('\n All tasks:')
            u=session.query(Tabla).order_by(asc(Tabla.limit_Date)).all()
            if len(u) > 0:
                for count,item in enumerate (u):
                    print(f'{count+1}. {item}. {item.limit_Date}')
                print()
            else:
                print('No tasks')

    def option_4(self):
        if self.user_options == '4':
            print('\n forgotten tasks')
            u = session.query(Tabla).order_by(asc(Tabla.limit_Date)).all()
            m=[]
            for item in u:
                if item.limit_Date < today:
                    m.append(item)
            if len(m) > 0:
                for c, i in enumerate(m):
                    print(f'{c+1}. {i}.{i.limit_Date}')
                print()
            else:
                print('You dont forget any tasks')

    def option_5(self):
        if self.user_options == '5':
            print('\n which is the tasks')
            task_ingre=input()
            print('\n Add the limit day in the next format (AAAA-MM-DD)')
            limit=input()
            x=limit.split('-')
            date_tasks=datetime(int (x[0]),int(x[1]),int(x[2])).date()
            new_tasks=Tabla(assignment=task_ingre, limit_Date= date_tasks)
            session.add(new_tasks)
            session.commit()
            print('Your tasks is in the Data\n')

    def option_6(self):
        if self.user_options == '6':
            u = session.query(Tabla).order_by(asc(Tabla.limit_Date)).all()
            if len(u) > 0:
                print('\n select the number of the tasks do you want to delete:')
                for count, i in enumerate(u):
                    print(f'{count+1}. {i}. {i.limit_Date}')
                delete=input()
                for c,i in enumerate(u):
                    if int(delete) == c + 1:
                        session.delete(i)
                        session.commit()
                print('\The tasks was deleted succefully')
            else:
                print('\n you dont have tasks to delete')


    def option_0(self):
        if self.user_options == '0':
            print('\nsee you later')
            exit()

while True:

    call = project_task()
    call.option_1()
    call.option_2()
    call.option_3()
    call.option_4()
    call.option_5()
    call.option_6()
    call.option_0()


