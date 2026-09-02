import whois

def check_whois(domain: str):
    """lookup domain registration, owner details, and whois information for any website"""
    try:
        w = whois.whois(domain)
        return {
            "domain": domain,
            "registrar": w.registrar,
            "created": str(w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date),
            "expires": str(w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date),
            "owner": w.org
        }
    except Exception as e:
        return f"> WHOIS lookup failed: {str(e)}"
