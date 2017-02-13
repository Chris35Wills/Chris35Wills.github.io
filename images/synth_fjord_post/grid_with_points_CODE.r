library(raster)
library(fields)
source("C:/GitHub/R_bits/my_functions/plotting.r")
source("C:/GitHub/synthetic_channels/meshing/development_scripts/parabola_funcs_where_obs_available.r")        

Nth.row <- function(dataframe, n) dataframe[(seq (n, to=nrow(dataframe), by=n)),]

spline_surface<-function(xyz, plotting=F){

  combo=as.data.frame(xyz)

  fit<- Tps(combo$x, combo$y) 

  coord<-data.frame(combo$x, combo$y)
  z<-data.frame(combo$z)

  fit<-Tps(coord,z)

  xg<-make.surface.grid(fields.x.to.grid(coord)) # makes a mesh grid of x and y
  if (plotting==TRUE){plot(xg)} # displays the mesh grid
  fhat<- predict( fit, xg) # indexes values of based on the thin plate spline to their xy index locations (i.e. this is 1d and is therefore a length of the dimensions of plot(xg))
  out.p<- as.surface( xg, fhat)
  
  return(out.p)
}


points_all=read.csv("C:/GitHub/synthetic_channels/USED_FOR_SYNTH_PAPER/site_aoi_Fenty_N/bamber2013_aoi_Fenty_N_gt500m_mc.csv")

points=Nth.row(points_all, 20)
keep=c('x','y','z')
points=points[keep]
out.p=spline_surface(points)

out.p.agg=aggregate(out.p)
###################
# plot it

persp(out.p$x, out.p$y, out.p$z*5,
      phi = 20, theta = 20,
      xlab = "easting (m)", ylab = "northing (m)", zlab="elevation (m)", scale=FALSE, expand=1,
      r=10,
      d=0.4 )-> res
      #main = "Surface spline"

#points(trans3d(points$x, points$y, points$z, pmat = res), col = 2, pch = 20, cex = 0.7)  # add points to wireframe plot
points(trans3d(points$x, points$y, points$z, pmat = res), col = 2, pch = 18, cex = 0.5)  # add points to wireframe plot
