## Objectives: 
1. model real relationships (users / posts / comments / tags)
2. use the ORM for the queries
3. wire up the admin.

## Model
### Required models & fields
- User: use django default user 
- Post:
  - post_author
  - post_title
  - post_content
  - post_tag
- Comment:
  - post
  - comment_author
  - comment_content
- Tag:
  - tag_content

### Model Relations
- User : Post = 1 : N
- Post : Comment = 1: N
- Post : Tag = N : M
- User : Comment = 1 : N
