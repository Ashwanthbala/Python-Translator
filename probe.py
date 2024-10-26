import requests

def check_url(out_file):
    good_url = []
    bad_url = []
    with open("urllist.txt", "r") as file:
        for line in file:
            url = line.strip()  # Remove any trailing whitespace or newline characters
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    good_url.append(url)
                else:
                    bad_url.append(url)
            except:
                bad_url.append(url)
                continue

    with open(out_file,"w") as file:
        file.write('\n'.join(good_url))






out_file = 'filtered.txt'

check_url(out_file)

