## API Usage + Web Scraping Workshop
#### (Vancouver, Feb 8, 2019)

This is a simple program that gets room rentals from Craigslist then posts them onto a Slack channel.
The goal of this workshop is not only for you to understand how the code here works, but also for you to
be able to add more functionality or features.

### Prerequisites
- A basic understanding of HTTP requests (GET and POST)
- A basic understanding of HTML (the tags: div, h1, p, etc.)
- Knowing a few things about the *Requests* and *BeautifulSoup* libraries would be good 


### To get started:
#### Set up the development/coding environment
1. Go to codenvy.com and create an account (you can use your own IDE, but for the sake of having the same
environments in the workshop, we will use this cloud-based IDE).
2. Sign up for an account.
3. Create a workspace and choose Python as the technology stack. You can create a team if you want.
4. That's it. You may have to verify you account, so be prepared to check for an email.

#### Installing required packages
1. In the terminal, type:
```
pip install python-craigslist
pip install slackclient
```
2. These two are required to make the code run.

#### Set up your Slack account
1. Create a new Slack app here: <https://api.slack.com/apps>. You may have to sign up and verify your email.
2. This is required so the Python program in your computer or Codenvy can have the ability to "speak" to Slack. 
In other words, Slack will be able to trust and receive data from the Python program.
3. Find the OAuth section. Get the OAuth access token.
3. Remember the OAuth. Now head to Slack itself then create a channel. Name it whatever you want.
4. When you select the channel you created, look at the URL. Get the thing that looks like **CE16CKMC4**.
5. Remember that. That is the channel address. You will use the OAuth and the channel address in the next section.

#### Create a **credentials.json** file
1. In your project directory, create a credentials.json file that looks like this:
```
{
  "SLACK_API_KEY": "xoxp-123456789123-987654321654-741852963741-828ae87c2ccad196807c70cbbed78780",
  "SLACK_DESTINATION": "CKAAW0AOP"
}
```
You need to use your own Slack API key (OAuth) and Slack destination (from the channel you created)

#### Running the code
1. You can just copy and paste the code from main.py in a Python file in your project directory.
2. Alternatively, you can clone the repository to Codenvy or your computer. But only do this if you know how to do it or want to 
get your hands dirty with git.
3. After you do the above, your project directory should look like this:
```
the_project_directory
├── credentials.json        # Your Slack API access key and Slack channel destination.
├── main.py                 # Work on this. Make it better, cooler, and more useful.
```

#### Afterword
This is meant for educational purposes only. Our primary goal is to make more people become better at problem solving by 
designing their own computer programs. The workshop focuses on that problem solving and design process rather than learning about
Python syntax/code.

Thanks. - AK
