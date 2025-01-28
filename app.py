from flask import Flask
from flask import render_template

# Create the Flask app
app = Flask(__name__)

# Define a route and its view function
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find_job')
def find_job():
    return render_template('/pages/find-job.html')

@app.route('/register_profile')
def register_profile():
    return render_template('/pages/register-profile.html')

@app.route('/admin_ads_management')
def admin_ads_management():
    return render_template('/admin-pages/admin-ads-management.html')

@app.route('/admin_home')
def admin_home():
    return render_template('/admin-pages/admin-home.html')

@app.route('/admin_all_employers')
def admin_all_employers():
    return render_template('/admin-pages/admin-all-employers.html')

@app.route('/admin_edit_employers')
def admin_edit_employers():
    return render_template('/admin-pages/admin-edit-employers.html')

@app.route('/admin_edit_JobSeekerProfile')
def admin_edit_JobSeekerProfile():
    return render_template('/admin-pages/admin-edit-JobSeekerProfile.html')

@app.route('/admin_employer_profile')
def admin_employer_profile():
    return render_template('/admin-pages/admin-employer-profile.html')

@app.route('/admin_employer_registration')
def admin_employer_registration():
    return render_template('/admin-pages/admin-employer-registration.html')

@app.route('/admin_jobListPage')
def admin_jobListPage():
    return render_template('/admin-pages/admin-jobListPage.html')

@app.route('/admin_Jobseeker_profile')
def admin_Jobseeker_profile():
    return render_template('/admin-pages/admin-Jobseeker-profile.html')

@app.route('/admin_postJob')
def admin_postJob():
    return render_template('/admin-pages/admin-postJob.html')

@app.route('/admin_sendAlert_employer')
def admin_sendAlert_employer():
    return render_template('/admin-pages/admin-sendAlert-employer.html')

@app.route('/admin_sendAlert_jobseeker')
def admin_sendAlert_jobseeker():
    return render_template('/admin-pages/admin-sendAlert-jobseeker.html')

@app.route('/admin_update_product_images')
def admin_update_product_images():
    return render_template('/admin-pages/admin-update-product-images.html')

@app.route('/admin_user_management')
def admin_user_management():
    return render_template('/admin-pages/admin-user-management.html')


@app.route('/advancedFilter_jobs')
def advancedFilter_jobs():
    return render_template('/pages/advancedFilter-jobs.html')

@app.route('/advertise_business')
def advertise_business():
    return render_template('/pages/advertise-business.html')

@app.route('/contact_us')
def contact_us():
    return render_template('/pages/contact-us.html')

@app.route('/edit_profile')
def edit_profile():
    return render_template('/pages/edit-profile.html')

@app.route('/feature_profile')
def feature_profile():
    return render_template('/pages/feature-profile.html')

@app.route('/filter_talent')
def filter_talent():
    return render_template('/pages/filter-talent.html')

@app.route('/find_talent')
def find_talent():
    return render_template('/pages/find-talent.html')

@app.route('/hr_outsourcing')
def hr_outsourcing():
    return render_template('/pages/hr-outsourcing.html')

@app.route('/opened_jobPost')
def opened_jobPost():
    return render_template('/pages/opened-jobPost.html')

@app.route('/post_job')
def post_job():
    return render_template('/pages/post-job.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('/pages/privacy-policy.html')

@app.route('/professional_resume')
def professional_resume():
    return render_template('/pages/professional-resume.html')

@app.route('/profile')
def profile():
    return render_template('/pages/profile.html')

@app.route('/refund_policy')
def refund_policy():
    return render_template('/pages/refund-policy.html')

@app.route('/searched_jobs')
def searched_jobs():
    return render_template('/pages/searched-jobs.html')

@app.route('/searched_talent')
def searched_talent():
    return render_template('/pages/searched-talent.html')

@app.route('/terms_condition')
def terms_condition():
    return render_template('/pages/terms-condition.html')

@app.route('/z_dummy_filters')
def z_dummy_filters():
    return render_template('/pages/z-dummy-filters.html')

@app.route('/z_test')
def z_test():
    return render_template('/pages/z-test.html')

@app.route('/employer_edit_profile')
def employer_edit_profile():
    return render_template('/pages/employer-pages/employer-edit-profile.html')

@app.route('/employer_home')
def employer_home():
    return render_template('/pages/employer-pages/employer-home.html')

@app.route('/employer_myJobs')
def employer_myJobs():
    return render_template('/pages/employer-pages/employer-myJobs.html')

@app.route('/employer_postJob')
def employer_postJob():
    return render_template('/pages/employer-pages/employer-postJob.html')

@app.route('/employer_profile')
def employer_profile():
    return render_template('/pages/employer-pages/employer-profile.html')

@app.route('/employer_sign_in')
def employer_sign_in():
    return render_template('/pages/employer-pages/employer-sign-in.html')
    

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
