import feedparser

miyeon_blog_rss_url = "https://cocococo331.tistory.com/rss"
rss_feed = feedparser.parse(miyeon_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
  if idx > MAX_POST_NUM:
    break
  feed_date = feed['published_parsed']
  latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br> \n"

  # 요기가 기존 readme 놓는 곳인감.
  markdown_text = """

Yeon Miyeon
--

![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white "Notion Profile 준비중..")
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white "GitHub Blog")](https://miyeon396.github.io)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&text=dd)](mailto:miyeon396@gmail.com)

- Java Back-End Developer 

<br />

> ⚒️ 가능 ⚒️

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)
![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![Switch](https://img.shields.io/badge/Switch-E60012?style=for-the-badge&logo=nintendo-switch&logoColor=white)

<br />

> 🎖 Badges 🎖

<a href="https://www.credly.com/badges/ede3beb6-1382-4174-a474-560e6eb65d29/public_url"><img src="https://images.credly.com/size/680x680/images/4bc21d8b-4afe-4fbd-9a90-a9de8bf7b240/AWS-SolArchitect-Associate-2020.png" width=120px></a>
<a href="https://www.credly.com/badges/5eac4b3c-6279-417b-8783-788398365400/public_url"><img src="https://images.credly.com/size/680x680/images/598f6ac6-2dbd-4394-8ae4-943b2f4c43ea/AWS-Developer-Associate-2020.png" width=120px></a>
<a href="https://www.credly.com/badges/6df2c2d7-ff5d-400d-a9c4-2176fb69333a/public_url"><img src="https://images.credly.com/size/680x680/images/8e968853-15af-4bbc-9d03-cf518971909c/AWS-SolArchitect-Professional-2020.png" width=120px></a>
<a href="https://www.credential.net/d6849be4-ecd6-4cd7-b372-4a1f9e01fc1c"><img src="https://api.accredible.com/v1/frontend/credential_website_embed_image/badge/21209568" width=120px></a>


<!-- 나중에 할거 -->
<!-- [![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=miyeon396)](https://github.com/miyeon396/github-readme-stats)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=miyeon396&layout=compact)](https://github.com/miyeon396)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fhttps%2F%2Fgithub.com%2Fmiyeon396%2F&count_bg=%23FFC6EF&title_bg=%238E8E8E&icon=&icon_color=%23FFB0F0&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
-->

> ✏️ Langs ✏️
> 
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=miyeon396)](https://github.com/miyeon396/github-readme-stats)

<!-- ![footer](https://capsule-render.vercel.app/api?section=footer&color=auto&type=waving) -->

<!--
**miyeon396/miyeon396** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
  
  
  """

  readme_text = f"{markdown_text}{latest_blog_post_list}"

  with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
