## Code collaboration rules

The code will be hosted on github. The workflow contain artifacts as issues, pull request branch, label, milestones etc.

#### FriendsWave


### Available branch by default

* ```nightly``` : where all the coding work is done (never commit directly here)
* ```staging``` : Where all the testing (staging) code is deployed
* ```main```  : Working code, this branch is in sync with the live code (never commit directly here, should never fail)

#### Workflow:

Every features of the project is defined as a issue in the issue board and is labeled as "feature", they are also assign
to one or more peoples in the project. Here is the steps on pull and work on a feature

- Pull code from ``nightly``` branch
- create a branch for that feature named following the format : ```module/[INTENTION]/[FEATURE_NAME]``` and work on that branch for that
feature only.
- push that branch on github and set it as upstream like : ```git push -u [remote_address] BRANCH_NAME```
- create a pull request by referencing the original issue (#1234)
- When everything is ok just init a pull request (PR) and it will be merged to dev branch by the repo maintainer
- after the merge just close the issue

#### Commit style:

A commit should be structured as following:
```text
Title

Description goes here

```

Example: login feature
```text
Login user with email and password

A visitor can login in to the system by providing his email and password... etc
```
