"""Model for the the 'feed' app.

The module models.py contains the essesntial field and
behaviour of data stored for the app named feed.

"""

from datetime import date
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    """Class for Post object for the blog."""

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    published_date_mdy = models.DateField(default=date.today)

    def __str__(self):
        """String representation of a Post object."""
        return self.title

class Course(models.Model):
    """Class for Course object for the blog."""

    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5
    SIXTH = 6
    SEVENTH = 7
    EIGHTH = 8
    ELECTIVE = 0

    SEMESTER = (
        (FIRST, 'First Semester'),
        (SECOND, 'Second Semester'),
        (THIRD, 'Third Semester'),
        (FOURTH, 'Fourth Semester'),
        (FIFTH, 'Fifth Semester'),
        (SIXTH, 'Sixth Semester'),
        (SEVENTH, 'Seventh Semester'),
        (EIGHTH, 'Eighth Semester'),
        (ELECTIVE, 'Department Electives'),
    )

    code = models.CharField(max_length=6)
    name = models.CharField(max_length=150)
    semester = models.IntegerField(choices=SEMESTER)
    session = models.CharField(max_length=20)

    def __str__(self):
        return self.code +": " +self.name

class CourseReviewData(models.Model):
    """Class for Course Review Data object."""

    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    submitter = models.CharField(max_length=150, blank=True, null=True)
    submitter_email = models.EmailField()
    course_instructor = models.CharField(max_length=150)
    grade_awarded = models.CharField(max_length=2)
    course_difficulty = models.CharField(max_length=20)
    pre_requisites = models.CharField(max_length=150)
    assesments_methods = models.TextField()
    topics_covered = models.TextField()
    weightage = models.TextField()
    lecture_lab_review = models.TextField()
    exam_review = models.TextField()
    performance_tips = models.TextField()
    references = models.TextField()

    def __str__(self):
        return self.course.code + "-" + self.submitter
        