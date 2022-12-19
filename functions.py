def label_fema_floodzones(row):
    '''
    this function re-labels the FEMA flood zones from string to int for raster conversion.
    Flood zone labels are taken from the D_Zone look-up table (section 2.81 in below report)
    https://www.fema.gov/sites/default/files/2020-02/Domain_Tables_Technical_Reference_Feb_2019.pdf
    '''
    if row['FLD_ZONE'] == "A": # 0.01 AEP inland flooding (using approximate methods)
        return 1
    if row['FLD_ZONE'] == "AE": # 0.01 AEP inland flooding (using detailed methods)
        return 2
    if row['FLD_ZONE'] == "AH": # 0.01 AEP shallow inland flooding (normally ponding)
        return 3
    if row['FLD_ZONE'] == "AO": # 0.01 AEP shallow inland flooding (usually sheet flow on sloping terrain)
        return 4
    if row['FLD_ZONE'] == 'AR': # Areas of previous protection decertification and in process of being restored
        return 5
    if row['FLD_ZONE'] == 'A99': # 0.01 AEP inland flooding which is protected
        return 6
    if row['FLD_ZONE'] == "V": # 0.01 AEP coastal flooding (using approximate methods)
        return 7
    if row['FLD_ZONE'] == "VE": # 0.01 AEP coastal flooding (using detailed methods)
        return 8
    if row['FLD_ZONE'] == "X": # areas of moderate to minimal flood risks (<=0.2 AEP)
        return 9
    if row['FLD_ZONE'] == "D": # areas with possible flood risk but no analysis done
        return 96
    if row['FLD_ZONE'] == "OPEN WATER":
        return 97
    if row['FLD_ZONE'] == "AREA NOT INCLUDED":
        return 98
    if row['FLD_ZONE'] == 'NP - NOT POPULATED':
        return 99




