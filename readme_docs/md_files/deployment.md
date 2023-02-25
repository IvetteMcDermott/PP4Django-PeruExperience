Deployment proccess:

1. Log in [Github](https://github.com/).
    - Open the repo to deploy. The one for the site is [here](https://github.com/IvetteMcDermott/PP4Django-PeruExperience).
2. Log in [Heroku](https://id.heroku.com/login).
    - Click in the "New" button in the top right.
    - Select "Create New App"
    - Give a name to the App and choose a region.
    - Click in "Create App" button.
    - Click in Settings.
    - Click in Reveal Config.
    - Add Vars Config (keys):
        - Cloudinary (Media Storage)
        - DataBase Elephant (DataBase Host)
        - PORT 8000
        - Django (Framework)
    - Go to Deploy in the nav bar. In Deploment Method, select GitHub/Connect to GitHub.
    - In Connect to GitHub, write the repository name and click in search.
    - Once the route for the repo appears under the search, click in "Connect" button.
    - The deployment can be Manual or Automatic, select the one of your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
    - Verify that "Branch to deploy" is master/main.
    - Click Deploy.

Steps to use this repository:

- Access to the repo in GitHub [here](https://github.com/IvetteMcDermott/PP4Django-PeruExperience).
- It can be "Fork" following the steps [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo).
- It can be "Clone" following the steps [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).
