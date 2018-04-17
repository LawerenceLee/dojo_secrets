class SessionsController < ApplicationController
  def new
  end

  def create
      @user = User.find_by_email(session_params[:email]).try(:authenticate, session_params[:password])
      if @user
        session[:user_id] = @user.id
        redirect_to "/users/#{@user.id}"
      else
        flash[:errors] = ["Invalid Combination"]
        redirect_to :new_session
      end
  end

  def destroy
      session[:user_id] = nil
      redirect_to :new_session
  end

  private
  def session_params 
    params.permit(:email, :password)
  end
end
