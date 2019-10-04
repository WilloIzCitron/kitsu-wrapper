from datetime import datetime


class Category:
    def __init__(self, type_, data):
        attributes = data['attributes']

        self.id = data['id']
        self.type = type_
        self.title = attributes['title']
        self.description = attributes['description']
        self.slug = attributes['slug']
        self.nsfw = attributes['nsfw']
        self.media_count = attributes['totalMediaCount']
        self.child_count = attributes['childCount']
        self.image_url = attributes['image']['original'] \
            if attributes['image'] else None

    @property
    def url(self):
        return f'https://kitsu.io/explore/{self.type}/category/{self.slug}'

    def __str__(self):
        return self.title


class MediaEntry:
    def __init__(self, id_, type_, attributes):
        self.id = id_
        self.type = type_
        self.title = attributes['canonicalTitle']
        self.synopsis = attributes['synopsis']
        self.subtype = attributes['subtype']
        self.status = attributes['status']
        self.slug = attributes['slug']
        self.rating = attributes['averageRating']
        self.user_count = attributes['userCount']
        self.favorites_count = attributes['favoritesCount']
        self.popularity_rank = attributes['popularityRank']
        self.rating_rank = attributes['ratingRank']
        self.age_rating = attributes['ageRating']
        self.age_rating_guide = attributes['ageRatingGuide']
        self.poster_image_url = attributes['posterImage']['original'] \
            if attributes['posterImage'] else None
        self.cover_image_url = attributes['coverImage']['original'] \
            if attributes['coverImage'] else None
        self.started_at = datetime.strptime(attributes['startDate'], '%Y-%m-%d') \
            if attributes['startDate'] else None
        self.ended_at = datetime.strptime(attributes['endDate'], '%Y-%m-%d') \
            if attributes['endDate'] else None
        self.next_release = datetime.strptime(attributes['nextRelease'], '%Y-%m-%dT%H:%M:%S.%f+09:00') \
            if attributes['nextRelease'] else None

    @property
    def url(self):
        return f'https://kitsu.io/{self.type}/{self.slug}'

    def __str__(self):
        return self.title


class Anime(MediaEntry):
    def __init__(self, type_, data):
        attributes = data['attributes']

        super().__init__(data['id'], type_, attributes)

        self.episode_count = attributes['episodeCount']
        self.episode_length = attributes['episodeLength']
        self.total_length = attributes['totalLength']
        self.youtube_video_id = attributes['youtubeVideoId']
        self.nsfw = attributes['nsfw']


class Manga(MediaEntry):
    def __init__(self, type_, data):
        attributes = data['attributes']

        super().__init__(data['id'], type_, attributes)

        self.chapter_count = attributes['chapterCount']
        self.volume_count = attributes['volumeCount']
        self.serialization = attributes['serialization']
