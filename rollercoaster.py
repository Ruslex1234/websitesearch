import requests
#page = requests.get('https://www.nrk.no/mp3/spillelister/sistspilt/?dato=11-12-2019&time=13')
#print (page.text.encode('utf8'))
years=['2019']
months = ['12']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27']
hours = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
for year in years:
    for month in months:
        for day in days:
            for hour in hours:
                url = 'https://www.nrk.no/mp3/spillelister/sistspilt/?dato='+month+"-"+day+"-"+year+"&time="+hour
                count = requests.get(url).text.count('About You')
                if count > 0:
                    print(year+month+day+hour)
