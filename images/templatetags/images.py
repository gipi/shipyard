from django import template

register = template.Library()

@register.inclusion_tag('images/image_row.html')
def image_row(host, image, version):
    repotag = image.get('RepoTags')[0]
    repository, tag = repotag.split(':')
    return {
        'repository': repository,
        'tag': tag,
        'id': image.get('Id'),
        'host_name': host.name,
        'host_id': host.id,
    }
