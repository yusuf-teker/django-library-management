from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from library.models import BooksModel
import logging
logger = logging.getLogger('return_demand')

@login_required(login_url='/')
def return_demand(request, slug):
    book = get_object_or_404(BooksModel, slug=slug)
    logger.info('Return demand from ' + request.user.username + ' Book Name: '+book.bookName)
    return render(request, 'pages/return-demand.html',  context={'slug':book.slug})


