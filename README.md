# CodeCraft: The Developer Platform for Sharing Code

CodeCraft is a developer platform that allows users to easily share and collaborate on small code blocks. Upon registering for an account on the platform, users can begin creating and sharing snippets through the use of QR codes or hyperlinks. Each source code is automatically embedded in a QR form, which can be scanned by other users to access the content. Users have the ability to edit their own snippets and view a history of all versions of their code. They can also delete their own snippets if desired. CodeCraft is designed to streamline the process of sharing and collaborating on code snippets with others, making it easier for developers to work together and build great software.

## Design Choices

I tried to make the software design for the application as modular as possible by breaking it up into small, independent parts and using common sense to guide me. This approach made it easier for me to develop and maintain the application, as I could get down to one component at a time.

I decided to utilize the `mongoengine` library in order to easily model the documents for storing code snippets in MongoDB. By using `mongoengine`, I was able to comfortably define the Python classes corresponding to my desired document structure for the users, snippets and source, and the library took care of the rest.

I believe that it will be easy to upgrade the structure if the need arises in the future. In fact, I plan to implement an embedded document for user comments directly on the source code in future versions of the app. This will allow users to discuss and annotate the code, which I think will be a useful feature.

As for the code blocks themselves, I opted to use `highlight.js` on the client side. One of the main reasons I chose `highlight.js` is that it supports a wide range of programming languages. This saved me time because I didn't have to build my own syntax highlighting implementation for all of the different languages that users might want to share code snippets in. 

## Development Setup

- Make sure you have [Python 3.6][1] or later installed on your system.
- Clone the CodeCraft repository:
  - `git clone https://github.com/voizlav/codecraft.git`
  - `cd codecraft`
- Set up a virtual environment for the project. This can be done by running the following commands:
  - `python -m venv venv`
  - `source venv/bin/activate`
- Install the required libraries and dependencies by running the following command:
  - `pip install -r requirements.txt`
- Create a `.env` file in the project directory and set up the necessary environment variables.
  - `DEBUG`
  - `FLASK_DEBUG`
  - `DATABASE_URI`
  - `DATABASE_NAME`
- To use CodeCraft, you will need to have a [MongoDB][2] database set up, either locally or through an [Atlas account][3].
  - e.g. `DATABASE_URI="mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database_name>"`
- To run the [Flask][4] app, you can use the following command in development:
  - `flask run`

[1]: https://www.python.org/downloads/release/python-360/
[2]: https://www.mongodb.com/docs/
[3]: https://www.mongodb.com/cloud/atlas/register
[4]: https://flask.palletsprojects.com/en/2.2.x/
