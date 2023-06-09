from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from filebrowser.base import FileObject

from .models import (EventRegistrations, Events, EventTypes, EventVenues,
                     PaidEventRegistrations, PaidEvents,
                     PrivateEventRegistrations, PrivateEvents)


class EventRegistrationsInline(admin.TabularInline):
    model = EventRegistrations
    extra = 1


class PrivateEventRegistrationsInline(EventRegistrationsInline):
    model = PrivateEventRegistrations


class PaidEventRegistrationsInline(EventRegistrationsInline):
    model = PaidEventRegistrations


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("name", "image_tag", "visitors_list_len", "max_visitors",
                    "updated", "created")
    list_filter = ("updated", "created", "visitors")
    search_fields = ("name", )
    list_editable = ("max_visitors", )
    filter_horizontal = ("visitors",)
    inlines = (EventRegistrationsInline,)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        form.base_fields["full_information"].help_text = "(Имеется поддержка вставки HTML кода)"
        return form

    @admin.display(description="Кол-во зарегестрированных посетителей")
    def visitors_list_len(self, obj):
        return obj.visitors_len()

    @admin.display(description="Изображение для мероприятия")
    def image_tag(self, obj):
        if obj.image and obj.image != '#' or '':
            obj = FileObject(f"{settings.BASE_DIR}{obj.image.url}")
            return format_html(
                f'<img src="{obj.version_generate("admin_thumbnail").url}"/>')
        else:
            return format_html(f'<img src="#"/>')


@admin.register(PrivateEvents)
class PrivateEventsAdmin(EventsAdmin):
    inlines = (PrivateEventRegistrationsInline,)


@admin.register(PaidEvents)
class PaidEventsAdmin(EventsAdmin):
    inlines = (PaidEventRegistrationsInline,)


@admin.register(EventVenues)
class EventVenuesAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "latitude", "longitude", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("name", "address")


@admin.register(EventTypes)
class EventTypesAdmin(admin.ModelAdmin):
    list_display = ("name", "updated", "created")
    list_filter = ("updated", "created")
    search_fields = ("name", )

admin.site.register((EventRegistrations, PrivateEventRegistrations, PaidEventRegistrations))