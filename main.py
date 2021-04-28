import requests

# Implicit Grant Flow from FitBit API
# Get token from doing request in browser
# token = input("Enter token: ")
token = ""  # emitted for github
header = {'Authorization': 'Bearer {}'.format(token)}


def get_date(text):
    day = input("\n"+text+" (yyyy-MM-dd): ")
    return day


def create_request(start, end, multi):
    if multi:
        request_url = "https://api.fitbit.com/1/user/-/sleep/date/"+start+"/"+end+".json"
    else:
        request_url = "https://api.fitbit.com/1/user/-/sleep/date/"+start+".json"
    return request_url


def single_day():
    request = create_request(get_date("Enter date"), "none", False)
    response = requests.get(request, headers=header).json()
    print_single_response(response)


def multi_day():
    print("\nMax 100 day range!")
    start = get_date("Start date")
    end = get_date("End date")

    request = create_request(start, end, True)
    response = requests.get(request, headers=header).json()

    print_multi_response(response)


def print_single_response(r):
    start_time = r['sleep'][0]['startTime'][11:19]
    efficiency = r['sleep'][0]['efficiency']
    deep = r['summary']['stages']['deep']
    light = r['summary']['stages']['light']
    rem = r['summary']['stages']['rem']
    awake = r['summary']['stages']['wake']
    total = r['summary']['totalMinutesAsleep']
    time_in_bed = r['summary']['totalTimeInBed']

    print("\nStart time: "+start_time)
    print("Efficiency: "+str(efficiency)+"%")
    print("\nTime in bed: "+str(round(time_in_bed/60, 1))+" hour(s)")
    print("Time asleep: "+str(round(total/60, 1))+" hour(s)")
    print("\nStages:")
    print("\tDeep: "+str(round(deep/total * 100, 1))+"% ("+str(round(deep, 2))+" minutes)")
    print("\tLight: " + str(round(light/total * 100, 1))+"% ("+str(round(light, 2))+" minutes)")
    print("\tREM: " + str(round(rem/total * 100, 1))+"% ("+str(round(rem, 2))+" minutes)")
    print("\tAwake: " + str(round(awake/total * 100, 1))+"% ("+str(round(awake, 2))+" minutes)")


def print_multi_response(r):
    delta = len(r['sleep'])

    total_asleep = 0
    total_efficiency = 0
    for i in range(delta):
        total_asleep += r['sleep'][i]['minutesAsleep']
        total_efficiency += r['sleep'][i]['efficiency']

    avg_efficiency = round(total_efficiency/delta, 1)
    avg_sleep = round((total_asleep/delta)/60, 2)

    print("\nTotal hours asleep: "+str(round(total_asleep/60, 2)))
    print("Avg. hours asleep: "+str(avg_sleep))
    print("Avg. sleep efficiency: "+str(avg_efficiency))


while True:
    choice = input("\nSingle or Multi? (s or m): ")
    if choice == "s":
        single_day()
    elif choice == "m":
        multi_day()
    else:
        print("Invalid choice.")
