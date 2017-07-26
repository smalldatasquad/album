# osf-example

Example of how to use the osf python library

# setup

```
pip install --upgrade pip
pip install -r requirements.txt
```


# run locally

Configure variables in run.py, and then run:
```
python run.py
```

# run in the cloud

In curl_example, edit scrape_friends.json and scrape_posts.json to include the email to send result to (send_to)
and the parameters you want to scrape with.

Then use curl_posts.sh and curl_friend.sh to make curl requests which initiate scraping in the cloud,
and then email the results to you when finished.
```
cd curl_example
# edit scrape_friends.json
./curl_friends.sh

# edit scrape_posts.json
./curl_posts.sh 
```

You may find that your first cloud run throws an error. If this happens, if you log into your facebook
through your normal browser you may see a prompt from Facebook asking if a recent login from Virgina
was really you (this was the scraper accessing Facebook on your behalf). 

If you approve that this was intended and then try running the curl command again it should work this time.
