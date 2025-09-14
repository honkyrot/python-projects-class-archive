import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# process overall results
response_dict = r.json()
print(f"Completed requests: {not response_dict['incomplete_results']}")

# process repository results
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # turn each repo into a clickable link
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# make visualization
fig = px.bar(x=repo_links, y=stars,
             title="Most-Starred Python Projects on GitHub",
             labels={'x': 'Repository', 'y': 'Stars'},
             hover_name=hover_texts,)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color="Red", marker_opacity=0.6)

fig.show()
