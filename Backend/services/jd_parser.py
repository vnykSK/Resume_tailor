import requests
from bs4 import BeautifulSoup


def scrape_job_url(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    return soup.get_text(separator=" ")



def parse_job_description(job_description=None, job_url=None):

    if job_description:
        return job_description

    if job_url:
        return scrape_job_url(job_url)

    raise Exception("Provide either job description or job URL")