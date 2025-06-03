import urllib.parse

def get_decoded_string(a: str) -> str:
    return urllib.parse.unquote(a)


def get_query_param(url:str, param_name:str) -> str | None:
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    if param_name in query_params:
        return urllib.parse.unquote(query_params[param_name][0])
    else:
        return None


if __name__ == "__main__":
    string = "4%2F0AUJR-x5si_9bXr8GSfNw_Wn0BhCgAO68ormPjBHUakiag3UmqQSHSplwy8z1p9BqgS0Iow"
    print(get_decoded_string(string))

    url = "http://localhost:4002/auth/google/callback?code=4%2F0AUJR-x4fjiDaJIi40Jz_ZCSOAUmK-Um5KfZNGdD67jhfXb-WDchC1S02u3VFAnfrZp-YbQ&scope=email+profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.profile+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email+openid&authuser=0&prompt=consent"
    print(get_query_param(url=url, param_name="code"))

