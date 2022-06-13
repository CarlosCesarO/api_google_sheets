from quickstart import main
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# def create_task():

#     creds = main()

#     try:
#         service = build('tasks', 'v1', credentials=creds)

#         body = [

#         ]

#         results = service.tasklists().insert(tasklist=,body={
#         "title": "TESTE"
#         }).execute()

#     except HttpError as err:
#         print(err)


def create_task():

    creds = main()

    try:
        service = build('tasks', 'v1', credentials=creds)

        body = [

        ]

        results = service.tasklists().get(tasklist="CONTEÚDO E PRODUTO").execute()

        print(results)

    except HttpError as err:
        print(err)


create_task()