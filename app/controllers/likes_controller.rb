class LikesController < ApplicationController
  before_action :require_login
  def create
    Like.create(user: current_user, secret: Secret.find(params[:secret_id]))
    redirect_to "/secrets"
  end

  def destroy
    @like = Like.find_or_create_by(user: current_user, secret: Secret.find(params[:secret_id]))
    @like.destroy if @like
    redirect_to "/secrets"
  end
end
