from pytils.translit import slugify

def generate_unique_slug(model, name):
    """
    Helper function to generate a unique slug for a given model instance and name.
    """
    slug = slugify(name)
    counter = 1
    while model.objects.filter(slug=slug).exists():
        slug = f"{slug}-{counter}"
        counter += 1
    return slug