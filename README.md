<div id="top"></div>

<h3 align="center">Data-Process-API</h3>

  <p align="center">
    API built with FastAPI and Dask which is responsible for scheduling uploaded csv files to process.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation-with-virtualenv">Installation with virtualenv</a></li>
        <li><a href="#installation-with-docker">Installation with docker</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The idea of this project was to create an API that process csv files in background and allow the client to get the processed file in the future.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Starlette](https://www.starlette.io/)
* [Dask](https://www.dask.org/)
* [Docker](https://docker.com/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Git
   ```sh
   https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
   ```

Clone the repository
   ```sh
   git clone https://github.com/mathelima/data-process-api.git
   ```

There is two ways to run the project. Using a Python virtualenv or a Docker container. When working with large files, it's recomended using the virtualenv.


Python
  ```sh
  https://www.python.org/downloads/
  ```

Docker
  ```sh
  https://www.docker.com/get-started
  ```

### Installation with virtualenv

1. Create the virtualenv
   ```sh
   python -m venv ./venv
   ```
2. Activate the venv

   ![image](https://user-images.githubusercontent.com/32756259/193638111-f6f1f3ec-4cb0-4c4b-8eeb-13e7e4a55cf4.png)

3. Install the project requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Run the project
   ```sh
   uvicorn main:app
   ```
   
### Installation with Docker

1. Build the API docker image

   ```sh
   docker build -t data-process-api .
   ```
2. Create a container using the image created

   ```sh
   docker run -d --name data-process-api -p 8000:8000 data-process-api
   ```
3. To see the logs of the application

   ```sh
   docker logs --follow data-process-api
   ```
4. Stop the container when finished

   ```sh
   docker stop data-process-api
   ```

 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

After using one of the methods of installation mentioned above, the API should be running on http://localhost:8000 and it's possible to realize some requests.

To upload a file to be processed by the API, use the method POST on http://localhost:8000/plays/ with the file attached as form-data on the body.

![image](https://user-images.githubusercontent.com/32756259/193642927-6359f8d2-b0c2-45bf-8ee7-867f2ca9e87a.png)

The file data.csv is an exemple of input.

![image](https://user-images.githubusercontent.com/32756259/193712599-9fb6b907-6f6f-40c0-8391-7b6121d6fb17.png)

The response should be the task_id of the process.

![image](https://user-images.githubusercontent.com/32756259/193643077-31d59076-d921-4335-95bb-65ffcdfddd61.png)



To get the processed file, use the method GET on http://localhost:8000/plays/{id} where id is the task_id returned on the last method.

![image](https://user-images.githubusercontent.com/32756259/193643220-39342eb3-e4bf-464e-98a7-290750139d6d.png)

The response should be the csv file processed.

![image](https://user-images.githubusercontent.com/32756259/193643363-7f0bac59-0cad-49cb-857d-31768eacb8f8.png)

To download the file, you should use the option Send and Download.

![image](https://user-images.githubusercontent.com/32756259/193643717-c2417ca6-2c00-4fb3-87ad-d365d66b5569.png)

In case of large files, the file downloaded will not be an .csv, but is possible to just change the extension to .csv.



_For more information, please look at the [Swagger](http://localhost:8000/docs)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- TESTING -->
## Testing

Run the tests using pytest:

   ```sh
   pytest
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Matheus Lima - [Linkedin](https://www.linkedin.com/in/matheus-lima-andrade/) - math.lima.andrade@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>
