
# First I create a dictionary indicating which moment of the day represent each hour

# horarios = {'Night': ['00', '01', '02', '03', '04', '05', '20', '21', '22', '23'], 'Morning': ['06', '07', '08', '09', '10', '11'], 'Afternoon': ['12', '13', '14', '15', '16'], 'Evening': ['17', '18', '19']}

# Then I create the function so I can replace the hour by a specific moment of the day

def cambia_hora(x):
    horarios = {'Night': ['00', '01', '02', '03', '04', '05', '20', '21', '22', '23'], 'Morning': ['06', '07', '08', '09', '10', '11'], 'Afternoon': ['12', '13', '14', '15', '16'], 'Evening': ['17', '18', '19']}
    for key, values in horarios.items():
        if x[0:2] in values:
            return key
    return x



# Now, for my hypotheses #3 I need to use the regex function to simplify the column of Activities. This way I can identify in a simple way if surfing is actually the activity ending the most in fatality 

import re

def cambia_activity(x):
    dicc_activities = { 
        'Surfing': '.*urf.*|.*addl.*|.*oard.*|.*Board.*|.*surf.*|.+Surf.*',
        'Swimming': '.*wi.*|.*mmi.*|.*bath.*|.*ading.*|.*swim.*',
        'Fishing': '.*shin.*|.*fish.*|.*Fish.*',
        'Diving': '.*spear.*|.*div.*|.*photo.*|.*subm.*|.*merged.*|.*norkel.*|.*scuba.*',
        'Boating': '.*kay.*|.*yak.*|.*banana.*|.*sail.*|.*atch.*|.*anoing.*',
        'Feeding': '.*feed.*|.*food.*'
        }
    for key, values in dicc_activities.items():
        if re.match(values, x):
            return key
    return 'Other'


