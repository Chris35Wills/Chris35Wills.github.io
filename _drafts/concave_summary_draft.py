def grid_log_density(xx,yy,zz):
	xi = np.linspace(min(xx), max(xx))
	yi = np.linspace(min(yy), max(yy))
	X, Y = np.meshgrid(xi, yi)
	zz_log = np.log(zz)
	Z_log = ml.griddata(xx, yy, zz_log, xi, yi)
	
	return Z_log

def smooth_density_surface_points(Z_log, xx, yy, density_to_nan_limit=-40):
	smooth = ndimage.filters.gaussian_filter(Z_log, sigma=1.0, order=0, mode='reflect')
	smooth[smooth<=density_to_nan_limit] = np.nan
	extent = (resamp_pnt_xx.min(), resamp_pnt_xx.max(), resamp_pnt_yy.min(), resamp_pnt_yy.max())

	return smooth, extent

def grid_contour(surface, extent, density_boundary):
	cs = plt.contour(surface, levels=[density_boundary], linewidth = 5, extent=extent)

	return cs
############
############

def density_hull_approximator(density_xyz_file, points_xy_file, opath, opath_no_file, itr, density_boundary=-16.500, save_contours_xy=0):
	
	## get x, y and density values from the R output into variables 

	Z_log = concave_hull_funcs.grid_log_density(xx,yy,zz) 

	## PLOT GAUSSIAN FILTERED DENSITY SURFACE [WITH POINTS]
	smooth, extent = concave_hull_funcs.smooth_density_surface_points(Z_log, resamp_pnt_xx, resamp_pnt_yy, opath_no_file, itr) 
	
		
	cs = concave_hull_funcs.grid_contour(smooth, extent, density_boundary)
	
	contour_x_list, contour_y_list = concave_hull_funcs.contour_vertices(cs) 	
	concave_hull_funcs.contour_points_check_plot(smooth, contour_x_list, contour_y_list, density_boundary, extent, opath_no_file, itr)

	if save_contours_xy==1:
		concave_hull_funcs.write_contour_verts(opath, contour_x_list, contour_y_list)