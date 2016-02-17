
## Basic classifier class;

class Classifier(object):
    # minimal list of spectators
    SPECTATORS = [
        MMC_PT,
        MMC_MASS,
    ]
    def __init__(self,
                 mass,
                 fields,
                 category,
                 region,
                 cuts=None,
                 spectators=None,
                 output_suffix="",
                 clf_output_suffix="",
                 partition_key='EventNumber',
                 transform=True,
                 mmc=True):

        fields = fields[:]
        if not mmc:
            try:
                fields.remove(MMC_MASS)
            except ValueError:
                pass

        self.mass = mass
        self.fields = fields
        self.category = category
        self.region = region
        self.spectators = spectators
        self.output_suffix = output_suffix
        self.clf_output_suffix = clf_output_suffix
        self.partition_key = partition_key
        self.transform = transform
        self.mmc = mmc
        self.background_label = 0
        self.signal_label = 1

        if spectators is None:
 
