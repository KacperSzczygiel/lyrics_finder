from find_path import Path

client_id = "zcBdtGYUjGLXuoUtcr0Gfe3WyTl9lOjoYsZHqLu9uGylOHnDuo2dvfUa7mfZp0fb"
client_secret = "vXro5SAhey2kD85II9KxUVsBaaabXz2cv8hJEHPg_uwJqzy6DGcGC_2SbiF576V9VfK86HAt3lPJMKJGZyni6Q"
access_token = "n7662RkbzNvb5TD8g3hwohLEW264nnYvr9J65iianH46QjPXFbOCezLBYW3mVegI"

song = Path(client_id, client_secret, access_token)
song.search_song()