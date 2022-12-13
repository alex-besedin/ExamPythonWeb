from django.contrib import admin

from KetoGo.common.models import ProductComment


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('get_user_name', 'get_product', 'date_and_time_of_publication')
    list_filter = ('to_product__category', 'to_product__name',)
    search_fields = ('comment_text',)
    search_help_text = 'Search comments containing an offensive word...'

    fieldsets = (
        (None, {'fields': ('comment_text',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('comment_text', 'to_user', 'get_product', 'date_and_time_of_publication',),
            },
        ),)

    @admin.display(ordering='to_product__category', description='For Product')
    def get_product(self, obj):
        return obj.to_product.name

    @admin.display(ordering='to_user__date_joined', description='By User')
    def get_user_name(self, obj):
        return obj.to_user.get_full_name()
