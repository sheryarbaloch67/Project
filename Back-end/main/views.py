from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
import random
from django.template.loader import get_template
from weasyprint import HTML
from django.template import loader

# Create your views here.

def cover(request):
    return render(request, 'index.html')


def test(request):
    teachers = Teacher.objects.all
    return render(request, 'test.html', {'all':teachers})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(dashboard)
            else:
                return render(request, 'signin.html', {'form': form, 'error': 'Invalid login'})
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Invalid form data'})

    else:
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

@login_required(login_url='signin/')
def signout(request):
    logout(request)
    return redirect('signin/')

@login_required(login_url='signin/')
def dashboard(request):
    if hasattr(request.user, 'teacher'):
        courses = Course.objects.filter(teacher=request.user.teacher)
        context = {
            'courses': courses,
        }
    return render(request, 'dashboard.html', context)


@login_required(login_url='signin/')
def profile(request):
    user_form = UserUpdateForm(instance=request.user)
    teacher_form = TeacherProfileForm(instance=request.user.teacher)
    password_form = PasswordChangeForm(request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        teacher_form = TeacherProfileForm(request.POST, instance=request.user.teacher)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if user_form.is_valid() and teacher_form.is_valid() and password_form.is_valid():
            print('In the if')
            user_form.save()
            teacher_form.save()
            user = password_form.save()
            update_session_auth_hash(request, user) # Important!
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'There was an error updating your profile. Please try again.')
    
    context = {
        'user_form': user_form,
        'teacher_form': teacher_form,
        'password_form': password_form,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='signin/')
def course(request):
    if hasattr(request.user, 'teacher'):
        teacher = request.user.teacher
        if request.method == 'POST':
            form = CourseForm(request.POST)
            if form.is_valid():
                course = form.save(commit=False)
                course.teacher = teacher
                course.save()
                return redirect(dashboard)
            else:
                return JsonResponse({'error': 'Invalid form'})
        else:
            form = CourseForm()
            courses = Course.objects.filter(teacher=teacher)
        context = {
            'form': form,
            'courses': courses,
        }
    return render(request, 'add course.html', context)

@login_required(login_url='signin/')
def delete_course(request, course_id):
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully.')
        return redirect('dashboard')
    return render(request, 'delete_course.html', {'course': course})


@login_required(login_url='signin/')
def lectures(request, course_id):
    if hasattr(request.user, 'teacher'):
        teacher = request.user.teacher
        course = get_object_or_404(Course, course_id=course_id, teacher=teacher)
        lectures = Lecture.objects.filter(course=course)
        context = {
            'course': course,
            'lectures': lectures
        }
        return render(request, 'all lectures.html', context)


@login_required(login_url='signin/')
def lecture(request, course_id):
    teacher = request.user.teacher
    course = get_object_or_404(Course, course_id=course_id, teacher=teacher)
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = course
            lecture.teacher = teacher
            lecture.save()
            return redirect('lectures', course_id=course_id)
    else:
        form = LectureForm()
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'add lecture.html', context)


@login_required(login_url='signin/')
def delete_lecture(request, course_id, lecture_id):
    lecture = get_object_or_404(Lecture, lecture_id=lecture_id, course_id=course_id)
    if request.method == 'POST':
        lecture.delete()
        update_lecture_ids(request, course_id)
        messages.success(request, 'Lecture deleted successfully.')
        return redirect('lectures', course_id=course_id)
    return render(request, 'delete_lecture.html', {'lecture': lecture})


@login_required(login_url='signin/')
def update_lecture_ids(request, course_id):
    lectures = Lecture.objects.filter(course_id=course_id).order_by('lecture_id')
    for i, lecture in enumerate(lectures, start=1):
        if lecture.lecture_id != i:
            lecture.lecture_id = i
            lecture.save()


@login_required(login_url='signin/')
def add_mcqs(request, course_id, lecture_id):
    course = Course.objects.get(course_id=course_id)
    lecture = Lecture.objects.get(lecture_id=lecture_id, course=course)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.course = course
            question.lecture = lecture
            question.teacher = request.user.teacher
            question.save()
            return redirect('lectures', course_id=course_id)
    else:
        form = QuestionForm()
    return render(request, 'add_mcqs.html', {'form': form, 'course': course, 'lecture': lecture})


@login_required(login_url='signin/')
def view_mcqs(request, course_id, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id, course_id=course_id)
    mcqs = Question.objects.filter(lecture=lecture)
    return render(request, 'show_mcqs.html', {'mcqs': mcqs})

@login_required(login_url='signin/')
def edit_mcq(request, course_id, lecture_id, question_id):
    mcq = get_object_or_404(Question, id=question_id, course_id=course_id, lecture_id=lecture_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=mcq)
        if form.is_valid():
            form.save()
            messages.success(request, 'MCQ updated successfully.')
            return redirect('view_mcqs', course_id=course_id, lecture_id=lecture_id)
    else:
        form = QuestionForm(instance=mcq)
    return render(request, 'edit_mcqs.html', {'form': form})


@login_required(login_url='signin/')
def delete_mcq(request, course_id, lecture_id, question_id):
    mcq = get_object_or_404(Question, id=question_id, course_id=course_id, lecture_id=lecture_id)
    if request.method == 'POST':
        mcq.delete()
        update_mcq_sno(request, lecture_id)
        messages.success(request, 'MCQ deleted successfully.')
        return redirect('view_mcqs', course_id=course_id, lecture_id=lecture_id)
    return render(request, 'delete_mcq.html', {'mcq': mcq})

@login_required(login_url='signin/')
def update_mcq_sno(request, lecture_id):
    mcqs = Question.objects.filter(lecture_id=lecture_id).order_by('s_no')
    for i, mcq in enumerate(mcqs, start=1):
        if mcq.s_no != i:
            mcq.s_no = i
            mcq.save()


@login_required(login_url='signin/')
def activity(request):
    if request.method == 'POST':
        # Get the form data
        course_id = request.POST['course']
        lecture_ids = request.POST.getlist('lecture')
        print("lectures:", lecture_ids)

        lectures = Lecture.objects.filter(course=course_id, lecture_id__in=lecture_ids).values_list('id', flat=True)

        print(lectures)

        print(course_id)

        try:
            # Get the number of MCQs to generate
            quantity = request.POST['quantity']

            print(quantity)

            # Perform your logic for generating MCQs based on the course_id, selected_lectures, and quantity
            questions = Question.objects.filter(course=course_id, lecture__in=lectures)
            print(list(questions))
            questions = random.sample(list(questions), int(quantity))
            for question in questions:
                options = [question.option_1, question.option_2, question.option_3, question.option_4]
                question.options = options

            print(list(questions))

            # Get the user's first and last name
            user = request.user
            user_first_name = user.first_name
            user_last_name = user.last_name
            
            # Get the course name
            course = Course.objects.get(course_id=course_id)
            course_name = course.course_name
            semester = request.POST['semester'] + ' ' + course.discipline + ' ' + course.semester

            # Render the template with the generated MCQs
            context = {
                'questions': questions,
                'user_first_name': user_first_name,
                'user_last_name': user_last_name,
                'course_name': course_name,
                'date': request.POST['date'],
                'duration': request.POST['duration'],
                'marks': request.POST['marks'],
                'activity_name': request.POST['ActName'],
                'semester': semester
            }
            # Render the templates
            question_paper_template = loader.get_template('question_paper.html')
            answer_key_template = loader.get_template('answer_key.html')
            question_paper_html = question_paper_template.render(context)
            answer_key_html = answer_key_template.render(context)

            # Concatenate the HTML for the question paper and answer key
            html = question_paper_html + answer_key_html

            # Return a single HTTP response with both pages
            return HttpResponse(html)
        except ValueError:
            return(HttpResponse("Enter the valid Quantity there are not enough MCQs"))
    return render(request, 'activity.html')

@login_required(login_url='signin/')
def get_lecture_count(request, course_id):
    lecture_count = Lecture.objects.filter(course_id=course_id).count()
    return JsonResponse(lecture_count, safe=False)


    #     # Render the template into HTML
    #     template = get_template('question_paper.html')
    #     html = template.render(context)

    #     # Generate the PDF from the HTML
    #     pdf_file = HTML(string=html).write_pdf()

    #     # Return the PDF file as a response
    #     response = HttpResponse(pdf_file, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="question_paper.pdf"'
    #     return response

    # return render(request, 'activity.html')