import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Product

mapping = {
    1: r"C:\Users\yughr\.gemini\antigravity\brain\fa15ef69-38fc-46eb-b605-09e40b401d47\headphones_1776366307173.png",
    2: r"C:\Users\yughr\.gemini\antigravity\brain\fa15ef69-38fc-46eb-b605-09e40b401d47\smart_watch_1776366324735.png",
    3: r"C:\Users\yughr\.gemini\antigravity\brain\fa15ef69-38fc-46eb-b605-09e40b401d47\running_shoes_1776366345671.png",
    5: r"C:\Users\yughr\.gemini\antigravity\brain\fa15ef69-38fc-46eb-b605-09e40b401d47\tshirt_1776366363068.png",
    6: r"C:\Users\yughr\.gemini\antigravity\brain\fa15ef69-38fc-46eb-b605-09e40b401d47\coffee_maker_1776366380580.png"
}

for pid, path in mapping.items():
    try:
        p = Product.objects.get(id=pid)
        with open(path, 'rb') as f:
            p.image.save(os.path.basename(path), File(f), save=True)
        print(f"Saved image for product {pid}: {p.name}")
    except Exception as e:
        print(f"Error on {pid}: {e}")
