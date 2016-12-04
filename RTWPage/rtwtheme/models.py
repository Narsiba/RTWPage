from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to

# Create your models here.
class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    topheading = models.CharField(max_length=200,
        help_text="The top heading of the carousel caption", default="We currently are in:")
    headline = models.CharField(max_length=200,
        help_text="The Headline in the middle of the carousel caption", default="Switzerland")
    subheading = models.CharField(max_length=200,
        help_text="The subheading of the carousel caption", blank=True, null=True)
    buttontext = models.CharField(max_length=200,
        help_text="The text on the button to enter the page", default="Enter")
#    featured_pictures_heading = models.CharField(max_length=200,
#        default="Featured Pictures")
#    featured_portfolio = models.ForeignKey("Portfolio", blank=True, null=True,
#        help_text="If selected items from this portfolio will be featured "
#                  "on the home page.")
#    latest_posts_heading = models.CharField(max_length=200,
#        default="Latest Posts")
#    content_heading = models.CharField(max_length=200,
#        default="About us!")


    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(max_length=50, default="Slide")


#class IconBlurb(Orderable):
#    '''
#    An icon box on a HomePage
#    '''
#    homepage = models.ForeignKey(HomePage, related_name="blurbs")
#    icon = FileField(verbose_name=_("Image"),
#        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
#        format="Image", max_length=255)
#    title = models.CharField(max_length=200)
#    content = models.TextField()
#    link = models.CharField(max_length=2000, blank=True,
#        help_text="Optional, if provided clicking the blurb will go here.")


class Portfolio(Page):
    '''
    A collection of individual portfolio items
    '''
    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")
