counties = ['Arapahoe','Denver', 'Jefferson']
if counties[1] == 'Denver':
   print(counties[1])
counties = ['Arapahoe', 'Denver','Jefferson']
if'El Paso' in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso is not in the list of counties')
if 'Arapahoe'in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties.')
else:
    print('Arapahoe and El Paso are not in the list of counties')

for county in counties:
    print(county)

counties_dict = {'Arapahoe': 369237,'Denver': 4123229, 'Jefferson': 390222}
for county, voters in counties_dict.items():
    print( county  +  ' county has '  +  str(voters)  +  ' registered voters.')

candidate_votes = int(input('how many votes did the candidate get in the election? '))

total_votes = int(input('what is the total number of votes in the election? '))

message_to_candidate = (
    f'you received {candidate_votes} number of votes. '
    f'the total number of votes in the election was {total_votes}. '
    f'you received {candidate_votes / total_votes * 100}% of the total votes.')


print(message_to_candidate)