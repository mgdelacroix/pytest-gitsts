import requests

def build_gist_list_url(user):
    return "https://api.github.com/users/%s/gists" % user

def get_user_gists(user):
    url = build_gist_list_url('mgdelacroix')
    gist_list = requests.get(url)
    return gist_list

def get_user_gists_status_code(user):
    gist_list = get_user_gists(user)
    return gist_list.status_code

if __name__ == '__main__':
    print(get_user_gists_status_code('mgdelacroix'))
