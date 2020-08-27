# User Activity
## ft-Backend-Assesment

Tasks Done

  - User Model and ActivityPeriod Models
  - Loaded sample data
  - API for user-activity-period list

### Endpoints 

  - http://ansumansingh.pythonanywhere.com/api/users/ (as per given sample TEST.json)
  - http://ansumansingh.pythonanywhere.com/api/users-paginated/ ( with pagination, differs with the given TEST.json)

Output
```
{
    "ok": true,
    "members": [
        {
            "id": "WEFAF14EF",
            "real_name": "James Miller",
            "tz": "Europe/Nicosia",
            "activity_periods": [
                {
                    "start_time": "May 11 2020 10:09 AM",
                    "end_time": "Jul 02 2020 09:56 AM"
                },
                {
                    "start_time": "May 11 2020 10:09 AM",
                    "end_time": "Jul 02 2020 09:56 AM"
                }
            ]
        },
        {
            "id": "WA6A33979",
            "real_name": "Jimmy Williams",
            "tz": "America/Resolute",
            "activity_periods": [
                {
                    "start_time": "Jan 12 2020 12:23 PM",
                    "end_time": "May 09 2020 12:29 PM"
                },
                {
                    "start_time": "Jan 12 2020 12:23 PM",
                    "end_time": "May 09 2020 12:29 PM"
                },
                {
                    "start_time": "Jan 12 2020 12:23 PM",
                    "end_time": "May 09 2020 12:29 PM"
                },
                {
                    "start_time": "Jan 12 2020 12:23 PM",
                    "end_time": "May 09 2020 12:29 PM"
                },
                {
                    "start_time": "Jan 12 2020 12:23 PM",
                    "end_time": "May 09 2020 12:29 PM"
                }
            ]
        }
	]
}

```


### Requirments

* django - Backend Development Web Framework.
* Django REST framework - RESTful support for django 
* flake - for pep8
* Faker - generates realistic fake data for sample
* tqdm - shows loader in terminal, while loading sample data.


### Installation

for running locally

```sh
$ git clone https://github.com/ansuman13/ft-user-activity.git
$ cd ft-user-activity
$ virtualenv -ppython3 venv
$ source venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python manage.py migrate
(venv)$ python manage.py load_sample 10
Creating user and their Activity:
100%|██████████████████████████████████████| 10/10 [00:03<00:00,  2.66it/s]
(venv)$ python manage.py runserver 8000
```


### management commands

| Command | Action |
| ------ | ------ |
| load_sample | Loads sample data of specificed users e.g. load_sample 10|
| delete_all_users | deletes all non-staff users  |

Django Admin Panel:  
    email: ############  
    password: #########

