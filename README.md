# Authentication methods evaluator
We all know passwords are no longer the best method of authentication. This APP was created as a platform to allow end users to test and evaluate the myriad of different authentication methods available to them, and to see some interesting data in the process. 

This app will include a mishmash of authentication methods, including traditional passwords, with or without multi-factor authentication, password managers, Time Based One Time Passwords, hardware and software authentication, session/web-browser authentication, centralized authentication, and magic link authentication. 

This app allows you create a session-limited "account" to authenticate to and, once authenticated, will return some of the tracked detail of authentication, such as time spent using this authentication method, number of errors made using this method, and a quick view of the architecture of how the method authenticates, for applicable methods it will even return a quick evaluation of the security of the authentication method.

## Installation
```bash
docker compose build
```
<!--- more to be added as it is built out--->

## Getting Started
To run the app, navigate to the root folder in a CLI and run
```bash
docker compose up
```
See in-app instructions for help with using specific features.

# License
MIT License

Copyright (c) 2023 Dan-ee-Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.