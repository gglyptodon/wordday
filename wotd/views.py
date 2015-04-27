from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Word

# Create your views here.
def main(request):
    context = {}
    words = Word.objects.all()
    context["words"] = words
    #auctions = Auction.objects.all()
    #auctions = Auction.objects.filter(
    #    end_date__gt=timezone.now()
    #).order_by(
    #    'end_date',
    #    'current_amount'
    #)
    #context["auctions"] = auctions
    return render(request, 'wotd/main.djhtml', context=context)

def word_detail(request, word_id):
    print("hi")
    context = {}
    word = Word.objects.get(id=word_id)
    context["word"] = word
    # context['auction_id'] = auction_id
    # auction = get_object_or_404(Auction, id=auction_id)
    # context['auction'] = auction #Auction.objects.get(id=auction_id)
    # if request.method == 'POST':
    #     if not request.user.is_authenticated():
    #         context['message'] = "fuck off"
    #     else:
    #         try:
    #             bid = int(request.POST['bid'])
    #             if auction.current_amount >= bid:
    #                 context['message'] = "MMOOORE"
    #             else:
    #                 context['message'] = "KK."
    #                 auction.current_amount = bid
    #                 auction.current_bidder = request.user
    #                 auction.save()
    #                 return redirect('.')
    #         except ValueError:
    #             context['message'] = "CEEEEEENTS!"

    return render(request, 'wotd/word_detail.djhtml', context=context)
