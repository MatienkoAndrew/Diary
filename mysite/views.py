from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary
from .forms import DiaryForm
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.

def main(request):
	posts = Diary.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'diary/main.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Diary, pk=pk)
	return render(request, 'diary/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = DiaryForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.worker = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = DiaryForm()
	return render(request, 'diary/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Diary, pk=pk)
	if request.method == "POST":
		form = DiaryForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.worker = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = DiaryForm(instance=post)
	return render(request, 'diary/post_edit.html', {'form': form})
