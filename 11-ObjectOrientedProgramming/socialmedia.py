class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        counter = 1
        print(f"{self.username} posts are:")
        for post in self.posts:
            print(f"{counter}. {post}")
            counter += 1

user1 = SocialMediaProfile("johndoe")
post1 = user1.add_post("Hello, world!")
post2 = user1.add_post("Had a great day at the park!")
post3 = user1.add_post("What's up, Natalie? How are you?")

SocialMediaProfile.display_timeline(user1)