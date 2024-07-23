def print_show_infor(tv_show):
    print(f"{tv_show['title']} ({tv_show['initial_release']}) - {tv_show['seasons']} seasons")


tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
print_show_infor(tv_show)
