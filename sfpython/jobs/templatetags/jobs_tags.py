from django import template

register = template.Library()

from jobs.models import Job

@register.assignment_tag()
def get_jobs():
    return Job.visible.all()


@register.filter()
def image_attributes(image):
    try:
        scaling_factor = 185 / float(image.height)
        if  scaling_factor * image.width > 250:
            return "width=250"
        else:
            return 'height=185'
    except:
        return "width=250"
    
@register.filter(name='chunks')
def chunks(iterable, chunk_size):
    if not hasattr(iterable, '__iter__'):
        # can't use "return" and "yield" in the same function
        yield iterable
    else:
        i = 0
        chunk = []
        for item in iterable:
            chunk.append(item)
            i += 1
            if not i % chunk_size:
                yield chunk
                chunk = []
        if chunk:
            # some items will remain which haven't been yielded yet,
            # unless len(iterable) is divisible by chunk_size
            yield chunk    
