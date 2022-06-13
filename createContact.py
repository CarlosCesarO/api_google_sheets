from quickstart import main
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

def create_contact(name,telephone,email):

    creds = main()

    try:
        service = build('people', 'v1', credentials=creds)

        results = service.people().createContact(body={
        "names": [
            {
                'givenName': name
            }
        ],
        "phoneNumbers": [
            {
                'value': telephone
            }
        ],
        "emailAddresses": [
            {
                'value': email
            }
        ]
        }).execute()

    except HttpError as err:
        print(err)