""" 
Day 23 - PyBlog CLI
Getting Started:
- Start MySQL
- Make a new database (pyblog_db)
- Run "setup_db.py"
- Check if it works by running "python main.py create-post" 
"""

from models import BlogPost, SessionLocal
import click


@click.group
def cli():
    """PyBlog CLI"""
    pass


@cli.command()
@click.option("--title", prompt="Title", help="Title of the blog post")
@click.option("--content", prompt="Content", help="Content of the blog post")
@click.option("--category", prompt="Category", help="Category of the blog post")
def create_post(title, content, category):
    session = SessionLocal()
    new_post = BlogPost(title=title, content=content, category=category)
    session.add(new_post)
    session.commit()
    session.close()
    click.echo(f"Post '{title}' has been created!")


@cli.command()
def list_posts():
    session = SessionLocal()
    posts = session.query(BlogPost).all()
    for post in posts:
        click.echo(f"{post.id}: {post.title} (Category: {post.category})")
    session.close()


@cli.command()
@click.argument("post_id")
def list_post_byId(post_id):
    session = SessionLocal()
    post = session.query(BlogPost).filter(BlogPost.id == post_id).first()
    click.echo(
        f"{post.id}: {post.title} (Category: {post.category})\nContent: {post.content}"
    )
    session.close()


@cli.command()
@click.argument("post_id")
@click.option("--title", prompt="Title", help="New title of the blog post")
@click.option("--content", prompt="Content", help="New content of the blog post")
@click.option("--category", prompt="Category", help="New category of the blog post")
def update_post(post_id, title, content, category):
    session = SessionLocal()
    post = session.query(BlogPost).filter(BlogPost.id == post_id).first()
    if post:
        post.title = title
        post.content = content
        post.category = category
        session.commit()
        click.echo(f"Post '{post.title} has been updated!'")
    else:
        click.echo("Post not found!")
    session.close()


@cli.command()
@click.argument("post_id")
def delete_post(post_id):
    session = SessionLocal()
    post = session.query(BlogPost).filter(BlogPost.id == post_id).first()
    if post:
        session.delete(post)
        session.commit()
        click.echo(f"Post '{post.title} has been deleted!'")
    else:
        click.echo("Post not found!")
    session.close()


if __name__ == "__main__":
    cli()
