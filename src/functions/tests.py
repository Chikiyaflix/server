import sys

import requests


def tmdb_test(config):
    if config.get("tmdb_api_key") != None and config.get("tmdb_api_key") != "":
        res = requests.get(
            "https://api.themoviedb.org/3/?api_key=%s" % (config.get("tmdb_api_key"))
        ).json()
        if res.get("status_code") != 34:
            print("\033[31mERROR! THE TMDB_API_KEY PROVIDED IS INCORRECT!\033[0m")
    else:
        print("\033[31mERROR! YOU HAVE NOT PROVIDED A TMDB_API_KEY!\033[0m")
        sys.exit()


def category_list_test(config):
    passed = True
    if isinstance(config.get("category_list"), list):
        for item in config.get("category_list"):
            if (
                (isinstance(item, dict))
                and (item.get("id", "") != "")
                and (item.get("name", "") != "")
                and (item.get("type") in ["Movies", "TV Shows"])
            ):
                pass
            else:
                passed = False
                break
    else:
        passed = False
    if passed == False:
        print("\033[31mERROR! YOUR CATEGORY_LIST IS NOT VALID!\033[0m")
        sys.exit()


def account_list_test(config):
    passed = True
    if isinstance(config.get("account_list"), list):
        for item in config.get("account_list"):
            if (
                (isinstance(item, dict))
                and (item.get("auth", "") != "")
                and (item.get("username", "") != "")
                and (item.get("password", "") != "")
            ):
                pass
            else:
                passed = False
                break
    else:
        passed = False
    if passed == False:
        print("\033[31mERROR! YOUR ACCOUNT_LIST IS NOT VALID!\033[0m")
        sys.exit()


def cloudflare_test(config):
    if config.get("cloudflare", "") != "":
        if not config.get("cloudflare").startswith("http") and not config.get(
            "cloudflare"
        ).startswith("//"):
            print(
                "\033[31mERROR! YOUR CLOUDFLARE URL IS NOT VALID! THE URL MUST START WITH HTTP:// OR HTTPS://\033[0m"
            )
            sys.exit()
        res = requests.get(config.get("cloudflare")).text
        if not res.startswith("libDrive"):
            print(
                "\033[31mERROR! YOUR CLOUDFLARE DEPLOYMENT IS NOT RETURNING A VALID RESPONSE! MAKE SURE IT IS CORRECTLY CONFIGURED!\033[0m"
            )
            sys.exit()
