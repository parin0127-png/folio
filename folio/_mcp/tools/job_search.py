from jobspy import scrape_jobs
import requests, re

def linkedin_jobs(query: str, location: str, time):
    """search for job listings, career opportunities, and hiring positions on linkedin by role and location"""
    try:
        jobs = scrape_jobs(
            site_name = ["indeed", "linkedin", "google"],
            search_term = query,
            location = location,
            results_wanted = 10,
            hours_old = time
        )

        if jobs.empty:
            return "> No job found !"

        results = []
        for _, job in jobs.iterrows():
            results.append(
                {
                    "title" : job.get("title"),
                    "company" : job.get("company"),
                    "location": job.get("location"),
                    "url" : job.get("job_url"),
                    "date" : str(job.get("date_posted"))
                }
            )
        return results
    except Exception as e:
        return f"> Job search failed: {e}."


def eu_job(query: str):
    try:
        url = "https://www.arbeitnow.com/api/job-board-api"
        # headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url)
        data = response.json()

        results = []
        for job in data.get("data" , []):
            title = job.get("title", "").lower()
            tags = " ".join(job.get("tags", [])).lower()

            desc = re.sub(r"<[^>]+>", "", job.get("description", "")).lower()
            if query.lower() in title or query.lower() in tags or query.lower() in desc:
                results.append({
                    "title": job.get("title"),
                    "company": job.get("company_name"),
                    "location": job.get("location"),
                    "url" : job.get("url"),
                    "remote": job.get("remote")
                })

            if len(results) >= 5:
                break 
        return results if results else "> No EU jobs found"
    except Exception as e:
        return f"> EU job search failed: {str(e)}"

def remote_tech_job(query: str):
    try:
        url = "https://remotive.com/api/remote-jobs"
        params = {"search": query, "limit": 5}
        data = requests.get(url, params = params).json()

        results = []
        for job in data.get("jobs", []):
            results.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "url": job.get("url"),
                "date": job.get("publication_date")
            }) 

        return results if results else "> No remote job found !"
    except Exception as e:
        return f"> Remote job search failed: {e}"


def startups_find(query: str):
    """find job openings, hiring, and career opportunities at top funded startups and tech companies"""
    STARTUPS = [
        "airbnb", "vercel", "figma", "stripe", "anthropic",
        "cloudflare", "datadog", "brex", "ramp", "rippling",
        "gusto", "snyk", "retool", "loom", "miro",
        "mercury", "deel", "cohere", "postman", "airbyte",
        "notion", "supabase", "gitlab", "mistral", "huggingface",
        "linear", "raycast", "resend", "cal", "dub",
        "trigger", "novu", "infisical", "formbricks", "documenso",
        "liveblocks", "tinybird", "together"
    ]
    try: 
        results = []

        for company in STARTUPS:
            try:
                url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
                data = requests.get(url, timeout = 3).json()
                for job in data.get("jobs", []):
                    if query.lower() in job.get("title", "").lower():
                        results.append({
                            "title": job.get("title"),
                            "company": company,
                            "url": job.get("absolute_url")
                        })
            except:
                pass

            try:
                url = f"https://jobs.ashbyhq.com/api/non-guest/job-board/job-postings?organizationHostedJobsPageName={company}"
                data = requests.get(url, timeout=3).json()
                for job in data.get("jobPostings", []):
                    if query.lower() in job.get("title", "").lower():
                        results.append({
                            "title"   : job.get("title"),
                            "company" : company,
                            "url"     : f"https://jobs.ashbyhq.com/{company}/{job.get('id')}"
                        })
            except:
                pass

            try:
                url = f"https://api.lever.co/v0/postings/{company}"
                data = requests.get(url, timeout = 3).json()
                for job in data:
                    if query.lower() in job.get("text", "").lower():
                        results.append({
                            "title"   : job.get("text"),
                            "company" : company,
                            "url"     : job.get("hostedUrl")
                        })
            except:
                pass

            if len(results) >= 5:
                break
        return results if results else "> No opening found in Startups"
    except Exception as e:
        return f"> Failed to openings in startups: {str(e)}"
    
def remote_and_eu_jobs(query: str):
    """find remote work, work from home, and european job openings and internships in tech"""
    results = []
    remote = remote_tech_job(query)
    eu = eu_job(query)

    if isinstance(remote, list):
        results.extend(remote)

    if isinstance(eu, list):
        results.extend(eu)

    return results if results else "> No jobs found"

