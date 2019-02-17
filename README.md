# How to test the code

Assuming docker is available for use on the machine, we can use below. 

```bash
git clone <current repo>
docker build --build-arg test_file=<test_file_name> --build-arg work_dir=<name_of_python_project_to_test> -t <docker_image_name> .
docker run <docker_image_name>
```

* we are using Python3 in the image
* docker_image_name: Chose any name
* work_dir: name of python project to test e.g. hello-world
* test_file_name: name of test file name e.g. for hello_world_test.py value will be will `hello_world`