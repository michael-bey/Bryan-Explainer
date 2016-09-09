# Slackpedia

Quick way to search for wikipedia's definition, now in slack! This buddy will tell you everything you want to know (as long as he can find it on wikipedia).


![](http://i.imgur.com/ozDu2je.gif)


## Usage

From any Slack channel, just type `/explaintobryan [search term]`. This will show the definition to the entire channel and tag the user of your choice (Bryan). Make sure you use the actual Slack ID instead of their username.

## Integrate with your team

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/explaintobryan`
  - URL: `https://yourdomain.herokuapp.com/slackpedia`
  - Method: `POST`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Quick way to search for wikipedia's definition.`
    - Usage hint: `[search term]`
  - Descriptive Label: `Search Wikipedia`

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Contributing

- Please use the [issue tracker](https://github.com/benichmt1/Bryan-Explainer/issues) to report any bugs or file feature requests.
