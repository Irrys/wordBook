
import requests


class Crawler:
    def __init__(self, url_base, user_agent):
        self.url_base = url_base
        self.user_agent = user_agent

    def request(self, word):
        url = self.url_base + word
        headers = {'User-Agent': self.user_agent}
        html_content = ''
        try:
            # Send a GET request to the URL with headers and verify=False to ignore SSL certificate
            response = requests.get(url, headers=headers, verify=True)

            # Check if the request was successful
            if response.status_code == 200:
                # Print the content of the response (HTML source code)
                # print(response.text[:1000]) # printing first 1000 characters for brevity
                print("request successful!")
                html_content = response.text
            else:
                print(f"Failed to retrieve the webpage: Status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Catch any exceptions that might occur
            print(f"An error occurred: {e}")

        return html_content
