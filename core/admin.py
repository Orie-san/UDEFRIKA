from django.contrib import admin
from core.models import CartOrderProducts, Product, Category, Vendor, CartOrder, ProductReview, wishlist_model, Address


class ProductAdmin(admin.ModelAdmin):
    list_editable = ['title', 'price', 'featured', 'product_status']
    list_display = ['user', 'title', 'image', 'price', 'category', 'vendor', 'featured', 'product_status', 'pid', 'language']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'product_status', 'sku']
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status', 'sku']


class CartOrderProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address', 'status']
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderProducts, CartOrderProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist_model, wishlistAdmin)
admin.site.register(Address, AddressAdmin)
