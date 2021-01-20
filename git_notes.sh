# ksi particuler commit wala data par apni repo ko wapis ly jany k lye.
# eg: mujhy apni <Linux> repo ko ca02af2 waly commit k bad wali state par ly jana h or is commit k bad jitny bhi commit hwy un sab ko undo karna h to:
cd github/Linux ; git checkout master; git reset --hard ca02af2; git push origin +master



# agar repo ko http me clone kya h, to push/pull ka maslay aaty hen or aap sy har push/pull par email or password manga jata h, is ko solve karny k lye:
1- git git remote -v  
if you get like below:
  origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
  origin  https://github.com/USERNAME/REPOSITORY.git (push)
run:
  git remote set-url origin git@github.com:User/UserRepo.git
  
