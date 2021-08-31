from user.models import Profile
from django.db import models

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id)


class Resume(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume = models.ImageField(
        upload_to=f'uploads/{user_directory_path}', null=True)

    def __str__(self) -> str:
        return f"resume of {self.profile.user.id}"


class Links(models.Model):
    resume = models.ForeignKey(Resume,  on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    github = models.TextField(verbose_name="GitHub URL", null=True, blank=True)
    gitlab = models.TextField(verbose_name="GitLab URL", null=True, blank=True)
    linkedIn = models.TextField(
        verbose_name="linkedIn URL", null=True, blank=True)
    portfolio = models.TextField(
        verbose_name="Portfolio Link", null=True, blank=True)
    other = models.TextField(verbose_name="Other URLs", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.resume} links"


class Educations(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    start_date_year = models.IntegerField()
    end_date_year = models.IntegerField()
    uni_name = models.TextField(verbose_name="Name of Institute", null=False)
    course = models.TextField(
        verbose_name="Course Name",
        null=False
    )
    percentage = models.TextField(verbose_name="Percent or CGPA", null=False)


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill = models.TextField(verbose_name="Skill name")


class Certificates(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    name = models.TextField(verbose_name="Certificate name")
    date = models.DateField(verbose_name="Date of Issue", null=True)
    certificate = models.ImageField(
        upload_to=f'uploads/{user_directory_path}/certificates')


class Work(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    company = models.TextField(verbose_name="Company Name", max_length=100)
    title = models.TextField(
        verbose_name="Title and Designation", max_length=100)
    desc1 = models.TextField(verbose_name="Work description 1", max_length=100)
    desc2 = models.TextField(verbose_name="Work description 2", max_length=100)
    start_date_year = models.TextField(verbose_name="Start date year")
    present_date_year = models.TextField(
        verbose_name="present date year", null=True)
    start_date_month = models.TextField(verbose_name="Start date month")
    present_date_month = models.TextField(
        verbose_name="present date month", null=True)


class Hobbies(models.Model):

    HOBBIES_CHOICES = [
        ('SI', 'Singing'),
        ('DA', 'Dancing'),
        ('PL', 'Playing'),
        ('SK', 'Sketching'),
        ('TR', 'Travelling'),
        ('RE', 'Reading'),
    ]
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    hobbies = models.CharField(
        max_length=2,
        choices=HOBBIES_CHOICES,
        default=None
    )
