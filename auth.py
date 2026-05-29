from flask import Blueprint, render_template, request, redirect, session
auth_bp=Blueprint("auth",__name__)
@auth_bp.route("/",methods=["GET","POST"])
def client_login():
    if request.method=="POST":
        session["login_type"]="client"; session["user"]=request.form.get("user_id","admin"); return redirect("/dashboard")
    return render_template("auth/client_login.html")
@auth_bp.route("/admin",methods=["GET","POST"])
def admin_login():
    if request.method=="POST":
        session["login_type"]="superadmin"; session["user"]=request.form.get("user_id","superadmin"); return redirect("/dashboard")
    return render_template("auth/admin_login.html")
@auth_bp.route("/logout")
def logout():
    session.clear(); return redirect("/")
@auth_bp.route("/forgot-password")
def forgot_password():
    return "Forgot password OTP/email workflow placeholder."
