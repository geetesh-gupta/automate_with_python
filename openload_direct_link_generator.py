

from openload import OpenLoad

username = '832f1bf304225c91'
key = '_fi7pPg3'

ol = OpenLoad(username, key)

file_id = 'LEt0K7TfwvI'

# Get a download ticket and captcha url.
preparation_resp = ol.prepare_download(file_id)
ticket = preparation_resp.get('ticket')

# Sometimes no captcha is sent in openload.co API response.
captcha_url = preparation_resp.get('captcha_url')

if captcha_url:
    # Solve captcha.
    captcha_response = solve_captcha(captcha_url)
else:
    captcha_response = ''

download_resp = ol.get_download_link(file_id, ticket, captcha_response)
direct_download_url = download_resp.get('url')

# Process download url.
print(direct_download_url)
