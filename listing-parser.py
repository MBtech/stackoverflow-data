import urllib2
from bs4 import BeautifulSoup

base_url = "https://stackoverflow.com/jobs?sort=p"

page = urllib2.urlopen(base_url)
soup = BeautifulSoup(page, 'html.parser')

pagination = soup.find('div', attrs={'class': 'pagination'})
pages = pagination.find_all('a')

# Need to use the second last <a> element
num_pages = int(pages[-2].find('span').get_text().strip())

job_items_div = soup.find('div', attrs={'class': 'listResults'})
job_items = job_items_div.find_all('div')

jobs = list()
for job_item in job_items:
    if job_item.has_attr('data-jobid'):
        # print job_item
        job_summary = job_item.find('div', attrs={'class': '-job-summary'})
        job = dict()
        title = job_summary.find('div', attrs={'class': '-title'})
        job['id'] = title.find('span')['data-jobid']
        job['title'] = title.find('h2').get_text().strip()
        company_info = job_summary.find('div', attrs={'class': '-company'})
        job['company'] = company_info.find_all('span')[0].get_text().strip()
        job['location'] = company_info.find_all(
            'span')[1].get_text().replace('-', '').strip()

        perks_info = job_summary.find(
            'div', attrs={'class': '-perks'})
        job['perks'] = list()
        if perks_info != None:
            perks_info = perks_info.find_all('span')


            for perk_info in perks_info:
                job['perks'].append(perk_info.get_text().strip())


        tags_info = job_summary.find(
            'div', attrs={'class': '-tags'}).find_all('a')
        job['tags'] = list()
        for tag_info in tags_info:
            job['tags'].append(str(tag_info.get_text().strip()))

        print job['title']
        print job['id']
        print job['company']
        print job['location']
        print job['tags']
        print job['perks']


# for page_num in range(2, num_pages+1):
#     url = "https://stackoverflow.com/jobs?sort=p&pg=" + str(page_num)
#     page = urllib2.urlopen(base_url)
#     soup = BeautifulSoup(page, 'html.parser')
