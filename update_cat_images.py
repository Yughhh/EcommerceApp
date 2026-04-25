import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category

mapping = {
    'books': 'categories/books.png',
    'clothing': 'categories/clothing.png',
    'electronics': 'categories/electronics.png',
    'home': 'categories/home.png',
    'sports': 'categories/sports.png',
}

for cat in Category.objects.all():
    name_lower = cat.name.lower()
    for key, image_path in mapping.items():
        if key in name_lower:
            cat.image = image_path
            cat.save()
            print(f"Updated {cat.name} with {image_path}")

print("Done updating category images!")
