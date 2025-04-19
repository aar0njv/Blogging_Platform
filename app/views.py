from app import models

def create_post(username):
    title = input("Enter the post title: ")
    content = input("Enter the post content: \n")
    post = {'title': title, 'content': content}

    if username not in models.posts_dict:
        models.posts_dict[username] = []

    models.posts_dict[username].append(post)
    print("Post created successfully. \n")


def view_posts(username):
    posts = models.posts_dict.get(username, {})
    if not posts:
        print(" No posts to show. \n")
        return

    print(" Blog Posts by {} : \n".format(username))
    for i, post in enumerate(posts):
        print("{}. {}\n   {}\n".format(i+1,post['title'],post['content']))



def edit_post(username):
    posts = models.posts_dict.get(username, [])

    if not posts:
        print("No post available to edit.\n")
        return
    
    view_posts(username)
    try:
        index = int(input("Enter the post number to edit : ")) -1
        if 0 <= index < len(posts):
            new_title = input(" Enter new title: ")
            new_content = input(" Enter the content: \n")
            posts[index] = {'title': new_title , 'content': new_content}
            print("Post updated successfully. \n")

        else:
            print(" Invalid post number. \n")
    except ValueError:
        print(" Please enter a valid post number. \n")



def delete_post(username):
    posts = models.posts_dict.get(username, [])
    if not posts:
        print(" No posts available to delete.\n")
        return

    view_posts(username)
    try:
        index = int(input("Enter post number to delete: ")) - 1
        if 0 <= index < len(posts):
            deleted = posts.pop(index)
            print(f" Deleted post: {deleted['title']}\n")
        else:
            print(" Invalid post number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")
