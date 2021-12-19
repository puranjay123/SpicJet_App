df2 = pd.read_csv('/root/revised_time_bands.csv')

   

    df2['COMP_START_TIME_BAND'] = pd.to_datetime(df2['COMP_START_TIME_BAND'], format='%H:%M').dt.time

    df2['COMP_END_TIME_BAND'] = pd.to_datetime(df2['COMP_END_TIME_BAND'], format='%H:%M').dt.time

   

    ndf = pd.merge(df1, df2, on='Market')


    qu = "COMP_START_TIME_BAND <= STD and \

       COMP_END_TIME_BAND >= STD"

    ndf = ndf.query(qu)

   

    print(ndf.shape)

    ndf.update(ndf.loc[:,'COMP_START_TIME_BAND'].apply(lambda x: x.strftime(format='%H:%M')))

    ndf.update(ndf.loc[:,'COMP_END_TIME_BAND'].apply(lambda x: x.strftime(format='%H:%M')))

    ndf.update(ndf.loc[:,'STD'].apply(lambda x: x.strftime(format='%H:%M')))

   

    ndf = ndf.drop(['FlightCode', 'SG_DEPARTURE_TIME'], axis=1)

    ndf = ndf.rename(columns = {"FlightNumber":"FlightCode", "STD":"SG_DEPARTURE_TIME"})

    ndf = ndf[["Market", "Origin", "Destination", "SECTOR",            "FlightCode", "SG_DEPARTURE_TIME", "COMP_START_TIME_BAND", "COMP_END_TIME_BAND"]]

 

    filename = "/root/FareComparisonFlightTimings_new.csv"

    ndf.to_csv(filename, index=False)

    print("returning filename", filename)

    return filename, ndf