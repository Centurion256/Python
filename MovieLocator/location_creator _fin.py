def file_reader(films, years):

    filmbase = open(films, 'r', encoding='latin-1')
    locations = dict()
    for line in info_generator(filmbase, years):
        if line[-1] not in locations:

            locations[line[-1]] = 0

        locations[line[-1]] += 1
    
    return locations


def info_generator(source, year):

    import re
    line = []
    line_prev = line

    while line_prev != '' or line != '':
        line_prev = line
        line = source.readline()
        decodable = lambda x: len(x) == len(x.decode())(line[0])
        if (re.search(".+[ ]\(\d{4}.*\)[\t ]?", line) == None) or not(decodable) or str(year) not in line:
                
            continue

        else:

            line = re.sub("\t(?=\()", "-REPLACE-", line)
            sliced = re.split("\"?[ ]\((?=\d{4})|(?<=\(\d{4})\) ?[{\(]?.+?[}\)]?\t{1,10}(?=\w)|\t{1,10}(?!\([\d\s]+?\)|\()", line)
            name = sliced[0].strip('\"')
            release = re.sub('/.+', '', sliced[1])
            location = re.sub("-REPLACE-.+$", '', sliced[2])
            country = location.split(',')[-1].strip(' ').strip('\n')
            yield name, release, location, country


def map_creator(data, name):

    import folium
    import branca

    country_data = 'world.json'
    lim = max(data.values())
    third_lim = 50 if int(lim**1/4) > 50 else int(lim**1/4)
    colorscale = branca.colormap.LinearColormap(colors=['white', 'green', 'yellow', 'red', 'black'],
                                                index=[0, 1, third_lim, int(lim**1/2), lim+1])

    def fix_names(country):

        transcriber = {
            'United States': 'USA',
            'United Kingdom': 'UK',
            'Libyan Arab Jamahiriya': 'Libya',
            'Syrian Arab Republic': 'Syria',
            'Republic of Moldova': 'Moldova',
            'Iran (Islamic Republic of)': 'Iran',
            'Burma': 'Myanmar',
            'Lao People\'s Democratic Republic': 'Laos',
            'Viet Nam': 'Vietnam',
            'Korea, Democratic People\'s Republic of': 'North Korea',
            'Korea, Republic of': 'South Korea',
            'Timor-Leste': 'East Timor',
            'Micronesia, Federated States of': 'Micronesia',
            'United Republic of Tanzania': 'Tanzania',
            'The former Yugoslav Republic of Macedonia': 'Macedonia'}

        return transcriber[country] if country in transcriber else country

    map_custom = folium.Map(location=[51.4826, 0.0],
                            zoom_start=5, min_zoom=3, max_zoom=20, max_bounds=True, prefer_canvas=True, no_wrap=True,
                            tiles='Mapbox Bright')
    fg1 = folium.FeatureGroup(name="Movies filmed", overlay=False)

    folium.GeoJson(data=open(country_data, 'r', encoding='utf-8-sig').read(),
                   tooltip=folium.features.GeoJsonTooltip(fields=['NAME']),
                   style_function=lambda x: {'fillColor': colorscale(data[fix_names(x['properties']['NAME'])])
                   if fix_names(x['properties']['NAME']) in data else colorscale(0)}).add_to(fg1)
    
    colorscale_pop = branca.colormap.LinearColormap(colors=['white', 'green', 'yellow', 'red', 'black'],
                                                    index=[0, 5000000, 100000000, 200000000, 800000000])

    fg2 = folium.FeatureGroup(name="Population", overlay=False)
    folium.GeoJson(data=open(country_data, 'r', encoding='utf-8-sig').read(),
                   tooltip=folium.features.GeoJsonTooltip(fields=['NAME']),
                   style_function=lambda x: {'fillColor': colorscale_pop(x['properties']['POP2005'])}).add_to(fg2)
    map_custom.add_child(fg1)
    map_custom.add_child(fg2)
    map_custom.add_child(folium.LayerControl())
    map_custom.save(name + '.html')


if __name__ == "__main__":

    while True:
        try:
            year = int(input('Please enter a year between 1890 and 2015: '))
            if year not in range(1890,2016):
                input('Incorrect input. Are you sure the year entered is between 1890 and 2015? Press \'Enter\' to '
                      'relaunch the program or Ctrl+C to quit. ')
                continue
        except:
            input('Incorrect input. Are you sure you entered a number? Press \'Enter\' to relaunch the program or '
                  'Ctrl+C to quit. ')
            continue
        break
    movie_by_country = file_reader('locations.list', year)
    map_creator(movie_by_country, 'locations')
    print('Finished. File \'locations.html\' created. Thank you for using the program!')
