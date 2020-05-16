"""Model for the the 'feed' app.

The module models.py contains the essesntial field and
behaviour of data stored for the app named feed.

"""

from datetime import date
from django.db import models
from django.conf import settings
from django.utils import timezone
from autoslug import AutoSlugField

class Post(models.Model):
    """Class for Post object for the blog."""

    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="title")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    published_date_mdy = models.DateField(default=date.today)

    def __str__(self):
        """String representation of a Post object."""
        return self.title

class Course(models.Model):
    """Class for Course object for the blog."""

    class Semester(models.TextChoices):
        """Class for Semester Choices."""
        FIRST = "first", "First"
        SECOND = "second", "Second"
        THIRD = "third", "Third"
        FOURTH = "fourth", "Fourth"
        FIFTH = "fifth", "Fifth"
        SIXTH = "sixth", "Sixth"
        SEVENTH = "seventh", "Seventh"
        EIGHTH = "eighth", "Eighth"
        ELECTIVE = "elective", "Elective"

    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=150)
    semester = models.CharField("Semester", max_length=20,
                                choices=Semester.choices, default=Semester.ELECTIVE)

    def __str__(self):
        return self.code + "-" + self.name

class CourseReviewData(models.Model):
    """Class for Course Review Data object."""

    class Difficulty(models.TextChoices):
        """Class for course difficulty choices."""
        VERY_EASY = "very-easy", "Very-Easy"
        EASY = "easy", "Easy"
        MODERATE = "moderate", "Moderate"
        DIFFICULT = "difficult", "Difficult"
        VERY_DIFFICULT = "very-difficult", "Very-Difficult"

    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    submitter = models.CharField(max_length=150, blank=True, null=True)
    submitter_email = models.EmailField()
    course_instructor = models.CharField(max_length=150)
    session = models.CharField(max_length=20)
    grade_awarded = models.CharField(max_length=2)
    course_difficulty = models.CharField(
        "Difficulty", max_length=20, choices=Difficulty.choices, default=Difficulty.MODERATE)
    pre_requisites = models.CharField(max_length=300)
    assesments_methods = models.TextField()
    topics_covered = models.TextField()
    weightage = models.TextField()
    lecture_lab_review = models.TextField()
    exam_review = models.TextField()
    performance_tips = models.TextField()
    references = models.TextField()
    slug = AutoSlugField(unique=True, always_update=False, populate_from="course")
    attendance_policy = models.CharField(
        max_length=150, default="80% attendace is required officially")

    def __str__(self):
        return self.course.code + "-" + self.submitter
              