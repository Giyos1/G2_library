from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseQuerySet(models.QuerySet):

    def delete(self):
        self.update(is_deleted=True)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model).filter(is_deleted=False)


class DeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = DeletedManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Author(BaseModel, DeleteModel):
    name = models.CharField(max_length=250)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ('-birth_date',)
        verbose_name = _('author')
        verbose_name_plural = _('authors')


class Status(models.TextChoices):
    ACTIVE = 'active', 'Active'
    DRAFT = 'draft', 'Draft'


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Status.ACTIVE)


class Book(BaseModel, DeleteModel):
    name = models.CharField(_('name'), max_length=50)
    descriptions = models.TextField(_('descriptions'), null=True, blank=True)
    author = models.ForeignKey(Author, verbose_name=_('author'), on_delete=models.PROTECT, related_name='book_author',
                               null=True, blank=True)
    price = models.IntegerField(_('price'), default=12000)
    status = models.CharField(_('status'), max_length=10, choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(_('image'), upload_to='books/', null=True)
    source = models.FileField(_('source'), upload_to='books', null=True, blank=True)

    # active = BookManager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-id',)
