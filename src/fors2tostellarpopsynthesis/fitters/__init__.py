from .fitter_jaxopt import (FILENAME_SSP_DATA, FULLFILENAME_SSP_DATA, SSP_DATA,
                            _get_package_dir, get_infos_comb, get_infos_mag,
                            get_infos_spec, lik_comb, lik_mag,
                            lik_normspec_from_mag, lik_spec, lik_spec_from_mag,
                            lik_ugri, mean_mags, mean_sfr, mean_spectrum,
                            mean_ugri, ssp_spectrum_fromparam)
from .fitter_util import (plot_fit_ssp_photometry,
                          plot_fit_ssp_spectrophotometry,
                          plot_fit_ssp_spectrophotometry_sl,
                          plot_fit_ssp_spectroscopy, plot_fit_ssp_ugri,
                          plot_params_kde, plot_SFH, rescale_photometry,
                          rescale_spectroscopy, rescale_starlight_inrangefors2)
from .met_weights_age_dep import calc_rest_sed_sfh_table_lognormal_mdf_agedep

#from .fitter_numpyro import (PARAM_MAX, PARAM_MIN, PARAM_NAMES, PARAM_SIGMA,
#                             PARAM_SIMLAW_NODUST, PARAM_SIMLAW_WITHDUST,
#                             PARAM_VAL, galaxymodel_nodust,
#                             galaxymodel_nodust_av, galaxymodel_withdust,
#                             galaxymodel_withdust_av)



__all__ = ["_get_package_dir",
           "FILENAME_SSP_DATA",
           "FULLFILENAME_SSP_DATA",
           "SSP_DATA",
           "lik_spec","lik_mag","lik_comb","lik_ugri","lik_spec_from_mag","lik_normspec_from_mag",
           "get_infos_spec","get_infos_mag","get_infos_comb",
           "mean_spectrum","mean_mags","mean_ugri","mean_sfr","ssp_spectrum_fromparam",
           "rescale_photometry",
           "rescale_spectroscopy",
           "rescale_starlight_inrangefors2",
           "plot_fit_ssp_photometry",
           "plot_fit_ssp_spectroscopy",
           "plot_fit_ssp_spectrophotometry",
           "plot_fit_ssp_spectrophotometry_sl",
           "plot_fit_ssp_ugri",
           "plot_SFH",
           "plot_params_kde",
           "calc_rest_sed_sfh_table_lognormal_mdf_agedep"] #,
           #"PARAM_SIMLAW_NODUST","PARAM_SIMLAW_WITHDUST",
           #"PARAM_NAMES","PARAM_VAL","PARAM_MIN","PARAM_MAX",
           #"PARAM_SIGMA","galaxymodel_nodust_av","galaxymodel_nodust",
           #"galaxymodel_withdust_av","galaxymodel_withdust"
           #]
