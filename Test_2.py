from pprint import pprint
import requests as rq

# https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&sort_by=popularity.desc&page={!!!!}
# https://api.themoviedb.org/3/genre/movie/list?language=en

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMTI3NGFmYTRlNTUyMjRjYzRlN2Q0NmNlMTNkOTZjOSIsInN1YiI6IjVkNmZhMWZmNzdjMDFmMDAxMDU5NzQ4OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lbpgyXlOXwrbY0mUmP-zQpNAMCw_h-oaudAJB6Cn5c8"
}


class Film:
    def __init__(self, page):
        self.page = page
        self.date = []
        self.genre = []
        self.popular = []

    def get_page(self):
        for i in range(1, self.page):
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&sort_by=popularity.desc&page={i}"
            self.date.extend(rq.get(url, headers=headers).json()["results"])

    def get_all_info(self):
        return self.date

    def get_page_with_steps(self):
        return self.date[3:19:4]

    def most_popular_film(self):
        return max(self.date, key=lambda r: r['popularity'])['title']

    def get_info_with_key(self, keywords):
        for move in self.date:
            if any(keyword in move['overview'] for keyword in keywords):
                return move['title']

    def get_genre(self):
        for i in self.date:
            self.genre.extend(i['genre_ids'])
            fset = frozenset(self.genre)
        return fset

    def delete_genre(self, genre):
        for i in self.date:
            if i['genre_ids'] in genre:
                self.date.remove(i)

    def name_most_popular_genre(self):
        count = []
        for i in self.date:
            for j in i['genre_ids']:
                count[j] += 1


x = Film(5)
pprint(x.get_page())
pprint(x.get_all_info())
pprint(x.get_page_with_steps())
pprint(x.most_popular_film())
pprint(x.get_info_with_key('emerges'))
pprint(x.get_genre())
pprint(x.delete_genre([18]))
pprint(x.name_most_popular_genre())
