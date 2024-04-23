from django.core.management.base import BaseCommand
from django_seed import Seed
from blog.models import Post,Categories
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help =  'Seeds the database with data'
    
    def handle(self,*args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(Categories,10)
        
        # Seed categories
        categories = Categories.objects.all()
        users = User.objects.all()
        
        # Add entities with categories
        for _ in range(30):  # Seed 10 posts
            seeder.add_entity(Post, 1, {
                'category': seeder.faker.random_element(categories),
                'author': seeder.faker.random_element(users)
            })

        inserted_pks = seeder.execute()
    
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded data. Posts PKs: {inserted_pks}"))