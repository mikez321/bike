# Notes on Deploying to AWS Elastic Beanstalk
After doing a little learning and experimenting, I was able to deploy the Bike-API to AWS Elastic Beanstalk.  Basically, deploying a Django/Django REST app can be accomplished in under 10 minutes (I actually was able to deploy a blank app that quickly) by following the [docs and developer guide provided by AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html).  So rather than talk about the simple steps found in the guide I'll go over the big hurdles I came across during my deployment and how I solved them.

### TL;DR
I troubleshot my issues by researching problems as they arose and comparing a working and not working deployed app's giant log files.  In the end, a self-caused, single-line problem in `wsgi.py` was one of my biggest hurdles in deploying to AWS.  Other than that, AWS EB is pretty straightforward.

### Hurdle: Wrong Platform
The above mentioned tutorial wants you to `eb init` the environment using a Python 3.6 Platform.  When I originally started the project it wouldn't even start because of version incompatibilities.  I discovered Python 3.7 environments while playing around with the CLI and manually creating new environments on the AWS website.

### Hurdle: Incorrect Importing of Environmental Variables
After solving my env issues I got errors about web services not running.  While experimenting with a working, deployed app, I realized my environment variables were not being brought in properly.  Rather than using python-dotenv's built in methods, I reverted back to `os.environ` since that's how the Python docs said they should be passed in.

### Hurdle: requirements.txt/pipfile.lock
In an effort to use `os.environ`, I had tried using `pipenv` for my virtual environment.  It took a little reading before I learned that using requirements.txt and installing with pip was the preferred way, and I might be causing issues by using pipenv with a Pipfile and pipfile.lock (which were .gitignored... more on that later).

### Hurdle: Long Error Logs
Fortunately/Unfortunately the AWS logs are very long and full logs are made up of multiple files/folders.  I spent a very long time comparing successful build logs with failing ones to track down issues.  Fortunately, once you find what you're looking for (and understand what it means) they can be really descriptive.

### Hurdle: Missed Settings Module
After lots of log looking, I found my error preventing me from deploying.  `No module found: bike.settings`.  Originally, I had named the API app 'bike' but manually renamed everything to 'api' so it would be more descriptive.  While I didn't understand why it wouldn't work (worked fine locally), I figured I broke some kind of default rule thus preventing other servers building the app.  I went through the app and renamed the app 'bike' to 'bicycle' so I could rename 'api' to 'bike' and let it find `bike.settings`.  While doing this, I realized a file I had never touched was `api/wsgi.py`.  Here it was, `bike.settings`.  I renamed that to `api.settings` and was deployed to AWS!

### Hurdle: Migrations
Now my app worked but the new error was `No table bike_bike`.  But `/cupcakes` was a 404 so I knew it was a database issue.  After some looking, I found [this stack overflow thread](https://stackoverflow.com/questions/30950941/running-django-migrations-when-deploying-to-elastic-beanstalk) which helped me find the right code to add to run database migrations in `.ebextensions/django.config`.  Now I just got no info at my bike and wheel endpoints... but 200 responses!

### Hurdle: .gitignore, .ebignore, database
The final hurdle was understanding which files were being sent up to AWS EB.  Since this project uses a simple SQLite database, I simply shipped it up to production (the joys of little projects) and there ya go.  Shipped and ready to work in the real world.
