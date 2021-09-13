
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from library.models import BooksModel
import logging
logger = logging.getLogger('extend_demand')

@login_required(login_url='/')
def extend_demand(request, slug):
    book = get_object_or_404(BooksModel, slug=slug)
    logger.info('Extend request from ' + request.user.username + ' Book Name: ' + book.bookName)
    return render(request, 'pages/extend-demand.html', context={'slug':book.slug})


