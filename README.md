# Distributed Behavioral Model for Bird-oid Objects

This project is motivated by a paper that I have recently by [Craig Reynolds](http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87/) titled: "Flocks, Herds, and Schools: A Distributed Behavioral Model". I also watched a very cool video by [Sebastian Lague](https://youtu.be/bqtqltqcQhw) that had some amazing graphics. I wanted to get into visualizing algorithms and using a computational biology example was a cool one.

## Packages
* p5 (Python version)

## Installation

```
pip install virtualenv

virtualenv boid

boid\Scripts\activate

pip install -r requirements.txt
```

One very common error that might occue when trying to run this code is getting a runtime error for GLFW. Simply go to the [glfw docs](https://www.glfw.org/download) and downlaod the precompiled binaries for the library. Next, extract them to your hard drive (preferably C:/* and not C:/ProgramFiles so you can avoid premission conflicts). Lastly, add that to your path variable environment, this should fix the error.

Link to StackOverflow issue is [here](https://github.com/p5py/p5/issues/76)

If you don't know how to add somwthing to your path variables please follow the below:

##### Windows
From the Start search bar, enter ‘env’ and select Edit environment variables for your account.
Under User variables check if there is an entry called Path:
If the entry exists, append the full path to `C:\glfw-3.2.1.bin.WIN64\lib-mingw-w64` using ; as a separator from existing values.

If the entry doesn’t exist, create a new user variable named Path with the full path to flutter\bin as its value.

Note that you have to close and reopen any existing console windows for these changes to take effect.


##### macOS/Linux
```
export PATH=/glfw-3.2.1.bin.WIN64/lib-mingw-w64:$PATH
```
Note that if you wish to set the PATH for all users, you need to log in as root in the bash shell
## Results
In progress.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
