from django.shortcuts import render
from .models import Post, BoardList, Comments
from .forms import CommentForm


class KoreaBoard(TemplateView):
	template_name = 'Korea/Board.html'

	def Korea_Post(request):
		posts = Post.object.all()
		return render(request, 'Korea/Board_detail.html', {'posts': posts})

class EastAsiaBoard(TemplateView):
	template_name = 'East_Asia/Board.html'

class EuropeBoard(TemplateView):
	template_name = 'Europe/Board.html'

class NorthAmericaBoard(TemplateView):
	template_name = 'North_America/Board.html'

class SouthAmericaBoard(TemplateView):
	template_name = 'South_America/Board.html'

class AustrailiaBoard(TemplateView):
	template_name = 'Austrailia/Board.html'

class AfricaBoard(TemplateView):
	template_name = 'Africa/Board.html'

class FreeBoard(TemplateView):
	template_name = 'FreeBoard.html'



# 여기서부터 게시판뷰 클래스
class BoardList():
	

class RateBestList():


class ViewBestList():


class CommentBestList():


# 여기서부터 게시글 뷰 클래스
class BoardDetailView(DetailView):
	model = BoardList

class BoardADView():



# 글내용
def Post_Detail(request, pk):
	post = Post.object.get(pk=pk)  # Post.DoesNotExist prob Err500
	return render(request, 'Korea/Post_detail.html', {'post': post,})



def Post_New(request):
	return render(request, 'Korea/post_form.html')
	#templates폴더 안에 각 나라별로 폴더 만들어서 세분화 할 것(post_form.html 파일 만들것)


def Comment_new(request, pk):
	if request.method = 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = Post.object.get(pk=pk)
			comment.save()
			return redirect('views.Post_Detail', pk)
		else:
			form = CommentForm()
		return render(request, 'Korea/post_form.html', {'form': form,})


def Comment_edit(request, post_pk, pk):
	comment = Comments.object.get(pk)

	if request.method = 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.post = Post.object.get(pk=post_pk)
			comment.save()
			return redirect('views.Post_Detail', post_pk)
		else:
			form = CommentForm(instance=comment)
		return render(request, 'Korea/post_form.html', {'form': form,})
