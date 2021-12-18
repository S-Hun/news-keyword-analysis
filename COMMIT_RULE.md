# :page_with_curl:

**[kor] [LINK](https://junhyunny.github.io/information/github/git-commit-message-rule/)**

# 1. Purpose

- Communicate with team members well.
- Trace **commit** easily.
- Work along the created issues.



# 2. Commit message rule

Example)

```json
Type: Subject
Body
Footer
```

## 2.1 Type

* Feat - If there is new feature.
* Fix - If there is bug fix.
* Build - If there is edit for **build**.
* Docs - If there are documents.
* Refactor - If there is code refactoring.
* Test - If there is test work.

## 2.1 Subject

* Subject must be less than 50 character.
* Subject dosen't have period(.) mark
* Subject must be written in imperative not pastance.
* First character of subject must be uppercase.

* If there is issue associated with commit, subject must have that issue number.

`Example) Feat: Add Networking management system

## 2.3 Body

* No longer than 72 characters.
* Write about “what” and “why” rather than “how”. 
* Reason of commit

`Example) - Network.data: Information of network for access`

## 2.4 Footer

* Issue tracker ID
* resolve - content of commit is made to resolve issue
* associate - content of commit is associated with issue
* reference - content of commit is an issue number worth referring to

`Example) resolve: #11`



# 3. Commit message function

- close
- closes
- closed
- fix
- fixes
- fixed
- resolve
- resolves
- resolved
