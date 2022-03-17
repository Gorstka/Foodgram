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
    search_fields = ["name", "measurement_unit"]


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
    search_fields = ["name", "ingredients", "pub_date", "text", "tags"]

    def favorites_count(self, obj):
        return Favorite.objects.filter(favorite=obj).count()


class FavoriteAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "favorite"]


class IngredientRecipeAdmin(admin.ModelAdmin):
    autocomplete_fields = ["ingredient", "recipe"]


class SubscribeAdmin(admin.ModelAdmin):
    autocomplete_fields = ["following", "follower"]


class ShopingCartAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer", "cart"]


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe, IngredientRecipeAdmin)
admin.site.register(Tag)
admin.site.register(Subscribe, SubscribeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShopingCart, ShopingCartAdmin)
