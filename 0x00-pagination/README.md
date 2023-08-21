## Pagination (0x00-pagination)

### Learning Objectives

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Resources

- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask request](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)

### Tasks

#### 0. Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

- File: `0-simple_helper_function.py`

#### 1. Simple pagination

Copy `index_range` from `0-simple_helper_function.py` into the file `1-simple_pagination.py`.

Implement a method named `get_page` that takes two integer arguments `page` with default value `1` and `page_size` with default value `10`.

- File: `1-simple_pagination.py`

#### 2. Hypermedia pagination

Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:

- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, `None` if no next page
