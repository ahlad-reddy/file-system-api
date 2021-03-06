# file-system-api

A simple application that exposes a REST API to browse information from a specified portion of the user's file system. 

## Installation

Docker is required to run this application. Make sure you've [downloaded the latest version](https://www.docker.com/get-started). 

To get started, simply clone the repo:
```bash
git clone https://github.com/ahlad-reddy/file-system-api.git
cd file-system-api
```

## Usage
### Running the Application

To run the application, run the following script, specifying the root directory to browse:
```bash
./run_app.sh /somepath/to/foo
```
This command starts a docker container in detatched mode with the API available at `0.0.0.0:5000` or `localhost:5000`. Calling the API returns information on the file system in JSON format. 

For example, consider the directory used above `/somepath/to/foo` has the following contents:
```bash
foo
├── bar
│   ├── baz
│   │   └── baz1
│   └── baz1   
├── foo1
└── foo2
```

Calling the API from the root directory will show the contents of `foo` along with information on each file (name, owner, permissions):
```bash
curl localhost:5000/

# {"directories":["bar"],"files":[{"name":"foo1","owner":"root","permissions":"644","size":23},{"name":"foo2","owner":"root","permissions":"644","size":23}]}
```

Calling the API on a directory will similarly return the contents of the directory:
```bash
curl localhost:5000/bar

# {"directories":["baz"],"files":[{"name":"bar1","owner":"root","permissions":"644","size":23}]}
```

Calling a file will return the contents of the file:
```bash
curl localhost:5000/bar/bar1

# {"content":"This file is named bar1"}
```

Calling a file or folder that doesn't exist will return an error:
```bash
curl localhost:5000/bar/bar1/bazfoo

# {"error":"path does not exist"}
```

To close the application, run `docker-compose down` or `docker-compose stop`.

### Testing

To test the application, run `./test_app.sh`. The script will print out a report measuring code coverage. 


