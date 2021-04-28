import requests

# Implicit Grant Flow from FitBit API
# Get token from doing request in browser
token = ""  # emitted for github
header = {'Authorization': 'Bearer {}'.format(token)}


def get_date():
    date = input("Enter date (yyyy-MM-dd): ")
    return date


def create_request(date):
    request_url = "https://api.fitbit.com/1/user/-/sleep/date/"+date+".json"
    return request_url


def format_and_print_response(response):
    deep = response['summary']['stages']['deep']
    light = response['summary']['stages']['light']
    rem = response['summary']['stages']['rem']
    awake = response['summary']['stages']['wake']
    total = response['summary']['totalMinutesAsleep']
    time_in_bed = response['summary']['totalTimeInBed']

    print("\nTime in bed: "+str(round(time_in_bed/60, 1))+" hour(s)")
    print("Time asleep: "+str(round(total/60, 1))+" hour(s)")
    print("\nStages:")
    print("\tDeep: "+str(round(deep/total, 2) * 100)+"% ("+str(round(deep/60, 2))+" hour(s))")
    print("\tLight: " + str(round(light/total, 2) * 100)+"% ("+str(round(light/60, 2))+" hour(s))")
    print("\tREM: " + str(round(rem/total, 2) * 100)+"% ("+str(round(rem/60, 2))+" hour(s))")
    print("\tAwake: " + str(round(awake/total, 2) * 100)+"% ("+str(round(awake/60, 2))+" hour(s))")


request = create_request(get_date())

response = requests.get(request, headers=header).json()

format_and_print_response(response)
