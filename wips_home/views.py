from wips_home.models import BlockLog
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from wips_home.forms import PostForm

def block_list(request):
	BlockLogS = BlockLog.objects.all()
	return render(request,'wips_home/block_list.html',{'BlockLogS':BlockLogS})
# Create your views here.
def block_list_post(request,pk):
	#form = PostForm()
	#form = PostForm()
	bpost = get_object_or_404(BlockLog,pk=pk)
	if request.method=="POST":
		form = PostForm(request.POST,instance=bpost)
		if form.is_valid():
			#BlockLog.block_stat = request.block_stat
			bpost=form.save()
			return redirect(request.path_info)
	else:
		form = PostForm(instance=bpost)

	return render(request, 'wips_home/block_list_post.html',{'BlockLog':bpost,'form':form})
#def edit_data(request):
	#form = PostForm()
	#return render(request, 'wips_home/block_list_post.html',{'form':form})