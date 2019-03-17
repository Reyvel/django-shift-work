=====
Usage
=====

To use Django Shift Work in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_shift_work.apps.DjangoShiftWorkConfig',
        ...
    )

Add Django Shift Work's URL patterns:

.. code-block:: python

    from django_shift_work import urls as django_shift_work_urls


    urlpatterns = [
        ...
        url(r'^', include(django_shift_work_urls)),
        ...
    ]
