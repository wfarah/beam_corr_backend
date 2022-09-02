
MODE_CORR = "correlator"
MODE_A = "mode_a"
MODE_B = "mode_b"

COORD_INIT = -99

POSSIBLE_BF_DTYPE = ["float16", "float32"]


def getBackendName():
    """
    Return name of backend
    """
    # return backend_name
    raise NotImplementedError("Not implemented Yet")


def startBackend(backend_name, *args, **kwargs):
    """
    Starts specific backend

    Parameters
    ----------
        backend_name : str
            Name of backend
    """
    if backend_name == "Corr": # or something
        _start_backend()
    if backend_name == "modeB": # or something
        _start_backend(mode_b)
    else:
        raise RuntimeError("Backend %s not found" %backend_name)


def start_bf_backend_modeA(nbeams, t_int, incoh):
    pass


def start_bf_backend_modeB(nbeams, chan_rate, dtype):
    """
    Start beamformer ModeB

    Parameters
    ----------
    nbeams : int
        Number of beams to produce on sky (No ICS)
    chan_rate : int
        FFT length for pre-beamformer channelizer
    dtype : str
        Data type for BF output ("float16" or "float32")
    """
    if type(nbeams) != int:
        raise RuntimeError("'nbeams' is not an integer")
    if type(chan_rate) != int:
        raise RuntimeError("'chan_rate' is not an integer")
    if dtype not in POSSIBLE_BF_DTYPE:
        raise RuntimeError("data type (%s) not in possible BF dtypes %s"
                %(dtype, POSSIBLE_BF_DTYPE))
    hpguppi.start_backend(nbeams, chan_rate, dtype)


def start_bf_backend_modeH(nbeams, chan_rate, output_fmt)



def _start_backend():
    """
    Helper function to start specific backends

    Should every backend have such function?
    """


class Beamformer(object):
    """
    Beamformer class
    """
    def __init__(self):
        self.nbeams = self._get_n_beams()

        # initialize beams
        # observers will then have to manually fill what beam coordinates
        # are
        for ibeam in range(self.nbeams): #this should include incoherent
            incoh = False
            # incoherent beam is always last
            if (i == self.nbeams - 1) and self._incoherent_enabled():
                incoh = True
            self.__setattr__("beam%i" %ibeam) =\
                    Beam(ra_off = COORD_INIT, 
                            dec_off = COORD_INIT, 
                            incoherent = incoh)

    def _get_n_beams(self):
        return NotImplementedError("Not implemented yet")

    def incoherent_enabled(self):
        return self._incoherent_enabled()

    def push_sky_beams(self, **kwargs):
        """
        Push sky beam offsets

        Paramters:
        ----------
            kwargs : dict
                dictionary with 
        """

        # check if correct (beamform) backend is set
        self._check_if_bf_mode()

        # Check whether all beams have been set
        for ibeam in range(self.nbeams):
            # if incoherent beam => no coordinates
            if (i == self.nbeams - 1) and self._incoherent_enabled():
                continue
            beam = self.__getattribute__("beam%i" %ibeam)
            if beam.ra_off == COORD_INIT and beam.dec_off == COORD_INIT:
                raise RuntimeError("Please set beam coordinates manually")

            
    def _check_if_bf_mode(self):
        return True


class Beam(object):
    """
    Beam class
    """
    def __init__(self, ra_off, dec_off, incoherent):
        """
        """
        self.ra_off = ra_off
        self.dec_off = dec_off
        self.incoherent = incoherent

    def push_coordinates(self):
        self._push_beam_coordinates()

    def _push_beam_coordinates(self):
        #hpguppi_push_bla_bla()
        raise NotImplementedError("Not implemented yet")


class Correlator(object):
    """
    Correlator class
    """
    def __init__(self):
        pass

    def get_corr_length(self):
        return corr_length

    def set_corr_length(self, corr_length):
        self._set_corr_length(corr_length)
