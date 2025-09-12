import random
import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.apps.api.models import BlogModel

BLOG_TITLES = [
    "Top 10 Travel Destinations",
    "How to Pack Efficiently",
    "A Guide to Solo Travel",
    "Best Beaches to Visit",
    "Cultural Festivals Around the World",
    "Mountain Hiking Tips",
    "City Exploration Guide",
    "Food Adventures Abroad",
    "Photography Tips for Travelers",
    "Eco-Friendly Travel Ideas",
]

IMAGE_URL = "https://picsum.photos/800/600"

def generate_description(title):
    """Random va uzunroq description yaratish, har bir phrase ichida 200 so‘z"""
    base_phrases = [
        "Explore the world with unique experiences",
        "Tips and tricks for an unforgettable journey",
        "Discover hidden gems and local secrets",
        "Perfect for adventure and relaxation",
        "Expert advice from seasoned travelers",
        "Inspiring stories and travel guides",
        "Make the most of your vacation",
        "Learn about culture, food, and history",
        "Step off the beaten path and explore",
        "Travel smart and create memories",
    ]

    words_pool = (
        "travel adventure explore journey destination experience culture history "
        "local food nature sightseeing guide tips tricks relaxation inspiration "
        "memories smart planning safety comfort unique hidden beautiful amazing "
        "discover learn create enjoy relax indulge excitement fun unforgettable "
        "luxury budget family friends solo backpacking hiking trekking walking "
        "city countryside beach mountains sea rivers lakes parks wildlife "
        "photography art architecture music festival tradition ceremony "
        "shopping market street cuisine delicacy restaurant cafe cuisine "
    ).split()

    descriptions = []
    for phrase in base_phrases:
        # 200 ta so‘zdan iborat jumla
        random_words = [random.choice(words_pool) for _ in range(50)]
        long_phrase = phrase + ". " + " ".join(random_words) + "."
        descriptions.append(long_phrase)

    selected_phrases = random.sample(descriptions, 5)
    return f"{title}: " + " ".join(selected_phrases)

class Command(BaseCommand):
    help = "Populate BlogModel with 10 random entries"

    def handle(self, *args, **options):
        for i, title in enumerate(BLOG_TITLES, start=1):
            blog = BlogModel(
                title=title,
                slug=slugify(title),
                description=generate_description(title),
            )

            # Rasmni internetdan yuklab olish va ImageField ga saqlash
            try:
                response = requests.get(f"{IMAGE_URL}?random={i}")
                if response.status_code == 200:
                    blog.image.save(f"{slugify(title)}.jpg", ContentFile(response.content), save=False)
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Failed to download image for {title}: {e}"))

            blog.save()
            self.stdout.write(self.style.SUCCESS(f"Created blog: {blog.title}"))
