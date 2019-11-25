# GIT GUIDE


Command line instructions 


##Git global setup
*git config --global user.name ""
*git config --global user.email ""



##Create a new repository
git clone https://contribute.dub.emea.dell.com/kevin_tang1/TestProject.git
cd TestProject
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master



Existing folder
cd existing_folder
git init
git remote add origin https://contribute.dub.emea.dell.com/kevin_tang1/TestProject.git
git add .
git commit -m "Initial commit"
git push -u origin master



Existing Git repository
cd existing_repo
git remote rename origin old-origin
git remote add origin https://contribute.dub.emea.dell.com/kevin_tang1/TestProject.git
git push -u origin --all
git push -u origin --tags

