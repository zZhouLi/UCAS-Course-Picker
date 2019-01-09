# UCAS Course Picker

> 2019.1.9

## Environment

- UCAS network

- Python3 

- `BeatifulSoup4` ,`requsets`   needed

  You can install them by `pip install BeatifulSoup4 requsets ` 

## Config

```python
username = "your_email@email.com"
password = "your_passeord"
courses = { 
    # "course_code":"dept_id"  
    # like:     "156560": "964"
}
```

## Run

`python ucase_course_picker.py`

## Tips

- How to find `course_code` 

  - Login the http://sep.ucas.cn

  - Click ![](https://ws2.sinaimg.cn/small/006tNc79ly1fz0cu2yg0vj305q058jrq.jpg)

  - Select `school timetable`

    ![](https://ws1.sinaimg.cn/large/006tNc79ly1fz0cv6e83dj32fm0fcwj7.jpg)

  - Click an iterm's `course code`, the you can get the real `course_code`in address

    ![](https://ws2.sinaimg.cn/large/006tNc79ly1fz0cw0g32sj30u401i3yy.jpg)

- How to find `dept_id`

  ![](https://ws1.sinaimg.cn/large/006tNc79ly1fz0d6n18kpj31fl0u04qq.jpg)
