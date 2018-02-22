
from django.conf.urls import url,include
from .views import (
                    Continuous_AssessmentListView,
                    AttendanceListView,
                    ExamMarkListView,
                    FeeListView,
                    BorrowingListView
                
                    
                    
                    
                    )
    

urlpatterns = [
    
        
    url(r'^$', Continuous_AssessmentListView.as_view(),name="studentscontinuous"),
    url(r'^attendance/$', AttendanceListView.as_view(),name="attendance"),
    url(r'^exammark/$', ExamMarkListView.as_view(),name="exammark"),
    url(r'^fees/$', FeeListView.as_view(),name="fees"),
    url(r'^borrowing/$', BorrowingListView.as_view(),name="borrowing")
   
    
    
]
