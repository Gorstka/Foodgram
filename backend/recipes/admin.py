from django.contrib import admin

from .models import (
    Favorite,
    Ingredient,
    IngredientRecipe,
    Recipe,
    ShopingCart,
    Subscribe,
    Tag,
)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "measurement_unit")
    list_filter = ("name",)


class RecipeIngredientInline(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    fields = (
        "author",
        "name",
        "text",
        "tags",
        "image",
        "cooking_time",
        "favorites_count",
    )
    list_display = (
        "name",
        "author",
    )
    list_filter = ("name", "author", "tags")
    readonly_fields = ("favorites_count",)
    inlines = [RecipeIngredientInline]
    autocomplete_fields = ["author"]
    search_fields = ["favorite__name"]

    def favorites_count(self, obj):
        return Favorite.objects.filter(favorite=obj).count()


class FavoriteAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "favorite"]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(Tag)
admin.site.register(Subscribe)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShopingCart)
